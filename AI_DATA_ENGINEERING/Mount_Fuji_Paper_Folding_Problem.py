import math

# Constants
mount_fuji_height = 3776  # Height of Mount Fuji in meters
initial_thickness = 0.00008  # Initial thickness of paper in meters

# Function to calculate minimum folds to exceed a given height
def min_folds_to_exceed_height(target_height, thickness=initial_thickness):
    folds = 0  # Initialize the number of folds
    while thickness < target_height:  # Loop until the thickness exceeds the target height
        thickness *= 2  # Double the thickness with each fold
        folds += 1  # Increment the fold count
    return folds  # Return the total number of folds

# Calculate minimum folds to exceed the height of Mount Fuji
mount_fuji_folds = min_folds_to_exceed_height(mount_fuji_height)
print(f"Minimum folds to exceed Mount Fuji height: {mount_fuji_folds}")

# Function to calculate minimum folds to exceed a specified height
def min_folds_to_exceed_custom_height(target_height, thickness):
    folds = 0  # Initialize the number of folds
    while thickness < target_height:  # Loop until the thickness exceeds the target height
        thickness *= 2  # Double the thickness with each fold
        folds += 1  # Increment the fold count
    return folds  # Return the total number of folds

# Example usage for a custom height
custom_height = 2.0  # Example height in meters
custom_folds = min_folds_to_exceed_custom_height(custom_height, initial_thickness)
print(f"Minimum folds to exceed {custom_height} meters: {custom_folds}")

# Function to calculate length of paper needed to reach a specific distance
def length_of_paper_needed(target_distance, thickness=initial_thickness):
    folds = min_folds_to_exceed_height(target_distance, thickness)  # Get the number of folds needed
    return thickness * (2 ** folds)  # Calculate the length of paper needed

# Example usage for distance to the Moon and nearest star
moon_distance = 384400000  # Distance to the Moon in meters
nearest_star_distance = 4.24 * 9.461e15  # Distance to Proxima Centauri in meters

moon_length = length_of_paper_needed(moon_distance)  # Calculate length for the Moon
star_length = length_of_paper_needed(nearest_star_distance)  # Calculate length for the nearest star

print(f"Length of paper needed to reach the Moon: {moon_length} meters")
print(f"Length of paper needed to reach the nearest star: {star_length} meters")

