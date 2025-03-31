def calculate_weight(weight, planet):
    gravity_factors = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14
    }
    
    if planet in gravity_factors:
        return round(weight * gravity_factors[planet], 2)
    else:
        return None

if __name__ == "__main__":
    earth_weight = float(input("Enter a weight on Earth: "))
    planet_name = input("Enter a planet: ")
    
    equivalent_weight = calculate_weight(earth_weight, planet_name)
    
    if equivalent_weight is not None:
        print(f"The equivalent weight on {planet_name}: {equivalent_weight}")
    else:
        print("Invalid planet name.")
