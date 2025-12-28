from music_player import *

C = 528
D = int(C * 9 / 8)
E = int(C * 5 / 4)
F = int(C * 4 / 3)
G = int(C * 3 / 2)
A = int(C * 5 / 3)
B = int(C * 15 / 8)
C2 = C << 1

# 2 ** 3, 2 ** 2, 3 ** 1, 2 ** 1, 3 ** 1, 2 ** 3 => 2 ** 3 * 3 ** 1 = 24
# 24 / 24, 27 / 24, 30 / 24, 32 / 24, 36 / 24, 40 / 24, 45 / 24, 48 / 24
# 24, 27, 30, 32, 36, 40, 45, 48
# CN / 3 / 8 = F(N - 2) / 8 = F(N - 5)

NOTES = [C, D, E, F, G, A, B, C2]

melody: Melody = Melody(
    60,
    [[x, y] for x in NOTES for y in NOTES]
)

wave: numpy.ndarray = render_wave(melody, SAMPLE_RATE, sine_wave)
