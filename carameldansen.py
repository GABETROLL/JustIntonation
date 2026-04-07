"""
  D#  A#  F
B   F#  C#  G#
"""
from music_player import *

FS_1 = 16 * 3
DS_1 = int(FS_1 * 5 / 6)
B1 = int(FS_1 * 4 / 3)
AS_1 = int(FS_1 * 5 / 4)
CS_1 = int(FS_1 * 3 / 4)
F1 = int(FS_1 * 15 / 16)
GS_1 = int(FS_1 * 9 / 8)

FS_2, FS_3, FS_4, FS_5 = octaves(FS_1, 4)
DS_2, DS_3, DS_4, DS_5 = octaves(DS_1, 4)
B2, B3, B4, B5 = octaves(B1, 4)
AS_2, AS_3, AS_4, AS_5 = octaves(AS_1, 4)
CS_2, CS_3, CS_4, CS_5 = octaves(CS_1, 4)
F2, F3, F4, F5 = octaves(F1, 4)
GS_2, GS_3, GS_4, GS_5 = octaves(GS_1, 4)

CHORD_VOICE = trumpet

# TIMING IS 4 / 4, BPM = 60.
# One quarter-note per second.
SIXTY_FOURTH_NOTES_PER_SECOND = 10

SAMPLES_PER_BEAT = SAMPLE_RATE // SIXTY_FOURTH_NOTES_PER_SECOND


def intro_brass_bar(chord: Sequence[Hertz | Note]) -> tuple[tuple[Hertz | Note]]:
    return (
        notes(chord, voice=CHORD_VOICE, duration_in_beats=2), (),
        notes(chord, voice=CHORD_VOICE, duration_in_beats=2), (),
        notes(chord, voice=CHORD_VOICE, duration_in_beats=4), (),
        (), (),
        chord, notes(chord, voice=CHORD_VOICE, duration_in_beats=2),
        (), chord,
        notes(chord, voice=CHORD_VOICE, duration_in_beats=4), (),
        (), (),
    )


intro_brass = Melody(
    SAMPLES_PER_BEAT,
    (
        intro_brass_bar((AS_3, CS_4, FS_4)) + intro_brass_bar((CS_4, F4, GS_4))
        + intro_brass_bar((DS_4, FS_4, AS_4)) + intro_brass_bar((DS_4, FS_4, B4))
    ) * 2,
)

bass_intro = Melody(
    SAMPLES_PER_BEAT * 16,
    (
        (FS_2,),
        (CS_2,),
        (DS_2,),
        (B1,),
    ),
)

intro_square_wave = Melody(
    SAMPLES_PER_BEAT * 2,
    (
        (FS_4,),
        (GS_4,),
        (AS_4,),
        (B4,),

        # 0

        (((Note(CS_5, duration_in_beats=3),), ()),),
        (((), (Note(CS_5, duration_in_beats=3),)),),
        (),
        (((Note(CS_5, duration_in_beats=3),), (),),),
        (),
        (CS_5,),
        (DS_5,),
        (CS_5,),

        (),
        (),
        (),
        (),
        (CS_5,),
        (DS_5,),
        (CS_5,),
        (B4,),

        (((Note(AS_4, duration_in_beats=3),), ()),),
        (((), (Note(AS_4, duration_in_beats=3),)),),
        (),
        (((Note(AS_4, duration_in_beats=3),), (),),),
        (),
        (B4,),
        (AS_4,),
        (FS_4,),

        (),
        (),
        (),
        (),
        (FS_4,),
        (GS_4,),
        (AS_4,),
        (B4,),

        # 1

        (((Note(CS_5, duration_in_beats=3),), ()),),
        (((), (Note(CS_5, duration_in_beats=3),)),),
        (),
        (((Note(CS_5, duration_in_beats=3),), (),),),
        (),
        (),
        (),
        (),

        (),
        (),
        (),
        (),
        (),
        (),
        (),
        (),

        (),
        (),
        (),
        (),
        (),
        (),
        (),
        (),

        (),
        (),
        (),
        (),
        (),
        (),
        (),
        (),
    ),
)

