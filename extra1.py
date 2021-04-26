from typing import List, TypedDict

Map = List[List[str]]
Direction = TypedDict("Direction", {"x": int, "y": int})
Player = TypedDict("Player", {"x": int, "y": int})


def reset_map() -> Map:
    # fmt: off
    return [
        ["*", "*", "*", "*", "*", "*", "*", "*", "*"],
        ["*", " ", " ", " ", " ", " ", " ", " ", "*"],
        ["*", " ", " ", " ", " ", " ", " ", " ", "*"],
        ["*", " ", " ", " ", " ", " ", " ", " ", "*"],
        ["*", "*", " ", "*", "*", " ", " ", " ", "*"],
        ["*", " ", " ", " ", " ", " ", " ", " ", "*"],
        ["*", " ", " ", " ", " ", "*", " ", " ", "*"],
        ["*", " ", " ", " ", " ", "*", " ", " ", "*"],
        ["*", "*", "*", "*", "*", "*", "*", "*", "*"],
    ]
    # fmt: on


def display_map(map: Map, player: Player):
    text = ""
    for y in range(len(map)):
        for x in range(len(map[0])):
            text += "P" if x == player["x"] and y == player["y"] else map[y][x]
        text += "\n"
    text += "------------------------------------"
    print(text)


def get_direction(user_input: str) -> Direction:
    return (
        {"x": 0, "y": -1}
        if user_input == "w"
        else {"x": -1, "y": 0}
        if user_input == "a"
        else {"x": 0, "y": 1}
        if user_input == "s"
        else {"x": 1, "y": 0}
        if user_input == "d"
        else {"x": 0, "y": 0}
    )


def update_player(map: Map, player: Player, direction: Direction) -> Player:
    new_player: Player = {
        "x": player["x"] + direction["x"],
        "y": player["y"] + direction["y"],
    }
    return new_player if map[new_player["y"]][new_player["x"]] == " " else player


def main():
    map = reset_map()
    player = {"x": 3, "y": 6}

    while True:
        display_map(map, player)
        user_input = input("Please input w/a/s/d or 0: ")
        if user_input == "0":
            break

        player = update_player(map, player, get_direction(user_input))
        print("\033[1A\033[2K\033[" + str(len(map) + 2) + "A")


main()
