"""
                D#
  D   A   E   B   F#
Bb  F   C   G   D
      Ab  Eb
"""

from music_player import *

C1 = 45 * 3 / 4
A1 = C1 * 5 / 3
A_FLAT_1 = C1 * 8 / 5
F1 = C1 * 4 / 3
D_FROM_F_1 = C1 * 10 / 9
B_FLAT_FROM_F_1 = C1 * 16 / 9
E_FLAT_1 = C1 * 6 / 5
E1 = C1 * 5 / 4
G1 = C1 * 3 / 2
B1 = C1 * 15 / 8
D_FROM_G_1 = C1 * 9 / 8
F_SHARP_FROM_B_1 = C1 * 45 / 32
D_SHARP_FROM_B_1 = C1 * 75 / 64
# (5 / 4) * (3 / 2) * (5 / 4) = (5 * 3 * 5) / (4 * 2 * 4) = 75 / 32 => 75 / 64


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


C2, C3, C4, C5, C6 = octaves(C1, 5)
A2, A3, A4, A5 = octaves(A1, 4)
A_FLAT_2, A_FLAT_3, A_FLAT_4, A_FLAT_5 = octaves(A_FLAT_1, 4)
F2, F3, F4, F5 = octaves(F1, 4)
D_FROM_F_2, D_FROM_F_3, D_FROM_F_4, D_FROM_F_5, D_FROM_F_6 = octaves(D_FROM_F_1, 5)
B_FLAT_FROM_F_2, B_FLAT_FROM_F_3, B_FLAT_FROM_F_4, B_FLAT_FROM_F_5 = octaves(B_FLAT_FROM_F_1, 4)
E_FLAT_2, E_FLAT_3, E_FLAT_4, E_FLAT_5, E_FLAT_6 = octaves(E_FLAT_1, 5)
E2, E3, E4, E5, E6 = octaves(E1, 5)
G2, G3, G4, G5 = octaves(G1, 4)
B2, B3, B4, B5 = octaves(B1, 4)
D_FROM_G_2, D_FROM_G_3, D_FROM_G_4, D_FROM_G_5, D_FROM_G_6 = octaves(D_FROM_G_1, 5)
F_SHARP_FROM_B_2, F_SHARP_FROM_B_3, F_SHARP_FROM_B_4, F_SHARP_FROM_B_5 = octaves(F_SHARP_FROM_B_1, 4)
D_SHARP_FROM_B_2, D_SHARP_FROM_B_3, D_SHARP_FROM_B_4, D_SHARP_FROM_B_5, D_SHARP_FROM_B_6 = octaves(D_SHARP_FROM_B_1, 5)