square_wave_slide = Melody(
    SAMPLES_PER_BEAT * 16 * 2,
    [
        [Slide(FS_3, FS_5)],
    ],
)

main = [
    # 2

    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],

    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],

    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],

    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],

    # 3
    [AS_3, CS_4, FS_4, AS_4],
    [AS_3, CS_4, FS_4, AS_4],
    [AS_3, CS_4, FS_4, AS_4],
    [AS_3, CS_4, FS_4, AS_4],
    [AS_3, CS_4, FS_4],
    [AS_3, CS_4, FS_4, B4],
    [AS_3, CS_4, FS_4, FS_4],
    [AS_3, CS_4, FS_4, AS_4],

    [GS_3, CS_4, F4, GS_4],
    [GS_3, CS_4, F4, GS_4],
    [GS_3, CS_4, F4, GS_4],
    [GS_3, CS_4, F4, GS_4],
    [GS_3, CS_4, F4],
    [GS_3, CS_4, F4, AS_4],
    [GS_3, CS_4, F4, CS_4],
    [GS_3, CS_4, F4, GS_4],

    [DS_3, FS_3, AS_3, FS_4],
    [DS_3, FS_3, AS_3, FS_4],
    [DS_3, FS_3, AS_3, FS_4],
    [DS_3, FS_3, AS_3, FS_4],
    [DS_3, FS_3, AS_3],
    [DS_3, FS_3, AS_3, GS_4],
    [DS_3, FS_3, AS_3, DS_4],
    [DS_3, FS_3, AS_3, F4],

    [B2, DS_3, FS_3, FS_4],
    [B2, DS_3, FS_3, FS_4],
    [B2, DS_3, FS_3, FS_4],
    [B2, DS_3, FS_3, FS_4],
    [B2, DS_3, FS_3],
    [B2, DS_3, FS_3, F4],
    [B2, DS_3, FS_3, FS_4],
    [B2, DS_3, FS_3, CS_4],
]

