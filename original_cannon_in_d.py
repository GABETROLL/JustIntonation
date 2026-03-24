"""
      B   F#  C#
C   G   D   A   E   B
"""

from music_player import (
    numpy,
    Note, Melody, octaves,
    SAMPLE_RATE,
    violin_wave,
    render_wave
)

D2 = 144
E2 = D2 * 9 / 8
F_SHARP_2 = D2 * 5 / 4
G2 = D2 * 4 / 3
A2 = D2 * 3 / 2
B_FROM_D_2 = D2 * 5 / 3
B_FROM_E_2 = D2 * 27 / 16
C2 = D2 * 8 / 9
C_SHARP_2 = D2 * 15 / 16

D3, D4, D5, D6 = octaves(D2, 4)
E3, E4, E5 = octaves(E2, 3)
F_SHARP_3, F_SHARP_4, F_SHARP_5 = octaves(F_SHARP_2, 3)
G3, G4, G5 = octaves(G2, 3)
A3, A4, A5 = octaves(A2, 3)
B_FROM_D_3, B_FROM_D_4, B_FROM_D_5 = octaves(B_FROM_D_2, 3)
B_FROM_E_3, B_FROM_E_4, B_FROM_E_5 = octaves(B_FROM_E_2, 3)
C3, C4, C5, C6 = octaves(C2, 4)
C_SHARP_3, C_SHARP_4, C_SHARP_5, C_SHARP_6 = octaves(C_SHARP_2, 4)

AMPLITUDE = 0.15

THIRTY_SECOND_NOTES_PER_SECOND = 8
SAMPLES_PER_THIRTY_SECOND_NOTE = SAMPLE_RATE // THIRTY_SECOND_NOTES_PER_SECOND

BASS_VOICE = violin_wave
MELODY_VOICE = violin_wave

bass = Melody(
    SAMPLES_PER_THIRTY_SECOND_NOTE << 3,
    [
        [D3],
        [A2],
        [B_FROM_D_2],
        [F_SHARP_2],

        [G2],
        [D2],
        [G2],
        [A2],
    ],
)

violin_1 = Melody(
    SAMPLES_PER_THIRTY_SECOND_NOTE << 3,
    [
        [F_SHARP_5],
        [E5],
        [D5],
        [C_SHARP_5],

        [B_FROM_D_4],
        [A4],
        [B_FROM_D_4],
        [C_SHARP_5],

        [D5],
        [C_SHARP_5],
        [B_FROM_D_4],
        [A4],

        [G4],
        [F_SHARP_4],
        [G4],
        [E4],
    ],
)

violin_2 = Melody(
    SAMPLES_PER_THIRTY_SECOND_NOTE << 2,
    [
        [D4],
        [F_SHARP_4],
        [A4],
        [G4],
        [F_SHARP_4],
        [D4],
        [F_SHARP_4],
        [E4],

        [D4],
        [B_FROM_D_3],
        [D4],
        [A4],
        [G4],
        [B_FROM_D_4],
        [A4],
        [G4],

        [F_SHARP_4],
        [D4],
        [E4],
        [C_SHARP_5],
        [D5],
        [F_SHARP_5],
        [A5],
        [A4],
    ],
)

