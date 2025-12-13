import sounddevice
import numpy
from time import sleep


SAMPLE_RATE = 44100
duration = SAMPLE_RATE
# int(1s * SAMPLE_RATE)
frequencies = {800: duration - 1}
# hz: index


def callback(outdata: numpy.ndarray, frames: int, time, status) -> None:
    """writes sound output to 'outdata' from sound_queue."""
    result = numpy.zeros((frames, 1))

    for frequency, frequency_index in enumerate(frequencies):
        for index, amplitude in zip(range(frames), range(frequency_index, -1, -1)):
            amplitude = 1 / amplitude

            wave_index = index + frequency_index
            input_index = wave_index * 2 * numpy.pi * frequency

            result[index] += amplitude * numpy.sin(input_index / SAMPLE_RATE)
        frequencies

