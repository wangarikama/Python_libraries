from matplotlib import pyplot as plt

# Example data for a bar chart
countries = ['south africa', 'Kenya', 'canada', 'Germany', 'France']
population = [5_000_000, 80_000_000, 60_000_000, 90_000_000, 70_000_000]

plt.bar(countries, population, color='red')
plt.title('Population by Country')
plt.xlabel('Countries')
plt.ylabel('Population')
plt.show()