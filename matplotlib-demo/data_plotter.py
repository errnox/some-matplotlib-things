import numpy
import pylab


"""
Simple Line Plot
----------------

Shows how to make and save a simple line plot with labels, title and grid.
"""


data = numpy.loadtxt('./datafile')
pylab.plot(data)

pylab.xlabel('time (s)')
pylab.ylabel('temperature (degrees C)')
pylab.title('Simple data visualization')
pylab.grid(True)
pylab.savefig('simple_plot')

pylab.show()
