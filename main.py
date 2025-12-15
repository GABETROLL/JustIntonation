"""
Continuously plays frequencies dictated in the terminal:

new: <frequency to start playing>
old: <frequency to stop playing>
frame + frames - frequency_command.command_frame"""
import sounddevice
import numpy
from music_player import *
from cannon_in_d import wave

current_frame: int = 0

def sine_wave(start_frame: int, duration_in_frames: int, hz: float, amplitude: float) -> numpy.ndarray:
    """
    Assuming that a sine wave frequency of `hz` Hz has been playing at a "frame rate", or sample rate,
    of `SAMPLE_RATE` for `start_frame` frames until now, this function returns the air pressure values for
    the upcoming `duration_in_frames` frames.

    The result should be returned as a numpy ndarray with shape `(duration_in_frames, 1)`.
    """
    return numpy.sin(
        numpy.arange(start_frame, start_frame + duration_in_frames) / SAMPLE_RATE * 2 * numpy.pi * frequency
    ) * amplitude


def almost_zero(x: float):
    """
    Returns if `x` is within a certain distance to 0 in the number line.
    """
    return -0.01 < x < 0.01


def callback(outdata: numpy.ndarray, frames: int, time, status) -> None:
    """writes sound output to 'outdata' from sound_queue."""
    global current_frame

    outdata[:] = wave[current_frame:current_frame + frames].reshape((frames,1))
    current_frame += frames


def main():
    print(f"wave: {wave.shape}")

    stream = sounddevice.OutputStream(channels=1, samplerate=SAMPLE_RATE, callback=callback)
    stream.start()

    while True:
        text = input(">>>")
        if text == "q":
            break

    stream.stop()


if __name__ == "__main__":
    main()