chorus_1: list[list[int]] = [
    [AS_3, CS_4, FS_4, FS_4],
    [AS_3, CS_4, FS_4, FS_4],
    [AS_3, CS_4, FS_4, FS_4],
    [AS_3, CS_4, FS_4, FS_4],
    [AS_3, CS_4, FS_4, FS_4],
    [AS_3, CS_4, FS_4, FS_4],
    [AS_3, CS_4, FS_4, FS_4],
    [AS_3, CS_4, FS_4, FS_4],

    [AS_3, CS_4, FS_4, GS_4],
    [AS_3, CS_4, FS_4, AS_4],
    [AS_3, CS_4, FS_4, AS_4],
    [AS_3, CS_4, FS_4, AS_4],
    [AS_3, CS_4, FS_4, AS_4],
    [AS_3, CS_4, FS_4, GS_4],
    [AS_3, CS_4, FS_4, FS_4],
    [AS_3, CS_4, FS_4],

    [AS_3, CS_4, FS_4, FS_4],
    [AS_3, CS_4, FS_4, FS_4],
    [AS_3, CS_4, FS_4, FS_4],
    [AS_3, CS_4, FS_4, FS_4],
    [AS_3, CS_4, FS_4, FS_4],
    [AS_3, CS_4, FS_4, FS_4],
    [AS_3, CS_4, FS_4, FS_4],
    [AS_3, CS_4, FS_4, FS_4],

    [AS_3, CS_4, FS_4, AS_4],
    [AS_3, CS_4, FS_4, GS_4],
    [AS_3, CS_4, FS_4, GS_4],
    [AS_3, CS_4, FS_4, FS_4],
    [AS_3, CS_4, FS_4],
    [AS_3, CS_4, FS_4],
    [AS_3, CS_4, FS_4],
    [AS_3, CS_4, FS_4],

    [GS_3, CS_4, F4, F4], 
    [GS_3, CS_4, F4, F4], 
    [GS_3, CS_4, F4, DS_4], 
    [GS_3, CS_4, F4, CS_4], 
    [GS_3, CS_4, F4], 
    [GS_3, CS_4, F4], 
    [GS_3, CS_4, F4], 
    [GS_3, CS_4, F4],

    [GS_3, CS_4, F4], 
    [GS_3, CS_4, F4], 
    [GS_3, CS_4, F4], 
    [GS_3, CS_4, F4, CS_4], 
    [GS_3, CS_4, F4, CS_4], 
    [GS_3, CS_4, F4, CS_4], 
    [GS_3, CS_4, F4, DS_4],
    [GS_3, CS_4, F4, F4],

    [DS_3, FS_3, AS_3, FS_4],
    [DS_3, FS_3, AS_3, FS_4],
    [DS_3, FS_3, AS_3, DS_4],
    [DS_3, FS_3, AS_3, CS_4],
    [DS_3, FS_3, AS_3],
    [DS_3, FS_3, AS_3],
    [DS_3, FS_3, AS_3],
    [DS_3, FS_3, AS_3],

    [B2, DS_3, FS_3],
    [B2, DS_3, FS_3, CS_4],
    [B2, DS_3, FS_3, DS_4],
    [B2, DS_3, FS_3, CS_4],
    [B2, DS_3, FS_3, FS_4],
    [B2, DS_3, FS_3, FS_4],
    [B2, DS_3, FS_3, DS_4],
    [B2, DS_3, FS_3, CS_4],

    # 2B

    [AS_3, CS_4, FS_4, FS_4],
    [AS_3, CS_4, FS_4, FS_4],
    [AS_3, CS_4, FS_4, FS_4],
    [AS_3, CS_4, FS_4, FS_4],
    [AS_3, CS_4, FS_4, FS_4],
    [AS_3, CS_4, FS_4, FS_4],
    [AS_3, CS_4, FS_4, FS_4],
    [AS_3, CS_4, FS_4, FS_4],

    [AS_3, CS_4, FS_4, GS_4],
    [AS_3, CS_4, FS_4, AS_4],
    [AS_3, CS_4, FS_4, AS_4],
    [AS_3, CS_4, FS_4, AS_4],
    [AS_3, CS_4, FS_4, AS_4],
    [AS_3, CS_4, FS_4, GS_4],
    [AS_3, CS_4, FS_4, FS_4],
    [AS_3, CS_4, FS_4],

    [AS_3, CS_4, FS_4, FS_4],
    [AS_3, CS_4, FS_4, FS_4],
    [AS_3, CS_4, FS_4, FS_4],
    [AS_3, CS_4, FS_4, FS_4],
    [AS_3, CS_4, FS_4, FS_4],
    [AS_3, CS_4, FS_4, FS_4],
    [AS_3, CS_4, FS_4, FS_4],
    [AS_3, CS_4, FS_4, FS_4],

    [AS_3, CS_4, FS_4, CS_5],
    [AS_3, CS_4, FS_4, B4],
    [AS_3, CS_4, FS_4, B4],
    [AS_3, CS_4, FS_4, AS_4],
    [AS_3, CS_4, FS_4, AS_4],
    [AS_3, CS_4, FS_4],
    [AS_3, CS_4, FS_4],
    [AS_3, CS_4, FS_4],

    [GS_3, CS_4, F4, F4], 
    [GS_3, CS_4, F4, F4], 
    [GS_3, CS_4, F4, GS_4], 
    [GS_3, CS_4, F4, CS_4], 
    [GS_3, CS_4, F4], 
    [GS_3, CS_4, F4], 
    [GS_3, CS_4, F4], 
    [GS_3, CS_4, F4],

    [GS_3, CS_4, F4], 
    [GS_3, CS_4, F4], 
    [GS_3, CS_4, F4, CS_4], 
    [GS_3, CS_4, F4, CS_4], 
    [GS_3, CS_4, F4, CS_4], 
    [GS_3, CS_4, F4, CS_4],
    [GS_3, CS_4, F4, AS_4],
    [GS_3, CS_4, F4, GS_4],

    [AS_3, CS_4, FS_4, FS_4],
    [AS_3, CS_4, FS_4, FS_4],
    [AS_3, CS_4, FS_4],
    [AS_3, CS_4, FS_4],
    [AS_3, CS_4, FS_4],
    [AS_3, CS_4, FS_4],
    [AS_3, CS_4, FS_4],
    [AS_3, CS_4, FS_4],

    [AS_3, CS_4, FS_4],
    [AS_3, CS_4, FS_4],
    [AS_3, CS_4, FS_4, AS_4],
    [AS_3, CS_4, FS_4, AS_4],
    [AS_3, CS_4, FS_4, AS_4],
    [AS_3, CS_4, FS_4, AS_4],
    [AS_3, CS_4, FS_4, GS_4],
    [AS_3, CS_4, FS_4, GS_4],
]


