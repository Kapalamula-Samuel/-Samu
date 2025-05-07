import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
def load_data(url: str, filename: str) -> pd.DataFrame:
    """Download and load the dataset from the specified URL."""
    !wget -nc {url}
    return pd.read_csv(filename, delimiter='\t')

# Examine the dataset
def examine_data(data: pd.DataFrame) -> None:
    """Print the first few rows and information about the dataset."""
    print(data.head())
    print(data.info())

# Check for missing values
def check_missing_values(data: pd.DataFrame) -> None:
    """Identify and print missing values in the dataset."""
    missing_values = data.isnull().sum()
    print(missing_values[missing_values > 0])

# Analyze the distribution of the target variable
def plot_sale_price_distribution(data: pd.DataFrame) -> None:
    """Visualize the distribution of the Sale Price variable."""
    sns.histplot(data['SalePrice'], kde=True)
    plt.title('Distribution of Sale Price')
    plt.xlabel('Sale Price')
    plt.ylabel('Frequency')
    plt.show()

# Research on kurtosis and skewness
def analyze_kurtosis_skewness(data: pd.DataFrame) -> None:
    """Calculate and print the kurtosis and skewness of the Sale Price variable."""
    kurtosis = data['SalePrice'].kurtosis()
    skewness = data['SalePrice'].skew()
    print(f'Kurtosis: {kurtosis}, Skewness: {skewness}')

# Check correlation coefficients between features
def check_correlation(data: pd.DataFrame) -> None:
    """Calculate and print the correlation coefficients with respect to Sale Price."""
    correlation_matrix = data.corr()
    print(correlation_matrix['SalePrice'].sort_values(ascending=False))

# Create a heatmap to visualize the relationships
def plot_correlation_heatmap(data: pd.DataFrame) -> None:
    """Visualize the correlation matrix as a heatmap."""
    correlation_matrix = data.corr()
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.show()

# Main execution
if __name__ == "__main__":
    url = "http://jse.amstat.org/v19n3/decock/AmesHousing.txt"
    filename = 'AmesHousing.txt'
    data = load_data(url, filename)
    examine_data(data)
    check_missing_values(data)
    plot_sale_price_distribution(data)
    analyze_kurtosis_skewness(data)
    check_correlation(data)
    plot_correlation_heatmap(data)
