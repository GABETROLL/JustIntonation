from music_player import *
from frequency_ratios import *

F3 = (1 << 5) * 11
A3 = (F3 * 5) >> 2        # 2 ** 2
C4 = (F3 * 3) >> 1        # 2 ** 1
C3 = (F3 * 3) >> 2        # 2 ** 2
E4 = (F3 * 15) >> 3       # 2 ** 3
E3 = (F3 * 15) >> 4       # 2 ** 4
G3 = (F3 * 9) >> 3        # 2 ** 3
B3 = (F3 * 45) >> 5       # 2 ** 5
D4 = (F3 * 27) >> 4       # 2 ** 4
D3 = (F3 * 27) >> 5       # 2 ** 5

BEATS_PER_MINUTE = 320
BEATS_PER_SECOND = BEATS_PER_MINUTE / 60
SAMPLES_PER_BEAT = int(SAMPLE_RATE / BEATS_PER_SECOND)

CHORD_AMPLITUDE = 0.4 / 4

VOICE_AMPLITUDE = 0.6


melody = ObjectiveMelody(
    SAMPLES_PER_BEAT,
    [
        [
            ObjectiveNote(frequency, dampened_piano_wave, CHORD_AMPLITUDE, 8) # F3 / 8 or F0 (44Hz)
            for frequency in [F3, A3, C4, E4]
        ], [], [], [], [], [], [], [],

        [
            ObjectiveNote(frequency, dampened_piano_wave, CHORD_AMPLITUDE, 8) # F3 / 16 or F-1 (22Hz)
            for frequency in [F3, A3, B3, D4]
        ], [], [], [], [], [], [], [],

        [
            ObjectiveNote(frequency, dampened_piano_wave, CHORD_AMPLITUDE, 8) # E3 / 10 or B-1 (33Hz)
            for frequency in [E3, G3, B3, D4]
        ], [], [], [], [], [], [], [],

        [
            ObjectiveNote(frequency, dampened_piano_wave, CHORD_AMPLITUDE, 8) # E3 / 15 or F-1 (22Hz)
            for frequency in [E3, G3, A3, C4]
        ], [], [], [], [], [], [], [],

        [
            ObjectiveNote(frequency, dampened_piano_wave, CHORD_AMPLITUDE, 8) # F3 / 27 or D_SHARP_0 (13.037...Hz)
            for frequency in [D3, F3, A3, C4]
        ], [], [], [], [], [], [], [],

        [
            ObjectiveNote(frequency, dampened_piano_wave, CHORD_AMPLITUDE, 8) # F3 / 27 or D_SHARP_0 (13.037...Hz)
            for frequency in [D3, F3, G3, B3]
        ], [], [], [], [], [], [], [],

        [
            ObjectiveNote(frequency, dampened_piano_wave, CHORD_AMPLITUDE, 16) # C3 / 4 or C1 (132Hz)
            for frequency in [C3, E3, G3, C4]
        ], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],

        [
            ObjectiveNote(frequency, dampened_piano_wave, CHORD_AMPLITUDE, 8)
            for frequency in [F3, A3, C4, E4]
        ],
        [],
        [],
        [ObjectiveNote(E4, dampened_piano_wave, VOICE_AMPLITUDE, 3)],
        [],
        [],
        [],
        [],

        [
            ObjectiveNote(frequency, dampened_piano_wave, CHORD_AMPLITUDE, 8)
            for frequency in [F3, A3, B3, D4]
        ],
        [],
        [],
        [ObjectiveNote(C4, dampened_piano_wave, VOICE_AMPLITUDE, 1)],
        [ObjectiveNote(D4, dampened_piano_wave, VOICE_AMPLITUDE, 1)],
        [ObjectiveNote(C4, dampened_piano_wave, VOICE_AMPLITUDE, 1)],
        [ObjectiveNote(D4, dampened_piano_wave, VOICE_AMPLITUDE, 2)],
        [],

        [
            ObjectiveNote(frequency, dampened_piano_wave, CHORD_AMPLITUDE, 8)
            for frequency in [E3, G3, B3, D4]
        ],
        [],
        [],
        [ObjectiveNote(C4, dampened_piano_wave, VOICE_AMPLITUDE, 1)],
        [ObjectiveNote(D4, dampened_piano_wave, VOICE_AMPLITUDE, 1)],
        [ObjectiveNote(C4, dampened_piano_wave, VOICE_AMPLITUDE, 1)],
        [ObjectiveNote(D4, dampened_piano_wave, VOICE_AMPLITUDE, 1)],
        [ObjectiveNote(E4, dampened_piano_wave, VOICE_AMPLITUDE, 1)],

        [
            ObjectiveNote(frequency, dampened_piano_wave, CHORD_AMPLITUDE, 8)
            for frequency in [E3, G3, A3, C4]
        ],
        [],
        [],
        [ObjectiveNote(C4, dampened_piano_wave, VOICE_AMPLITUDE, 1)],
        [ObjectiveNote(B3, dampened_piano_wave, VOICE_AMPLITUDE, 1)],
        [ObjectiveNote(A3, dampened_piano_wave, VOICE_AMPLITUDE, 3)],
        [],
        [],

        [
            ObjectiveNote(frequency, dampened_piano_wave, CHORD_AMPLITUDE, 8)
            for frequency in [D3, F3, A3, C4]
        ], [], [], [], [], [], [], [],

        [
            ObjectiveNote(frequency, dampened_piano_wave, CHORD_AMPLITUDE, 8)
            for frequency in [D3, F3, G3, B3]
        ],
        [],
        [],
        [ObjectiveNote(B3, dampened_piano_wave, VOICE_AMPLITUDE, 2)],
        [],
        [ObjectiveNote(C4, dampened_piano_wave, VOICE_AMPLITUDE, 1)],
        [ObjectiveNote(D4, dampened_piano_wave, VOICE_AMPLITUDE, 1)],
        [ObjectiveNote(E4, dampened_piano_wave, VOICE_AMPLITUDE, 1)],

        [
            ObjectiveNote(frequency, dampened_piano_wave, CHORD_AMPLITUDE, 16)
            for frequency in [C3, E3, G3, C4]
        ] + [ObjectiveNote(B3, dampened_piano_wave, VOICE_AMPLITUDE, 3)],
        [],
        [],
        [ObjectiveNote(A3, dampened_piano_wave, VOICE_AMPLITUDE, 1)],
        [ObjectiveNote(G3, dampened_piano_wave, VOICE_AMPLITUDE, 1)],
        [ObjectiveNote(A3, dampened_piano_wave, VOICE_AMPLITUDE, 1)],
        [ObjectiveNote(B3, dampened_piano_wave, VOICE_AMPLITUDE, 1)],
        [ObjectiveNote(C4, dampened_piano_wave, VOICE_AMPLITUDE, 1)],

        [ObjectiveNote(D4, dampened_piano_wave, VOICE_AMPLITUDE, 1)],
        [ObjectiveNote(C4, dampened_piano_wave, VOICE_AMPLITUDE, 3)],
        [], [], [], [], [], [],
    ],
)

# for index in range(len(melody.notes)):
#     print(simplify_fraction(melody.notes[index]))

wave = render_wave(
    melody,
    SAMPLE_RATE,
    dampened_piano_wave,
)
