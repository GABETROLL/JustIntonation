"""
            G#  D#  A#
  D   A   E   B   F#  C#
Bb  F   C   G   D
      Ab  Eb
"""

from music_player import *

BEATS_PER_MINUTE = 500

C1 = 45 * 3 / 4
A1 = C1 * 5 / 3
A_FLAT_1 = C1 * 8 / 5
F1 = C1 * 4 / 3
D_FROM_F_1 = C1 * 10 / 9
B_FLAT_FROM_F_1 = C1 * 16 / 9
E_FLAT_1 = C1 * 6 / 5
E1 = C1 * 5 / 4
G1 = C1 * 3 / 2
G_SHARP_FROM_E_1 = C1 * 25 / 16
B1 = C1 * 15 / 8
D_FROM_G_1 = C1 * 9 / 8
D_SHARP_FROM_B_1 = C1 * 75 / 64
F_SHARP_FROM_B_1 = C1 * 45 / 32
A_SHARP_FROM_F_SHARP_1 = C1 * 225 / 128
C_SHARP_FROM_F_SHARP_1 = C1 * 135 / 128
# (5 / 4) * (3 / 2) * (3 / 2) * (3 / 2) = 135 / 128


C2, C3, C4, C5, C6, C7, C8 = octaves(C1, 7)
A2, A3, A4, A5, A6, A7 = octaves(A1, 6)
A_FLAT_2, A_FLAT_3, A_FLAT_4, A_FLAT_5, A_FLAT_6, A_FLAT_7 = octaves(A_FLAT_1, 6)
F2, F3, F4, F5, F6, F7 = octaves(F1, 6)
D_FROM_F_2, D_FROM_F_3, D_FROM_F_4, D_FROM_F_5, D_FROM_F_6, D_FROM_F_7 = octaves(D_FROM_F_1, 6)
B_FLAT_FROM_F_2, B_FLAT_FROM_F_3, B_FLAT_FROM_F_4, B_FLAT_FROM_F_5, B_FLAT_FROM_F_6, B_FLAT_FROM_F_7 = octaves(B_FLAT_FROM_F_1, 6)
E_FLAT_2, E_FLAT_3, E_FLAT_4, E_FLAT_5, E_FLAT_6, E_FLAT_7 = octaves(E_FLAT_1, 6)
E2, E3, E4, E5, E6, E7 = octaves(E1, 6)
G2, G3, G4, G5, G6, G7 = octaves(G1, 6)
G_SHARP_FROM_E_2, G_SHARP_FROM_E_3, G_SHARP_FROM_E_4, G_SHARP_FROM_E_5, G_SHARP_FROM_E_6, G_SHARP_FROM_E_7 = octaves(G_SHARP_FROM_E_1, 6)
B2, B3, B4, B5, B6, B7 = octaves(B1, 6)
D_FROM_G_2, D_FROM_G_3, D_FROM_G_4, D_FROM_G_5, D_FROM_G_6, D_FROM_G_7 = octaves(D_FROM_G_1, 6)
D_SHARP_FROM_B_2, D_SHARP_FROM_B_3, D_SHARP_FROM_B_4, D_SHARP_FROM_B_5, D_SHARP_FROM_B_6, D_SHARP_FROM_B_7 = octaves(D_SHARP_FROM_B_1, 6)
F_SHARP_FROM_B_2, F_SHARP_FROM_B_3, F_SHARP_FROM_B_4, F_SHARP_FROM_B_5, F_SHARP_FROM_B_6, F_SHARP_FROM_B_7 = octaves(F_SHARP_FROM_B_1, 6)
A_SHARP_FROM_F_SHARP_2, A_SHARP_FROM_F_SHARP_3, A_SHARP_FROM_F_SHARP_4, A_SHARP_FROM_F_SHARP_5, A_SHARP_FROM_F_SHARP_6, A_SHARP_FROM_F_SHARP_7 = octaves(A_SHARP_FROM_F_SHARP_1, 6)
C_SHARP_FROM_F_SHARP_2, C_SHARP_FROM_F_SHARP_3, C_SHARP_FROM_F_SHARP_4, C_SHARP_FROM_F_SHARP_5, C_SHARP_FROM_F_SHARP_6, C_SHARP_FROM_F_SHARP_7 = octaves(C_SHARP_FROM_F_SHARP_1, 6)

