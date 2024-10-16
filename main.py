from calculations import calculate_tank_size, calculate_materials, calculate_cost
from materials import MATERIALS

def get_user_input():
    # Print welcome message
    print("\nWelcome to the Global Communities Septic Tank Design Project!")
    print("This tool will help you calculate the optimal size, material volume, and cost of your septic tank based on the inputs provided.\n")

    # Gather user inputs for the calculation
    population = int(input("Enter population size: "))
    waste_per_person = float(input("Enter average waste per person per day (liters): "))
    retention_time = float(input("Enter retention time (days): "))
    seasonal_variation = float(input("Enter seasonal water variation (liters, optional, default is 0): ") or 0)

    # List materials for selection
    print("\nAvailable materials:")
    for i, material in enumerate(MATERIALS.keys(), 1):
        print(f"{i}. {material}")
    
    material_choice = int(input("\nSelect the material by number: "))
    material = list(MATERIALS.keys())[material_choice - 1]
    material_cost = float(input(f"Enter the cost per unit for {material} (in Ghanaian Cedis): "))
    
    return population, waste_per_person, retention_time, seasonal_variation, material, material_cost

def main():
    # Get user inputs
    population, waste_per_person, retention_time, seasonal_variation, material, material_cost = get_user_input()

    # Calculate tank size
    tank_size = calculate_tank_size(population, waste_per_person, retention_time, seasonal_variation)

    # Calculate material volume needed
    material_volume = calculate_materials(tank_size, material)

    # Calculate total cost
    total_cost = calculate_cost(material_volume, material_cost)

    # Display the results
    print(f"\nSeptic Tank Size: {tank_size:.2f} cubic meters")
    print(f"Material Volume Needed: {material_volume:.2f} units")
    print(f"Total Cost: {total_cost:.2f} Ghanaian Cedis")

if __name__ == "__main__":
    main()
