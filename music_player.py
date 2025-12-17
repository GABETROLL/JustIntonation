import numpy
from dataclasses import dataclass
from typing import Callable
from matplotlib import pyplot

Hertz: type = int

"""
@dataclass
class Fraction:
    numerator: int
    denominator: int


@dataclass
class NoteRatio:
    other_note_id: int
    ratio: Fraction


@dataclass
class Note:
    id_number: int
    beat: int
    duration_in_beats: int
    value: NoteRatio | Hertz


@dataclass
class Melody:
    tempo: float
    notes: list[Note]


class MusicAsRatios:
    def __init__(self, notes: list[Melody]):
        # TODO: VALIDATE NOTES
        self.notes = notes


@dataclass
class PlayFrequency:
    \"\"\"Describes when a frequency should start playing, and for how many frames.\"\"\"
    command_frame: int
    duration: int
    frequency: Hertz
    amplitude: float


def transform_music(music_as_ratios: MusicAsRatios) -> list[FrequencyCommand]:
    \"\"\"
    Reads music from ratios format, and returns it as a list of FrequencyCommand.
    \"\"\"
    pass
"""

SAMPLE_RATE = 14400


@dataclass
class Melody:
    beats_per_minute: float
    notes: list[list[Hertz]]


def domain(frequency: Hertz, sample_rate: int, start_sample_index: int, end_sample_index: int) -> numpy.ndarray:
    return numpy.linspace(
        start_sample_index * 2 * frequency / sample_rate,
        (end_sample_index - 1) * 2 * frequency / sample_rate,
        end_sample_index - start_sample_index,
    ) * numpy.pi


def trumpet(frequency: Hertz, sample_rate: int, start_sample_index: int, end_sample_index: int) -> numpy.ndarray:
    return numpy.sin(
        domain(frequency, sample_rate, start_sample_index, end_sample_index)
    ) + numpy.sin(
        domain(frequency * 2, sample_rate, start_sample_index, end_sample_index)
    ) / 2 + numpy.sin(
        domain(frequency * 3, sample_rate, start_sample_index, end_sample_index)
    ) / 3 + numpy.sin(
        domain(frequency * 4, sample_rate, start_sample_index, end_sample_index)
    ) / 4 + numpy.sin(
        domain(frequency * 5, sample_rate, start_sample_index, end_sample_index)
    ) / 5


def other(frequency: Hertz, sample_rate: int, start_sample_index: int, end_sample_index: int) -> numpy.ndarray:
    return numpy.sin(
        domain(frequency, sample_rate, start_sample_index, end_sample_index)
    ) + numpy.sin(
        domain(frequency * 3, sample_rate, start_sample_index, end_sample_index)
    ) / 3 + numpy.sin(
        domain(frequency * 5, sample_rate, start_sample_index, end_sample_index)
    ) / 5 + numpy.sin(
        domain(frequency * 7, sample_rate, start_sample_index, end_sample_index)
    ) / 7 + numpy.sin(
        domain(frequency * 9, sample_rate, start_sample_index, end_sample_index)
    ) / 9


def sine_wave(frequency: Hertz, sample_rate: int, start_sample_index: int, end_sample_index: int) -> numpy.ndarray:
    numpy.sin(numpy.arange(start_sample_index, end_sample_index) / sample_rate)

    big_wave: numpy.ndarray = numpy.sin(domain)
    step: int = sample_rate // frequency
    return big_wave[::step]   


def render_wave(melody: Melody, sample_rate: int, voice: Callable[[Hertz, int, int, int], numpy.ndarray]) -> numpy.ndarray:
    beats_per_second: float = melody.beats_per_minute / 60
    samples_per_beat_rounded: int = int(sample_rate / beats_per_second)

    beats: int = len(melody.notes)

    result: numpy.ndarray = numpy.zeros((samples_per_beat_rounded * beats,))
    one_hertz_wave: numpy.ndarray = numpy.sin(
        numpy.arange(0, samples_per_beat_rounded ** 2 * beats) * 2 * numpy.pi / sample_rate
    )

    # print(f"result: {result.shape}, one_hertz_wave: {one_hertz_wave.shape}")

    for beat_index, beat in enumerate(melody.notes):
        start_sample_index: int = beat_index * samples_per_beat_rounded
        end_sample_index: int = start_sample_index + samples_per_beat_rounded

        # start the frequency as it had always been playing
        for frequency in beat:
            beat_wave: numpy.ndarray = one_hertz_wave[:samples_per_beat_rounded * frequency:frequency]

            # print(f"Difference: {end_sample_index - start_sample_index}, beat_wave: {beat_wave.shape}, range: {len(range(0, samples_per_beat_rounded * frequency, frequency))}")

            result[start_sample_index:end_sample_index] += beat_wave

        """pyplot.plot(result[start_sample_index:end_sample_index])
        pyplot.show()
        pyplot.close()"""

    return result
