import random

# An example of the Monty Hall problem showing that switching doors is better than sticking with your original choice.

def monty_hall(switch = True) -> bool:
    # Pick a random door to hide the prize behind.
    doors = [False, False, False]
    doors[random.randint(0, 2)] = True
    # Pick a random door to choose.
    choice = random.randint(0, 2)
    # Reveal a door that is not the prize and not the choice.
    reveal = -1
    for i in range(3):
        if not doors[i] and i != choice:
            reveal = i
            break
    # Switch to the other door.
    if switch:
        for i in range(3):
            if i != choice and i != reveal:
                choice = i
                break
    # Return whether the choice was correct.
    return doors[choice]

def main():
    # Run the simulation 10000 times.
    wins = 0
    for _ in range(10000):
        wins += monty_hall()
    print(f"Win rate when switching: {100 * wins / 10000:.2f}%")
    wins = 0
    for _ in range(10000):
        wins += monty_hall(False)
    print(f"Win rate when not switching: {100 * wins / 10000:.2f}%")

if __name__ == "__main__":
    main()