melody = Melody(
    480,
    [
        [Note(G1, duration_in_beats=2), Note(G2, duration_in_beats=2), Note(E4, duration_in_beats=2), Note(C5, duration_in_beats=2)], [],
        [Note(A1, duration_in_beats=2), Note(A2, duration_in_beats=2), Note(F4, duration_in_beats=2), Note(D_FROM_F_5, duration_in_beats=2)], [],
        [Note(B1, duration_in_beats=2), Note(B2, duration_in_beats=2), Note(F_SHARP_FROM_B_4, duration_in_beats=2), Note(D_SHARP_FROM_B_5, duration_in_beats=2)], [],

        # 1

        [Note(C2, duration_in_beats=2), Note(C3, duration_in_beats=2), Note(G4, duration_in_beats=2), Note(E5, duration_in_beats=2)], [],
        [Note(f, duration_in_beats=2) for f in [G3, C4, E4, F_SHARP_FROM_B_4, D_SHARP_FROM_B_5]], [],
        [Note(f, duration_in_beats=2) for f in [G1, G2, G4, E5]], [],
        [Note(f, duration_in_beats=2) for f in [G3, C4, E4, F_SHARP_FROM_B_4, D_SHARP_FROM_B_5]], [],
        [Note(f, duration_in_beats=2) for f in [C2, C3, G4, E5]], [],
        [Note(f, duration_in_beats=2) for f in [G3, C4, E4]] + [Note(f) for f in [F_SHARP_FROM_B_4, D_SHARP_FROM_B_5]],
        [Note(f, duration_in_beats=3) for f in [F4, D_FROM_F_5]],
        [Note(f, duration_in_beats=2) for f in [G1, G2]], [],
        [Note(f, duration_in_beats=2) for f in [G3, C4, E4, F4, A_FLAT_4]], [],

        [Note(f, duration_in_beats=2) for f in [F1, F2, F4, A4]], [],
        [Note(f, duration_in_beats=2) for f in [F3, A3, C4, F4, C5]], [],
        [Note(f, duration_in_beats=2) for f in [C1, C2, F4, D_FROM_F_5]], [],
        [Note(f, duration_in_beats=2) for f in [F3, A3, C4]] + [Note(f, duration_in_beats=8) for f in [F4, C5]], [],
        [Note(f, duration_in_beats=2) for f in [F1, F2]], [],
        [Note(f, duration_in_beats=2) for f in [F3, A3, C4]], [],
        [Note(f, duration_in_beats=2) for f in [C1, C2]], [],
        [Note(f, duration_in_beats=2) for f in [F3, A3, C4, F_SHARP_FROM_B_4, D_SHARP_FROM_B_5]], [],

        [Note(f, duration_in_beats=2) for f in [C2, C3, G4, E5]], [],
        [Note(f, duration_in_beats=2) for f in [G3, C4, E4, G4, E5]], [],
        [Note(f, duration_in_beats=2) for f in [G1, G2, E4, G4, E5]], [],
        [Note(f, duration_in_beats=2) for f in [G3, C4, E4, G4, E5]], [],
        [Note(f, duration_in_beats=2) for f in [C2, C3, G4, E5]], [],
        [Note(f, duration_in_beats=2) for f in [G3, C4, E4]] + [Note(f) for f in [F_SHARP_FROM_B_4, D_SHARP_FROM_B_5]],
        [Note(f, duration_in_beats=3) for f in [F4, D_FROM_F_5]],
        [Note(f, duration_in_beats=2) for f in [G1, G2]], [],
        [Note(f, duration_in_beats=2) for f in [G3, C4, E4, F4, B_FLAT_FROM_F_4]], [],

        [Note(f, duration_in_beats=2) for f in [G1, G2, G4, B4]], [],
        [Note(f, duration_in_beats=2) for f in [G3, B3, D_FROM_G_4, G4, D_FROM_G_5]], [],
        [Note(f, duration_in_beats=2) for f in [D_FROM_G_1, D_FROM_G_1, D_FROM_G_4, G4, E5]], [],
        [Note(f, duration_in_beats=2) for f in [G3, B3, D_FROM_G_4]] + [Note(f, duration_in_beats=4) for f in [G4, D_FROM_G_5]], [],
        [Note(f, duration_in_beats=2) for f in [G1, G2]], [],
        [Note(f, duration_in_beats=2) for f in [G1, G2]] + [Note(f, duration_in_beats=4) for f in [G4, D_FROM_G_5]], [],
        [Note(f, duration_in_beats=2) for f in [A1, A2]], [],
        [Note(f, duration_in_beats=2) for f in [B1, B2, F_SHARP_FROM_B_4, D_SHARP_FROM_B_5]], [],

        [Note(f, duration_in_beats=2) for f in [C2, C3, G4, E5]], [],
        [Note(f, duration_in_beats=2) for f in [G3, C4, E4, F_SHARP_FROM_B_4, D_SHARP_FROM_B_5]], [],
        [Note(f, duration_in_beats=2) for f in [G1, G2, G4, E5]], [],
        [Note(f, duration_in_beats=2) for f in [G3, C4, E4, F_SHARP_FROM_B_4, D_SHARP_FROM_B_5]], [],
        [Note(f, duration_in_beats=2) for f in [C2, C3, G4, E5]], [],
        [Note(f, duration_in_beats=2) for f in [G3, C4, E4]] + [Note(f) for f in [F_SHARP_FROM_B_4, D_SHARP_FROM_B_5]],
        [Note(f, duration_in_beats=3) for f in [F4, D_FROM_F_5]],
        [Note(f, duration_in_beats=2) for f in [G1, G2]], [],
        [Note(f, duration_in_beats=2) for f in [G3, C4, E4, F4, A_FLAT_4]], [],

        [Note(f, duration_in_beats=2) for f in [F1, F2, F4, A4]], [],
        [Note(f, duration_in_beats=2) for f in [F3, A3, C4, F4, C5]], [],
        [Note(f, duration_in_beats=2) for f in [C1, C2, F4, D_FROM_F_5]], [],
        [Note(f, duration_in_beats=2) for f in [F3, A3, C4]] + [Note(f, duration_in_beats=4) for f in [F4, C5]], [],
        [Note(f, duration_in_beats=2) for f in [F1, F2]], [],
        [Note(f, duration_in_beats=2) for f in [F3, A3, C4, F4, C5]], [],
        [Note(f, duration_in_beats=2) for f in [C1, C2, F4, D_FROM_F_5]], [],
        [Note(f, duration_in_beats=2) for f in [F3, A3, C4, F_SHARP_FROM_B_4, D_SHARP_FROM_B_5]], [],

        [Note(f, duration_in_beats=2) for f in [C2, C3, G4, E5]], [],
        [Note(f, duration_in_beats=2) for f in [G3, C4, E4]] + [Note(f, duration_in_beats=4) for f in [G4, E5]], [],
        [Note(f, duration_in_beats=2) for f in [G1, G2]], [],
        [Note(f, duration_in_beats=2) for f in [G3, C4, E4, G4, E5]], [],
        [Note(f, duration_in_beats=2) for f in [G1, G2, G4, D_FROM_G_5]], [],
        [Note(f, duration_in_beats=2) for f in [G3, B3, D_FROM_G_4]] + [Note(f, duration_in_beats=4) for f in [G4, D_FROM_G_5]], [],
        [Note(f, duration_in_beats=2) for f in [D_FROM_G_1, D_FROM_G_2]], [],
        [Note(f, duration_in_beats=2) for f in [G3, B3, D_FROM_G_4, G4, D_FROM_G_5]], [],

        [Note(f, duration_in_beats=2) for f in [C2, C3]] + [Note(f, duration_in_beats=8) for f in [G4, C5]], [],
        [Note(f, duration_in_beats=2) for f in [G3, C4, E4]], [],
        [Note(f, duration_in_beats=2) for f in [G1, G2]], [],
        [Note(f, duration_in_beats=2) for f in [G3, C4, E4]], [],
        [Note(f, duration_in_beats=2) for f in [C2, C3]], [],
        [Note(f, duration_in_beats=2) for f in [G1, G2, E5, C6]], [],
        [Note(f, duration_in_beats=2) for f in [A1, A2, F5, D_FROM_F_6]], [],
        [Note(f, duration_in_beats=2) for f in [B1, B2, F_SHARP_FROM_B_5, D_SHARP_FROM_B_6]], [],

        # 2

        [Note(f, duration_in_beats=2) for f in [C2, C3, G5, E6]], [],
        [Note(f, duration_in_beats=2) for f in [G3, C4, E4, F_SHARP_FROM_B_5, D_SHARP_FROM_B_6]], [],
        [Note(f, duration_in_beats=2) for f in [G1, G2, G5, E6]], [],
        [Note(f, duration_in_beats=2) for f in [G3, C4, E4, F_SHARP_FROM_B_5, D_SHARP_FROM_B_6]], [],
        [Note(f, duration_in_beats=2) for f in [C2, C3, G5, E6]], [],
        [Note(f, duration_in_beats=2) for f in [G3, C4, E4]] + [Note(f) for f in [F_SHARP_FROM_B_5, D_SHARP_FROM_B_6]],
        [Note(f, duration_in_beats=3) for f in [F5, D_FROM_F_6]],
        [Note(f, duration_in_beats=2) for f in [G1, G2]], [],
        [Note(f, duration_in_beats=2) for f in [G3, C4, E4, F5, A_FLAT_5]], [],

        [Note(f, duration_in_beats=2) for f in [F1, F2, F5, A5]], [],
        [Note(f, duration_in_beats=2) for f in [F3, A3, C4, F5, C6]], [],
        [Note(f, duration_in_beats=2) for f in [C1, C2, F5, D_FROM_F_6]], [],
        [Note(f, duration_in_beats=2) for f in [F3, A3, C4]] + [Note(f, duration_in_beats=4) for f in [F5, C6]], [],
        [Note(f, duration_in_beats=2) for f in [F1, F2]], [],
        [Note(f, duration_in_beats=2) for f in [F3, A3, C4, F5, C6]], [],
        [Note(f, duration_in_beats=2) for f in [C1, C2, F5, D_FROM_F_6]], [],
        [Note(f, duration_in_beats=2) for f in [F3, A3, C4, F_SHARP_FROM_B_5, D_SHARP_FROM_B_6]], [],

        [Note(f, duration_in_beats=2) for f in [C2, C3, G5, E6]], [],
        [Note(f, duration_in_beats=2) for f in [G3, C4, E4, F_SHARP_FROM_B_5, D_SHARP_FROM_B_6]], [],
        [Note(f, duration_in_beats=2) for f in [G1, G2, G5, E6]], [],
        [Note(f, duration_in_beats=2) for f in [G3, C4, E4, F_SHARP_FROM_B_5, D_SHARP_FROM_B_6]], [],
        [Note(f, duration_in_beats=2) for f in [C2, C3, G5, E6]], [],
        [Note(f, duration_in_beats=2) for f in [G3, C4, E4]] + [Note(f) for f in [F_SHARP_FROM_B_5, D_SHARP_FROM_B_6]],
        [Note(f, duration_in_beats=2) for f in [G5, E6]],
        [Note(f, duration_in_beats=2) for f in [G1, G2]],
        [Note(f) for f in [G5, E6]],
        [Note(f, duration_in_beats=2) for f in [G3, C4, E4, G5, B_FLAT_FROM_F_5]], [], # This may sound wolfish...

        [Note(f, duration_in_beats=2) for f in [G1, G2, G5, D_FROM_G_6]], [],
        [Note(f, duration_in_beats=2) for f in [G3, B3, D_FROM_G_4, G5, D_FROM_G_6]], [],
        [Note(f, duration_in_beats=2) for f in [D_FROM_G_1, D_FROM_G_2, G5, E6]], [],
        [Note(f, duration_in_beats=2) for f in [G3, B3, D_FROM_G_4]] + [Note(f, duration_in_beats=8) for f in [G5, D_FROM_G_6]], [],
        [Note(f, duration_in_beats=2) for f in [G1, G2]], [],
        [Note(f, duration_in_beats=2) for f in [G1, G2]], [],
        [Note(f, duration_in_beats=2) for f in [F1, F2]], [],
        [Note(f, duration_in_beats=2) for f in [E1, E2, F_SHARP_FROM_B_5, D_SHARP_FROM_B_6]], [],

        [Note(f, duration_in_beats=2) for f in [C2, C3, G5, E6]], [],
        [Note(f, duration_in_beats=2) for f in [G3, C4, E4, F_SHARP_FROM_B_5, D_SHARP_FROM_B_6]], [],
        [Note(f, duration_in_beats=2) for f in [G1, G2, G5, E6]], [],
        [Note(f, duration_in_beats=2) for f in [G3, C4, E4, F_SHARP_FROM_B_5, D_SHARP_FROM_B_6]], [],
        [Note(f, duration_in_beats=2) for f in [C2, C3, G5, E6]], [],
        [Note(f, duration_in_beats=2) for f in [G3, C4, E4]] + [Note(f) for f in [F_SHARP_FROM_B_5, D_SHARP_FROM_B_6]],
        [Note(f, duration_in_beats=3) for f in [F5, D_FROM_F_6]],
        [Note(f, duration_in_beats=2) for f in [G1, G2]], [],
        [Note(f, duration_in_beats=2) for f in [G3, C4, E4, F5, A_FLAT_5]], [],

        [Note(f, duration_in_beats=2) for f in [F1, F2, F5, A5]], [],
        [Note(f, duration_in_beats=2) for f in [F3, A3, C4, F5, C6]], [],
        [Note(f, duration_in_beats=2) for f in [C1, C2, F5, D_FROM_F_6]], [],
        [Note(f, duration_in_beats=2) for f in [F3, A3, C4]] + [Note(f, duration_in_beats=4) for f in [F5, C6]], [],
        [Note(f, duration_in_beats=2) for f in [F1, F2]], [],
        [Note(f, duration_in_beats=2) for f in [F3, A3, C4, F5, C6]], [],
        [Note(f, duration_in_beats=2) for f in [C1, C2, F5, D_FROM_F_6]], [],
        [Note(f, duration_in_beats=2) for f in [F3, A3, C4, F_SHARP_FROM_B_5, D_SHARP_FROM_B_6]], [],

        [Note(f, duration_in_beats=2) for f in [C2, C3, G5, E6]], [],
        [Note(f, duration_in_beats=2) for f in [G3, C4, E4]] + [Note(f, duration_in_beats=4) for f in [G5, E6]], [],
        [Note(f, duration_in_beats=2) for f in [G1, G2]], [],
        [Note(f, duration_in_beats=2) for f in [G3, C4, E4, G5, E6]], [],
        [Note(f, duration_in_beats=2) for f in [G1, G2, G5, D_FROM_G_6]], [],
        [Note(f, duration_in_beats=2) for f in [G3, B3, D_FROM_G_4]] + [Note(f, duration_in_beats=4) for f in [G5, D_FROM_G_6]], [],
        [Note(f, duration_in_beats=2) for f in [D_FROM_G_1, D_FROM_G_2]], [],
        [Note(f, duration_in_beats=2) for f in [G3, B3, D_FROM_G_4, G5, D_FROM_G_6]], [],

        [Note(f, duration_in_beats=2) for f in [C2, C3]] + [Note(f, duration_in_beats=4) for f in [G5, C6]], [],
        [Note(f, duration_in_beats=2) for f in [G3, C4, E4]], [],
        [Note(f, duration_in_beats=2) for f in [G1, G2]] + [Note(f, duration_in_beats=4) for f in [E5, G5]], [],
        [Note(f, duration_in_beats=2) for f in [G3, C4, E4]], [],
        [Note(f, duration_in_beats=2) for f in [C2, C3, G5, C6]], [],
        [Note(f, duration_in_beats=2) for f in [C2, C3, G5, C6]], [],
        [Note(f, duration_in_beats=2) for f in [C2, C3, G5, C6]], [],
        [], [],

        # 3

        [Note(f, duration_in_beats=4) for f in [C2, C3]] + [Note(f, duration_in_beats=2) for f in [C4, G4]], [],
        [Note(f, duration_in_beats=2) for f in [C4, E4]], [],
        [Note(f, duration_in_beats=4) for f in [G1, G2]] + [Note(f, duration_in_beats=2) for f in [C4, G4]], [],
        [Note(f, duration_in_beats=1) for f in [C4, E4]], [Note(f, duration_in_beats=1) for f in [C4, G4]],
        [Note(f, duration_in_beats=4) for f in [C2, C3]], [Note(f, duration_in_beats=1) for f in [C4, G4]],
        [Note(f, duration_in_beats=2) for f in [C4, E4]], [],
        [Note(f, duration_in_beats=4) for f in [G1, G2]] + [Note(f, duration_in_beats=2) for f in [C4, G4]], [],
        [Note(f, duration_in_beats=2) for f in [C4, E4]], [],

        [Note(f, duration_in_beats=4) for f in [A_FLAT_1, A_FLAT_2]] + [Note(f, duration_in_beats=2) for f in [C4, E_FLAT_4]], [],
        [Note(f, duration_in_beats=4) for f in [C4, A_FLAT_4]], [],
        [Note(f, duration_in_beats=4) for f in [E_FLAT_1, E_FLAT_2]], [],
        [Note(f, duration_in_beats=8) for f in [C4, E_FLAT_4]], [],
        [Note(f, duration_in_beats=4) for f in [A_FLAT_1, A_FLAT_2]], [],
        [], [],
        [Note(f, duration_in_beats=4) for f in [E_FLAT_1, E_FLAT_2]], [],
        [], [],

        [Note(f, duration_in_beats=4) for f in [B_FLAT_FROM_F_1, B_FLAT_FROM_F_2]] + [Note(f, duration_in_beats=2) for f in [B_FLAT_FROM_F_3, F4]], [],
        [Note(f, duration_in_beats=2) for f in [B_FLAT_FROM_F_3, D_FROM_F_4]], [],
        [Note(f, duration_in_beats=4) for f in [F1, F2]] + [Note(f, duration_in_beats=2) for f in [B_FLAT_FROM_F_3, F4]], [],
        [Note(f) for f in [B_FLAT_FROM_F_3, D_FROM_F_4]], [Note(f, duration_in_beats=2) for f in [B_FLAT_FROM_F_3, F4]],
        [Note(f, duration_in_beats=4) for f in [B_FLAT_FROM_F_1, B_FLAT_FROM_F_2]], [Note(f) for f in [B_FLAT_FROM_F_3, F4]],
        [Note(f, duration_in_beats=2) for f in [B_FLAT_FROM_F_3, D_FROM_F_4]], [],
        [Note(f, duration_in_beats=4) for f in [F1, F2]] + [Note(f, duration_in_beats=2) for f in [B_FLAT_FROM_F_3, F4]], [],
        [Note(f, duration_in_beats=2) for f in [B_FLAT_FROM_F_3, D_FROM_F_4]], [],

        [Note(f, duration_in_beats=2) for f in [F1, F2, C4, F4]], [],
        [Note(f, duration_in_beats=4) for f in [F_SHARP_FROM_B_1, F_SHARP_FROM_B_2, C4, F_SHARP_FROM_B_4]], [],
        [], [],
        [Note(f, duration_in_beats=4) for f in [G1, G2, B3, G4]], [],
        [], [],
        [Note(f, duration_in_beats=2) for f in [G1, G2, B3, G4]], [],
        [Note(f, duration_in_beats=4) for f in [G1, G2, B3, G4]], [],
        [], [],
    ]
)

wave = render_wave(melody, SAMPLE_RATE, dampened_piano_wave, 0.125)
