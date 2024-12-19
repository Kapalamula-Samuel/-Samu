# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Problem 1: Generate random numbers with a normal distribution
mean = 0  # Mean of the normal distribution
std_dev = 1  # Standard deviation of the normal distribution
num_samples = 1000  # Number of samples to generate
data = np.random.normal(mean, std_dev, num_samples)  # Generate random data

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
# Create a dictionary mapping labels to numerical values
label_mapping = {'A': 0, 'B': 1}  
# Map the labels in the 'labels' array to numerical values
numerical_labels = np.vectorize(label_mapping.get)(labels)  

# Visualize combined data with labels using numerical_labels for color
plt.scatter(x_combined, y_combined, c=numerical_labels, alpha=0.5)  # Create a scatter plot with color coding
plt.title('Combined Data with Labels')  # Title of the combined data plot
plt.xlabel('Combined X')  # X-axis label
plt.ylabel('Combined Y')  # Y-axis label
plt.show()  # Display the combined data plot
