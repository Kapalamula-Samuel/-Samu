import numpy as np
import matplotlib.pyplot as plt

# Function to generate elevation data based on a sine function
def generate_elevation_data(x, y):
    return np.sin(np.sqrt(x**2 + y**2))

# Function to calculate the gradient of the elevation data
def calculate_gradient(x, y):
    # Calculate partial derivatives
    dx = np.cos(np.sqrt(x**2 + y**2)) * (x / np.sqrt(x**2 + y**2))
    dy = np.cos(np.sqrt(x**2 + y**2)) * (y / np.sqrt(x**2 + y**2))
    return np.array([dx, dy])  # Return gradient as a numpy array

# Function to perform gradient descent
def gradient_descent(starting_point, learning_rate, num_iterations):
    point = np.array(starting_point)  # Convert starting point to numpy array
    path = [point]  # Initialize path with the starting point
    
    for _ in range(num_iterations):
        grad = calculate_gradient(point[0], point[1])  # Calculate gradient at current point
        point = point - learning_rate * grad  # Update point by moving against the gradient
        path.append(point)  # Append new point to path
    
    return path  # Return the path taken during descent

# Visualization of the descent path on a contour plot
def visualize_descent(path):
    x = np.linspace(-5, 5, 100)  # Create an array of x values
    y = np.linspace(-5, 5, 100)  # Create an array of y values
    X, Y = np.meshgrid(x, y)  # Create a grid of x and y values
    Z = generate_elevation_data(X, Y)  # Generate elevation data for the grid

    # Create a filled contour plot
    plt.contourf(X, Y, Z, levels=50, cmap='viridis')
    path = np.array(path)  # Convert path to numpy array for plotting
    plt.plot(path[:, 0], path[:, 1], marker='o', color='red')  # Plot the descent path
    plt.title('Gradient Descent Path')  # Set plot title
    plt.xlabel('X-axis')  # Label x-axis
    plt.ylabel('Y-axis')  # Label y-axis
    plt.colorbar(label='Elevation')  # Add color bar to indicate elevation levels
    plt.show()  # Display the plot

# Parameters for gradient descent
starting_point = [4, 4]  # Initial point for descent
learning_rate = 0.1  # Step size for each iteration
num_iterations = 50  # Number of iterations to perform

# Execute gradient descent and store the path
path = gradient_descent(starting_point, learning_rate, num_iterations)

# Visualize the result of the gradient descent
visualize_descent(path)
