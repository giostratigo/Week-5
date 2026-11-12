def movements():
    # Store each direction followed by its number of steps.
    path = ["Move Forward", 10, "Move Backward", 5,
            "Move Left", 3, "Move Right", 1]
    return path


def run_task2():
    print("Moving...")

    # Retrieve the list of movements.
    path = movements()

    # Access each direction and its steps using their indexes.
    for index in range(0, len(path), 2):
        print(f"{path[index]} for {path[index + 1]} steps")


# Start the program.
run_task2()