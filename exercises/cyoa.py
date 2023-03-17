"""EX06 - Choose Your Own Adventure."""

__author__ = "730556365"

points: int = 0
player: str = ""

def main() -> None:
    global points, player
    greet()
    print(player)


def greet() -> None:
    global player
    player = input(f"Welcome to (name of game)! What is your name?: ")



if __name__ == "__main__":
    main()