violin_3 = Melody(
    SAMPLES_PER_THIRTY_SECOND_NOTE << 1,
    [
        [Note(B_FROM_D_4, duration_in_beats=2)], [],
        [Note(G4, duration_in_beats=2)], [],
        [Note(A4, duration_in_beats=2)], [],
        [Note(F_SHARP_4, duration_in_beats=2)], [],
        [Note(D4, duration_in_beats=2)], [],
        [Note(D5, duration_in_beats=2)], [],
        [Note(D5, duration_in_beats=3)], [],
        [], [C_SHARP_5],

        [D5], [C_SHARP_5], [D5], [D4],
        [C_SHARP_4], [A4], [E4], [F_SHARP_4],
        [D4], [D5], [C_SHARP_5], [B_FROM_D_4],
        [C_SHARP_5], [F_SHARP_5], [A5], [B_FROM_D_5],

        [G5], [F_SHARP_5], [E5], [G5],
        [F_SHARP_5], [E5], [D5], [C_SHARP_5],
        [B_FROM_D_4], [A4], [G4], [F_SHARP_4],
        [E4], [G4], [F_SHARP_4], [E4],

        [D4], [E4], [F_SHARP_4], [G4],
        [A4], [E4], [A4], [G4],
        [F_SHARP_4], [B_FROM_D_4], [A4], [G4],
        [A4], [G4], [F_SHARP_4], [E4],
        # ?
        [D4], [B_FROM_D_3], [B_FROM_D_4], [C_SHARP_5],
        [D5], [C_SHARP_5], [B_FROM_D_4], [A4],
        [G4], [F_SHARP_4], [E4], [B_FROM_D_4],
        [A4], [B_FROM_D_4], [A4], [G4],
    ],
)

violin_4 = Melody(
    SAMPLES_PER_THIRTY_SECOND_NOTE << 2,
    [
        [F_SHARP_4], [F_SHARP_5],
        [Note(E5, duration_in_beats=2)], [],
        [], [D5],
        [Note(F_SHARP_5, duration_in_beats=2)], [],

        [Note(B_FROM_D_5, duration_in_beats=2)], [],
        [Note(A5, duration_in_beats=2)], [],
        [Note(B_FROM_D_5, duration_in_beats=2)], [],
        [Note(C_SHARP_6, duration_in_beats=2)], [],

        [D6], [D5],
        [Note(C_SHARP_5, duration_in_beats=2)], [],
        [], [B_FROM_D_4],
        [Note(D5, duration_in_beats=2)], [],

        [Note(D5, duration_in_beats=3)], [],
        [], [D5],
        [D5], [G5],
        [E5], [A5],
    ],
)

violin_5 = Melody(
    SAMPLES_PER_THIRTY_SECOND_NOTE,
    [
        [Note(A5, duration_in_beats=2)], [],
        [F_SHARP_5], [G5],
        [Note(A5, duration_in_beats=2)], [],
        [F_SHARP_5], [G5],
        [A5], [A4],
        [B_FROM_E_4], [C_SHARP_5],
        [D5], [E5],
        [F_SHARP_5], [G5],
        [Note(F_SHARP_5, duration_in_beats=2)], [],
        [D5], [E5],
        [Note(F_SHARP_5, duration_in_beats=2)], [],
        [F_SHARP_4], [G4],
        [A4], [B_FROM_D_4],
        [A4], [G4],
        [A4], [F_SHARP_4],
        [G4], [A4],

        [Note(G4, duration_in_beats=2)], [],
        [B_FROM_D_4], [A4],
        [Note(G4, duration_in_beats=2)], [],
        [F_SHARP_4], [E4],
        [F_SHARP_4], [E4],
        [D4], [E4],
        [F_SHARP_4], [G4],
        [A4], [B_FROM_D_4],
        [Note(G4, duration_in_beats=2)], [],
        [B_FROM_D_4], [A4],
        [Note(B_FROM_D_4, duration_in_beats=2)], [],
        [C_SHARP_5], [D5],
        [A4], [B_FROM_D_4], # ?
        [C_SHARP_5], [D5],
        [E5], [F_SHARP_5],
        [G5], [A5],         # ?

        [Note(F_SHARP_5, duration_in_beats=2)], [],
        [D5], [E5],
        [Note(F_SHARP_5, duration_in_beats=2)], [],
        [E5], [D4],
        [E5], [C_SHARP_5],
        [D5], [E5],
        [F_SHARP_5], [E5],
        [D5], [C_SHARP_5],
        [Note(D5, duration_in_beats=2)], [],
        [B_FROM_D_4], [C_SHARP_5],
        [Note(D5, duration_in_beats=2)], [],
        [D4], [E4], # ?
        [F_SHARP_4], [G4],
        [F_SHARP_4], [E4],
        [F_SHARP_4], [D5],
        [C_SHARP_5], [D5],
        [Note(B_FROM_D_4, duration_in_beats=2)], [],
        [D5], [C_SHARP_5],
        [Note(B_FROM_D_4, duration_in_beats=2)], [],
        [A4], [G4],
        [A4], [G4],
        [F_SHARP_4], [G4],
        [A4], [B_FROM_D_4],
        [C_SHARP_5], [D5],
        [Note(B_FROM_E_4, duration_in_beats=2)], [],
        [D5], [C_SHARP_5],
        [Note(D5, duration_in_beats=2)], [],
        [C_SHARP_5], [B_FROM_D_4],
        [C_SHARP_5], [D5],
        [E5], [D5],
        [C_SHARP_5], [D5],
        [B_FROM_D_4], [C_SHARP_5], # ?
    ],
)

