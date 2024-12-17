import matplotlib.pyplot as plt

def rice_grains_per_day(day):
    # Calculating the number of rice grains received on a specific day.
    return 2 ** (day - 1)

def cumulative_rice_grains(day):
    # Calculating the cumulative total of rice grains up to a specific day.
    total_rice = sum(rice_grains_per_day(d) for d in range(1, day + 1))
    return total_rice

def survival_days(total_rice, total_people):
    # Calculate how many days the rice will last for a given number of people.
    return total_rice // total_people

def plot_rice_growth(days):
    # Generate lists for daily and cumulative rice grains over the specified number of days.
    daily_rice = [rice_grains_per_day(d) for d in range(1, days + 1)]
    cumulative_rice = [cumulative_rice_grains(d) for d in range(1, days + 1)]
    
    # Create a plot to visualize the data.
    plt.figure(figsize=(10, 5))
    plt.plot(range(1, days + 1), daily_rice, label='Daily Rice Received', color='blue')
    plt.plot(range(1, days + 1), cumulative_rice, label='Cumulative Rice Received', color='orange')
    plt.title('Rice Grain Distribution Over Time')
    plt.xlabel('Days')
    plt.ylabel('Number of Rice Grains')
    plt.legend()
    plt.grid()
    plt.show()

# Example usage
days = 100  # Total number of days to simulate
total_people = 4  # Example number of people
total_rice = cumulative_rice_grains(days)  # Calculate total rice for the given days
print(f"Days of survival for {total_people} people with {total_rice} grains: {survival_days(total_rice, total_people)}")

# Plot the rice growth over the specified number of days
plot_rice_growth(days)
