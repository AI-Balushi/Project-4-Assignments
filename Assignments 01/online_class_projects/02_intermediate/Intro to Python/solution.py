MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14

def calculate_weight(weight, planet):
    gravity_factors = {
        "Mercury": MERCURY_GRAVITY,
        "Venus": VENUS_GRAVITY,
        "Mars": MARS_GRAVITY,
        "Jupiter": JUPITER_GRAVITY,
        "Saturn": SATURN_GRAVITY,
        "Uranus": URANUS_GRAVITY,
        "Neptune": NEPTUNE_GRAVITY
    }
    
    return round(weight * gravity_factors.get(planet, 0), 2)

def main():
    earth_weight = float(input("Enter a weight on Earth: "))
    planet_name = input("Enter a planet: ")
    
    equivalent_weight = calculate_weight(earth_weight, planet_name)
    
    if equivalent_weight:
        print(f"The equivalent weight on {planet_name}: {equivalent_weight}")
    else:
        print("Invalid planet name.")

if __name__ == "__main__":
    main()
