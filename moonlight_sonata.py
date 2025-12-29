from music_player import *

C_SHARP_3 = 138
C_SHARP_2 = C_SHARP_3 / 2
C_SHARP_4 = C_SHARP_3 * 2
A2 = C_SHARP_3 * 4 / 5
A1 = A2 / 2
A3 = A2 * 2
C3 = A2 * 6 / 5
C4 = C3 * 2
F_SHARP_2 = C_SHARP_3 * 2 / 3
F_SHARP_1 = F_SHARP_2 / 2
F_SHARP_3 = F_SHARP_2 * 2
F_SHARP_4 = F_SHARP_2 * 4
D2 = F_SHARP_2 * 4 / 5
D3 = D2 * 2
D4 = D2 * 4
E3 = C_SHARP_3 * 6 / 5
E2 = E3 / 2
E4 = E3 * 2
G_SHARP_3 = C_SHARP_3 * 3 / 2
G_SHARP_2 = G_SHARP_3 / 2
G_SHARP_1 = G_SHARP_3 / 4
G_SHARP_4 = G_SHARP_3 * 2
B3 = G_SHARP_3 * 6 / 5
B2 = B3 / 2
B1 = B3 / 4
D_SHARP_4 = G_SHARP_3 * 3 / 2

BEATS_PER_MINUTE = 360
SAMPLES_PER_BEAT_ROUNDED = int(SAMPLE_RATE / (BEATS_PER_MINUTE / 60))

NOTE_AMPLITUDE = 0.25


melody = Melody(
    360,
    [
        [Note(sine_wave, C_SHARP_2, NOTE_AMPLITUDE, 24), Note(sine_wave, C_SHARP_3, NOTE_AMPLITUDE, 24), Note(sine_wave, G_SHARP_3, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, C_SHARP_4, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, E4, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, G_SHARP_3, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, C_SHARP_4, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, E4, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, G_SHARP_3, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, C_SHARP_4, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, E4, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, G_SHARP_3, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, C_SHARP_4, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, E4, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, B1, NOTE_AMPLITUDE, 24), Note(sine_wave, B2, NOTE_AMPLITUDE, 24), Note(sine_wave, G_SHARP_3, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, C_SHARP_4, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, E4, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, G_SHARP_3, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, C_SHARP_4, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, E4, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, G_SHARP_3, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, C_SHARP_4, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, E4, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, G_SHARP_3, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, C_SHARP_4, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, E4, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, A1, NOTE_AMPLITUDE, 12), Note(sine_wave, A2, NOTE_AMPLITUDE, 12), Note(sine_wave, A3, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, C_SHARP_4, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, E4, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, A3, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, C_SHARP_4, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, E4, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, F_SHARP_1, NOTE_AMPLITUDE, 12), Note(sine_wave, F_SHARP_2, NOTE_AMPLITUDE, 12), Note(sine_wave, A3, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, D4, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, F_SHARP_4, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, A3, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, D4, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, F_SHARP_4, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, G_SHARP_1, NOTE_AMPLITUDE, 12), Note(sine_wave, G_SHARP_2, NOTE_AMPLITUDE, 12), Note(sine_wave, G_SHARP_3, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, C4, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, F_SHARP_4, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, G_SHARP_3, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, C_SHARP_4, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, E4, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, G_SHARP_1, NOTE_AMPLITUDE, 12), Note(sine_wave, G_SHARP_2, NOTE_AMPLITUDE, 12), Note(sine_wave, G_SHARP_3, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, C_SHARP_4, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, D_SHARP_4, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, F_SHARP_3, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, C4, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, D_SHARP_4, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, C_SHARP_2, NOTE_AMPLITUDE, 24), Note(sine_wave, C_SHARP_2, NOTE_AMPLITUDE, 24), Note(sine_wave, E3, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, G_SHARP_3, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, C_SHARP_4, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, G_SHARP_3, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, C_SHARP_4, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, E4, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, G_SHARP_3, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, C_SHARP_4, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, E4, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, G_SHARP_3, NOTE_AMPLITUDE, 2), Note(sine_wave, G_SHARP_4, NOTE_AMPLITUDE, 5)], [],
        [Note(sine_wave, C_SHARP_4, NOTE_AMPLITUDE, 2)], [],
        [Note(sine_wave, E4, NOTE_AMPLITUDE, 2)], [Note(sine_wave, G_SHARP_4, NOTE_AMPLITUDE, 1)],
    ]
)

wave = render_wave(melody, SAMPLE_RATE, sine_wave)