repeated_three = [
    notes((C2, C3,     C4, G4), duration_in_beats=2), (),
    notes((C4, E4), duration_in_beats=2), (),
    notes((G1, G2,     C4, G4), duration_in_beats=2), (),
    (C4, E4), notes((C4, G4), duration_in_beats=2),
    notes((C2, C3), duration_in_beats=2), (C4, G4),
    notes((C4, E4), duration_in_beats=2), (),
    notes((G1, G2,     C4, G4), duration_in_beats=2), (),
    notes((C4, E4), duration_in_beats=2), (),

    notes((A_FLAT_1, A_FLAT_2,     C4, E_FLAT_4), duration_in_beats=2), (),
    notes((C4, A_FLAT_4), duration_in_beats=4), (),
    notes((E_FLAT_1, E_FLAT_2), duration_in_beats=2), (),
    notes((C4, E_FLAT_4), duration_in_beats=8), (),
    notes((A_FLAT_1, A_FLAT_2), duration_in_beats=2), (),
    (), (),
    notes((E_FLAT_1, E_FLAT_2), duration_in_beats=2), (),
    (), (),

    notes((B_FLAT_FROM_F_1, B_FLAT_FROM_F_2,     B_FLAT_FROM_F_3, F4), duration_in_beats=2), (),
    notes((B_FLAT_FROM_F_3, D_FROM_F_4), duration_in_beats=2), (),
    notes((F1, F2,                               B_FLAT_FROM_F_3, F4), duration_in_beats=2), (),
    (B_FLAT_FROM_F_3, D_FROM_F_4), notes((B_FLAT_FROM_F_3, F4), duration_in_beats=2),
    notes((B_FLAT_FROM_F_1, B_FLAT_FROM_F_2), duration_in_beats=2), (B_FLAT_FROM_F_3, F4),
    notes((B_FLAT_FROM_F_3, D_FROM_F_4), duration_in_beats=2), (),
    notes((F1, F2,                               B_FLAT_FROM_F_3, F4), duration_in_beats=2), (),
    notes((B_FLAT_FROM_F_3, D_FROM_F_4), duration_in_beats=2), (),

    notes((F1, F2,                                 C4, F4), duration_in_beats=2), (),
    notes((F_SHARP_FROM_B_1, F_SHARP_FROM_B_2,     C4, F_SHARP_FROM_B_4), duration_in_beats=4), (),
    (), (),
    notes((G1, G2,                                 B3, G4), duration_in_beats=8), (),
    (), (),
    (), (),
    (), (),
    (), (),

    notes((C2, C3,     C4, G4), duration_in_beats=2), (),
    notes((C4, E4), duration_in_beats=2), (),
    notes((G1, G2,     C4, G4), duration_in_beats=2), (),
    (C4, E4), notes((C4, G4), duration_in_beats=2),
    notes((C2, C3), duration_in_beats=2), (C4, G4),
    notes((C4, E4), duration_in_beats=2), (),
    notes((G1, G2,     C4, G4), duration_in_beats=2), (),
    notes((C4, E4), duration_in_beats=2), (),

    notes((A_FLAT_1, A_FLAT_2,     C4, E_FLAT_4), duration_in_beats=2), (),
    notes((C4, A_FLAT_4), duration_in_beats=4), (),
    notes((E_FLAT_1, E_FLAT_2), duration_in_beats=2), (),
    notes((C4, E_FLAT_4), duration_in_beats=8), (),
    notes((A_FLAT_1, A_FLAT_2), duration_in_beats=2), (),
    (), (),
    notes((E_FLAT_1, E_FLAT_2), duration_in_beats=2), (),
    (), (),

    notes((B_FLAT_FROM_F_1, B_FLAT_FROM_F_2,     B_FLAT_FROM_F_3, F4), duration_in_beats=2), (),
    notes((B_FLAT_FROM_F_3, D_FROM_F_4), duration_in_beats=2), (),
    notes((F1, F2,                               B_FLAT_FROM_F_3, F4), duration_in_beats=2), (),
    (B_FLAT_FROM_F_3, D_FROM_F_4), notes((B_FLAT_FROM_F_3, F4), duration_in_beats=2),
    notes((B_FLAT_FROM_F_1, B_FLAT_FROM_F_2), duration_in_beats=2), (B_FLAT_FROM_F_3, F4),
    notes((B_FLAT_FROM_F_3, D_FROM_F_4), duration_in_beats=2), (),
    notes((F1, F2,                               B_FLAT_FROM_F_3, F4), duration_in_beats=2), (),
    notes((B_FLAT_FROM_F_3, D_FROM_F_4), duration_in_beats=2), (),
]

