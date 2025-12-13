"""
Continuously plays frequencies dictated in the terminal:

new: <frequency to start playing>
old: <frequency to stop playing>
"""
import sounddevice
import numpy
from matplotlib import pyplot
from time import sleep


SAMPLE_RATE = 44100
frequencies = {800: [0, True]}
# hz: (start_index, active)


def sine_wave(start_frame: int, sound_playing_frames: int, frames: int, hz: float):
    """
    Assuming that a sine wave frequency of `hz` Hz has been playing at a "frame rate", or sample rate,
    of `SAMPLE_RATE` for `start_frame` frames until now, this function returns the air pressure values for
    the upcoming `frames` frames, where the frequency only plays for `sound_playing_frames`, cutting off abruptly.

    The result should be returned as a numpy ndarray with shape `(frames, 1)`.
    """
    result_frames = numpy.zeros((frames, 1))

    for result_frame_index in range(sound_playing_frames):
        objective_frame_index: int = start_frame + result_frame_index
        sin_input: float = objective_frame_index * 2 * numpy.pi * hz / SAMPLE_RATE
        result_frames[result_frame_index] = numpy.sin(sin_input)

    return result_frames


def almost_zero(x: float):
    """
    Returns if `x` is within a certain distance to 0 in the number line.
    """
    return -0.01 < x < 0.01


def callback(outdata: numpy.ndarray, frames: int, time, status) -> None:
    """writes sound output to 'outdata' from sound_queue."""
    # params may need annotations... :/
    result = None

    for frequency, (start_index, active) in frequencies.copy().items():
        wave = sine_wave(start_index, frames, frames, frequency)

        if not active:
            for index, value in enumerate(wave):
                if almost_zero(value):

                    wave = sine_wave(start_index, index, frames, frequency)
                    frequencies.pop(frequency)

                    break
        else:
            frequencies[frequency][0] += frames

        if result is None:
            result = wave
        else:
            result += wave

    if result is None:
        result = numpy.arange(frames) / SAMPLE_RATE
        result = result.reshape(-1, 1)

    outdata[:] = result


def main():
    stream = sounddevice.OutputStream(channels=1, samplerate=SAMPLE_RATE, callback=callback)
    stream.start()

    while True:
        new = input("new: ")
        frequencies.setdefault(int(eval(new)), [0, True])

        old = input("old: ")
        old_frequency = int(eval(old))
        frequencies[old_frequency][1] = False
        sleep(0.01)


if __name__ == "__main__":
    main()
