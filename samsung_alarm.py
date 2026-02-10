from music_player import *

D2 = 72                   # 1:1
E2 = D2 * 9 / 8           # 9:8
F_SHARP_2 = D2 * 5 / 4    # 5:4
G2 = D2 * 4 / 3           # 4:3
A2 = D2 * 3 / 2           # 3:2
B2 = D2 * 5 / 3           # 5:3
C_SHARP_3 = D2 * 15 / 8   # 15:8

D3 = D2 * 2               # 2:1
E3 = E2 * 2               # 9:4
F_SHARP_3 = F_SHARP_2 * 2 # 5:2
G3 = G2 * 2               # 8:3
A3 = A2 * 2               # 3:1
B3 = B2 * 2               # 10:3
C_SHARP_4 = C_SHARP_3 * 2 # 15:4

D4 = D3 * 2               # 4:1
E4 = E3 * 2               # 9:2
F_SHARP_4 = F_SHARP_3 * 2 # 5:1
G4 = G3 * 2               # 16:3
A4 = A3 * 2               # 6:1
B4 = B3 * 2               # 20:3
C_SHARP_5 = C_SHARP_4 * 2 # 15:2

D5 = D4 * 2               # 8:1
E5 = E4 * 2               # 9:1
F_SHARP_5 = F_SHARP_4 * 2 # 10:1
G5 = G4 * 2               # 32:3
A5 = A4 * 2               # 12:1
B5 = B4 * 2               # 40:3
C_SHARP_6 = C_SHARP_5 * 2 # 15:1

F_SHARP_1 = D2 * 5 / 8
A0 = D2 * 3 / 8
D_MINUS_1 = D2 / 8
D_SHARP_5 = D2 * 25 / 3
D1 = D2 / 2
A1 = D2 * 2 / 3
G0 = D2 * 1 / 3

melody: Melody = Melody(
    240,
    [
        [Note(D3, duration_in_beats=4), Note(F_SHARP_5, duration_in_beats=2)], [],    # 5:1   2:1 = D3
        [Note(E5, duration_in_beats=2)], [],                                                  # 9:2   1:1 = D2
        [Note(C_SHARP_3, duration_in_beats=4), Note(F_SHARP_5, duration_in_beats=1)], # 16:3  5:8 = F_SHARP_1
        [Note(A5, duration_in_beats=1)],                                                      # 32:5  3:8 = A0
        [Note(D5, duration_in_beats=2)], [],                                                  # 64:15 1:8 = D_MINUS_1
        [Note(B2, duration_in_beats=4), Note(F_SHARP_5, duration_in_beats=2)], [],    # 6:1   5:3 = B2
        [Note(E5, duration_in_beats=2)], [],                                                  # 27:5  1:3 = G0
        [Note(A2, duration_in_beats=4), Note(F_SHARP_5, duration_in_beats=1)],        # 20:3  1:2 = D1
        [Note(A5, duration_in_beats=1)],                                                      # 8:1   3:2 = A2
        [Note(D5, duration_in_beats=2)], [],                                                  # 16:3  1:2 = D1
        [Note(G2, duration_in_beats=4), Note(G5, duration_in_beats=1)],               # 8:1   4:3 = G2
        [Note(F_SHARP_5, duration_in_beats=1)],                                               # 15:2  2:3 = A1
        [Note(E5, duration_in_beats=1)],                                                      # 27:4  1:3 = G0
        [Note(D5, duration_in_beats=1)],                                                      # 6:1   4:3 = G2
        [Note(A2, duration_in_beats=4), Note(C_SHARP_5, duration_in_beats=1)],        # 5:1   3:2 = A2
        [Note(D5, duration_in_beats=1)],                                                      # 16:3  1:2 = D1
        [Note(E5, duration_in_beats=1)],                                                      # 6:1   3:2 = A2
        [Note(C_SHARP_5, duration_in_beats=1)],                                               # 5:1   3:2 = A2
        [Note(D3, duration_in_beats=8), Note(D5, duration_in_beats=1)],               # 2:1   2:1 = D3
        [Note(E5, duration_in_beats=1)],                                                      # 9:2   1:1 = D2
        [Note(F_SHARP_5, duration_in_beats=1)],                                               # 5:1   2:1 = D3
        [Note(G5, duration_in_beats=1)],                                                      # 16:3  2:3 = A1
        [Note(A5, duration_in_beats=2)], [],                                                  # 6:1   2:1 = D3
        [Note(A4, duration_in_beats=2)], [],                                                  # 3:1   2:1 = D3
        [Note(D3, duration_in_beats=4), Note(F_SHARP_5, duration_in_beats=2)], [],    # 5:1   2:1 = D3
        [Note(E5, duration_in_beats=2)], [],                                                  # 9:2   1:1 = D2
        [Note(C_SHARP_3, duration_in_beats=4), Note(F_SHARP_5, duration_in_beats=1)], # 16:3  5:8 = F_SHARP_1
        [Note(A5, duration_in_beats=1)],                                                      # 32:5  3:8 = A0
        [Note(D5, duration_in_beats=2)], [],                                                  # 64:15 1:8 = D_MINUS_1
        [Note(B2, duration_in_beats=4), Note(F_SHARP_5, duration_in_beats=2)], [],    # 6:1   5:3 = B2
        [Note(E5, duration_in_beats=2)], [],                                                  # 27:5  1:3 = G0
        [Note(A2, duration_in_beats=4), Note(F_SHARP_5, duration_in_beats=1)],        # 20:3  1:2 = D1
        [Note(A5, duration_in_beats=1)],                                                      # 8:1   3:2 = A2
        [Note(D5, duration_in_beats=2)], [],                                                  # 16:3  1:2 = D1
        [Note(G2, duration_in_beats=4), Note(G5, duration_in_beats=1)],               # 8:1   4:3 = G2
        [Note(F_SHARP_5, duration_in_beats=1)],                                               # 15:2  2:3 = A1
        [Note(E5, duration_in_beats=1)],                                                      # 27:4  1:3 = G0
        [Note(D5, duration_in_beats=1)],                                                      # 6:1   4:3 = G2
        [Note(A2, duration_in_beats=4), Note(C_SHARP_5, duration_in_beats=1)],        # 5:1   3:2 = A2
        [Note(D5, duration_in_beats=1)],                                                      # 16:3  1:2 = D1
        [Note(E5, duration_in_beats=1)],                                                      # 6:1   3:2 = A2
        [Note(C_SHARP_5, duration_in_beats=1)],                                               # 5:1   3:2 = A2
        [Note(D3, duration_in_beats=8), Note(D5, duration_in_beats=1)],               # 4:1   2:1 = D3
        [Note(A5, duration_in_beats=1)],                                                      # 6:1   2:1 = D3
        [Note(F_SHARP_5, duration_in_beats=1)],                                               # 5:1   2:1 = D3
        [Note(A5, duration_in_beats=1)],                                                      # 6:1   2:1 = D3
        [Note(D5, duration_in_beats=4)], [], [], [],                                          # 4:1   2:1 = D3
    ],
)

wave: numpy.ndarray = render_wave(
    melody,
    SAMPLE_RATE,
    dampened_piano_wave,
    0.2
)

# print(melody.notes)