main_melody = [
    notes((C2, C3,         G4, E5), duration_in_beats=2), (),
    notes((G3, C4, E4,     F_SHARP_FROM_B_4, D_SHARP_FROM_B_5), duration_in_beats=2), (),
    notes((G1, G2,         G4, E5), duration_in_beats=2), (),
    notes((G3, C4, E4,     F_SHARP_FROM_B_4, D_SHARP_FROM_B_5), duration_in_beats=2), (),
    notes((C2, C3,         G4, E5), duration_in_beats=2), (),
    notes((G3, C4, E4), duration_in_beats=2) + (F_SHARP_FROM_B_4, D_SHARP_FROM_B_5), notes((F4, D_FROM_F_5), duration_in_beats=3),
    notes((G1, G2), duration_in_beats=2), (),
    notes((G3, C4, E4,     F4, A_FLAT_4), duration_in_beats=2), (),

    notes((F1, F2,         F4, A4), duration_in_beats=2), (),
    notes((F3, A3, C4,     F4, C5), duration_in_beats=2), (),
    notes((C1, C2,         F4, D_FROM_F_5), duration_in_beats=2), (),
    notes((F3, A3, C4), duration_in_beats=2) + notes((F4, C5), duration_in_beats=8), (),
    notes((F1, F2), duration_in_beats=2), (),
    notes((F3, A3, C4), duration_in_beats=2), (),
    notes((C1, C2), duration_in_beats=2), (),
    notes((F3, A3, C4,     F_SHARP_FROM_B_4, D_SHARP_FROM_B_5), duration_in_beats=2), (),

    notes((C2, C3,         G4, E5), duration_in_beats=2), (),
    notes((G3, C4, E4,     G4, E5), duration_in_beats=2), (),
    notes((G1, G2,         G4, E5), duration_in_beats=2), (), # CORRECTED.
    notes((G3, C4, E4,     G4, E5), duration_in_beats=2), (),
    notes((C2, C3,         G4, E5), duration_in_beats=2), (),
    notes((G3, C4, E4), duration_in_beats=2) + (F_SHARP_FROM_B_4, D_SHARP_FROM_B_5), notes((F4, D_FROM_F_5), duration_in_beats=3),
    notes((G1, G2), duration_in_beats=2), (),
    notes((G3, C4, E4,     F4, B_FLAT_FROM_F_4), duration_in_beats=2), (),

    notes((G1, G2,                     G4, B4), duration_in_beats=2), (),
    notes((G3, B3, D_FROM_G_4,         G4, D_FROM_G_5), duration_in_beats=2), (),
    notes((D_FROM_G_1, D_FROM_G_1,     G4, E5), duration_in_beats=2), (),
    notes((G3, B3, D_FROM_G_4), duration_in_beats=2) + notes((G4, D_FROM_G_5), duration_in_beats=4), (),
    notes((G1, G2), duration_in_beats=2), (),
    notes((G1, G2), duration_in_beats=2) + notes((G4, D_FROM_G_5), duration_in_beats=4), (),
    notes((A1, A2), duration_in_beats=2), (),
    notes((B1, B2,                     F_SHARP_FROM_B_4, D_SHARP_FROM_B_5), duration_in_beats=2), (),

    notes((C2, C3,         G4, E5), duration_in_beats=2), (),
    notes((G3, C4, E4,     F_SHARP_FROM_B_4, D_SHARP_FROM_B_5), duration_in_beats=2), (),
    notes((G1, G2,         G4, E5), duration_in_beats=2), (),
    notes((G3, C4, E4,     F_SHARP_FROM_B_4, D_SHARP_FROM_B_5), duration_in_beats=2), (),
    notes((C2, C3,         G4, E5), duration_in_beats=2), (),
    notes((G3, C4, E4), duration_in_beats=2) + (F_SHARP_FROM_B_4, D_SHARP_FROM_B_5), notes((F4, D_FROM_F_5), duration_in_beats=3),
    notes((G1, G2), duration_in_beats=2), (),
    notes((G3, C4, E4,     F4, A_FLAT_4), duration_in_beats=2), (),

    notes((F1, F2,         F4, A4), duration_in_beats=2), (),
    notes((F3, A3, C4,     F4, C5), duration_in_beats=2), (),
    notes((C1, C2,         F4, D_FROM_F_5), duration_in_beats=2), (),
    notes((F3, A3, C4), duration_in_beats=2) + notes((F4, C5), duration_in_beats=4), (),
    notes((F1, F2), duration_in_beats=2), (),
    notes((F3, A3, C4,     F4, C5), duration_in_beats=2), (),
    notes((C1, C2,         F4, D_FROM_F_5), duration_in_beats=2), (),
    notes((F3, A3, C4,     F_SHARP_FROM_B_4, D_SHARP_FROM_B_5), duration_in_beats=2), (),

    notes((C2, C3,                 G4, E5), duration_in_beats=2), (),
    notes((G3, C4, E4), duration_in_beats=2) + notes((G4, E5), duration_in_beats=4), (),
    notes((G1, G2), duration_in_beats=2), (),
    notes((G3, C4, E4,             G4, E5), duration_in_beats=2), (),
    notes((G1, G2,                 G4, D_FROM_G_5), duration_in_beats=2), (),
    notes((G3, B3, D_FROM_G_4), duration_in_beats=2) + notes((G4, D_FROM_G_5), duration_in_beats=4), (),
    notes((D_FROM_G_1, D_FROM_G_2), duration_in_beats=2), (),
    notes((G3, B3, D_FROM_G_4,     G4, D_FROM_G_5), duration_in_beats=2), (),

    notes((C2, C3), duration_in_beats=2) + notes((G4, C5), duration_in_beats=8), (),
    notes((G3, C4, E4), duration_in_beats=2), (),
    notes((G1, G2), duration_in_beats=2), (),
    notes((G3, C4, E4), duration_in_beats=2), (),
    notes((C2, C3), duration_in_beats=2), (),
    notes((G1, G2,     E5, C6), duration_in_beats=2), (),
    notes((A1, A2,     F5, D_FROM_F_6), duration_in_beats=2), (),
    notes((B1, B2,     F_SHARP_FROM_B_5, D_SHARP_FROM_B_6), duration_in_beats=2), (),

    # 2

    notes((C2, C3,         G5, E6), duration_in_beats=2), (),
    notes((G3, C4, E4,     F_SHARP_FROM_B_5, D_SHARP_FROM_B_6), duration_in_beats=2), (),
    notes((G1, G2,         G5, E6), duration_in_beats=2), (),
    notes((G3, C4, E4,     F_SHARP_FROM_B_5, D_SHARP_FROM_B_6), duration_in_beats=2), (),
    notes((C2, C3,         G5, E6), duration_in_beats=2), (),
    notes((G3, C4, E4), duration_in_beats=2) + (F_SHARP_FROM_B_5, D_SHARP_FROM_B_6), notes((F5, D_FROM_F_6), duration_in_beats=3),
    notes((G1, G2), duration_in_beats=2), (),
    notes((G3, C4, E4,     F5, A_FLAT_5), duration_in_beats=2), (),

    notes((F1, F2,         F5, A5), duration_in_beats=2), (),
    notes((F3, A3, C4,     F5, C6), duration_in_beats=2), (),
    notes((C1, C2,         F5, D_FROM_F_6), duration_in_beats=2), (),
    notes((F3, A3, C4), duration_in_beats=2) + notes((F5, C6), duration_in_beats=4), (),
    notes((F1, F2), duration_in_beats=2), (),
    notes((F3, A3, C4,     F5, C6), duration_in_beats=2), (),
    notes((C1, C2,         F5, D_FROM_F_6), duration_in_beats=2), (),
    notes((F3, A3, C4,     F_SHARP_FROM_B_5, D_SHARP_FROM_B_6), duration_in_beats=2), (),

    notes((C2, C3,         G5, E6), duration_in_beats=2), (),
    notes((G3, C4, E4,     F_SHARP_FROM_B_5, D_SHARP_FROM_B_6), duration_in_beats=2), (),
    notes((G1, G2,         G5, E6), duration_in_beats=2), (),
    notes((G3, C4, E4,     F_SHARP_FROM_B_5, D_SHARP_FROM_B_6), duration_in_beats=2), (),
    notes((C2, C3,         G5, E6), duration_in_beats=2), (),
    notes((G3, C4, E4), duration_in_beats=2) + (F_SHARP_FROM_B_5, D_SHARP_FROM_B_6), notes((G5, E6), duration_in_beats=3),
    notes((G1, G2), duration_in_beats=2), (G5, E6),
    notes((G3, C4, E4,     G5, B_FLAT_FROM_F_5), duration_in_beats=2), (), # This may sound wolfish...

    notes((G1, G2,                     G5, D_FROM_G_6), duration_in_beats=2), (),
    notes((G3, B3, D_FROM_G_4,         G5, D_FROM_G_6), duration_in_beats=2), (),
    notes((D_FROM_G_1, D_FROM_G_2,     G5, E6), duration_in_beats=2), (),
    notes((G3, B3, D_FROM_G_4), duration_in_beats=2) + notes((G5, D_FROM_G_6), duration_in_beats=8), (),
    notes((G1, G2), duration_in_beats=2), (),
    notes((G1, G2), duration_in_beats=2), (),
    notes((F1, F2), duration_in_beats=2), (),
    notes((E1, E2,                     F_SHARP_FROM_B_5, D_SHARP_FROM_B_6), duration_in_beats=2), (),

    notes((C2, C3,         G5, E6), duration_in_beats=2), (),
    notes((G3, C4, E4,     F_SHARP_FROM_B_5, D_SHARP_FROM_B_6), duration_in_beats=2), (),
    notes((G1, G2,         G5, E6), duration_in_beats=2), (),
    notes((G3, C4, E4,     F_SHARP_FROM_B_5, D_SHARP_FROM_B_6), duration_in_beats=2), (),
    notes((C2, C3,         G5, E6), duration_in_beats=2), (),
    notes((G3, C4, E4), duration_in_beats=2) + (F_SHARP_FROM_B_5, D_SHARP_FROM_B_6), notes((F5, D_FROM_F_6), duration_in_beats=3),
    notes((G1, G2), duration_in_beats=2), (),
    notes((G3, C4, E4,     F5, A_FLAT_5), duration_in_beats=2), (),

    notes((F1, F2,         F5, A5), duration_in_beats=2), (),
    notes((F3, A3, C4,     F5, C6), duration_in_beats=2), (),
    notes((C1, C2,         F5, D_FROM_F_6), duration_in_beats=2), (),
    notes((F3, A3, C4), duration_in_beats=2) + notes((F5, C6), duration_in_beats=4), (),
    notes((F1, F2), duration_in_beats=2), (),
    notes((F3, A3, C4,     F5, C6), duration_in_beats=2), (),
    notes((C1, C2,         F5, D_FROM_F_6), duration_in_beats=2), (),
    notes((F3, A3, C4,     F_SHARP_FROM_B_5, D_SHARP_FROM_B_6), duration_in_beats=2), (),

    notes((C2, C3,                 G5, E6), duration_in_beats=2), (),
    notes((G3, C4, E4), duration_in_beats=2) + notes((G5, E6), duration_in_beats=4), (),
    notes((G1, G2), duration_in_beats=2), (),
    notes((G3, C4, E4,             G5, E6), duration_in_beats=2), (),
    notes((G1, G2,                 G5, D_FROM_G_6), duration_in_beats=2), (),
    notes((G3, B3, D_FROM_G_4), duration_in_beats=2) + notes((G5, D_FROM_G_6), duration_in_beats=4), (),
    notes((D_FROM_G_1, D_FROM_G_2), duration_in_beats=2), (),
    notes((G3, B3, D_FROM_G_4,     G5, D_FROM_G_6), duration_in_beats=2), (),

    notes((C2, C3), duration_in_beats=2) + notes((G5, C6), duration_in_beats=4), (),
    notes((G3, C4, E4), duration_in_beats=2), (),
    notes((G1, G2), duration_in_beats=2) + notes((E5, G5), duration_in_beats=4), (),
    notes((G3, C4, E4), duration_in_beats=2), (),
    notes((C2, C3,         E5, C6), duration_in_beats=2), (), # CORRECTED.
    notes((C2, C3,         E5, C6), duration_in_beats=2), (), # CORRECTED.
    notes((C2, C3,         E5, C6), duration_in_beats=2), (), # CORRECTED.
    (), (),

    # 3
    *repeated_three,

    notes((F1, F2,                                 C4, F4), duration_in_beats=2), (),
    notes((F_SHARP_FROM_B_1, F_SHARP_FROM_B_2,     C4, F_SHARP_FROM_B_4), duration_in_beats=4), (),
    (), (),
    notes((G1, G2,                                 B3, G4), duration_in_beats=4), (),
    (), (),
    notes((G1, G2,                                 B3, G4), duration_in_beats=2), (),
    notes((G1, G2,                                 B3, G4), duration_in_beats=4), (),
    (), (),

    # 4

    notes((C2, C3,         E5, C6), duration_in_beats=2), (),
    notes((G3, C4, E4,     G5), duration_in_beats=2), (),
    notes((G1, G2,         E5, C6), duration_in_beats=2), (),
    notes((G3, C4, E4), duration_in_beats=2) + (G5,), notes((E5, C6), duration_in_beats=2),
    notes((C2, C3), duration_in_beats=2), (E5, C6),
    notes((G3, C4, E4,     G5), duration_in_beats=2), (),
    notes((G1, G2,         E5, C6), duration_in_beats=2), (),
    notes((G3, C4, E4,     G5), duration_in_beats=2), (),

    notes((A_FLAT_1, A_FLAT_2,        E_FLAT_5, C6), duration_in_beats=2), (),
    notes((A_FLAT_3, C4, E_FLAT_4,    A_FLAT_5), duration_in_beats=2), (),
    notes((E_FLAT_1, E_FLAT_2,        E_FLAT_5, C6), duration_in_beats=2), (),
    notes((A_FLAT_3, C4, E_FLAT_4), duration_in_beats=2) + (A_FLAT_5,), notes((E_FLAT_5, C6), duration_in_beats=2),
    notes((A_FLAT_1, A_FLAT_2), duration_in_beats=2), (E_FLAT_5, C6),
    notes((A_FLAT_3, C4, E_FLAT_4,    A_FLAT_5), duration_in_beats=2), (),
    notes((E_FLAT_1, E_FLAT_2,        E_FLAT_5, C6), duration_in_beats=2), (),
    notes((A_FLAT_3, C4, E_FLAT_4,    A_FLAT_5), duration_in_beats=2), (),

    notes((B_FLAT_FROM_F_1, B_FLAT_FROM_F_2), duration_in_beats=2), (),
    notes((B_FLAT_FROM_F_3, D_FROM_F_4, F4,    D_FROM_F_5, B_FLAT_FROM_F_5), duration_in_beats=2), (),
    notes((F1, F2,                             D_FROM_F_5, B_FLAT_FROM_F_5), duration_in_beats=2), (),
    notes((B_FLAT_FROM_F_3, D_FROM_F_4, F4), duration_in_beats=2) + (F5,), notes((D_FROM_F_5, B_FLAT_FROM_F_5), duration_in_beats=2),
    notes((B_FLAT_FROM_F_1, B_FLAT_FROM_F_2), duration_in_beats=2), (D_FROM_F_5, B_FLAT_FROM_F_5),
    notes((B_FLAT_FROM_F_3, D_FROM_F_4, F4,    F5), duration_in_beats=2), (),
    notes((F1, F2,                             D_FROM_F_5, B_FLAT_FROM_F_5), duration_in_beats=2), (),
    notes((B_FLAT_FROM_F_3, D_FROM_F_4, F4,    F5), duration_in_beats=2), (),

    notes((G1, G2,     D_FROM_F_5, B_FLAT_FROM_F_5), duration_in_beats=2), (),
    notes((G3, B3, D_FROM_G_4), duration_in_beats=2) + notes((D_FROM_F_5, B_FLAT_FROM_F_5), duration_in_beats=4), (),
    notes((D_FROM_G_1, D_FROM_G_2), duration_in_beats=2), (),
    notes((G3, B3, D_FROM_G_4), duration_in_beats=2) + notes((D_FROM_G_5, B5), duration_in_beats=4), (),
    notes((G1, G2), duration_in_beats=2), (),
    notes((G1, G2,    D_FROM_G_5, B5), duration_in_beats=2), (),
    notes((A1, A2), duration_in_beats=2) + notes((D_FROM_G_5, B5), duration_in_beats=4), (),
    notes((B1, B2), duration_in_beats=2), (),

    notes((C2, C3), duration_in_beats=2), (),
    notes((G3, C4, E4,     E5, C6), duration_in_beats=2), (),
    notes((G1, G2,         E5, C6), duration_in_beats=2), (),
    notes((G3, C4, E4), duration_in_beats=2) + (G5,), notes((E5, C6), duration_in_beats=2),
    notes((C2, C3), duration_in_beats=2), (E5, C6),
    notes((G3, C4, E4,     G5), duration_in_beats=2), (),
    notes((G1, G2,         E5, C6), duration_in_beats=2), (),
    notes((G3, C4, E4,     G5), duration_in_beats=2), (),

    notes((A_FLAT_1, A_FLAT_2), duration_in_beats=2), (),
    notes((A_FLAT_3, C4, E_FLAT_4,    E_FLAT_5, C6), duration_in_beats=2), (),
    notes((E_FLAT_1, E_FLAT_2,        E_FLAT_5, C6), duration_in_beats=2), (),
    notes((A_FLAT_3, C4, E_FLAT_4), duration_in_beats=2) + (A_FLAT_5,), notes((E_FLAT_5, C6), duration_in_beats=2),
    notes((A_FLAT_1, A_FLAT_2), duration_in_beats=2), (E_FLAT_5, C6),
    notes((A_FLAT_3, C4, E_FLAT_4,    A_FLAT_5), duration_in_beats=2), (),
    notes((E_FLAT_1, E_FLAT_2,        E_FLAT_5, C6), duration_in_beats=2), (),
    notes((A_FLAT_3, C4, E_FLAT_4,    A_FLAT_5), duration_in_beats=2), (),

    notes((B_FLAT_FROM_F_1, B_FLAT_FROM_F_2), duration_in_beats=2), (),
    notes((B_FLAT_FROM_F_3, D_FROM_F_4, F4,    D_FROM_F_5, B_FLAT_FROM_F_5), duration_in_beats=2), (),
    notes((F1, F2,                             D_FROM_F_5, B_FLAT_FROM_F_5), duration_in_beats=2), (),
    notes((B_FLAT_FROM_F_3, D_FROM_F_4, F4), duration_in_beats=2) + (F5,), notes((D_FROM_F_5, B_FLAT_FROM_F_5), duration_in_beats=2),
    notes((B_FLAT_FROM_F_1, B_FLAT_FROM_F_2), duration_in_beats=2), (D_FROM_F_5, B_FLAT_FROM_F_5),
    notes((B_FLAT_FROM_F_3, D_FROM_F_4, F4,    F5), duration_in_beats=2), (),
    notes((F1, F2,                             D_FROM_F_5, B_FLAT_FROM_F_5), duration_in_beats=2), (),
    notes((B_FLAT_FROM_F_3, D_FROM_F_4, F4,    F5), duration_in_beats=2), (),

    notes((G1, G2,     D_FROM_F_5, B_FLAT_FROM_F_5), duration_in_beats=2), (),
    notes((G3, B3, D_FROM_G_4), duration_in_beats=2) + notes((D_FROM_F_5, B_FLAT_FROM_F_5), duration_in_beats=4), (),
    notes((D_FROM_G_1, D_FROM_G_2), duration_in_beats=2), (),
    notes((G3, B3, D_FROM_G_4), duration_in_beats=2) + notes((D_FROM_G_5, B5), duration_in_beats=4), (),
    notes((G1, G2), duration_in_beats=2), (),
    notes((G1, G2), duration_in_beats=2), (),
    notes((G1, G2), duration_in_beats=4), (),
    (), (),
]

