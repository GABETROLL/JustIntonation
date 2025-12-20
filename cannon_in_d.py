"""
If home = D = 288:
E = D * 9 / 8 = 324,
F# = D * 5 / 4 = 360,
G = D * 4 / 3 = 384,
A = D * 3 / 2 = 432
B = D * 5 / 3 = 480
C# = D * 15 / 8 = 540

D => 576
E => 648
F# => 720
G => 468
A => 864
B => 960
C# => 1080

...
"""
from music_player import *

HOME = D3 = 288
B2 = int(D3 * 5 / 6)
G2 = int(D3 * 2 / 3)
F_SHARP_3 = int(D3 * 5 / 4)
A3 = int(D3 * 3 / 2)
C_SHARP_4 = int(A3 * 5 / 4)
E4 = int(A3 * 3 / 2)

D2 = D3 >> 1
E2 = E4 >> 2
F_SHARP_2 = F_SHARP_3 >> 1
A2 = A3 >> 1
C_SHARP_2 = C_SHARP_4 >> 2

E3 = E4 >> 1
G3 = G2 << 1
B3 = B2 << 1
C_SHARP_3 = C_SHARP_4 >> 1

D4 = D3 << 1
F_SHARP_4 = F_SHARP_3 << 1
G4 = G2 << 2
A4 = A3 << 1
B4 = B2 << 2
C5 = int(G4 * 4 / 3)
C_SHARP_5 = C_SHARP_4 << 1

D5 = D3 << 2
E5 = E4 << 1
F_SHARP_5 = F_SHARP_3 << 2
G5 = G2 << 3
A5 = A3 << 2
B5 = B2 << 3
C_SHARP_6 = C_SHARP_4 << 2

D6 = D3 << 3

