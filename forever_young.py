from music_player import *

ONE_3 = 528
THREE_3 = int(ONE_3 * 5 / 4)
FIVE_3 = int(ONE_3 * 3 / 2)
SEVEN_3 = int(ONE_3 * 15 / 8)
TWO_3 = int(ONE_3 * 9 / 8)
SIX_3 = int(ONE_3 * 5 / 3)
FOUR_3 = int(ONE_3 * 4 / 3)
"""TWO_3 = ONE_3 * 2 ** (2 / 12)
THREE_3 = ONE_3 * 2 ** (4 / 12)
FOUR_3 = ONE_3 * 2 ** (5 / 12)
FIVE_3 = ONE_3 * 2 ** (7 / 12)
SIX_3 = ONE_3 * 2 ** (9 / 12)
SEVEN_3 = ONE_3 * 2 ** (11 / 12)"""

ONE_2 = ONE_3 >> 1
TWO_2 = TWO_3 >> 1
FOUR_2 = FOUR_3 >> 1
FIVE_2 = FIVE_3 >> 1
SIX_2 = SIX_3 >> 1
SEVEN_2 = SEVEN_3 >> 1

notes = [
    [ONE_3, THREE_3, FIVE_3],
    [ONE_3, THREE_3, FIVE_3],
    [ONE_3, THREE_3, FIVE_3, FIVE_3],
    [ONE_3, THREE_3, FIVE_3, SIX_3],
    [ONE_3, THREE_3, FIVE_3, SIX_3],
    [ONE_3, THREE_3, FIVE_3, SIX_3],
    [ONE_3, THREE_3, FIVE_3, FIVE_3],
    [ONE_3, THREE_3, FIVE_3, FIVE_3],

    [SEVEN_2, TWO_3, FIVE_3, TWO_3],
    [SEVEN_2, TWO_3, FIVE_3, TWO_3],
    [SEVEN_2, TWO_3, FIVE_3, TWO_3],
    [SEVEN_2, TWO_3, FIVE_3, TWO_3],
    [SEVEN_2, TWO_3, FIVE_3, TWO_3],
    [SEVEN_2, TWO_3, FIVE_3, THREE_3],
    [SEVEN_2, TWO_3, FIVE_3, FOUR_3],
    [SEVEN_2, TWO_3, FIVE_3, THREE_3],

    [SIX_2, ONE_3, THREE_3, THREE_3],
    [SIX_2, ONE_3, THREE_3, THREE_3],
    [SIX_2, ONE_3, THREE_3, FIVE_3],
    [SIX_2, ONE_3, THREE_3, FOUR_3],
    [SIX_2, ONE_3, THREE_3, FOUR_3],
    [SIX_2, ONE_3, THREE_3, FOUR_3],
    [SIX_2, ONE_3, THREE_3, THREE_3],
    [SIX_2, ONE_3, THREE_3, ONE_3],

    [FOUR_2, SIX_2, ONE_3, ONE_3],
    [FOUR_2, SIX_2, ONE_3, ONE_3],
    [FOUR_2, SIX_2, ONE_3, ONE_3],
    [FOUR_2, SIX_2, ONE_3, ONE_3, ONE_2, FOUR_2],
    [FOUR_2, SIX_2, ONE_3, ONE_3, FOUR_2, SIX_2],
    [FOUR_2, SIX_2, ONE_3, ONE_3, FOUR_2, SIX_2],
    [FOUR_2, SIX_2, ONE_3, ONE_3, SIX_2, ONE_3],
    [FOUR_2, SIX_2, ONE_3, ONE_3, SIX_2, ONE_3],

    [FIVE_2, SEVEN_2, TWO_3, SEVEN_2, TWO_3],
    [FIVE_2, SEVEN_2, TWO_3, SEVEN_2, TWO_3],
    [FIVE_2, SEVEN_2, TWO_3, TWO_3],
    [FIVE_2, SEVEN_2, TWO_3, TWO_3],
    [FIVE_2, SEVEN_2, TWO_3, TWO_3],
    [FIVE_2, SEVEN_2, TWO_3, TWO_3],
    [FIVE_2, SEVEN_2, TWO_3, THREE_3],
    [FIVE_2, SEVEN_2, TWO_3, FOUR_3],

    [SIX_2, ONE_3, THREE_3, THREE_3],
    [SIX_2, ONE_3, THREE_3, THREE_3],
    [SIX_2, ONE_3, THREE_3, TWO_3],
    [SIX_2, ONE_3, THREE_3, ONE_3],
    [SIX_2, ONE_3, THREE_3, ONE_3],
    [SIX_2, ONE_3, THREE_3, ONE_3],
    [SIX_2, ONE_3, THREE_3, SIX_2],
    [SIX_2, ONE_3, THREE_3, SIX_2],

    [FOUR_2, SIX_2, ONE_3, SIX_2],
    [FOUR_2, SIX_2, ONE_3, ONE_3],
    [FOUR_2, SIX_2, ONE_3, ONE_3],
    [FOUR_2, SIX_2, ONE_3, ONE_3],
    [FOUR_2, SIX_2, ONE_3, ONE_3],
    [FOUR_2, SIX_2, ONE_3, ONE_3],
    [FOUR_2, SIX_2, ONE_3, SIX_2],
    [FOUR_2, SIX_2, ONE_3, SIX_2],

    [FIVE_2, SEVEN_2, TWO_3, SIX_2],
    [FIVE_2, SEVEN_2, TWO_3, TWO_3],
    [FIVE_2, SEVEN_2, TWO_3, TWO_3],
    [FIVE_2, SEVEN_2, TWO_3, THREE_3],
    [FIVE_2, SEVEN_2, TWO_3, THREE_3],
    [FIVE_2, SEVEN_2, TWO_3, THREE_3],
    [FIVE_2, SEVEN_2, TWO_3, FOUR_3],
    [FIVE_2, SEVEN_2, TWO_3, FOUR_3],
]

BEATS_PER_MINUTE = 240
SAMPLES_PER_BEAT = SAMPLE_RATE // (BEATS_PER_MINUTE // 60)

melody = Melody(SAMPLES_PER_BEAT, notes)

wave = render_wave(melody, SAMPLE_RATE, sine_wave, 1 / 10)
