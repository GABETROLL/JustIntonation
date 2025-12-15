"""
Continuously plays frequencies dictated in the terminal:

new: <frequency to start playing>
old: <frequency to stop playing>
frame + frames - frequency_command.command_frame"""
import sounddevice
import numpy
from matplotlib import pyplot
from time import sleep
from dataclasses import dataclass
from music_player import *

FramesLeft: type = int

SAMPLE_RATE = 44100
frequencies: dict[Hertz, FramesLeft]  = {}

frequency_commands: list[FrequencyCommand] = [
    FrequencyCommand(0, START, 300, 1),
]
current_command_index: int = 0
frame: int = 0


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
    result = numpy.zeros((frames, 1))

    while current_command_index < len(frequency_commands):
        frequency_command: FrequencyCommand = frequency_commands[current_command_index]

        if not (frame <= frequency_command.command_frame < frame + frames):
            break

        frame_index_in_block: int = frequency_command.command_frame - frame

        if duration < frame + frames - frequency_command.command_frame:
            frequency_wave: numpy.ndarray = sine_wave(
                frequency_command.command_frame,
                frequency_command.duration,
                frequency_command.frequency,
                frequency_command.amplitude,
            )

            result[frame_index_in_block:frame_index_in_block + duration] += frequency_wave
        else:
            current_duration: int = frame + frames - frequency_command.command_frame

            frequency_wave: numpy.ndarray = sine_wave(
                frequency_command.command_frame,
                current_duration,
                frequency_command.frequency,
                frequency_command.amplitude,
            )

            result[frame_index_in_block:frame + frames] += frequency_wave

            frequencies[frequency_command.frequency] = frequency_command.duration - current_duration

        current_command_index += 1

    for frequency, frames_left in frequencies.items():
        pass

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
