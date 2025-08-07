import matplotlib.pyplot as plt

# Example data for a pie chart
activities = ['Reading', 'Gaming', 'Sports', 'Traveling']
hours_spent = [6, 8, 5, 5] 
plt.pie(hours_spent, labels=activities, autopct='%1.1f%%')
plt.title('Time Spent on Activities')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()