violin_6 = Melody(
    SAMPLES_PER_THIRTY_SECOND_NOTE << 2,
    [
        [D5], [],
        [C_SHARP_5], [],
        [B_FROM_D_4], [],
        [D5], [],
        [D4], [],
        [D4], [],
        [D4], [],
        [E4], [],
        [], [A4],
        [], [A4],
        [], [F_SHARP_4],
        [], [A4],
        [], [G4],
        [], [F_SHARP_4],
        [], [G4],
        [], [E5],
    ]
)

violin_7_1_3 = Melody(
    SAMPLES_PER_THIRTY_SECOND_NOTE << 1,
    [
        [F_SHARP_5], [F_SHARP_4], [G4], [F_SHARP_4],
        [E4], [E5], [F_SHARP_5], [E5],
        [D5], [F_SHARP_4], [D4], [B_FROM_D_4],
        [A4], [A3], [G3], [A3],
        [B_FROM_D_3], [B_FROM_D_4], [C_SHARP_5], [B_FROM_D_4],
        [A4], [A3], [G3], [A3],
        [B_FROM_D_3], [B_FROM_D_4], [A4], [B_FROM_D_4],
        [C_SHARP_5], [C_SHARP_4], [B_FROM_E_3], [C_SHARP_4],
    ],
)

violin_7_2 = Melody(
    SAMPLES_PER_THIRTY_SECOND_NOTE << 1,
    [
        [F_SHARP_5], [F_SHARP_4], [G4], [F_SHARP_4],
        [E4], [E5], [F_SHARP_5], [E5],
        [D5], [F_SHARP_4], [D4], [B_FROM_D_4],
        [A4], [A3], [G3], [A3],
        [B_FROM_D_3], [B_FROM_D_4], [C_SHARP_5], [B_FROM_D_4],
        [C_SHARP_5], [A3], [G3], [A3],
        [B_FROM_D_3], [B_FROM_D_4], [A4], [B_FROM_D_4],
        [C_SHARP_5], [C_SHARP_4], [B_FROM_E_3], [C_SHARP_4], # ?
    ],
)

violin_8_1 = Melody(
    SAMPLES_PER_THIRTY_SECOND_NOTE << 1,
    [
        [D4], [D5], [E5], [D5],
        [C_SHARP_5], [C_SHARP_4], [B_FROM_D_3], [C_SHARP_4], # ?
        [B_FROM_D_3], [B_FROM_D_4], [A4], [B_FROM_D_4],
        [C_SHARP_5], [C_SHARP_4], [F_SHARP_4], [E4],

        [D4], [D5], [E5], [G5], # ?
        [F_SHARP_5], [F_SHARP_4], [A4], [F_SHARP_5],
        [D5], [G5], [F_SHARP_5], [G5],
        [E5], [A4], [G5], [A4], # ?
    ],
)

