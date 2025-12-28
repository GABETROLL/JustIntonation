import numpy
from dataclasses import dataclass
from typing import Callable, Optional
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
class Note:
    frequency: Hertz # TODO: THIS CHANGE BREAKS LOTS OF FILES!
    voice: Optional[Callable[[numpy.ndarray], numpy.ndarray]] = None
    amplitude: Optional[float] = None # numpy.ScalarType, but dataclass doesn't allow it
    duration_in_beats: int = 1


@dataclass
class Melody:
    beats_per_minute: float
    notes: list[list[Hertz | Note]]


def _dampen(samples: int) -> numpy.ndarray:
    return numpy.arange(samples - 1, -1, -1) / samples


def trumpet(domain: numpy.ndarray) -> numpy.ndarray:
    return numpy.sin(domain) + numpy.sin(2 * domain) / 2 + numpy.sin(3 * domain) / 3 \
        + numpy.sin(4 * domain) / 4 + numpy.sin(5 * domain) / 5 + numpy.sin(6 * domain) / 6


def other(domain: numpy.ndarray) -> numpy.ndarray:
    return numpy.sin(domain) + numpy.sin(3 * domain) / 3 + numpy.sin(5 * domain) / 5 \
         + numpy.sin(7 * domain) / 7 + numpy.sin(9 * domain) / 9 \
         + numpy.sin(11 * domain) / 11 + numpy.sin(13 * domain) / 13


def sine_wave(domain: numpy.ndarray) -> numpy.ndarray:
    return numpy.sin(domain)


def piano_wave(domain: numpy.ndarray) -> numpy.ndarray:
    result = numpy.sin(domain) * 0.6 + numpy.sin(2 * domain) * 0.04
    result += result * result * result
    return result


def dampened_piano_wave(domain: numpy.ndarray, amplitude: float = 1.0) -> numpy.ndarray:
    return piano_wave(domain) * _dampen(domain.size) * amplitude


def get_sin_domain(start_sample_index: int, end_sample_index: int, frequency: int, sample_rate: int) -> numpy.ndarray:
    return numpy.arange(start_sample_index, end_sample_index) * frequency % sample_rate * 2 * (numpy.pi / sample_rate)


def render_wave(melody: Melody, sample_rate: int, default_voice: Callable[[numpy.ndarray], numpy.ndarray], default_amplitude: numpy.ScalarType = 1.0) -> numpy.ndarray:
    beats_per_second: float = melody.beats_per_minute / 60
    samples_per_beat_rounded: int = int(sample_rate / beats_per_second)

    beats: int = len(melody.notes)

    result: numpy.ndarray = numpy.zeros((samples_per_beat_rounded * beats,))

    # one_hertz_wave: numpy.ndarray = voice(
    #     numpy.arange(sample_rate) * 2 * numpy.pi / sample_rate
    # )

    # print(f"result: {result.shape}, one_hertz_wave: {one_hertz_wave.shape}")

    for beat_index, beat in enumerate(melody.notes):
        start_sample_index: int = beat_index * samples_per_beat_rounded

        # Either it's a note, or just a frequency,
        # which would default to an amplitude of 1.
        for note in beat:
            voice: Callable[[numpy.ndarray], numpy.ndarray] = default_voice
            frequency: int = 1
            amplitude: numpy.ScalarType = default_amplitude
            duration_in_samples: int = samples_per_beat_rounded

            end_sample_index: int = 0

            if isinstance(note, Note):
                frequency = note.frequency
                if note.voice is not None:
                    voice = note.voice
                if note.amplitude is not None:
                    amplitude = note.amplitude
                duration_in_samples = note.duration_in_beats * samples_per_beat_rounded
            else:
                frequency: Hertz = note

            end_sample_index = start_sample_index + duration_in_samples

            beat_wave: numpy.ndarray = voice(
                get_sin_domain(start_sample_index, end_sample_index, frequency, sample_rate)
            ) * amplitude

            # beat_wave: numpy.ndarray = one_hertz_wave[::samples_per_frequency]

            # print(f"Difference: {end_sample_index - start_sample_index}")
            # print(f"one_hertz_wave: {one_hertz_wave.shape}, beat_wave: {beat_wave.shape}")
            # print(f"range: {len(range(start_sample_index * frequency, end_sample_index * frequency, frequency))}")

            result[start_sample_index:end_sample_index] += beat_wave

        """ pyplot.plot(result[start_sample_index:end_sample_index])
        pyplot.show()
        pyplot.close() """

    return result
