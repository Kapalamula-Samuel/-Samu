# Introduction to Data Analysis using Fisher's Iris Dataset

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Dataset Preparation
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
iris_data = pd.read_csv(url, header=None, names=columns)

# Data Overview
print(iris_data.head())
print(iris_data.describe())
print(iris_data.info())

# Feature Exploration
sns.pairplot(iris_data, hue='species')
plt.show()

# Confirming Relationships between Features
# Select only numerical columns for correlation calculation
numerical_data = iris_data.select_dtypes(include=['number'])  
correlation_matrix = numerical_data.corr()
sns.heatmap(correlation_matrix, annot=True)
plt.show()

# Proposing a Method
# Extracting necessary data
X = iris_data.drop('species', axis=1)
y = iris_data['species']

# Creating Diagrams
sns.boxplot(x='species', y='sepal_length', data=iris_data)
plt.show()

# Explaining Results of Visualized Graphs and Tables
# The visualizations provide insights into the distribution and relationships of the features.
