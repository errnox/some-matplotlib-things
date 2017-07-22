import numpy as np
import matplotlib.pyplot as plt
import pylab


num_rows = 6
num_data_sets = 4
num_data_points = 50


fig = plt.figure()

for row_num in range(num_rows):
  subplot = plt.subplot(num_rows / 2, 2, row_num + 1)

  # Preciser title positioning
  plt.text(.5, .75, "Plot #%s" % str(row_num + 1), rotation=45)
  plt.xlabel('Foo')
  plt.ylabel('Bar')
  plt.grid(True)

  # Alternative:
  # plt.title("Plot #%s" % str(row_num))

  for data_set_num in range(num_data_sets):
    plt.plot(sorted(np.random.random(num_data_points)), '-')

    # Some modifications
    #
    # plt.errorbar(sorted(np.random.random(num_data_points))[data_set_num],
    #                     data_set_num, xerr=.2, yerr=.4)
    #
    # plt.imshow(pylab.rand(5, 5), interpolation='nearest')

# Tighter layout for readable subplot titles
plt.tight_layout()
plt.show()
