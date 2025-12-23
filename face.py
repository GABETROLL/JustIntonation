from music_player import *
from frequency_ratios import *

F4 = (1 << 5) * 11
A4 = (F4 * 5) >> 2  # 2
C5 = (F4 * 3) >> 1  # 1
C4 = (F4 * 3) >> 2  # 2
E5 = (F4 * 15) >> 3 # 3
E4 = (F4 * 15) >> 4 # 4
G4 = (F4 * 9) >> 3  # 3
B4 = (F4 * 45) >> 5 # 5
D5 = (F4 * 27) >> 4 # 4
D4 = (F4 * 27) >> 5 # 5

melody = Melody(
    60,
    [
        [F4, A4, C5, E5],
        [F4, A4, B4, D5],
        [E4, G4, B4, D5],
        [E4, G4, A4, C5],
        [D4, F4, A4, C5],
        [D4, F4, G4, B4],
        [C4, E4, G4, C5],
    ],
)

# for index in range(len(melody.notes)):
#     print(simplify_fraction(melody.notes[index]))

wave = render_wave(
    melody,
    SAMPLE_RATE,
    sine_wave,
)
