import numpy as np
import matplotlib.pyplot as plt

# Parameters for the normal distribution
mean = 0
std_dev = 1
num_samples = 500

# Generate normally distributed data
data = np.random.normal(mean, std_dev, num_samples)

# Problem 2: Visualize the data with a histogram
plt.hist(data, bins=30, alpha=0.7, color='blue')  # Create a histogram
plt.title('Histogram of Normally Distributed Data')  # Title of the histogram
plt.xlabel('Value')  # X-axis label
plt.ylabel('Frequency')  # Y-axis label
plt.show()  # Display the histogram

# Problem 3: Visualize the data with a scatter plot
x = np.random.rand(num_samples)  # Generate random x values
y = data  # Use the normally distributed data for y values
plt.scatter(x, y, alpha=0.5)  # Create a scatter plot
plt.title('Scatter Plot of Random Data')  # Title of the scatter plot
plt.xlabel('Random X')  # X-axis label
plt.ylabel('Normally Distributed Y')  # Y-axis label
plt.show()  # Display the scatter plot

# Problem 4: Add new data
new_data = np.random.normal(mean, std_dev, num_samples)  # Generate new random data
combined_data = np.concatenate((data, new_data))  # Combine the original and new data

# Problem 5: Combine datasets
x_combined = np.concatenate((x, np.random.rand(num_samples)))  # Combine x values
y_combined = combined_data  # Use the combined data for y values

# Problem 6: Label the data
labels = np.array(['A'] * num_samples + ['B'] * num_samples)  # Create labels for the data

# Convert labels to numerical values for color mapping
label_mapping = {'A': 0, 'B': 1}  # Create a dictionary mapping labels to numerical values
numerical_labels = np.vectorize(label_mapping.get)(labels)  # Map the labels in the 'labels' array to numerical values

# Visualize combined data with labels using numerical_labels for color
plt.scatter(x_combined, y_combined, c=numerical_labels, alpha=0.5)  # Create a scatter plot with color coding
plt.title('Combined Data with Labels')  # Title of the combined data plot
plt.xlabel('Combined X')  # X-axis label
plt.ylabel('Combined Y')  # Y-axis label
plt.show()  # Display the combined data plot

# Additional Task: Using np.random.multivariate_normal() to create 500 random numbers
mean_vector = [0, 0]  # Mean for the two-dimensional normal distribution
cov_matrix = [[1, 0], [0, 1]]  # Covariance matrix
multivariate_data = np.random.multivariate_normal(mean_vector, cov_matrix, 500)  # Generate 500 random numbers

# Visualizing the multivariate normal distribution
plt.scatter(multivariate_data[:, 0], multivariate_data[:, 1], alpha=0.5, color='green')  # Scatter plot for multivariate data
plt.title('Scatter Plot of Multivariate Normal Distribution')  # Title for the multivariate plot
plt.xlabel('X-axis')  # X-axis label
plt.ylabel('Y-axis')  # Y-axis label
plt.show()  # Display the multivariate plot
