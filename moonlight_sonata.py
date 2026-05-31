"""
            C
  F#  C#  G#  D#
D   A   E   B   F#  C#
  F   C   G   D        E
            A#
(9 / 4) * (6 / 5) = (2 * 3 * 3 * 3) / (2 * 2 * 5) = (3 * 3 * 3) / (2 * 5) = 27 / 10

(3 / 2) * (6 / 5) = (2 * 3 * 3) / (2 * 5) =  (3 * 3) / (5) = 9 / 5
(9 / 5) / 2 = 9 / 10
"""
from music_player import *

"""
        G#  D#  A#      C
      E   B   F#  C#  G#  D#
F   C   G   D   A   E   B
"""

CS_1 = 34
A1 = Fraction(CS_1 * 8, 5)
C_FROM_GS_1 = Fraction(CS_1 * 15, 16)
C_FROM_A_1 = Fraction(CS_1 * 24, 25)
OTHER_CS_1 = Fraction(CS_1 * 81, 80)
OTHER_E_1 = Fraction(CS_1 * 243, 200)
FS_1 = Fraction(CS_1 * 4, 3)
FS_FROM_B_1 = Fraction(CS_1 * 27, 20)
F1 = Fraction(CS_1 * 32, 25)
D1 = Fraction(CS_1 * 16, 15)
D_FROM_G_1 = Fraction(CS_1 * 27, 25)
E1 = Fraction(CS_1 * 6, 5)
G1 = Fraction(CS_1 * 36, 25)
GS_1 = Fraction(CS_1 * 3, 2)
AS_1 = Fraction(CS_1 * 216, 125)
B1 = Fraction(CS_1 * 9, 5)
DS_1 = Fraction(CS_1 * 9, 8)

CS_2, CS_3, CS_4, CS_5 = octaves(CS_1, 4)
A2, A3, A4, A5 = octaves(A1, 4)
C_FROM_GS_2, C_FROM_GS_3, C_FROM_GS_4, C_FROM_GS_5 = octaves(C_FROM_GS_1, 4)
C_FROM_A_2, C_FROM_A_3, C_FROM_A_4, C_FROM_A_5 = octaves(C_FROM_A_1, 4)
OTHER_CS_2, OTHER_CS_3, OTHER_CS_4, OTHER_CS_5 = octaves(OTHER_CS_1, 4)
OTHER_E_2, OTHER_E_3, OTHER_E_4, OTHER_E_5 = octaves(OTHER_E_1, 4)
FS_2, FS_3, FS_4, FS_5 = octaves(FS_1, 4)
FS_FROM_B_2, FS_FROM_B_3, FS_FROM_B_4, FS_FROM_B_5 = octaves(FS_FROM_B_1, 4)
F2, F3, F4, F5 = octaves(F1, 4)
D2, D3, D4, D5 = octaves(D1, 4)
D_FROM_G_2, D_FROM_G_3, D_FROM_G_4, D_FROM_G_5 = octaves(D_FROM_G_1, 4)
E2, E3, E4, E5 = octaves(E1, 4)
G2, G3, G4, G5 = octaves(G1, 4)
GS_2, GS_3, GS_4, GS_5 = octaves(GS_1, 4)
AS_2, AS_3, AS_4, AS_5 = octaves(AS_1, 4)
B2, B3, B4, B5 = octaves(B1, 4)
DS_2, DS_3, DS_4, DS_5 = octaves(DS_1, 4)

BEATS_PER_SECOND = 2
SAMPLES_PER_BEAT_ROUNDED = SAMPLE_RATE // BEATS_PER_SECOND

NOTE_AMPLITUDE = 0.25

