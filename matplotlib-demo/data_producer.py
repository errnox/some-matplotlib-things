import random


datafile = open('datafile', 'w')

for i in range(50):
    for j in range(3):
        datafile.write(str(random.randrange(0, 9, 1)))
    datafile.write('\n')

datafile.close()
