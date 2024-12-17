import math  # Importing math library for potential mathematical operations
import matplotlib.pyplot as plt  # Importing matplotlib for plotting

def time_to_cover_solar_system(initial_size, doubling_time, solar_system_size):
    time = 0  # Initialize time to zero
    size = initial_size  # Set the initial size of the bun
    sizes = [size]  # List to store sizes over time
    times = [time]  # List to store time points

    # Loop until the size of the bun reaches or exceeds the solar system size
    while size < solar_system_size:
        time += doubling_time  # Increment time by the doubling time
        size *= 2  # Doubling the size of the bun
        sizes.append(size)  # Appending the new size to the sizes list
        times.append(time)  # Appending the new time to the times list

    return time, sizes, times  # Return total time, sizes, and times

def plot_growth(times, sizes):
    plt.figure(figsize=(10, 5))  # Set the figure size for the plot
    plt.plot(times, sizes, marker='o')  # Plot sizes against time with markers
    plt.yscale('log')  # Set y-axis to logarithmic scale for better visualization
    plt.title('Growth of Chestnut Bun Size Over Time')  # Title of the plot
    plt.xlabel('Time (minutes)')  # Label for x-axis
    plt.ylabel('Size (units)')  # Label for y-axis
    plt.grid(True)  # Enable grid for better readability
    plt.show()  # Displaying the plot

if __name__ == "__main__":
    initial_size = 1  # Initial size of the chestnut bun
    doubling_time = 5  # Time in minutes for the size to double
    solar_system_size = 1.4e9  # Approximate size of the solar system in units

    # Calling the function to calculate total time, sizes, and times
    total_time, sizes, times = time_to_cover_solar_system(initial_size, doubling_time, solar_system_size)
    print(f'Time to cover the solar system: {total_time} minutes')  # Output the total time
    plot_growth(times, sizes)  # Calling the function to plot the growth

