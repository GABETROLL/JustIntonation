import numpy
from frequency_ratios import simplify_fraction, product
from dataclasses import dataclass
from typing import Sequence, Callable, Optional, Union
# from matplotlib import pyplot

Hertz: type = int


class Fraction:
    def __init__(self, numerator: int, denominator: int) -> None:
        if not isinstance(numerator, int):
            raise TypeError(f"numerator must be int. Got: {numerator}, of type {type(numerator)}")
        if not isinstance(denominator, int):
            raise TypeError(f"denominator must be int. Got: {denominator}, of type {type(denominator)}")
        if denominator == 0:
            raise ValueError(f"denominator can't be 0 for a fraction. Got: {denominator}.")

        self.numerator = numerator
        self.denominator = denominator
    
    def __str__(self):
        return f"\{self.numerator} / {self.denominator}\\"

    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"

    def __mul__(self, other):
        """
        Returns `self` multiplied by `other`.
        
        if `other` is an instance of `Fraction`, this method will return the product of the two fractions
        (like how it's taught in elementary/primary school, these are the "Rational numbers").
        if `other` is anything else, this method will return a copy of `self`, with its
        numerator multiplied by `other`.
        """
        if isinstance(other, Fraction):
            return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
        return Fraction(self.numerator * other, self.denominator)

    def as_float(self) -> float:
        return self.numerator / self.denominator

@dataclass
class NoteRatio:
    other_note_id: int
    ratio: Fraction


class Note:
    def __init__(
        self,
        frequency: Hertz | Fraction | NoteRatio,
        voice: Optional[Callable[[numpy.ndarray], numpy.ndarray]] = None,
        amplitude: Union[Union[numpy.ScalarType], None] = None,
        duration_in_beats: int = 1,
        note_id: int = None,
    ) -> None:
        if note_id is not None and not isinstance(note_id, int):
            raise TypeError(f"Note's id must be an int. Got: {note_id}, of type: {type(note_id)}.")
        if not isinstance(frequency, (Hertz, Fraction, NoteRatio)):
            raise TypeError(f"Note's frequency must be an int or a Fraction (measured in Hertz), or a NoteRatio. Got: {frequency}, of type: {type(frequency)}.")
        if amplitude is not None and not isinstance(amplitude, numpy.ScalarType):
            raise TypeError(f"Note's voice must be a numpy.ScalarType. Got: {amplitude}, of type: {type(amplitude)}.")
        if not isinstance(duration_in_beats, int):
            raise TypeError(f"Note's duration_in_beats must be an int. Got: {duration_in_beats}, of type: {type(duration_in_beats)}.")

        self.id = note_id
        self.frequency = frequency
        self.voice = voice
        self.amplitude = amplitude
        self.duration_in_beats = duration_in_beats


"""
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
class Slide:
    start_frequency: Hertz | NoteRatio
    end_frequency: Hertz | NoteRatio
    voice: Optional[Callable[[numpy.ndarray], numpy.ndarray]] = None
    amplitude: Optional[float] = None # numpy.ScalarType, but dataclass doesn't allow it
    duration_in_beats: int = 1
    id: int = None

    @staticmethod
    def get_domain(duration_in_beats: int, start_frequency: int, end_frequency: int, sample_rate: int, samples_per_beat: int) -> numpy.ndarray:
        """
        Gives the domain x, such that numpy.sin(x) returns the wave
        that corresponds with a note that slides from `self.start_frequency` to `self.end_frequency`.

        (i think this is already made so that the slide seems linear on a piano)
        TODO: ALLOW FRACTIONS!
        """
        duration_in_samples: int = duration_in_beats * samples_per_beat

        u = start_frequency
        v = end_frequency

        base = (v / u) ** (1 / duration_in_samples)

        n = numpy.arange(duration_in_samples, dtype=float)
        n = base ** n
        n *= (1 / numpy.log(base)) * u * 2 * (numpy.pi / sample_rate)

        return n


@dataclass
class Melody:
    samples_per_beat: int
    notes: list[list[Hertz | Fraction | Note | Slide]]


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
    frequencies: Sequence[Hertz | Fraction],
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


def shaven_note(voice: Callable[[numpy.ndarray], numpy.ndarray], samples_to_shave: int) -> Callable[[numpy.ndarray], numpy.ndarray]:
    def inner(domain: numpy.ndarray) -> numpy.ndarray:
        result = voice(domain)

        # shave at left of result

        assert result.ndim == 1

        if len(result) <= samples_to_shave:
            return numpy.zeros(shape=(len(result),))

        # TODO: FINISH
        return result

    return inner


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


def get_sin_domain(start_sample_index: int, end_sample_index: int, frequency: int | Fraction, sample_rate: int) -> numpy.ndarray:
    # TODO: THS S CHEATNG!!! T (should be) PERFECT FRACTONS!
    if isinstance(frequency, Fraction):
        frequency = frequency.as_float()

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

    note_values: dict[int, Union[int, float]] = {}

    def _render_wave(list_of_beats: Sequence[Sequence[Hertz | Note | Slide | Fraction | Sequence]], samples_per_beat_rounded: int, sample_index: int):
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

                if isinstance(note, Slide) or isinstance(note, Note):
                    if isinstance(note, Note):
                        if isinstance(note.frequency, NoteRatio):

                            if note.frequency.other_note_id not in note_values:
                                raise LookupError(f"Note with other note id: {note.frequency.other_note_id} not found.")

                            frequency = note.frequency.ratio * note_values[note.frequency.other_note_id]
                        else:
                            # Wether `note.frequency` turns out to be a Fraction
                            # or an integer, the `get_sin_domain` later in this code
                            # should handle it.
                            frequency = note.frequency

                    note_values[note.id] = frequency

                    if note.voice is not None:
                        voice = note.voice
                    if note.amplitude is not None:
                        amplitude = note.amplitude
                    duration_in_samples = note.duration_in_beats * samples_per_beat_rounded
                else:
                    # Wether `note.frequency` turns out to be a Fraction
                    # or an integer, the `get_sin_domain` later in this code
                    # should handle it.
                    frequency = note

                end_sample_index = start_sample_index + duration_in_samples

                if isinstance(note, Slide):
                    domain: numpy.ndarray = note.get_domain(note.duration_in_beats, note.start_frequency, note.end_frequency, sample_rate, samples_per_beat_rounded)
                else:
                    # in here, `get_sin_domain` should handle both integer and fraction frequencies.
                    domain: numpy.ndarray = get_sin_domain(
                        start_sample_index, end_sample_index, frequency, sample_rate,
                    )

                print(frequency)

                beat_wave: numpy.ndarray = voice(domain) * amplitude
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
