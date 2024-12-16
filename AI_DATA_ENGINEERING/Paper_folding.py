def calculate_thickness(folds):
    thickness = 0.00008  # initial thickness in mm
    for _ in range(folds):  # Looping through the number of folds
        thickness *= 43  # Each fold increases the thickness by a factor of 43
    return thickness  # Returning the final thickness after all folds

def compare_methods(folds):
    start_time = time.time()  # Starting the timer for method 1
    thickness1 = calculate_thickness(folds)  # Calculating thickness using method 1
    method1_time = time.time() - start_time  # Calculating the time taken for method 1

    start_time = time.time()  # Starting the timer for method 2
    thickness2 = 0.00008 * (43 ** folds)  # Calculating thickness using method 2
    method2_time = time.time() - start_time  # Calculating the time taken for method 2

    return thickness1, method1_time, thickness2, method2_time  # Returning thickness and time for both methods

def visualize_thickness(folds):
    thicknesses = [calculate_thickness(i) for i in range(folds + 1)]  # Generating thicknesses for each fold
    plt.plot(range(folds + 1), thicknesses, marker='o')  # Plotting the thicknesses
    plt.title('Thickness of Paper vs. Number of Folds')  # Setting the title of the plot
    plt.xlabel('Number of Folds')  # Labeling the x-axis
    plt.ylabel('Thickness (m)')  # Labeling the y-axis
    plt.grid()  # Adding a grid to the plot for better readability
    plt.show()  # Displaying the plot

def convert_meters_to_kilometers(meters):
    return meters / 10000  # Converting meters to kilometers

if __name__ == "__main__":  # Ensuring the following code runs only if this script is executed directly
    folds = 10  # Setting the number of folds to 10
    thickness1, method1_time, thickness2, method2_time = compare_methods(folds)  # Comparing methods and storing results
    print(f"Method 1 Thickness: {thickness1} m, Time: {method1_time} seconds")  # Printing results for method 1
    print(f"Method 2 Thickness: {thickness2} m, Time: {method2_time} seconds")  # Printing results for method 2
    
    # Convert thickness to kilometers
    thickness1_km = convert_meters_to_kilometers(thickness1)  # Converting method 1 thickness to kilometers
    thickness2_km = convert_meters_to_kilometers(thickness2)  # Converting method 2 thickness to kilometers
    print(f"Method 1 Thickness in km: {thickness1_km} km")  # Printing method 1 thickness in kilometers
    print(f"Method 2 Thickness in km: {thickness2_km} km")  # Printing method 2 thickness in kilometers
    
    visualize_thickness(folds)  # Visualizing the thickness for the given number of folds
