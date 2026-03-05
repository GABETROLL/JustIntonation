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
    beats_per_minute: float
    notes: list[list[Hertz | Note]]

    @staticmethod
    def _beats_per_beat(beats: Sequence[Sequence[Hertz | Note | Sequence]]) -> int:
        print(f"{beats = }")

        sub_lengths: set[int] = set()

        for beat in beats:
            print(f"{beat = }, {sub_lengths = }")

            assert hasattr(beat, "__iter__") and hasattr(beat, "__len__")

            for sequence in beat:
                print(f"{sequence = }")

                if hasattr(sequence, "__iter__") and hasattr(sequence, "__len__"):
                    sub_length: int = Melody._beats_per_beat(sequence) * len(sequence)

                    print(f"{sub_length = }")

                    sub_lengths.add(sub_length)

                    print(f"{sub_lengths = }")

        sub_lengths: list[int] = list(sub_lengths)

        print(f"{sub_lengths = }")

        simplify_fraction(sub_lengths) # I appologize for making this algorithm so slow...

        print(f"{sub_lengths = }")

        result: int = product(sub_lengths)

        print(f"{result = }")

        return result

    @staticmethod
    def from_fractional_beats(
        notes: Sequence[Sequence[Hertz | Note | Sequence]],
        beats_per_beat: int | None = None,
        original_beat_index: int | None = None,
        out: list[list[Hertz | Note]] | None = None,
    ) -> tuple[tuple[Hertz | Note]]:
        """
        Unwraps music from "rational beats" into a Melody.

        Example with Cannon in D:

        this:
        [
            [D, [[A], [[[FS],[G]]], [A], [[[FS],[G]]]]],
            ...
        ]
        turns into:
        [
            [Note(D, duration_in_beats=8), Note(A, duration_in_beats=2)], [],
            [FS], [G],
            [Note(A, duration_in_beats=2)], [],
            [FS], [G],
            ...
        ]

        Explanation:

        list of beats --> [
            beat --> [
                D,                          # <-- 8 beats total
                list of beats --> [
                    beat --> [A],           # <-- 2 beats total
                    beat --> [
                        list of beats --> [
                            beat --> [FS],  # <-- 1 beat total
                            beat --> [G],   # <-- 1 beat total
                        ],
                    ],
                    beat --> [A],           # <-- 2 beats total
                    beat --> [
                        list of beats --> [
                            beat --> [FS],  # <-- 1 beat total
                            beat --> [G],   # <-- 1 beat total
                        ],
                    ],
                ],
            ],
            ...
        ]

        This:

        list of beats --> [             # 3 * 4 beats = 12 beats per beat. 2 beats * 12 beats per beat = 24 beats.
            beat --> [
                list of beats --> [     # 1 * 1 * 1 beat = 1 beat per beat. 3 beats * 1 beat per beat = 3 beats. 
                    [C], [C], [C],
                ],
            ],
            beat --> [
                list of beats --> [     # 1 * 1 * 1 * 1 beat = 1 beat pear beat. 4 beats * 1 beat per beat = 4 beats.
                    [D], [D], [D], [D],
                ],
            ],
        ]

        Turns into:

        [
            [Note(C, duration_in_beats=4)], [], [], [],
            [Note(C, duration_in_beats=4)], [], [], [],
            [Note(C, duration_in_beats=4)], [], [], [],
            [Note(D, duration_in_beats=3)], [], [],
            [Note(D, duration_in_beats=3)], [], [],
            [Note(D, duration_in_beats=3)], [], [],
            [Note(D, duration_in_beats=3)], [], [],
        ]
        """
        if beats_per_beat is None:
            beats_per_beat = Melody._beats_per_beat(notes) 

        if out is None:
            out = [[] for _ in range(beats_per_beat * len(notes))]
        
        if original_beat_index is None:
            original_beat_index = 0

        beat_index: int = original_beat_index

        print(f"{beats_per_beat = }, {out = }, len(out) = {len(out)} {original_beat_index = }, {beat_index = }")

        for local_beat_index, beat in enumerate(notes):
            beat_index = original_beat_index + local_beat_index * beats_per_beat

            print(f"{local_beat_index = }, {beat_index = }")

            for item in beat:

                print(f"{item = }")

                if hasattr(item, "__iter__") and hasattr(item, "__len__"):
                    Melody.from_fractional_beats(item, beats_per_beat // len(item), beat_index, out)
                elif isinstance(item, Note):
                    out[beat_index].append(
                        Note(item.frequency, item.voice, item.amplitude, item.duration_in_beats * beats_per_beat)
                    )
                else:
                    # Assume that if `item` is not a beat or a note, it must be a frequency.
                    # TODO: MAKE DURATON CORRECT!
                    out[beat_index].append(Note(item, duration_in_beats=beats_per_beat))

        return out


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


def other(domain: numpy.ndarray) -> numpy.ndarray:
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
    samples_per_beat_rounded: int = sample_rate * 60 // melody.beats_per_minute

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
            # TODO: MAKE PARAMETER !!!

            # beat_wave: numpy.ndarray = one_hertz_wave[::samples_per_frequency]

            # print(f"Difference: {end_sample_index - start_sample_index}")
            # print(f"one_hertz_wave: {one_hertz_wave.shape}, beat_wave: {beat_wave.shape}")
            # print(f"range: {len(range(start_sample_index * frequency, end_sample_index * frequency, frequency))}")

            result[start_sample_index:end_sample_index] += beat_wave

        """ pyplot.plot(result[start_sample_index:end_sample_index])
        pyplot.show()
        pyplot.close() """

    return result