third_hand = Melody(
    BEATS_PER_MINUTE,
    [
        # 6

        (), (),
        (E4, C5), (G4,),
        (E4, C5), (),
        (G4,), (E4, C5),
        (), (G4,),
        (E4, C5), (),
        notes((G4,), duration_in_beats=2), (),
        (E4, C5), (),

        (), (),
        (C5, A4), (F4,),
        (C5, A4), (),
        (F4,), (C5, A4),
        (), (F4,),
        (C5, A4), (),
        notes((F4,), duration_in_beats=2), (),
        (C5, A4), (),

        (), (),
        (E4, C5), (G4,),
        (E4, C5), (),
        (G4,), (E4, C5),
        (), (E4, C5),
        (G4,), (),
        notes((E4, C5), duration_in_beats=2), (),
        (G4,), (),

        (), (),
        (D_FROM_G_4, B4), (G4,),
        (D_FROM_G_4, B4), (),
        (G4,), (D_FROM_G_4, B4),
        (), (D_FROM_G_4, B4),
        (G4,), (),
        notes((D_FROM_G_4, B4), duration_in_beats=2), (),
        (G4,), (),

        (), (),
        (E4, C5), (G4,),
        (E4, C5), (),
        (G4,), (E4, C5),
        (), (E4, C5),
        (G4,), (),
        notes((E4, C5), duration_in_beats=2), (),
        (G4,), (),

        (), (),
        (F4, C5), (A4,),
        (F4, C5), (),
        (A4,), (F4, C5),
        (), (F4, C5),
        (A4,), (),
        notes((F4, C5), duration_in_beats=2), (),
        (A4,), (),

        (), (),
        (E4, C5), (G4,),
        notes((E4, C5), duration_in_beats=2), (),
        (G4,), (D_FROM_G_4, B4),
        (), (D_FROM_G_4, B4),
        (G4,), (),
        notes((D_FROM_G_4, B4), duration_in_beats=2), (),
        (G4,), (),

        (), (),
        (E4, C5), (G4,),
        notes((E4, C5), duration_in_beats=2), (),
        (G4,), (E4, C5),
        (), (E4,),
        (G4,), (), # Add C5 as well?
        notes((E4,), duration_in_beats=2), (),
        (), (),

        # 7

        (), (),
        (), (),
        (), (),
        (), (),
        (), (),
        (), (),
        (), (),
        (), (),

        (), (),
        (), (),
        (), (),
        (), (),
        (), (),
        (G4,), (G_SHARP_FROM_E_4,),
        (A4,), (A_SHARP_FROM_F_SHARP_4,),
        (B4,), (C5,),

        (C_SHARP_FROM_F_SHARP_5,), (),
        (), (),
        (), (),
        (), (),
        (), (),
        (), (),
        (), (),
        (), (),

        (), (),
        (), (),
        (), (),
        (), (),
        (), (),
        (A_SHARP_FROM_F_SHARP_4,), (B4,),
        (C5,), (C_SHARP_FROM_F_SHARP_5,),
        (D_FROM_G_5,), (D_SHARP_FROM_B_5,),

        (E5,), (),
        (), (),
        (), (),
        (), (),
        (), (),
        (), (),
        (), (),
        (), (),

        (), (),
        (), (),
        (), (),
        (), (),
        (), (),
        (B4,), (C5,),
        (C_SHARP_FROM_F_SHARP_5,), (D_FROM_G_5,),
        (D_SHARP_FROM_B_5,), (E5,),

        (F5,), (),
        (), (),
        (), (),
        (), (),
        (), (),
        (), (),
        (), (),
        (), (),

        (), (),
        (), (),
        (), (),
        (), (),
        (), (),
        (C5,), (C_SHARP_FROM_F_SHARP_5,),
        (D_FROM_G_5,), (D_SHARP_FROM_B_5,),
        (E5,), (F5,),

        # 8

        (), (),
        (), (),
        (), (),
        (), (),
        (), (),
        (), (),
        (), (),
        (), (),

        (), (),
        (), (),
        (), (),
        (), (),
        (), (),
        (), (),
        (), (),
        (), (),

        (), (),
        (), (),
        (), (),
        (), (),
        (), (),
        (), (),
        (), (),
        (), (),

        (), (),
        (), (),
        (), (),
        (), (),
        (), (),
        (), (),
        (), (),
        (), (),

        (), (),
        (), (),
        (), (),
        (), (),
        (), (),
        (), (),
        (), (),
        (), (),

        (), (),
        (), (),
        (), (),
        (), (),
        (), (),
        (), (),
        (), (),
        (), (),

        (), (),
        (), (),
        (), (),
        (), (),
        (), (),
        (), (),
        (), (),
        (), (),

        (), (),
        (), (),
        (), (),
        (), (),
        (), (),
        (), (),
        (), (),
        (), (),

        # 9

        (), (),
        (C6,), (B5,),
        (A_SHARP_FROM_F_SHARP_5,), (A5,),
        (G_SHARP_FROM_E_5,), (G5,),
        (F_SHARP_FROM_B_5,), (F5,),
        (E5,), (D_SHARP_FROM_B_5,),
        (D_FROM_G_5,), (C_SHARP_FROM_F_SHARP_5,),
        (C5,), (B4,),

        (), (),
        (A5,), (G_SHARP_FROM_E_5,),
        (G5,), (F_SHARP_FROM_B_5,),
        (F5,), (E5,),
        (D_SHARP_FROM_B_5,), (D_FROM_G_5,),
        (C_SHARP_FROM_F_SHARP_5,), (C5,),
        (B4,), (A_SHARP_FROM_F_SHARP_4,),
        (A4,), (G_SHARP_FROM_E_4,),

        (), (),
        (G5,), (F_SHARP_FROM_B_5,),
        (F5,), (E5,),
        (D_SHARP_FROM_B_5,), (D_FROM_G_5,),
        (C_SHARP_FROM_F_SHARP_5,), (C5,),
        (B4,), (A_SHARP_FROM_F_SHARP_4,),
        (A4,), (G_SHARP_FROM_E_4,),
        (G4,), (F_SHARP_FROM_B_4,),

        (F4,), (F_SHARP_FROM_B_4,),
        (G4,), (G_SHARP_FROM_E_4,),
        (A4,), (A_SHARP_FROM_F_SHARP_4,),
        (B4,), (C5,),
        (C_SHARP_FROM_F_SHARP_5,), (D_FROM_G_5,),
        (D_SHARP_FROM_B_5,), (E5,),
        (F5,), (F_SHARP_FROM_B_5,),
        (G5,), (G_SHARP_FROM_E_5,),

        (Note(A5, duration_in_beats=2),), (),
        (Note(C6, duration_in_beats=2),), (),
        (Note(C6, duration_in_beats=2),), (),
        (Note(E6, duration_in_beats=2),), (),
        (Note(D_SHARP_FROM_B_6, duration_in_beats=2),), (),
        (Note(C_SHARP_FROM_F_SHARP_6, duration_in_beats=2),),  (),
        (Note(C6, duration_in_beats=2),), (),
        (Note(B5, duration_in_beats=2),), (),

        (A_SHARP_FROM_F_SHARP_5,), (A5,),
        (G_SHARP_FROM_E_5,), (G5,),
        (F_SHARP_FROM_B_5,), (F5,),
        (F_SHARP_FROM_B_5,), (G5,),
        (G_SHARP_FROM_E_5,), (A5,),
        (A_SHARP_FROM_F_SHARP_5,), (B5,),
        (C6,), (C_SHARP_FROM_F_SHARP_6,),
        (D_FROM_G_6,), (D_SHARP_FROM_B_6,),

        (Note(E6, duration_in_beats=2),), (),
        (Note(F6, duration_in_beats=2),), (),
        (Note(F6, duration_in_beats=2),), (),
        (Note(G6, duration_in_beats=2),), (),
        (Note(G6, duration_in_beats=2),), (),
        (Note(F6, duration_in_beats=2),), (),
        (Note(E6, duration_in_beats=2),), (),
        (Note(D_FROM_G_6, duration_in_beats=2),), (),

        (Note(C_SHARP_FROM_F_SHARP_6, duration_in_beats=2),), (),
        (Note(C6, duration_in_beats=2),), (),
        (Note(B5, duration_in_beats=2),), (),
        (Note(A_SHARP_FROM_F_SHARP_5, duration_in_beats=2),), (),
        (), (),
        (), (),
        (), (),
        (), (),

        # 10

        notes((B4, B5), duration_in_beats=2), (),
        notes((B4, B5), duration_in_beats=4), (),
        (), (),
        notes((B4, B5), duration_in_beats=4), (),
        (), (),
        notes((C5, C6), duration_in_beats=2), (), # s t really ths note?
        notes((B4, B5), duration_in_beats=4), (),
        (), (),

        (C6,), (C_SHARP_FROM_F_SHARP_6,),
        (D_FROM_G_6,), (D_SHARP_FROM_B_6,),
        (E6,), (F6,),
        (F_SHARP_FROM_B_6,), (G6,),
        (G_SHARP_FROM_E_6,), (A6,),
        (A_SHARP_FROM_F_SHARP_6,), (B6,),
        (C7,), (C_SHARP_FROM_F_SHARP_7,),
        (D_FROM_G_7,), (D_SHARP_FROM_B_7,),

        (E7,), (F7,),
        (F_SHARP_FROM_B_7,), (G7,),
        (G_SHARP_FROM_E_7,), (A7,),
        (A_SHARP_FROM_F_SHARP_7,), (B7,),
        (C8,), (),
        (), (),
        (), (),
        (), (),
    ],
)

