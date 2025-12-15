import numpy
from dataclasses import dataclass

Hertz: type = float

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


def render_wave(melody: Melody, sample_rate: int) -> numpy.ndarray:
    beats_per_second: float = melody.beats_per_minute / 60
    samples_per_beat_rounded: int = int(sample_rate / beats_per_second)

    result: numpy.ndarray = numpy.zeros((samples_per_beat_rounded * len(melody.notes),))

    for beat_index, beat in enumerate(melody.notes):
        start_sample_index: int = beat_index * samples_per_beat_rounded
        end_sample_index: int = start_sample_index + samples_per_beat_rounded

        # start the frequency as it had always been playing
        for frequency in beat:
            print(result[start_sample_index:end_sample_index].shape)

            beat_wave: numpy.ndarray = numpy.sin(
                numpy.arange(start_sample_index, end_sample_index) / sample_rate * 2 * numpy.pi * frequency
            )

            print(beat_wave.shape)

            result[start_sample_index:end_sample_index] += beat_wave

    return result
