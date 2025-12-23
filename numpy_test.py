import numpy
from matplotlib import pyplot

start_sample_index: int = 0
end_sample_index: int = 14400

sample_rate: int = 14400
frequency_0: int = 432
frequency_1: int = int(432 * 5 / 4)

samples: numpy.ndarray = numpy.arange(start_sample_index, end_sample_index)

domain_0: numpy.ndarray = samples * frequency_0 % sample_rate * 2 * (numpy.pi / sample_rate)
domain_1: numpy.ndarray = samples * frequency_1 % sample_rate * 2 * (numpy.pi / sample_rate)

pyplot.plot(numpy.sin(domain_0))
pyplot.plot(numpy.sin(domain_1))
pyplot.show()