violin_8_2_3 = Melody(
    SAMPLES_PER_THIRTY_SECOND_NOTE << 1,
    [
        [D4], [D5], [E5], [D5],
        [C_SHARP_5], [C_SHARP_4], [D4], [C_SHARP_4], # ?
        [B_FROM_D_3], [B_FROM_D_4], [A4], [B_FROM_D_4],
        [C_SHARP_5], [C_SHARP_4], [F_SHARP_4], [E4],

        [D4], [D5], [E5], [G5], # ?
        [F_SHARP_5], [F_SHARP_4], [A4], [F_SHARP_5],
        [D5], [G5], [F_SHARP_5], [G5],
        [E5], [A4], [G5], [A4], # ?
    ],
)

violin_9 = Melody(
    SAMPLES_PER_THIRTY_SECOND_NOTE << 1,
    [
        [F_SHARP_4], [A4], [A4], [A4],
        [A4], [A4], [A4], [A4],
        [F_SHARP_4], [F_SHARP_4], [F_SHARP_4], [F_SHARP_4],
        [F_SHARP_4], [F_SHARP_4], [A4], [A4],

        [G4], [G4], [G4], [D5],
        [D5], [D5], [D5], [D5],
        [D5], [D5], [B_FROM_D_4], [B_FROM_D_4],
        [A4], [A4], [E5], [C_SHARP_5],
    ],
)

violin_10_1 = Melody(
    SAMPLES_PER_THIRTY_SECOND_NOTE << 1,
    [
        [A4], [F_SHARP_5], [F_SHARP_5], [F_SHARP_5],
        [E5], [E5], [E5], [E5],
        [D5], [D5], [D5], [D5],
        [A5], [A5], [A5], [A5],
        [B_FROM_D_5], [B_FROM_D_5], [B_FROM_D_5], [B_FROM_D_5],
        [A5], [A5], [A5], [A5],
        [B_FROM_D_5], [B_FROM_D_5], [B_FROM_D_5], [B_FROM_D_5],
        [C_SHARP_6], [C_SHARP_6], [C_SHARP_6], [C_SHARP_6],
    ]
)

violin_10_2_3 = Melody(
    SAMPLES_PER_THIRTY_SECOND_NOTE << 1,
    [
        [A4], [F_SHARP_5], [F_SHARP_5], [F_SHARP_5],
        [E5], [E5], [E5], [E5],
        [D5], [D5], [D5], [D5],
        [A5], [A5], [A5], [A5],
        [B_FROM_D_5], [B_FROM_D_5], [B_FROM_D_5], [B_FROM_D_5],
        [A5], [A5], [A5], [A5],
        [B_FROM_D_5], [B_FROM_D_5], [B_FROM_D_5], [B_FROM_D_5],
        [C_SHARP_6], [C_SHARP_5], [C_SHARP_5], [C_SHARP_5], # MISTAKE?
    ]
)

