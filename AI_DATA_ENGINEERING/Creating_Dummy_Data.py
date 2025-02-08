import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# 1. Creating random numbers using a two-dimensional normal distribution
mean = [0, 0]
cov = [[1, 0], [0, 1]]  # Diagonal covariance
data = np.random.multivariate_normal(mean, cov, 100)

# 2. Visualizing the data with scatter plots
plt.figure(figsize=(10, 6))
plt.scatter(data[:, 0], data[:, 1], alpha=0.5)
plt.title('Scatter Plot of Random Data')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid()
plt.show()

# 3. Creating histograms of the data
plt.figure(figsize=(10, 6))
plt.hist(data[:, 0], bins=20, alpha=0.5, label='X-axis data')
plt.hist(data[:, 1], bins=20, alpha=0.5, label='Y-axis data')
plt.title('Histograms of Random Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()
plt.show()

# 4. Adding new data points and combining them with the original set
new_data = np.random.multivariate_normal(mean, cov, 50)
combined_data = np.vstack((data, new_data))

# 5. Combining data into a single ndarray
combined_data = np.array(combined_data)

# 6. Labeling the data points
plt.figure(figsize=(10, 6))
plt.scatter(combined_data[:, 0], combined_data[:, 1], alpha=0.5)
for i in range(combined_data.shape[0]):
    plt.annotate(f'Point {i}', (combined_data[i, 0], combined_data[i, 1]), fontsize=8)
plt.title('Labeled Scatter Plot of Combined Data')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid()
plt.show()

