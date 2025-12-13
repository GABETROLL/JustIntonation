import numpy
from matplotlib import pyplot

frames = 383
samplerate = 44100

t = (numpy.arange(frames)) / samplerate
t = t.reshape(-1, 1)

pyplot.plot(numpy.sin(2 * numpy.pi * 440 * t))
pyplot.show()
