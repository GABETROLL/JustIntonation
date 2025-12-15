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

D2 = int(D3 / 2)
E2 = int(E4 / 4)
F_SHARP_2 = int(F_SHARP_3 / 2)
A2 = int(A3 / 2)
C_SHARP_2 = int(C_SHARP_4 / 4)

E3 = int(E4 / 2)
G3 = G2 * 2
B3 = B2 * 2
C_SHARP_3 = int(C_SHARP_4 / 2)

D4 = D3 * 2
F_SHARP_4 = F_SHARP_3 * 2
G4 = G2 * 4
A4 = A3 * 2
B4 = B2 * 4
C_SHARP_5 = C_SHARP_4 * 2

D5 = D3 * 4
E5 = E4 * 2
F_SHARP_5 = F_SHARP_3 * 4
G5 = G2 * 8
A5 = A3 * 4
B5 = B2 * 8
C_SHARP_6 = C_SHARP_4 * 4

wave: numpy.ndarray = render_wave(
    Melody(
        240,
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

            [B2, B5, D5],
            [B2, B5, D5],
            [F_SHARP_3, B5, D5],
            [F_SHARP_3, B5, D5],
            [B3, B5, D5],
            [B3, B5, D5],
            [D4, B5, D5],
            [D4, B5, D5],

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

            [288, 1728],
            [288, 1728],
            [432, 1440],
            [432, 1536],
            [576, 1728],
            [576, 1728],
            [432, 1440],
            [432, 1536],

            [216, 1728],
            [216, 864],
            [324, 960],
            [324, 1080],
            [432, 1152],
            [432, 1296],
            [324, 1440],
            [324, 1536],

            [240, 1440],
            [240, 1440],
            [360, 1152],
            [360, 1296],
            [480, 1440],
            [480, 1440],
            [360, 720],
            [360, 768],

            [180, 864],
            [180, 960],
            [270, 864],
            [270, 768],
            [360, 864],
            [360, 1152],
            [270, 1080],
            [270, 1152],

            [192, 960],
            [192, 960],
            [288, 1152],
            [288, 1080],
            [384, 960],
            [384, 960],
            [288, 864],
            [288, 768],

            [144, 864],
            [144, 768],
            [216, 720],
            [216, 768],
            [288, 864],
            [288, 1152],
            [216, 1080],
            [216, 1152],

            [192, 960],
            [192, 960],
            [288, 960],
            [288, 960],
            [384],
            [384],
            [288],
            [288],

            [216, 768, 960],
            [216, 768, 960],
            [324, 768, 960],
            [324, 768, 960],
            [432, 864, 1080],
            [432, 864, 1080],
            [324, 864, 1080],
            [324, 864, 1080],

            [288, 432, 576, 1728],
            [288, 432, 576, 1728],
            [288, 432, 576, 1728],
            [288, 432, 576, 1728],
            [288, 432, 576, 1728],
            [288, 432, 576, 1728],
            [288, 432, 576, 1728],
            [288, 432, 576, 1728],
            [288, 432, 576, 1728],
            [288, 432, 576, 1728],

            [288, 432, 576, 1440, 1728, 2304], 
            [288, 432, 576, 1440, 1728, 2304], 
            [288, 432, 576, 1440, 1728, 2304], 
            [288, 432, 576, 1440, 1728, 2304], 
            [288, 432, 576, 1440, 1728, 2304], 
            [288, 432, 576, 1440, 1728, 2304], 
            [288, 432, 576, 1440, 1728, 2304], 
            [288, 432, 576, 1440, 1728, 2304], 
        ],
    ),
    SAMPLE_RATE
)
