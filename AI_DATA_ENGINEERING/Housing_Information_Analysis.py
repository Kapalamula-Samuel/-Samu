import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
# Download the dataset if it doesn't exist
!wget -nc http://jse.amstat.org/v19n3/decock/AmesHousing.txt
data = pd.read_csv('AmesHousing.txt', delimiter='\t') # Read data with tab delimiter

# Examine the dataset
print(data.head())
print(data.info())

# Check for missing values
missing_values = data.isnull().sum()
print(missing_values[missing_values > 0])

# Analyze the distribution of the target variable
sns.histplot(data['SalePrice'], kde=True)
plt.title('Distribution of Sale Price')
plt.xlabel('Sale Price')
plt.ylabel('Frequency')
plt.show()

# Research on kurtosis and skewness
kurtosis = data['SalePrice'].kurtosis()
skewness = data['SalePrice'].skew()
print(f'Kurtosis: {kurtosis}, Skewness: {skewness}')

# Check correlation coefficients between features
correlation_matrix = data.corr()
print(correlation_matrix['SalePrice'].sort_values(ascending=False))

# Create a heatmap to visualize the relationships
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()
