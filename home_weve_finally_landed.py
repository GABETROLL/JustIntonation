from music_player import *

E2 = 336
E3 = E2 << 1
E4 = E3 << 1
E5 = E4 << 1
G2 = int(E2 * 6 / 5)
G3 = G2 << 1
G4 = G3 << 1
G5 = G4 << 1
B_FLAT_2 = int(G2 * 6 / 5)
B_FLAT_3 = B_FLAT_2 << 1
B_FLAT_4 = B_FLAT_3 << 1
B2 = int(G2 * 5 / 4)
B3 = B2 << 1
B4 = B3 << 1
D3 = int(G2 * 3 / 2)
D4 = D3 << 1
D5 = D4 << 1
F_SHARP_3 = int(D3 * 5 / 4)
F_SHARP_4 = F_SHARP_3 << 1
F_SHARP_5 = F_SHARP_4 << 1
A3 = int(D3 * 3 / 2)
A2 = A3 >> 1
A4 = A3 << 1
A5 = A4 << 1

melody = Melody(
    60 << 3,
    [
        [A2],
        [A2, D3],
        [A2, D3, E3],
        [A2, D3, E3, F_SHARP_3],
        [A2, D3, E3, F_SHARP_3],
        [A2, D3, E3, F_SHARP_3],
        [A2, D3, E3, F_SHARP_3],
        [A2, D3, E3, F_SHARP_3],
        [A2, D3, E3, F_SHARP_3],
        [A2, D3, E3, F_SHARP_3],
        [A2, D3, E3, F_SHARP_3],
        [A2, D3, E3, F_SHARP_3],
        [A2, D3, E3, F_SHARP_3],
        [A2, D3, E3, F_SHARP_3],
        [A2, D3, E3, F_SHARP_3],
        [A2, D3, E3, F_SHARP_3],

        [G2],
        [G2, E3],
        [G2, E3, G3],
        [G2, E3, G3, B3],
        [G2, E3, G3, B3],
        [G2, E3, G3, B3],
        [G2, E3, G3, B3],
        [G2, E3, G3, B3],
        [G2, E3, G3, B3],
        [G2, E3, G3, B3],
        [G2, E3, G3, B3],
        [G2, E3, G3, B3],
        [G2, E3, G3, B3],
        [G2, E3, G3, B3],
        [G2, E3, G3, B3],
        [G2, E3, G3, B3],

        [D3],
        [D3, G3],
        [D3, G3, B3],
        [D3, G3, B3, D4],
        [D3, G3, B3, D4],
        [D3, G3, B3, D4],
        [D3, G3, B3, D4],
        [D3, G3, B3, D4],
        [D3, G3, B3, D4],
        [D3, G3, B3, D4],
        [D3, G3, B3, D4],
        [D3, G3, B3, D4],
        [D3, G3, B3, D4],
        [D3, G3, B3, D4],
        [D3, G3, B3, D4],
        [D3, G3, B3, D4],

        [D3],
        [D3, G3],
        [D3, G3, B_FLAT_3],
        [D3, G3, B_FLAT_3, D4],
        [D3, G3, B_FLAT_3, D4],
        [D3, G3, B_FLAT_3, D4],
        [D3, G3, B_FLAT_3, D4],
        [D3, G3, B_FLAT_3, D4],

        [G3],
        [G3, B_FLAT_3],
        [G3, B_FLAT_3, D4],
        [G3, B_FLAT_3, D4, E4],
        [G3, B_FLAT_3, D4, E4],
        [G3, B_FLAT_3, D4, E4],
        [G3, B_FLAT_3, D4, E4],
        [G3, B_FLAT_3, D4, E4],

        [D5],
        [A4],
        [F_SHARP_4],
        [D4],
        [A3],
        [F_SHARP_3],
        [D3],
        [A2],

        [D5],
        [A4],
        [F_SHARP_4],
        [D4],
        [A3],
        [F_SHARP_3],
        [D3],
        [A2],

        [E5],
        [B4],
        [G4],
        [E4],
        [E4],
        [B3],
        [G3],
        [E3],

        [E5],
        [B4],
        [G4],
        [E4],
        [E4],
        [B3],
        [G3],
        [E3],

        [G5],
        [D5],
        [B4],
        [G4],
        [G4],
        [D4],
        [B3],
        [G3],

        [G5],
        [D5],
        [B4],
        [G4],
        [G4],
        [D4],
        [B3],
        [G3],

        [D5],
        [B_FLAT_4],
        [G4],
        [D5],
        [B_FLAT_4],
        [G4],
        [D5],
        [B_FLAT_4],

        [E5],
        [D5],
        [B_FLAT_4],
        [G4],
        [E5],
        [D5],
        [B_FLAT_4],
        [G4],
    ]
)

wave: numpy.ndarray = render_wave(
    melody, SAMPLE_RATE, sine_wave
)
