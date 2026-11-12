def directions():
    # Create and return the list of directions.
    steps = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return steps


def menu():
    print("Please select a direction:")

    # Retrieve the available directions.
    steps = directions()

    # Display each direction with its index number.
    for index in range(len(steps)):
        print(f"{index}: {steps[index]}")


def run_task3():
    # Display the menu.
    menu()


# Start the program.
run_task3()