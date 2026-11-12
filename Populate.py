def directions():
    # Create and return the available directions.
    steps = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return steps


def menu_and_input():
    print("\nPlease select a direction:")

    # Retrieve and display each direction with its index.
    steps = directions()
    for index in range(len(steps)):
        print(f"{index}: {steps[index]}")

    # Convert the user's response to an index and return the direction.
    choice = int(input())
    return steps[choice]


def run_task4():
    # Create an empty list to store the escape route.
    route = []
    print("Working out escape route...")

    # Ask for five directions and add each one to the route.
    for count in range(5):
        direction = menu_and_input()
        route.append(direction)

    print(f"\nEscape route: {route}")


# Start the program.
run_task4()