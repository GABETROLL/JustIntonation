import numpy
from frequency_ratios import simplify_fraction, product
from dataclasses import dataclass
from typing import Sequence, Callable, Optional
# from matplotlib import pyplot

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
    samples_per_beat: int
    notes: list[list[Hertz | Note]]


def octaves(note: int, n: int) -> tuple[int, ...]:
    """
    Returns the next `n` octaves of `note` ABOVE `note`, in a tuple.

    The 0th item in the resulting tuple is note * 2,
    the second is note * 4, ..., and the last element is
    note * 2 ** n.

    Example:
    octaves(288) = (576, 1152, 2304)
    """
    return tuple(note * 2 ** m for m in range(1, n + 1))


def notes(
    frequencies: Sequence[Hertz],
    voice: Callable[[numpy.ndarray], numpy.ndarray] | None = None,
    amplitude: float | None = None,
    duration_in_beats: int = 1,
) -> tuple[Note, ...]:
    return tuple(Note(f, voice=voice, amplitude=amplitude, duration_in_beats=duration_in_beats) for f in frequencies)


def _dampen(samples: int) -> numpy.ndarray:
    return numpy.arange(samples - 1, -1, -1) / samples


def trumpet(domain: numpy.ndarray) -> numpy.ndarray:
    return numpy.sin(domain) + numpy.sin(2 * domain) / 2 + numpy.sin(3 * domain) / 3 \
        + numpy.sin(4 * domain) / 4 + numpy.sin(5 * domain) / 5 + numpy.sin(6 * domain) / 6


def square_wave(domain: numpy.ndarray) -> numpy.ndarray:
    return (
        numpy.sin(domain) + numpy.sin(3 * domain) / 3 + numpy.sin(5 * domain) / 5
         + numpy.sin(7 * domain) / 7 + numpy.sin(9 * domain) / 9
         + numpy.sin(11 * domain) / 11 + numpy.sin(13 * domain) / 13
    ) / 7


def triangle(domain: numpy.ndarray) -> numpy.ndarray:
    return (
        -numpy.cos(domain) - numpy.cos(3 * domain) / 9 - numpy.cos(5 * domain) / 25
        - numpy.cos(7 * domain) / 49 - numpy.cos(9 * domain) / 81 - numpy.cos(11 * domain) / 121
    ) / 4


def sine_wave(domain: numpy.ndarray) -> numpy.ndarray:
    return numpy.sin(domain)


def piano_wave(domain: numpy.ndarray) -> numpy.ndarray:
    result = numpy.sin(domain) * 0.6 + numpy.sin(2 * domain) * 0.04
    result += result * result * result
    return result


def dampened_piano_wave(domain: numpy.ndarray, amplitude: float = 1.0) -> numpy.ndarray:
    return piano_wave(domain) * _dampen(domain.size) * amplitude


def violin_wave(domain: numpy.ndarray, amplitude: float = 1.0) -> numpy.ndarray:
    HARMONICS_DB = [-33, -38, -51, -55, -54, -65, -61, -65, -71, -81, -76, -78, -78, -80, -78, -90, -83, -81, None, -79, -86]
    harmonics_pressure = [(10 ** ((h + 20) / 20)) * amplitude if h is not None else 0 for h in HARMONICS_DB]

    print(harmonics_pressure, sum(harmonics_pressure))

    wave = numpy.zeros(domain.shape)
    
    for harmonic_index, harmonic_volume in enumerate(harmonics_pressure):
        if harmonic_volume is None:
            continue

        wave += harmonic_volume * numpy.sin((harmonic_index + 1) * domain)

    size_sqrt: numpy.float_ = numpy.sqrt(domain.size)

    wave *= numpy.sqrt(numpy.arange(domain.size)) / size_sqrt
    wave *= numpy.sqrt(numpy.arange(domain.size - 1, -1, -1)) / size_sqrt
    wave *= 2

    # (assuming the domain is a 1D ndarray, this can be done)

    return wave


def get_sin_domain(start_sample_index: int, end_sample_index: int, frequency: int, sample_rate: int) -> numpy.ndarray:
    return numpy.arange(start_sample_index, end_sample_index) * frequency % sample_rate * 2 * (numpy.pi / sample_rate)


def render_wave(
    melody: Melody, sample_rate: int,
    default_voice: Callable[[numpy.ndarray], numpy.ndarray], default_amplitude: numpy.ScalarType = 1.0
) -> numpy.ndarray:
    amount_of_beats: int = len(melody.notes)
    result: numpy.ndarray = numpy.zeros((melody.samples_per_beat * amount_of_beats,))

    # one_hertz_wave: numpy.ndarray = voice(
    #     numpy.arange(sample_rate) * 2 * numpy.pi / sample_rate
    # )

    # print(f"result: {result.shape}, one_hertz_wave: {one_hertz_wave.shape}")

    def _render_wave(list_of_beats: Sequence[Sequence[Hertz | Note | Sequence]], samples_per_beat_rounded: int, sample_index: int):
        for beat_index, beat in enumerate(list_of_beats):
            start_sample_index: int = sample_index + samples_per_beat_rounded * beat_index

            for note in beat:
                # note is a Sequence, and, so,
                # i'm assuming that it's another list of beats!
                if hasattr(note, "__len__") and hasattr(note, "__iter__"):
                    _render_wave(note, samples_per_beat_rounded // len(note), start_sample_index)

                    continue

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
                # TODO: MAKE PARAMETER !!!
                # TODO: CHANGE

                # beat_wave: numpy.ndarray = one_hertz_wave[::samples_per_frequency]

                # print(f"Difference: {end_sample_index - start_sample_index}")
                # print(f"one_hertz_wave: {one_hertz_wave.shape}, beat_wave: {beat_wave.shape}")
                # print(f"range: {len(range(start_sample_index * frequency, end_sample_index * frequency, frequency))}")

                result[start_sample_index:end_sample_index] += beat_wave

        """ pyplot.plot(result[start_sample_index:end_sample_index])
        pyplot.show()
        pyplot.close() """

    _render_wave(melody.notes, melody.samples_per_beat, 0)

    return result
