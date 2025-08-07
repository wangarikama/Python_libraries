import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests

#array of numbers 1 to 10 and mean
my_array = np.arange(1, 11)
mean_value = np.mean(my_array)
print("Array:", my_array)
print("Mean value:", mean_value)

#load dataset into pandas and show statistics
data  = {
    'Name': ['Kamau', 'Stephen', 'Chris'],
    'Age': [15, 18, 20],
    'Grade': ['80', '45', '68']  # Note: Grades are strings
}
df = pd.DataFrame(data)
print("\nSummary statistics:")
print(df.describe()) 

#fetch data from a public API 
response = requests.get('https://jsonplaceholder.typicode.com/posts')
if response.status_code == 200:
    api_data = response.json()
    print("\nAPI Data:")
else:
    print("\nFailed to fetch API data:", response.status_code) 

    #line graph
    months = ['January', 'February', 'March', 'April']
    sales = [1500, 2000, 1800, 2200]

    plt.figure(figsize=(10, 5))
    plt.plot(months, sales, marker='o')
    plt.title('Monthly Sales Data')
    plt.xlabel('Months')
    plt.ylabel('Sales')
    plt.grid(True)
    plt.show() 