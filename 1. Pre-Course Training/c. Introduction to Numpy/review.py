import numpy as np

temperatures = np.genfromtxt('temperature_data.csv', delimiter=',')

# TODO
temperatures_fixed = temperatures + 3

# TODO
monday_temperatures = temperatures_fixed[0]

# TODO
thursday_friday_morning = temperatures_fixed[3:5, 1]

# TODO
temperature_extremes = temperatures_fixed[(temperatures_fixed < 50) | (temperatures_fixed > 60)]