melody = Melody(
    SAMPLES_PER_BEAT_ROUNDED,
    [
        notes((CS_2, CS_3), duration_in_beats=12) + (GS_3,),
        [CS_4],
        [E4],
        [GS_3],
        [CS_4],
        [E4],
        [GS_3],
        [CS_4],
        [E4],
        [GS_3],
        [CS_4],
        [E4],
        notes((B1, B2), duration_in_beats=12) + (GS_3,),
        [CS_4],
        [E4],
        [GS_3],
        [CS_4],
        [E4],
        [GS_3],
        [CS_4],
        [E4],
        [GS_3],
        [CS_4],
        [E4],
        notes((A1, A2), duration_in_beats=6) + (A3,),
        [CS_4],
        [E4],
        [A3],
        [CS_4],
        [E4],
        notes((FS_1, FS_2), duration_in_beats=6) + (A3,),
        [D4],
        [FS_4],
        [A3],
        [D4],
        [FS_4],
        notes((GS_1, GS_2), duration_in_beats=6) + (GS_3,),
        [C_FROM_GS_4],
        [FS_4],
        [GS_3],
        [CS_4],
        [E4],
        notes((GS_1, GS_2), duration_in_beats=6) + (GS_3,),
        [CS_4],
        [DS_4],
        [FS_3],
        [C_FROM_GS_4],
        [DS_4],
        notes((CS_2, GS_2, CS_3), duration_in_beats=12) + (E3,),
        [GS_3],
        [CS_4],
        [GS_3],
        [CS_4],
        [E4],
        [GS_3],
        [CS_4],
        [E4],
        [GS_3, [[Note(GS_4, duration_in_beats=5)], []]],
        [CS_4],
        [E4, [[], [GS_4]]],
        notes((C_FROM_GS_2, GS_2, C_FROM_GS_3), duration_in_beats=12) + (Note(GS_4, duration_in_beats=9),) + (GS_3,),
        [DS_4],
        [FS_4],
        [GS_3],
        [DS_4],
        [FS_4],
        [GS_3],
        [DS_4],
        [FS_4],
        [GS_3, [[Note(GS_4, duration_in_beats=5)], []]],
        [DS_4],
        [FS_4, [[], [GS_4]]],
        notes((CS_2, CS_3, GS_4), duration_in_beats=6) + (GS_3,),
        [CS_4],
        [E4],
        [GS_3],
        [CS_4],
        [E4],
        notes((FS_1, FS_2, A4), duration_in_beats=6) + (A3,),
        [CS_4],
        [FS_4],
        [A3],
        [CS_4],
        [FS_4],
        notes((B1, B2, GS_4), duration_in_beats=6) + (GS_3,),
        [B3],
        [E4],
        [GS_3],
        [B3],
        [E4],
        notes((B1, B2), duration_in_beats=6) + notes((FS_FROM_B_4,), duration_in_beats=3) + (A3,),
        [B3],
        [DS_4],
        notes((B4,), duration_in_beats=3) + (A3,),
        [B3],
        [DS_4],
        notes((E2, E3), duration_in_beats=12) + notes((E4,), duration_in_beats=2) + (GS_3,),
        [B3],
        [E4],
        [GS_3],
        [B3],
        [E4],
        [GS_3],
        [B3],
        [E4],
        [GS_3],
        [B3],
        [E4],
        notes((E2, E3), duration_in_beats=12) + (G3,),
        [B3],
        [E4],
        [G3],
        [B3],
        [E4],
        [G3],
        [B3],
        [E4],
        [G3, [[Note(G4, duration_in_beats=5)], []]],
        [B3],
        [E4, [[], [G4]]],
        notes((D_FROM_G_2, D_FROM_G_3), duration_in_beats=12) + notes((G4,), duration_in_beats=9) + (G3,), # TODO: CORRECT D
        [B3],
        [F4],
        [G3],
        [B3],
        [F4],
        [G3],
        [B3],
        [F4],
        [G3, [[Note(G4, duration_in_beats=5)], []]],
        [B3],
        [F4, [[], [G4]]],
        notes((C_FROM_A_2, C_FROM_A_3), duration_in_beats=3) + notes((G4,), duration_in_beats=9) + (G3,),
        [C_FROM_A_4],
        [E4],
        notes((B1, B2), duration_in_beats=3) + (G3,),
        [B3],
        [E4],
        notes((AS_1, AS_2), duration_in_beats=6) + (G3,),
        [OTHER_CS_4],
        [OTHER_E_4],
        notes((FS_FROM_B_4,), duration_in_beats=3) + (FS_FROM_B_3,),
        [OTHER_CS_4],
        [OTHER_E_4],
        notes((B1, B2, FS_FROM_B_4), duration_in_beats=6) + (FS_FROM_B_3,),
        [B3],
        [D_FROM_G_4],
        [FS_FROM_B_3],
        [B3],
        [D_FROM_G_4],
        notes((OTHER_E_2, G4), duration_in_beats=3) + (G3,),
        [B3],
        [OTHER_CS_4],
        notes((G2, OTHER_E_4), duration_in_beats=3) + (OTHER_E_3,),
        [B3],
        [OTHER_CS_4],
    ]
)

wave = render_wave(melody, SAMPLE_RATE, sine_wave, NOTE_AMPLITUDE)
