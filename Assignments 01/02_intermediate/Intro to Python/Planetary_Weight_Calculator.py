def main():

    earth_weight_str = input("Enter a weight on Earth: ")
    earth_weight = float(earth_weight_str)

    planet = input("Enter a planet: ")

    MERCURY_GRAVITY = 0.376
    VENUS_GRAVITY = 0.889
    MARS_GRAVITY = 0.378
    JUPITER_GRAVITY = 2.36
    SATURN_GRAVITY = 1.081
    URANUS_GRAVITY = 0.815
    NEPTUNE_GRAVITY = 1.14

    if planet == "Mercury":
        gravity = MERCURY_GRAVITY
    elif planet == "Venus":
        gravity = VENUS_GRAVITY
    elif planet == "Mars":
        gravity = MARS_GRAVITY
    elif planet == "Jupiter":
        gravity = JUPITER_GRAVITY
    elif planet == "Saturn":
        gravity = SATURN_GRAVITY
    elif planet == "Uranus":
        gravity = URANUS_GRAVITY
    else:
        gravity = NEPTUNE_GRAVITY

    planetary_weight = earth_weight * gravity

    rounded_weight = round(planetary_weight, 2)

    print("The equivalent weight on " + planet + ": " + str(rounded_weight))

if __name__ == "__main__":
    main()