melody = Melody(
    360,
    [
        [D3],
        [D3],
        [A3],
        [A3],
        [D4],
        [D4],
        [F_SHARP_4],
        [F_SHARP_4],

        [A2],
        [A2],
        [E3],
        [E3],
        [A3],
        [A3],
        [C_SHARP_4],
        [C_SHARP_4],

        [B2],
        [B2],
        [F_SHARP_3],
        [F_SHARP_3],
        [B3],
        [B3],
        [D4],
        [D4],

        [F_SHARP_2],
        [F_SHARP_2],
        [C_SHARP_3],
        [C_SHARP_3],
        [F_SHARP_3],
        [F_SHARP_3],
        [A3],
        [A3],

        [G2],
        [G2],
        [D3],
        [D3],
        [G3],
        [G3],
        [B3],
        [B3],

        [D2],
        [D2],
        [A2],
        [A2],
        [D3],
        [D3],
        [F_SHARP_3],
        [F_SHARP_3],

        [G2],
        [G2],
        [D3],
        [D3],
        [G3],
        [G3],
        [B3],
        [B3],

        [A2],
        [A2],
        [E3],
        [E3],
        [A3],
        [A3],
        [C_SHARP_4],
        [C_SHARP_4],

        # 2

        [D3, F_SHARP_5],
        [D3, F_SHARP_5],
        [A3, F_SHARP_5],
        [A3, F_SHARP_5],
        [D4, F_SHARP_5],
        [D4, F_SHARP_5],
        [F_SHARP_4, F_SHARP_5],
        [F_SHARP_4, F_SHARP_5],

        [A2, E5],
        [A2, E5],
        [E3, E5],
        [E3, E5],
        [A3, E5],
        [A3, E5],
        [C_SHARP_4, E5],
        [C_SHARP_4, E5],

        [B2, D5],
        [B2, D5],
        [F_SHARP_3, D5],
        [F_SHARP_3, D5],
        [B3, D5],
        [B3, D5],
        [D4, D5],
        [D4, D5],

        [F_SHARP_2, C_SHARP_5],
        [F_SHARP_2, C_SHARP_5],
        [C_SHARP_3, C_SHARP_5],
        [C_SHARP_3, C_SHARP_5],
        [F_SHARP_3, C_SHARP_5],
        [F_SHARP_3, C_SHARP_5],
        [A3, C_SHARP_5],
        [A3, C_SHARP_5],

        [G2, B4],
        [G2, B4],
        [D3, B4],
        [D3, B4],
        [G3, B4],
        [G3, B4],
        [B3, B4],
        [B3, B4],

        [D2, A4],
        [D2, A4],
        [A2, A4],
        [A2, A4],
        [D3, A4],
        [D3, A4],
        [F_SHARP_3, A4],
        [F_SHARP_3, A4],

        [G2, B4],
        [G2, B4],
        [D3, B4],
        [D3, B4],
        [G3, B4],
        [G3, B4],
        [B3, B4],
        [B3, B4],

        [A2, C_SHARP_4],
        [A2, C_SHARP_4],
        [E3, C_SHARP_4],
        [E3, C_SHARP_4],
        [A3, C_SHARP_4],
        [A3, C_SHARP_4],
        [C_SHARP_4],
        [C_SHARP_4],

        # 3

        [D3, D5, F_SHARP_5],
        [D3, D5, F_SHARP_5],
        [A3, D5, F_SHARP_5],
        [A3, D5, F_SHARP_5],
        [D4, D5, F_SHARP_5],
        [D4, D5, F_SHARP_5],
        [F_SHARP_4, D5, F_SHARP_5],
        [F_SHARP_4, D5, F_SHARP_5],

        [A2, C_SHARP_5, E5],
        [A2, C_SHARP_5, E5],
        [E3, C_SHARP_5, E5],
        [E3, C_SHARP_5, E5],
        [A3, C_SHARP_5, E5],
        [A3, C_SHARP_5, E5],
        [C_SHARP_4, C_SHARP_5, E5],
        [C_SHARP_4, C_SHARP_5, E5],

        [B2, B4, D5],
        [B2, B4, D5],
        [F_SHARP_3, B4, D5],
        [F_SHARP_3, B4, D5],
        [B3, B4, D5],
        [B3, B4, D5],
        [D4, B4, D5],
        [D4, B4, D5],

        [F_SHARP_2, A4, C_SHARP_5],
        [F_SHARP_2, A4, C_SHARP_5],
        [C_SHARP_3, A4, C_SHARP_5],
        [C_SHARP_3, A4, C_SHARP_5],
        [F_SHARP_3, A4, C_SHARP_5],
        [F_SHARP_3, A4, C_SHARP_5],
        [A3, A4, C_SHARP_5],
        [A3, A4, C_SHARP_5],

        [G2, G4, B4],
        [G2, G4, B4],
        [D3, G4, B4],
        [D3, G4, B4],
        [G3, G4, B4],
        [G3, G4, B4],
        [B3, G4, B4],
        [B3, G4, B4],

        [D2, F_SHARP_4, A4],
        [D2, F_SHARP_4, A4],
        [A2, F_SHARP_4, A4],
        [A2, F_SHARP_4, A4],
        [D3, F_SHARP_4, A4],
        [D3, F_SHARP_4, A4],
        [F_SHARP_3, F_SHARP_4, A4],
        [F_SHARP_3, F_SHARP_4, A4],

        [G2, G4, B4],
        [G2, G4, B4],
        [D3, G4, B4],
        [D3, G4, B4],
        [G3, G4, B4],
        [G3, G4, B4],
        [B3, G4, B4],
        [B3, G4, B4],

        [A2, A3, C_SHARP_4],
        [A2, A3, C_SHARP_4],
        [E3, A3, C_SHARP_4],
        [E3, A3, C_SHARP_4],
        [A3, A3, C_SHARP_4],
        [A3, A3, C_SHARP_4],
        [A3, C_SHARP_4],
        [A3, C_SHARP_4],

        # 4

        [D3, D5],
        [D3, D5],
        [A3, C_SHARP_5],
        [A3, C_SHARP_5],
        [D4, D5],
        [D4, D5],
        [A3, F_SHARP_4],
        [A3, F_SHARP_4],

        [A2, A4],
        [A2, A4],
        [E3, E4],
        [E3, E4],
        [A3, A4],
        [A3, A4],
        [E3, G4],
        [E3, G4],

        [B2, F_SHARP_4],
        [B2, F_SHARP_4],
        [F_SHARP_3, B4],
        [F_SHARP_3, B4],
        [B3, A4],
        [B3, A4],
        [F_SHARP_3, G4],
        [F_SHARP_3, G4],

        [F_SHARP_2, A4],
        [F_SHARP_2, A4],
        [C_SHARP_3, G4],
        [C_SHARP_3, G4],
        [F_SHARP_3, F_SHARP_4],
        [F_SHARP_3, F_SHARP_4],
        [C_SHARP_3, E4],
        [C_SHARP_3, E4],

        [G2, D4],
        [G2, D4],
        [D3, D4],
        [D3, D4],
        [G3, B4],
        [G3, B4],
        [D3, C_SHARP_5],
        [D3, C_SHARP_5],

        [D2, D5],
        [D2, D5],
        [A2, C_SHARP_5],
        [A2, C_SHARP_5],
        [D3, B4],
        [D3, B4],
        [A2, A4],
        [A2, A4],

        [G2, B4],
        [G2, B4],
        [D3, A4],
        [D3, A4],
        [G3, B4],
        [G3, B4],
        [D3, D5],
        [D3, D5],

        [A2, D5],
        [A2, D5],
        [E3, D5],
        [E3, D5],
        [A3, C_SHARP_5],
        [A3, C_SHARP_5],
        [E3, D5],
        [E3, D5],

        # 5

        [D3, A5],
        [D3, A5],
        [A3, F_SHARP_5],
        [A3, G5],
        [D4, A5],
        [D4, A5],
        [A3, F_SHARP_5],
        [A3, G5],

        [A2, A5],
        [A2, A4],
        [E3, B4],
        [E3, C_SHARP_5],
        [A3, D5],
        [A3, E5],
        [E3, F_SHARP_5],
        [E3, G5],

        [B2, F_SHARP_5],
        [B2, F_SHARP_5],
        [F_SHARP_3, D5],
        [F_SHARP_3, E5],
        [B3, F_SHARP_5],
        [B3, F_SHARP_5],
        [F_SHARP_3, F_SHARP_4],
        [F_SHARP_3, G4],

        [F_SHARP_2, A4],
        [F_SHARP_2, B4],
        [C_SHARP_3, A4],
        [C_SHARP_3, G4],
        [F_SHARP_3, A4],
        [F_SHARP_3, F_SHARP_4],
        [C_SHARP_3, G4],
        [C_SHARP_3, A4],

        [G2, G4],
        [G2, G4],
        [D3, B4],
        [D3, A4],
        [G3, G4],
        [G3, G4],
        [D3, F_SHARP_4],
        [D3, E4],

        [D2, F_SHARP_4],
        [D2, E4],
        [A2, D4],
        [A2, E4],
        [D3, F_SHARP_4],
        [D3, G4],
        [A2, A4],
        [A2, B4],

        [G2, G4],
        [G2, G4],
        [D3, B4],
        [D3, A4],
        [G3, B4],
        [G3, B4],
        [D3, C_SHARP_5],
        [D3, D5],

        [A2, C_SHARP_5],
        [A2, A4],
        [E3, B4],
        [E3, C_SHARP_5],
        [A3, D5],
        [A3, E5],
        [E3, F_SHARP_5],
        [E3, G5],

        # 5

        [D3, A5],
        [D3, A5],
        [A3, F_SHARP_5],
        [A3, G5],
        [D4, A5],
        [D4, A5],
        [A3, F_SHARP_5],
        [A3, G5],

        [A2, A5],
        [A2, A4],
        [E3, B4],
        [E3, C_SHARP_5],
        [A3, D5],
        [A3, E5],
        [E3, F_SHARP_5],
        [E3, G5],

        [B2, F_SHARP_5],
        [B2, F_SHARP_5],
        [F_SHARP_3, D5],
        [F_SHARP_3, E5],
        [B3, F_SHARP_5],
        [B3, F_SHARP_5],
        [F_SHARP_3, F_SHARP_4],
        [F_SHARP_3, G4],

        [F_SHARP_2, A4],
        [F_SHARP_2, B4],
        [C_SHARP_3, A4],
        [C_SHARP_3, G4],
        [F_SHARP_3, A4],
        [F_SHARP_3, D5],
        [C_SHARP_3, C_SHARP_5],
        [C_SHARP_3, D5],

        [G2, B4],
        [G2, B4],
        [D3, D5],
        [D3, C_SHARP_5],
        [G3, B4],
        [G3, B4],
        [D3, A4],
        [D3, G4],

        [D2, A4],
        [D2, G4],
        [A2, F_SHARP_4],
        [A2, G4],
        [D3, A4],
        [D3, D5],
        [A2, C_SHARP_5],
        [A2, D5],

        [G2, B4],
        [G2, B4],
        [D3, B4],
        [D3, B4],
        [G3],
        [G3],
        [D3],
        [D3],

        [A2, G4, B4],
        [A2, G4, B4],
        [E3, G4, B4],
        [E3, G4, B4],
        [A3, A4, C_SHARP_5],
        [A3, A4, C_SHARP_5],
        [E3, A4, C_SHARP_5],
        [E3, A4, C_SHARP_5],

        [D3, F_SHARP_5],
        [D3, F_SHARP_5],
        [A3, F_SHARP_5],
        [A3, F_SHARP_5],
        [D4, F_SHARP_5],
        [D4, F_SHARP_5],
        [A3, F_SHARP_5],
        [A3, F_SHARP_5],

        [A2, F_SHARP_5],
        [A2, F_SHARP_5],
        [E3, F_SHARP_5],
        [E3, G5],
        [A3, F_SHARP_5],
        [A3, F_SHARP_5],
        [E3, E5],
        [E3, E5],

        [B2, D5],
        [B2, D5],
        [F_SHARP_3, D5],
        [F_SHARP_3, D5],
        [B3, D5],
        [B3, D5],
        [F_SHARP_3, D5],
        [F_SHARP_3, D5],

        [F_SHARP_2, D5],
        [F_SHARP_2, D5],
        [C_SHARP_3, D5],
        [C_SHARP_3, E5],
        [F_SHARP_3, D5],
        [F_SHARP_3, D5],
        [C_SHARP_3, C5],
        [C_SHARP_3, C5],

        [G2, B4],
        [G2, B4],
        [D3, B4],
        [D3, B4],
        [G3, C_SHARP_5],
        [G3, C_SHARP_5],
        [D3, C_SHARP_5],
        [D3, C_SHARP_5],

        [D2, D5],
        [D2, D5],
        [A2, D5],
        [A2, D5],
        [D3, A4],
        [D3, A4],
        [A2, A4],
        [A2, A4],

        [G2, D5],
        [G2, D5],
        [D3, C5],
        [D3, C5],
        [G3, B4],
        [G3, B4],
        [D3, C5],
        [D3, C5],

        [A2, C_SHARP_5],
        [A2, C_SHARP_5],
        [E3, C_SHARP_5],
        [E3, C_SHARP_5],
        [A3, C_SHARP_5],
        [A3, C_SHARP_5],
        [E3, C_SHARP_5],
        [E3, C_SHARP_5],

        [D3, A3, D4, F_SHARP_5, A5, D6],
    ],
)


print(C_SHARP_2, C_SHARP_3, C_SHARP_4, C_SHARP_5, C_SHARP_6)
print(D2, D3, D5, D5, D6)
print(E2, E3, E4, E5)
print(F_SHARP_2, F_SHARP_3, F_SHARP_4, F_SHARP_5)
print(G2, G3, G4, G5)
print(A2, A3, A4, A5)
print(B2, B3, B4, B5)

wave: numpy.ndarray = render_wave(
    melody,
    SAMPLE_RATE,
    other,
)
