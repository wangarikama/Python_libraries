import matplotlib.pyplot as plt

# Example data for a line chart
time_of_day = ['Morning', 'Afternoon', 'Evening', 'Night']
temperatures = [20, 25, 22, 18]

plt.plot(time_of_day, temperatures, marker='o')
plt.title('Temperature Variation Throughout the Day')
plt.xlabel('Time of Day')
plt.ylabel('Temperature (°C)')
plt.grid()
plt.show()