melody_1 = Melody(
    BEATS_PER_MINUTE,
    [
        notes((G1, G2,     E4, C5), duration_in_beats=2), (),
        notes((A1, A2,     F4, D_FROM_F_5), duration_in_beats=2), (),
        notes((B1, B2,     F_SHARP_FROM_B_4, D_SHARP_FROM_B_5), duration_in_beats=2), (),

        # 1 - 4
        *main_melody,
    ]
)

melody_2 = Melody(
    BEATS_PER_MINUTE,
    [
        # 5 - 8
        *main_melody,

        # 9
        *repeated_three,

        notes((G1, G2), duration_in_beats=2), (),
        notes((G1, G2), duration_in_beats=4), (),
        (), (),
        notes((G1, G2), duration_in_beats=4), (),
        (), (),
        notes((G_SHARP_FROM_E_1, G_SHARP_FROM_E_2), duration_in_beats=2), (),
        notes((G1, G2), duration_in_beats=2), (),
        (), (),

        # 10

        notes((G1, G2), duration_in_beats=2), (),
        notes((G1, G2), duration_in_beats=4), (),
        (), (),
        notes((G1, G2), duration_in_beats=4), (),
        (), (),
        notes((A_FLAT_1, A_FLAT_2), duration_in_beats=2), (),
        notes((G1, G2), duration_in_beats=2), (),
        (), (),

        notes((G1, G2, B4, B5), duration_in_beats=4), (),
        (), (),
        notes((A_FLAT_1, A_FLAT_2, C5, C6), duration_in_beats=2), (),
        notes((G1, G2, B4, B5), duration_in_beats=2), (),
        (), (),
        notes((A_FLAT_1, A_FLAT_2, C5, C6), duration_in_beats=2), (),
        notes((G1, G2, B4, B5), duration_in_beats=2), (),
        (), (),

        notes((A_FLAT_1, A_FLAT_2, C5, C6), duration_in_beats=2), (),
        notes((G1, G2, B4, B5), duration_in_beats=2), (),
        (), (),
        notes((A_FLAT_1, A_FLAT_2, C5, C6), duration_in_beats=2), (),
        notes((G1, G2, B4, B5), duration_in_beats=2), (),
        (), (),
        (), (),
        (), (),
    ],
)

SAMPLES_PER_MINUTE = SAMPLE_RATE * 60
SAMPLES_PER_BEAT = SAMPLES_PER_MINUTE // BEATS_PER_MINUTE
BEATS_PER_PART = 16 * 8
SAMPLES_PER_PART = BEATS_PER_PART * SAMPLES_PER_BEAT

AMPLITUDE = 0.125

wave = numpy.concatenate(
    (
        render_wave(melody_1, SAMPLE_RATE, dampened_piano_wave, AMPLITUDE),
        render_wave(melody_2, SAMPLE_RATE, dampened_piano_wave, AMPLITUDE) + numpy.pad(
            render_wave(third_hand, SAMPLE_RATE, dampened_piano_wave, AMPLITUDE),
            (SAMPLES_PER_PART, 0),
        ),
    ),
)
