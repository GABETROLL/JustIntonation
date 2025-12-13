from dataclasses import dataclass

Hertz: type = float


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



StartOrStopPlaying: type = bool

START: StartOrStopPlaying = True
STOP: StartOrStopPlaying = False


@dataclass
class FrequencyCommand:
"""Describes when a frequency should either start or stop playing."""
    command_frame: int
    command: StartOrStopPlaying
    frequency: Hertz
    amplitude: float


def transform_music(music_as_ratios: MusicAsRatios) -> list[FrequencyCommand]:
    """
    Reads music from ratios format, and returns it as a list of FrequencyCommand.
    """
    pass