violin_11 = Melody(
    SAMPLES_PER_THIRTY_SECOND_NOTE,
    [
        [Note(D5, duration_in_beats=2)], [], [D4], [E4],
        [Note(F_SHARP_4, duration_in_beats=2)], [], [Note(D4, duration_in_beats=2)], [],
        [Note(C_SHARP_4, duration_in_beats=2)], [], [C_SHARP_5], [D5],
        [Note(E5, duration_in_beats=2)], [], [Note(C_SHARP_5, duration_in_beats=2)], [],
        [Note(B_FROM_D_4, duration_in_beats=2)], [], [B_FROM_D_3], [C_SHARP_4],
        [Note(D4, duration_in_beats=2)], [], [Note(B_FROM_D_3, duration_in_beats=2)], [],
        [Note(C_SHARP_4, duration_in_beats=2)], [], [A4], [G4],
        [Note(F_SHARP_4, duration_in_beats=2)], [], [Note(E4, duration_in_beats=2)], [],

        [Note(D4, duration_in_beats=2)], [], [G4], [F_SHARP_4],
        [Note(E4, duration_in_beats=2)], [], [Note(G4, duration_in_beats=2)], [], # ?
        [Note(F_SHARP_4, duration_in_beats=2)], [], [D4], [E4],
        [Note(F_SHARP_4, duration_in_beats=2)], [], [Note(A4, duration_in_beats=2)], [],
        [Note(G4, duration_in_beats=2)], [], [B_FROM_D_4], [A4],
        [Note(G4, duration_in_beats=2)], [], [Note(F_SHARP_4, duration_in_beats=2)], [],
        [Note(E4, duration_in_beats=2)], [], [A4], [G4], # ?
        [Note(F_SHARP_4, duration_in_beats=2)], [], [Note(E4, duration_in_beats=2)], [],

        [Note(F_SHARP_4, duration_in_beats=2)], [], [D5], [C_SHARP_5],
        [Note(D5, duration_in_beats=2)], [], [Note(F_SHARP_4, duration_in_beats=2)], [],
        [Note(A4, duration_in_beats=2)], [], [A4], [B_FROM_D_4],
        [Note(C_SHARP_5, duration_in_beats=2)], [], [Note(A4, duration_in_beats=2)], [],
        [Note(F_SHARP_4, duration_in_beats=2)], [], [D5], [E5], # ?
        [Note(F_SHARP_5, duration_in_beats=2)], [], [Note(D5, duration_in_beats=2)], [],
        [Note(F_SHARP_5, duration_in_beats=2)], [], [F_SHARP_5], [E5],
        [Note(D5, duration_in_beats=2)], [], [Note(C_SHARP_5, duration_in_beats=2)], [],

        [Note(B_FROM_D_4, duration_in_beats=2)], [], [B_FROM_D_4], [A4],
        [Note(B_FROM_D_4, duration_in_beats=2)], [], [Note(C_SHARP_5, duration_in_beats=2)], [], # ?
        [Note(D5, duration_in_beats=2)], [], [F_SHARP_5], [E5],
        [Note(D5, duration_in_beats=2)], [], [Note(F_SHARP_5, duration_in_beats=2)], [],
        [Note(G5, duration_in_beats=2)], [], [D5], [C_SHARP_5],
        [Note(B_FROM_D_4, duration_in_beats=2)], [], [Note(B_FROM_D_4, duration_in_beats=2)], [],
        [Note(A4, duration_in_beats=2)], [], [Note(E4, duration_in_beats=2)], [],
        [Note(A4, duration_in_beats=2)], [], [Note(A4, duration_in_beats=2)], [],
    ],
)

violin_12_1 = Melody(
    SAMPLES_PER_THIRTY_SECOND_NOTE << 1,
    [
        [Note(A4, duration_in_beats=6)], [], [], [],
        [], [], [Note(A4, duration_in_beats=2)], [],
        [Note(D4, duration_in_beats=6)], [], [], [],
        [], [], [Note(A4, duration_in_beats=2)], [],

        [Note(G4, duration_in_beats=4)], [], [], [],
        [Note(A4, duration_in_beats=4)], [], [], [],
        [Note(F_SHARP_4, duration_in_beats=2)], [], [Note(D4, duration_in_beats=2)], [],
        [Note(D4, duration_in_beats=3)], [], [], [C_SHARP_4],
    ],
)

violin_12_2_3 = Melody(
    SAMPLES_PER_THIRTY_SECOND_NOTE << 1,
    [
        [Note(A4, duration_in_beats=6)], [], [], [],
        [], [], [Note(A4, duration_in_beats=2)], [],
        [Note(D4, duration_in_beats=6)], [], [], [],
        [], [], [Note(A4, duration_in_beats=2)], [],

        [Note(G4, duration_in_beats=4)], [], [], [],
        [Note(A4, duration_in_beats=4)], [], [], [],
        [Note(G4, duration_in_beats=2)], [], [Note(D4, duration_in_beats=2)], [],
        [Note(D4, duration_in_beats=3)], [], [], [C_SHARP_4],
    ],
)

