from typing import List, TypedDict

Map = List[List[str]]
Direction = TypedDict("Direction", {"x": int, "y": int})
Player = TypedDict("Player", {"x": int, "y": int})
Baggage = TypedDict("Baggage", {"x": int, "y": int})
Shelf = TypedDict("Shelf", {"x": int, "y": int})


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


def display_map(map: Map, player: Player, baggage: Baggage, shelf: Shelf):
    text = ""
    for y in range(len(map)):
        for x in range(len(map[0])):
            text += (
                "P"
                if x == player["x"] and y == player["y"]
                else "B"
                if x == baggage["x"] and y == baggage["y"]
                else "S"
                if x == shelf["x"] and y == shelf["y"]
                else map[y][x]
            )
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


def update_baggage(
    map: Map, baggage: Baggage, player: Player, direction: Direction
) -> Baggage:
    if (
        player["x"] + direction["x"] != baggage["x"]
        or player["y"] + direction["y"] != baggage["y"]
    ):
        return baggage

    new_baggage: Baggage = {
        "x": baggage["x"] + direction["x"],
        "y": baggage["y"] + direction["y"],
    }
    return new_baggage if map[new_baggage["y"]][new_baggage["x"]] == " " else baggage


def update_player(
    map: Map, baggage: Baggage, shelf: Shelf, player: Player, direction: Direction
) -> Player:
    new_player: Player = {
        "x": player["x"] + direction["x"],
        "y": player["y"] + direction["y"],
    }

    return (
        new_player
        if map[new_player["y"]][new_player["x"]] == " "
        and (new_player["x"] != baggage["x"] or new_player["y"] != baggage["y"])
        and (new_player["x"] != shelf["x"] or new_player["y"] != shelf["y"])
        else player
    )


def main():
    map = reset_map()
    player: Player = {"x": 3, "y": 6}
    baggage: Baggage = {"x": 5, "y": 4}
    shelf: Shelf = {"x": 4, "y": 7}

    while True:
        display_map(map, player, baggage, shelf)
        if baggage["x"] == shelf["x"] and baggage["y"] == shelf["y"]:
            print("Congratulations!!")
            break

        user_input = input("Please input w/a/s/d or 0: ")
        if user_input == "0":
            break

        direction = get_direction(user_input)
        baggage = update_baggage(map, baggage, player, direction)
        player = update_player(map, baggage, shelf, player, get_direction(user_input))
        print("\033[1A\033[2K\033[" + str(len(map) + 2) + "A")


main()
