# Sorori Shinzaemon Problem

import matplotlib.pyplot as plt

def rice_grains_per_day(day):
#Calculating the number of rice grains received on a specific day.
    return 2 ** (day - 1)

def cumulative_rice_grains(day):
#Calculating the cumulative total of rice grains up to a specific day.
    return (2 ** day) - 1

def survival_days(rice_grains, people):
#Determine how many days people can survive based on the amount of rice.
    daily_rice = rice_grains / people
    days = 0
    while daily_rice >= 1:
        days += 1
        daily_rice -= rice_grains_per_day(days)
    return days

def plot_rice_growth(days):
#Ploting a line graph to visualize the trend of rice accumulation.
    x = list(range(1, days + 1))
    y = [cumulative_rice_grains(day) for day in x]
    
    plt.plot(x, y, marker='o')
    plt.title('Rice Accumulation Over Days')
    plt.xlabel('Days')
    plt.ylabel('Cumulative Rice Grains')
    plt.grid()
    plt.show()

# Example usage
if __name__ == "__main__":
    day = 10
    print(f"Rice grains on day {day}: {rice_grains_per_day(day)}")
    print(f"Cumulative rice grains up to day {day}: {cumulative_rice_grains(day)}")
    
    total_rice = 1024  # Example total rice grains
    total_people = 4   # Example number of people
    print(f"Days of survival for {total_people} people with {total_rice} grains: {survival_days(total_rice, total_people)}")
    
    plot_rice_growth(day)