"""melody = Melody(
    360,
    intro + chorus_1 + [
        [AS_3, CS_4, FS_4, CS_4],
        [AS_3, CS_4, FS_4, CS_4],
        [AS_3, CS_4, FS_4, AS_4],
        [AS_3, CS_4, FS_4, GS_4],
        [AS_3, CS_4, FS_4, FS_4],
        [AS_3, CS_4, FS_4, FS_4],
        [AS_3, CS_4, FS_4, FS_4],
        [AS_3, CS_4, FS_4, GS_4],

        [GS_3, CS_4, F4, GS_4],
        [GS_3, CS_4, F4, FS_4],
        [GS_3, CS_4, F4, GS_4],
        [GS_3, CS_4, F4, FS_4],
        [GS_3, CS_4, F4, GS_4],
        [GS_3, CS_4, F4, GS_4],
        [GS_3, CS_4, F4, AS_4],
        [GS_3, CS_4, F4, AS_4],

        [DS_3, FS_3, AS_3, DS_4],
        [DS_3, FS_3, AS_3, DS_4],
        [DS_3, FS_3, AS_3, AS_4],
        [DS_3, FS_3, AS_3, GS_4],
        [DS_3, FS_3, AS_3, FS_4],
        [DS_3, FS_3, AS_3, FS_4],
        [DS_3, FS_3, AS_3, FS_4],
        [DS_3, FS_3, AS_3, GS_4],

        [B2, DS_3, FS_3, GS_4],
        [B2, DS_3, FS_3, FS_4],
        [B2, DS_3, FS_3, GS_4],
        [B2, DS_3, FS_3, AS_4],
        [B2, DS_3, FS_3, GS_4],
        [B2, DS_3, FS_3, GS_4],
        [B2, DS_3, FS_3, FS_4],
        [B2, DS_3, FS_3, FS_4],

        [AS_3, CS_4, FS_4, CS_4],
        [AS_3, CS_4, FS_4, CS_4],
        [AS_3, CS_4, FS_4, AS_4],
        [AS_3, CS_4, FS_4, GS_4],
        [AS_3, CS_4, FS_4, FS_4],
        [AS_3, CS_4, FS_4, FS_4],
        [AS_3, CS_4, FS_4, FS_4],
        [AS_3, CS_4, FS_4, GS_4],

        [GS_3, CS_4, F4, GS_4],
        [GS_3, CS_4, F4, FS_4],
        [GS_3, CS_4, F4, GS_4],
        [GS_3, CS_4, F4, FS_4],
        [GS_3, CS_4, F4, GS_4],
        [GS_3, CS_4, F4, GS_4],
        [GS_3, CS_4, F4, AS_4],
        [GS_3, CS_4, F4, AS_4],

        [DS_3, FS_3, AS_3, CS_5],
        [DS_3, FS_3, AS_3, CS_5],
        [DS_3, FS_3, AS_3, B4],
        [DS_3, FS_3, AS_3, AS_4],
        [DS_3, FS_3, AS_3, FS_4],
        [DS_3, FS_3, AS_3, FS_4],
        [DS_3, FS_3, AS_3, FS_4],
        [DS_3, FS_3, AS_3, GS_4],

        [B2, DS_3, FS_3, GS_4],
        [B2, DS_3, FS_3, GS_4],
        [B2, DS_3, FS_3, AS_4],
        [B2, DS_3, FS_3, AS_4],
        [B2, DS_3, FS_3, GS_4],
        [B2, DS_3, FS_3, GS_4],
        [B2, DS_3, FS_3, FS_4],
        [B2, DS_3, FS_3, FS_4],

        [AS_3, CS_4, FS_4, GS_4],
        [AS_3, CS_4, FS_4, GS_4],
        [AS_3, CS_4, FS_4, GS_4],
        [AS_3, CS_4, FS_4, GS_4],
        [AS_3, CS_4, FS_4, GS_4],
        [AS_3, CS_4, FS_4, AS_4],
        [AS_3, CS_4, FS_4, CS_4],
        [AS_3, CS_4, FS_4, CS_4],

        [GS_3, CS_4, F4],
        [GS_3, CS_4, F4],
        [GS_3, CS_4, F4],
        [GS_3, CS_4, F4],
        [GS_3, CS_4, F4],
        [GS_3, CS_4, F4],
        [GS_3, CS_4, F4],
        [GS_3, CS_4, F4],

        [DS_3, FS_3, AS_3, GS_4],
        [DS_3, FS_3, AS_3, GS_4],
        [DS_3, FS_3, AS_3, GS_4],
        [DS_3, FS_3, AS_3, GS_4],
        [DS_3, FS_3, AS_3, GS_4],
        [DS_3, FS_3, AS_3, AS_4],
        [DS_3, FS_3, AS_3, CS_4],
        [DS_3, FS_3, AS_3, CS_4],

        [B2, DS_3, FS_3, CS_4],
        [B2, DS_3, FS_3, DS_4],
        [B2, DS_3, FS_3, CS_4],
        [B2, DS_3, FS_3],
        [B2, DS_3, FS_3],
        [B2, DS_3, FS_3],
        [B2, DS_3, FS_3],
        [B2, DS_3, FS_3],

        [AS_3, CS_4, FS_4, AS_4],
        [AS_3, CS_4, FS_4, AS_4],
        [AS_3, CS_4, FS_4, AS_4],
        [AS_3, CS_4, FS_4, AS_4],
        [AS_3, CS_4, FS_4, AS_4],
        [AS_3, CS_4, FS_4, CS_5],
        [AS_3, CS_4, FS_4, AS_4],
        [AS_3, CS_4, FS_4, GS_4],

        [GS_3, CS_4, F4],
        [GS_3, CS_4, F4],
        [GS_3, CS_4, F4],
        [GS_3, CS_4, F4],
        [GS_3, CS_4, F4],
        [GS_3, CS_4, F4],
        [GS_3, CS_4, F4],
        [GS_3, CS_4, F4],

        [DS_3, FS_3, AS_3, GS_4],
        [DS_3, FS_3, AS_3, GS_4],
        [DS_3, FS_3, AS_3, GS_4],
        [DS_3, FS_3, AS_3, GS_4],
        [DS_3, FS_3, AS_3, GS_4],
        [DS_3, FS_3, AS_3, AS_4],
        [DS_3, FS_3, AS_3, CS_4],
        [DS_3, FS_3, AS_3, CS_4],

        [B2, DS_3, FS_3, CS_4],
        [B2, DS_3, FS_3, DS_4],
        [B2, DS_3, FS_3, CS_4],
        [B2, DS_3, FS_3],
        [B2, DS_3, FS_3],
        [B2, DS_3, FS_3],
        [B2, DS_3, FS_3],
        [B2, DS_3, FS_3, CS_4],
    ] + chorus_1
)"""

SQUARE_WAVE_AMPLITUDE = 0.3

intro_brass_wave = render_wave(intro_brass, SAMPLE_RATE, trumpet, 0.1)
intro_square_wave_wave = render_wave(intro_square_wave, SAMPLE_RATE, square_wave, SQUARE_WAVE_AMPLITUDE)
bass_intro_wave = render_wave(bass_intro, SAMPLE_RATE, trumpet, 0.07)
square_wave_slide_wave = render_wave(square_wave_slide, SAMPLE_RATE, square_wave, SQUARE_WAVE_AMPLITUDE)

wave = numpy.concatenate(
    (
        numpy.pad(
            bass_intro_wave,
            (len(intro_square_wave_wave) - len(bass_intro_wave), 0),
        ) + numpy.pad(
            intro_brass_wave,
            (len(intro_square_wave_wave) - len(intro_brass_wave), 0),
        ) + intro_square_wave_wave,
        square_wave_slide_wave,
    ),
)
