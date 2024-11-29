import numpy as np
import matplotlib.pyplot as plt
covid_data = np.array([
    [1500, 2000, 1800, 1200, 900],  # Day 1
    [1600, 2100, 1900, 1300, 950],  # Day 2
    [1700, 2200, 2000, 1400, 1000],  # Day 3
    [1650, 2150, 1950, 1350, 980],  # Day 4
    [1750, 2250, 2050, 1450, 1020],  # Day 5
    [1800, 2300, 2100, 1500, 1050],  # Day 6
    [1900, 2400, 2200, 1600, 1100]   # Day 7
])
total_cases_per_country = covid_data.sum(axis=0)
highest_total_cases_country = np.argmax(total_cases_per_country)
average_daily_cases = covid_data.mean(axis=1)
highest_daily_total_cases = np.argmax(covid_data.sum(axis=1))
percentage_change = ((covid_data[-1] - covid_data[0]) / covid_data[0]) * 100
highest_percentage_increase_country = np.argmax(percentage_change)
normalized_data = (covid_data - covid_data.min(axis=0)) / (covid_data.max(axis=0) - covid_data.min(axis=0))
days = np.arange(1, 8)
countries = ['Country A', 'Country B', 'Country C', 'Country D', 'Country E']
plt.figure(figsize=(10, 6))
for i in range(covid_data.shape[1]):
    plt.plot(days, covid_data[:, i], marker='o', label=countries[i])
highest_day = highest_daily_total_cases + 1
highest_day_total = covid_data.sum(axis=1)[highest_daily_total_cases]

plt.axvline(x=highest_day, color='red', linestyle='--', label='Highest Total Cases Day')
plt.scatter([highest_day], [highest_day_total], color='red', zorder=5, label='Highest Day Total')
plt.title('Daily COVID-19 Cases for Each Country')
plt.xlabel('Days')
plt.ylabel('Number of Cases')
plt.xticks(days)
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
print("Task 1: Basic Statistics")
print("Total cases per country:", total_cases_per_country)
print("Country with highest total cases:", countries[highest_total_cases_country])

print("\nTask 2: Daily Analysis")
print("Average daily cases across all countries:", average_daily_cases)
print("Day with highest total cases:", highest_day)

print("\nTask 3: Trends")
print("Percentage change (Day 1 to Day 7) per country:", percentage_change)
print("Country with highest percentage increase:", countries[highest_percentage_increase_country])

print("\nTask 4: Normalized Data")
print("Normalized dataset:\n", normalized_data)