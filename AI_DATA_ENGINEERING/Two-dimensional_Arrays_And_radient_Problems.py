import numpy as np
import matplotlib.pyplot as plt

# Create a linear function
def linear_function(x):
    """Returns the value of the linear function y = 2x + 1."""
    return 2 * x + 1

# Generate x values
x_values = np.linspace(-10, 10, 100)  # 100 points from -10 to 10
y_values = linear_function(x_values)   # Calculate y values using the linear function

# Concatenate arrays
data = np.column_stack((x_values, y_values))  # Combine x and y values into a single array

# Calculate gradients
def calculate_gradients(x):
    """Calculates the gradients of the linear function at given x values."""
    return np.gradient(linear_function(x))  # Use numpy's gradient function

gradients = calculate_gradients(x_values)  # Calculate gradients for the x values

# Plotting the linear function and its gradients
plt.figure(figsize=(10, 5))  # Set the figure size
plt.plot(x_values, y_values, label='Linear Function: y = 2x + 1', color='blue')  # Plot the linear function
plt.plot(x_values, gradients, label='Gradients', color='red', linestyle='--')  # Plot the gradients
plt.title('Linear Function and Gradients')  # Set the title of the plot
plt.xlabel('x')  # Label for x-axis
plt.ylabel('y')  # Label for y-axis
plt.legend()  # Show legend
plt.grid()  # Show grid
plt.show()  # Display the plot

# Template for gradient calculation function
def compute_gradient(func, x):
    """Computes the gradient of a function at a specific point using central difference."""
    h = 1e-5  # Small step for numerical differentiation
    return (func(x + h) - func(x - h)) / (2 * h)  # Central difference formula

# Example usage
x_point = 5  # Point at which to calculate the gradient
gradient_at_x = compute_gradient(linear_function, x_point)  # Calculate the gradient at x = 5
print(f'The gradient at x = {x_point} is {gradient_at_x}')  # Output the result