violin_13 = Melody(
    SAMPLES_PER_THIRTY_SECOND_NOTE << 1,
    [
        [Note(D4, duration_in_beats=2)], [], [Note(D5, duration_in_beats=2)], [],
        [Note(C_SHARP_5, duration_in_beats=4)], [], [], [],
        [Note(B_FROM_D_4, duration_in_beats=4)], [], [], [],
        [Note(A4, duration_in_beats=4)], [], [], [],

        [Note(D4, duration_in_beats=3)], [], [], [E4],
        [Note(F_SHARP_4, duration_in_beats=2)], [], [], [],
        [Note(B_FROM_D_4, duration_in_beats=4)], [], [], [],
        [Note(E4, duration_in_beats=3)], [], [], [E4],

        # 2

        [Note(F_SHARP_4, duration_in_beats=3)], [], [], [F_SHARP_5],
        [F_SHARP_5], [G5], [F_SHARP_5], [E4],
        [Note(D5, duration_in_beats=3)], [], [], [D5],
        [D5], [E4], [D5], [C_SHARP_5],

        [Note(B_FROM_D_4, duration_in_beats=4)], [], [], [],
        [Note(D5, duration_in_beats=4)], [], [], [],
        [D5], [C5], [B_FROM_D_4], [C5],
        [Note(A4, duration_in_beats=3)], [], [], [A4],

        # 3

        [Note(A4, duration_in_beats=3)], [], [], [A5],
        [A5], [B_FROM_D_5], [A5], [G5],
        [Note(F_SHARP_5, duration_in_beats=3)], [], [], [F_SHARP_5],
        [F_SHARP_5], [G5], [F_SHARP_5], [E4],

        [D5], [C5], [B_FROM_D_4], [C5],
        [Note(A4, duration_in_beats=3)], [], [], [A4],
        [Note(G4, duration_in_beats=2)], [], [Note(D5, duration_in_beats=2)], [],
        [Note(C_SHARP_5, duration_in_beats=3)], [], [], [C_SHARP_5],

        # 4

        [Note(D5, duration_in_beats=2)], [], [Note(D5, duration_in_beats=4)], [],
        [], [], [Note(C_SHARP_5, duration_in_beats=4)], [],
        [], [], [Note(B_FROM_D_4, duration_in_beats=4)], [],
        [], [], [Note(A4, duration_in_beats=4)], [],

        [], [], [Note(G4, duration_in_beats=4)], [],
        [], [], [Note(F_SHARP_4, duration_in_beats=5)], [],
        [], [], [], [E4], # ?
        [Note(E4, duration_in_beats=4)], [], [], [],
    ],
)

violin_14 = Melody(
    SAMPLES_PER_THIRTY_SECOND_NOTE << 2,
    [
        [F_SHARP_4], [Note(F_SHARP_5, duration_in_beats=2)],
        [], [E5],
        [D5], [Note(D6, duration_in_beats=2)],
        [], [C6],

        [Note(B_FROM_D_5, duration_in_beats=2)], [],
        [D6], [A5],
        [Note(B_FROM_D_5, duration_in_beats=2)], [],
        [Note(A5, duration_in_beats=2)], [],
    ],
)

violin_15 = Melody(
    SAMPLES_PER_THIRTY_SECOND_NOTE << 1,
    [
        [Note(A5, duration_in_beats=4)], [], [], [],
        [Note(A4, duration_in_beats=3)], [], [], [G4],
        [Note(F_SHARP_4, duration_in_beats=4)], [], [], [],
        [Note(F_SHARP_5, duration_in_beats=3)], [], [], [E5],

        [Note(D5, duration_in_beats=6)], [], [], [],
        [], [], [Note(D5, duration_in_beats=2)], [],
        [Note(D5, duration_in_beats=4)], [], [], [],
        [Note(C_SHARP_5, duration_in_beats=4)], [], [], [],
    ],
)

