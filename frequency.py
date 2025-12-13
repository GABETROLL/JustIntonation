import random
import sounddevice
import numpy


SAMPLE_RATE = 44100
old_frequency = 440
frequency = 512
start_index = 0


def sine_wave(hz: float, frames: int):
    t = (start_index + numpy.arange(frames)) / SAMPLE_RATE
    t = t.reshape(-1, 1)

    return numpy.sin(2 * numpy.pi * hz * t)


def almost_equal(a: float, b: float):
    return -0.01 < a - b < 0.01


def ascending(previous: float, next_sample: float):
    return previous < next_sample


def callback(outdata: numpy.ndarray, frames: int, time, status) -> None:
    """writes sound output to 'outdata' from sound_queue."""
    # params may need annotations... :/
    global start_index, old_frequency

    old_wave = sine_wave(old_frequency, frames)
    new_wave = sine_wave(frequency, frames)

    wave = old_wave

    if old_frequency != frequency:
        for index, (old_value, new_value) in enumerate(zip(old_wave, new_wave)):
            if almost_equal(old_value, new_value) and ascending(old_wave[index - 1], old_wave[index]):
                start_index += index
                wave[index:] = sine_wave(frequency, frames - index)
                start_index += frames - index
                break

        old_frequency = frequency
    else:
        start_index = (start_index + frames) % (SAMPLE_RATE / frequency)
    outdata[:] = wave


stream = sounddevice.OutputStream(channels=1, samplerate=SAMPLE_RATE, callback=callback)
stream.start()

while True:
    old_frequency = frequency
    frequency = random.randint(100, 1000)
    sounddevice.sleep(25)
