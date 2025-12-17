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


def trumpet(domain: numpy.ndarray) -> numpy.ndarray:
    return numpy.sin(domain) + numpy.sin(2 * domain) / 2 + numpy.sin(3 * domain) / 3 \
        + numpy.sin(4 * domain) / 4 + numpy.sin(5 * domain) / 5 + numpy.sin(6 * domain) / 6


def other(domain: numpy.ndarray) -> numpy.ndarray:
    return numpy.sin(domain) + numpy.sin(domain) / 3 + numpy.sin(domain) / 5 \
         + numpy.sin(domain) / 7 + numpy.sin(domain) / 9


def sine_wave(domain: numpy.ndarray) -> numpy.ndarray:
    return numpy.sin(domain)


def render_wave(melody: Melody, sample_rate: int, voice: Callable[[numpy.ndarray], numpy.ndarray]) -> numpy.ndarray:
    beats_per_second: float = melody.beats_per_minute / 60
    samples_per_beat_rounded: int = int(sample_rate / beats_per_second)

    beats: int = len(melody.notes)

    result: numpy.ndarray = numpy.zeros((samples_per_beat_rounded * beats,))
    """one_hertz_wave: numpy.ndarray = voice(
        numpy.arange(0, samples_per_beat_rounded ** 2 * beats) * 2 * numpy.pi / sample_rate
    )"""

    # print(f"result: {result.shape}, one_hertz_wave: {one_hertz_wave.shape}")

    for beat_index, beat in enumerate(melody.notes):
        start_sample_index: int = beat_index * samples_per_beat_rounded
        end_sample_index: int = start_sample_index + samples_per_beat_rounded

        # start the frequency as it had always been playing
        for frequency in beat:
            # print(f"{frequency = }")
            beat_wave: numpy.ndarray = voice(
                numpy.arange(start_sample_index, end_sample_index) * frequency * 2 * (numpy.pi / sample_rate)
            )

            # print(f"Difference: {end_sample_index - start_sample_index}")
            # print(f"one_hertz_wave: {one_hertz_wave.shape}, beat_wave: {beat_wave.shape}")
            # print(f"range: {len(range(start_sample_index * frequency, end_sample_index * frequency, frequency))}")

            result[start_sample_index:end_sample_index] += beat_wave

        """ pyplot.plot(result[start_sample_index:end_sample_index])
        pyplot.show()
        pyplot.close() """

    return result