violin_16_1_2 = Melody(
    SAMPLES_PER_THIRTY_SECOND_NOTE << 2,
    [
        [D5], [D4],
        [C_SHARP_4], [C_SHARP_5],
        [B_FROM_D_4], [B_FROM_D_3],
        [A3], [A4],

        [G4], [G5],
        [F_SHARP_5], [F_SHARP_4],
        [E4], [B_FROM_D_4], # ?
        [E4], [E5],
    ],
)

violin_17_1 = Melody(
    SAMPLES_PER_THIRTY_SECOND_NOTE << 1,
    [
        [Note(F_SHARP_5, duration_in_beats=2)], [], [Note(F_SHARP_4, duration_in_beats=2)], [],
        [Note(E4, duration_in_beats=2)], [], [Note(E5, duration_in_beats=2)], [],
        [Note(D5, duration_in_beats=2)], [], [Note(D4, duration_in_beats=2)], [],
        [Note(C_SHARP_4, duration_in_beats=2)], [], [Note(C_SHARP_5, duration_in_beats=2)], [],

        [Note(B_FROM_D_4, duration_in_beats=2)], [], [Note(B_FROM_D_5, duration_in_beats=2)], [],
        [Note(A5, duration_in_beats=2)], [], [Note(A4, duration_in_beats=2)], [],
        [Note(G5, duration_in_beats=3)], [], [], [E5], # ?
        [Note(A4, duration_in_beats=2)], [], [Note(A4, duration_in_beats=2)], [],
    ],
)

end = Melody(
    SAMPLES_PER_THIRTY_SECOND_NOTE << 3,
    [
        [Note(D3, BASS_VOICE), A4, F_SHARP_5, D5],
    ],
)

SAMPLES_PER_QUARTER_NOTE = SAMPLES_PER_THIRTY_SECOND_NOTE << 3

SAMPLES_PER_BASS_SEQUENCE = 8 * SAMPLES_PER_QUARTER_NOTE

bass_wave = numpy.tile(
    render_wave(bass, SAMPLE_RATE, BASS_VOICE, AMPLITUDE),
    (28,)
)
# REPEAT 19 TIMES

violin_1_melodies = (violin_1, violin_2, violin_3, violin_4, violin_5, violin_6, violin_7_1_3, violin_8_1, violin_9, violin_10_1, violin_11, violin_12_1, violin_13, violin_14, violin_15, violin_16_1_2, violin_17_1)
violin_2_melodies = (violin_1, violin_2, violin_3, violin_4, violin_5, violin_6, violin_7_2, violin_8_2_3, violin_9, violin_10_2_3, violin_11, violin_12_2_3, violin_13, violin_14, violin_15, violin_16_1_2)
violin_3_melodies = (violin_1, violin_2, violin_3, violin_4, violin_5, violin_6, violin_7_2, violin_8_2_3, violin_9, violin_10_2_3, violin_11, violin_12_2_3, violin_13, violin_14, violin_15)

whole_violin_1, whole_violin_2, whole_violin_3 = tuple(
    numpy.pad(
        numpy.concatenate([
            render_wave(part, SAMPLE_RATE, MELODY_VOICE, AMPLITUDE)
            for part in melody
        ]),
        (SAMPLES_PER_BASS_SEQUENCE * (index + 1), 0)
    ) for index, melody in enumerate((violin_1_melodies, violin_2_melodies, violin_3_melodies))
)

end_wave = render_wave(
    end, SAMPLE_RATE, MELODY_VOICE, AMPLITUDE,
)

# print(SAMPLE_RATE, SAMPLES_PER_BEAT, SAMPLES_PER_BASS_SEQUENCE)
# print(bass_wave.shape, whole_violin_1.shape, whole_violin_2.shape, whole_violin_3.shape, end_wave.shape)

wave = numpy.concatenate((
    bass_wave + whole_violin_1 + whole_violin_2 + whole_violin_3,
    end_wave,
))
