import matplotlib.pyplot as plt

date = ['2017-01-01', '2017-01-01', '2017-01-03', '2017-01-04', '2017-01-05']
amount_37 = [18207.52, 11150.29, 6986.73, 7441.53, 4867.45]
amount_20 = [3678.06, 29876.00, 11996.56, 30987.45, 29510.77]

plt.plot(date, amount_37, color='green', label='37')
plt.plot(date, amount_20, color='red', label=20)
plt.show()