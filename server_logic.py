import math
import random
from typing import Dict, List

import numpy as np
import tree_node

def avoid_my_neck(
    my_head: Dict[str, int], my_body: List[dict], possible_moves: List[str]
) -> List[str]:
    if {"x": my_head["x"], "y": my_head["y"] + 1} in my_body and "up" in possible_moves:
        possible_moves.remove("up")
    if {
        "x": my_head["x"],
        "y": my_head["y"] - 1,
    } in my_body and "down" in possible_moves:
        possible_moves.remove("down")
    if {
        "x": my_head["x"] + 1,
        "y": my_head["y"],
    } in my_body and "right" in possible_moves:
        possible_moves.remove("right")
    if {
        "x": my_head["x"] - 1,
        "y": my_head["y"],
    } in my_body and "left" in possible_moves:
        possible_moves.remove("left")
    return possible_moves


def avoid_border(
    my_head: Dict[str, int],
    my_body: List[dict],
    possible_moves: List[str],
    board_height: int,
    board_width: int,
) -> List[str]:
    if board_height - 1 == my_head["y"] and "up" in possible_moves:
        possible_moves.remove("up")
    if 0 == my_head["y"] and "down" in possible_moves:
        possible_moves.remove("down")
    if board_width - 1 == my_head["x"] and "right" in possible_moves:
        possible_moves.remove("right")
    if 0 == my_head["x"] and "left" in possible_moves:
        possible_moves.remove("left")
    return possible_moves


def get_foods_sorted_by_distance_asc(my_head: Dict[str, int], foods: List[dict]):
    length_food_list = []
    for food in foods:
        distance = math.sqrt(
            (food["x"] - my_head["x"]) ** 2 + (food["y"] - my_head["y"]) ** 2
        )
        length_food_list.append({"distance": distance, "food": food})
    length_food_list_sorted = sorted(length_food_list, key=lambda x: x["distance"])
    food_list_sorted = list(map(lambda x: x["food"], length_food_list_sorted))
    return food_list_sorted


def combine_preferred_directions_with_possible_moves(
    preferred_directions: List[str], possible_moves: List[str]
):
    result = []
    for preferred_direction in preferred_directions:
        if preferred_direction in possible_moves:
            result.append(preferred_direction)
    return result


def get_preferred_directions_to_food(
    my_head: Dict[str, int], food: Dict[str, int], possible_moves: List[str]
):
    preferred_direction = []
    if food["x"] == my_head["x"] and food["y"] < my_head["y"]:
        preferred_direction = combine_preferred_directions_with_possible_moves(
            ["down", "left", "right", "up"], possible_moves
        )
    elif food["x"] == my_head["x"] and food["y"] > my_head["y"]:
        preferred_direction = combine_preferred_directions_with_possible_moves(
            ["up", "left", "right", "down"], possible_moves
        )
    elif food["x"] < my_head["x"] and food["y"] == my_head["y"]:
        preferred_direction = combine_preferred_directions_with_possible_moves(
            ["left", "up", "down", "right"], possible_moves
        )
    elif food["x"] > my_head["x"] and food["y"] == my_head["y"]:
        preferred_direction = combine_preferred_directions_with_possible_moves(
            ["right", "up", "down", "left"], possible_moves
        )
    elif food["x"] < my_head["x"] and food["y"] < my_head["y"]:
        preferred_direction = combine_preferred_directions_with_possible_moves(
            ["down", "left", "up", "right"], possible_moves
        )
    elif food["x"] < my_head["x"] and food["y"] > my_head["y"]:
        preferred_direction = combine_preferred_directions_with_possible_moves(
            ["up", "left", "down", "right"], possible_moves
        )
    elif food["x"] > my_head["x"] and food["y"] < my_head["y"]:
        preferred_direction = combine_preferred_directions_with_possible_moves(
            ["down", "right", "up", "left"], possible_moves
        )
    elif food["x"] > my_head["x"] and food["y"] > my_head["y"]:
        preferred_direction = combine_preferred_directions_with_possible_moves(
            ["up", "right", "down", "left"], possible_moves
        )
    return preferred_direction


def get_number_of_connected_tile(
    start: Dict[str, int],
    my_body: List[dict],
    other_snakes: List[List[dict]],
    board_height: int,
    board_width: int,
):
    processed_tiles = []
    not_accessible_tiles = my_body[:-1]
    for other_snake in other_snakes:
        not_accessible_tiles = not_accessible_tiles + other_snake["body"]
    number_of_connected_tile = get_number_of_connected_tile_recursively(
        start, not_accessible_tiles, board_height, board_width, processed_tiles
    )
    return number_of_connected_tile


def get_number_of_connected_tile_recursively(
    start: Dict[str, int],
    not_accessible_tiles: List[dict],
    board_height: int,
    board_width: int,
    processed_tiles: List[dict],
):
    if start in processed_tiles:
        return 0
    if start in not_accessible_tiles:
        return 0
    if start["x"] < 0 or start["x"] == board_width:
        return 0
    if start["y"] < 0 or start["y"] == board_height:
        return 0
    processed_tiles.append(start)
    result = 1
    result = result + get_number_of_connected_tile_recursively(
        {"x": start["x"] + 1, "y": start["y"]},
        not_accessible_tiles,
        board_height,
        board_width,
        processed_tiles,
    )
    result = result + get_number_of_connected_tile_recursively(
        {"x": start["x"], "y": start["y"] + 1},
        not_accessible_tiles,
        board_height,
        board_width,
        processed_tiles,
    )
    result = result + get_number_of_connected_tile_recursively(
        {"x": start["x"] - 1, "y": start["y"]},
        not_accessible_tiles,
        board_height,
        board_width,
        processed_tiles,
    )
    result = result + get_number_of_connected_tile_recursively(
        {"x": start["x"], "y": start["y"] - 1},
        not_accessible_tiles,
        board_height,
        board_width,
        processed_tiles,
    )
    return result


def possible_move_to_index(possible_move: str, my_head: Dict[str, int]):
    if possible_move == "up":
        return {"x": my_head["x"], "y": my_head["y"] + 1}
    if possible_move == "down":
        return {"x": my_head["x"], "y": my_head["y"] - 1}
    if possible_move == "right":
        return {"x": my_head["x"] + 1, "y": my_head["y"]}
    if possible_move == "left":
        return {"x": my_head["x"] - 1, "y": my_head["y"]}


def re_prioritize_preferred_directions_based_on_free_connected_tile(
    my_head: Dict[str, int],
    my_body: List[dict],
    other_snakes: List[dict],
    board_height: int,
    board_width: int,
    possible_moves_prioritized: List[str],
):
    result_list = []
    for move in possible_moves_prioritized:
        possible_move_index = possible_move_to_index(move, my_head)
        number_of_connected_tile = get_number_of_connected_tile(
            possible_move_index, my_body, other_snakes, board_height, board_width
        )
        result_list.append(
            {"move": move, "number_of_connected_tile": number_of_connected_tile}
        )
    result_list = sorted(
        result_list, key=lambda x: x["number_of_connected_tile"], reverse=True
    )
    result_list = list(map(lambda x: x["move"], result_list))
    return result_list


def get_surrounding_tiles(tile: Dict[str, int], board_height: int, board_width: int):
    result = []
    if tile["x"] + 1 < board_width:
        result.append({"x": tile["x"] + 1, "y": tile["y"]})
    if tile["y"] + 1 < board_height:
        result.append({"x": tile["x"], "y": tile["y"] + 1})
    if tile["x"] - 1 > -1:
        result.append({"x": tile["x"] - 1, "y": tile["y"]})
    if tile["y"] - 1 > -1:
        result.append({"x": tile["x"], "y": tile["y"] - 1})
    return result


def populate_min_step_to_reach_matrix(
    min_step_to_reach_matrix: List[List[int]],
    body: List[dict],
    other_snakes_body: List[dict],
    board_height: int,
    board_width: int,
):
    matrix_before_change = None
    matrix_after_change = False
    while matrix_before_change != matrix_after_change:
        # print_min_step_to_reach_matrix(min_step_to_reach_matrix)
        # print('========')
        matrix_before_change = str(min_step_to_reach_matrix)
        for x in range(board_width):
            for y in range(board_height):
                tile = {"x": x, "y": y}
                surrounding_tiles = get_surrounding_tiles(
                    tile, board_height, board_width
                )
                surrounding_tiles = list(
                    filter(
                        lambda n: min_step_to_reach_matrix[n["x"]][n["y"]] != "-",
                        surrounding_tiles,
                    )
                )
                if len(surrounding_tiles) == 0:
                    continue
                surrounding_min_steps = list(
                    map(
                        lambda t: min_step_to_reach_matrix[t["x"]][t["y"]],
                        surrounding_tiles,
                    )
                )
                surrounding_min_steps = list(
                    dict.fromkeys(surrounding_min_steps)
                )  # unique min steps
                surrounding_min_steps = sorted(surrounding_min_steps, key=lambda n: n)
                for surrounding_min_step in surrounding_min_steps:
                    surrounding_tiles_with_min_steps = list(
                        filter(
                            lambda n: min_step_to_reach_matrix[n["x"]][n["y"]]
                            == surrounding_min_step,
                            surrounding_tiles,
                        )
                    )
                    if len(surrounding_tiles_with_min_steps) == 0:
                        continue
                    if surrounding_min_step == 0:
                        not_accessible_tiles = other_snakes_body + body
                    else:
                        not_accessible_tiles = (
                            other_snakes_body + body[:-(surrounding_min_step)]
                        )
                    if tile in not_accessible_tiles:
                        continue
                    origina_value = min_step_to_reach_matrix[x][y]
                    if origina_value == "-":
                        min_step_to_reach_matrix[x][y] = surrounding_min_step + 1
                    else:
                        min_step_to_reach_matrix[x][y] = min(
                            surrounding_min_step + 1, min_step_to_reach_matrix[x][y]
                        )
        matrix_after_change = str(min_step_to_reach_matrix)
    # print_min_step_to_reach_matrix(min_step_to_reach_matrix)
    # print('-------------------')


def print_min_step_to_reach_matrix(min_step_to_reach_matrix: List[List[int]]):
    min_step_to_reach_matrix = np.transpose(min_step_to_reach_matrix)
    height = len(min_step_to_reach_matrix)
    for i in range(height):
        print(min_step_to_reach_matrix[height - i - 1])
    print("==========================\n")


def get_step_to_reach_matrix_str(min_step_to_reach_matrix: List[List[int]]):
    min_step_to_reach_matrix = np.transpose(min_step_to_reach_matrix)
    height = len(min_step_to_reach_matrix)
    result = ""
    for i in range(height):
        result = result + str(min_step_to_reach_matrix[height - i - 1]) + "\n"
    return result


def populate_shortest_paths_tree(
    min_step_to_reach_matrix: List[List[int]],
    start,
    end,
    board_height,
    board_width,
    parent_tree_node,
):
    if start == end:
        return
    # debug
    surrounding_tiles = get_surrounding_tiles(start, board_height, board_width)
    surrounding_tiles = list(
        filter(
            lambda t: min_step_to_reach_matrix[t["x"]][t["y"]] != "-", surrounding_tiles
        )
    )
    if len(surrounding_tiles) == 0:
        return
    if min_step_to_reach_matrix[start["x"]][start["y"]] == "-":
        return
    # TODO: can change here to to support second, third and etc shortest paths
    # surrounding_tiles = sorted(surrounding_tiles, key=lambda c:len(n))
    # surrounding_tiles_min_steps = min(list(map(lambda t: min_step_to_reach_matrix[t['x']][t['y']], surrounding_tiles)))
    surrounding_tiles_with_min_steps = list(
        (
            filter(
                lambda t: min_step_to_reach_matrix[t["x"]][t["y"]]
                == min_step_to_reach_matrix[start["x"]][start["y"]] - 1,
                surrounding_tiles,
            )
        )
    )
    if len(surrounding_tiles_with_min_steps) > 0:
        for sub_tile in surrounding_tiles_with_min_steps:
            sub_tree_node = TreeNode()
            sub_tree_node.parent = parent_tree_node
            sub_tree_node.data = sub_tile
            parent_tree_node.children.append(sub_tree_node)
            populate_shortest_paths_tree(
                min_step_to_reach_matrix,
                sub_tile,
                end,
                board_height,
                board_width,
                sub_tree_node,
            )


def get_shortest_paths_to_target(body, other_snakes, board_height, board_width, target):
    other_snakes_body = []
    for other_snake in other_snakes:
        other_snakes_body = other_snakes_body + other_snake["body"]
    min_step_to_reach_matrix = [
        ["-" for x in range(board_width)] for y in range(board_height)
    ]
    min_step_to_reach_matrix[body[0]["x"]][body[0]["y"]] = 0
    populate_min_step_to_reach_matrix(
        min_step_to_reach_matrix, body, other_snakes_body, board_height, board_width
    )
    # print_min_step_to_reach_matrix(min_step_to_reach_matrix)
    #
    # now only care about all shortest paths only
    # TODO: consider longer paths next time
    shortest_paths_tree_root_node = TreeNode()
    shortest_paths_tree_root_node.data = target
    populate_shortest_paths_tree(
        min_step_to_reach_matrix,
        target,
        {"x": body[0]["x"], "y": body[0]["y"]},
        board_height,
        board_width,
        shortest_paths_tree_root_node,
    )
    if len(shortest_paths_tree_root_node.children) != 0:
        shortest_paths = shortest_paths_tree_root_node.tree2list()
        [item.reverse() for item in shortest_paths]
        return (min_step_to_reach_matrix, shortest_paths)
    else:
        print("valid path not found")
        return (min_step_to_reach_matrix, [])


def get_first_shortest_path_to_food(data: dict):
    board_height = data["board"]["height"]
    board_width = data["board"]["width"]
    foods = data["board"]["food"]
    head = data["you"]["head"]
    body = data["you"]["body"]
    other_snakes = data["board"]["snakes"]
    other_snakes = list(filter(lambda s: s["body"] != body, other_snakes))
    foods_sorted_by_distance = get_foods_sorted_by_distance_asc(head, foods)
    for food in foods:
        (
            min_step_to_reach_matrix_head_to_food,
            shortest_paths_head_to_food,
        ) = get_shortest_paths_to_target(
            body, other_snakes, board_height, board_width, food
        )
        # print(f'shortest_paths_head_to_food:\nhead:{body[0]},\nfood:{foods[0]},\nmin_step_to_reach_matrix_head_to_food:\n{get_step_to_reach_matrix_str(min_step_to_reach_matrix_head_to_food)}shortest_paths_head_to_food:\n' + '\n'.join(' '.join(map(str, sl)) for sl in shortest_paths_head_to_food) + '\n---------')
        for path in shortest_paths_head_to_food:
            path.reverse()  # path body is reversed of path
            original_tail_to_food = path[:-1] + body
            #
            body_after_eating_food = original_tail_to_food[: (len(body) + 1)]
            # not using 'original_tail_to_food[-(len(body) + 0):]' this is to handle 1 unit of body length increase after eating food
            tail_after_eating_food = body_after_eating_food[-1]
            (
                min_step_to_reach_matrix_food_to_tail,
                shortest_paths_food_to_tail,
            ) = get_shortest_paths_to_target(
                body_after_eating_food,
                other_snakes,
                board_height,
                board_width,
                tail_after_eating_food,
            )
            # return first shortest path to food, if there is valid path for food_to_tail after eaten food
            path.reverse()
            if len(shortest_paths_food_to_tail) > 0:
                # able to survive after eating food
                # pick this path
                # print(f'valid shortest path found\n{path}')
                return path
            else:
                # print(f'invalid shortest path food to tail:\n{path}')
                # print(f'food:{food},\ntail:{tail_after_eating_food},\nbody:{body_after_eating_food}')
                # print_min_step_to_reach_matrix(min_step_to_reach_matrix_food_to_tail)
                pass
    return []


def get_move_in_shortest_path_to_food(data):
    first_shortest_path_to_food = get_first_shortest_path_to_food(data)
    if len(first_shortest_path_to_food) != 0:
        print(f"first_shortest_path_to_food:{first_shortest_path_to_food}")
        path = first_shortest_path_to_food
    else:
        print("chase tail")
        snakes_without_my_body = list(
            filter(lambda s: s["body"] != data["you"]["body"], data["board"]["snakes"])
        )
        my_body_without_tail = data["you"]["body"]
        min_step_to_reach_matrix, paths_to_tail = get_shortest_paths_to_target(
            my_body_without_tail,
            snakes_without_my_body,
            data["board"]["height"],
            data["board"]["width"],
            data["you"]["body"][-1],
        )
        print_min_step_to_reach_matrix(min_step_to_reach_matrix)
        print(f"path_to_tail:{paths_to_tail}")
        path = paths_to_tail[0]  # first shortest path to tail
    # print(f'path:{path}')
    step0 = path[0]
    step1 = path[1]
    if step1["x"] > step0["x"]:
        return "right"
    elif step1["x"] < step0["x"]:
        return "left"
    elif step1["y"] > step0["y"]:
        return "up"
    else:  # step1['y'] > step0['y']
        return "down"


def get_move_with_max_free_space(data):
    my_head = data["you"]["head"]
    my_body = data["you"]["body"]
    possible_moves = ["up", "down", "left", "right"]
    possible_moves = avoid_my_neck(my_head, my_body, possible_moves)
    possible_moves = avoid_border(
        my_head,
        my_body,
        possible_moves,
        data["board"]["height"],
        data["board"]["width"],
    )
    if data["board"]["snakes"]:
        for snake in data["board"]["snakes"]:
            possible_moves = avoid_my_neck(my_head, snake["body"], possible_moves)
    # print(f'possible_moves:{possible_moves}')
    if data["board"]["food"]:
        nearest_food = get_foods_sorted_by_distance_asc(my_head, data["board"]["food"])[
            0
        ]
        print(f"nearest_food:{nearest_food}")
        possible_moves_prioritized = get_preferred_directions_to_food(
            my_head, nearest_food, possible_moves
        )
        print(f"possible_moves_prioritized based on food:{possible_moves_prioritized}")
        possible_moves_prioritized = (
            re_prioritize_preferred_directions_based_on_free_connected_tile(
                my_head,
                my_body,
                data["board"]["snakes"],
                data["board"]["height"],
                data["board"]["width"],
                possible_moves_prioritized,
            )
        )
        print(
            f"possible_moves_prioritized based on free connected tile:{possible_moves_prioritized}"
        )
    # print(f'possible_moves_prioritized:{possible_moves_prioritized}')
    # debug start
    # get_first_shortest_path_to_food(data)
    # debug end
    move = possible_moves_prioritized[0]
    # print(f'possible_moves_prioritized:{possible_moves_prioritized}')
    print(
        f"=======> {data['game']['id']} MOVE {data['turn']}: {move} picked from all valid options in {possible_moves_prioritized}"
    )
    return move


def choose_move(data: dict) -> str:
    print(f'\n\nturn:{data["turn"]}\n, data:{data}')
    # return get_move_with_max_free_space(data)
    direction = get_move_in_shortest_path_to_food(data)
    print(f'turn:{data["turn"]}, direction:{direction}')
    print("=======================\n\n")
    return direction


data = {
    "game": {
        "id": "63d80eb8-22f4-4ea3-9b6a-29c9b7cc61b3",
        "ruleset": {
            "name": "solo",
            "version": "v1.0.22",
            "settings": {
                "foodSpawnChance": 15,
                "minimumFood": 1,
                "hazardDamagePerTurn": 0,
                "royale": {"shrinkEveryNTurns": 0},
                "squad": {
                    "allowBodyCollisions": False,
                    "sharedElimination": False,
                    "sharedHealth": False,
                    "sharedLength": False,
                },
            },
        },
        "timeout": 500,
        "source": "",
    },
    "turn": 169,
    "board": {
        "height": 7,
        "width": 7,
        "snakes": [
            {
                "id": "gs_R3FTmRbx6HQMvMBfr3KWJ6w7",
                "name": "snake1",
                "latency": "301",
                "health": 100,
                "body": [
                    {"x": 0, "y": 5},
                    {"x": 0, "y": 4},
                    {"x": 0, "y": 3},
                    {"x": 0, "y": 2},
                    {"x": 1, "y": 2},
                    {"x": 1, "y": 1},
                    {"x": 1, "y": 0},
                    {"x": 2, "y": 0},
                    {"x": 2, "y": 1},
                    {"x": 2, "y": 2},
                    {"x": 3, "y": 2},
                    {"x": 3, "y": 1},
                    {"x": 4, "y": 1},
                    {"x": 5, "y": 1},
                    {"x": 6, "y": 1},
                    {"x": 6, "y": 2},
                    {"x": 6, "y": 3},
                    {"x": 5, "y": 3},
                    {"x": 5, "y": 2},
                    {"x": 4, "y": 2},
                    {"x": 4, "y": 3},
                    {"x": 4, "y": 4},
                    {"x": 3, "y": 4},
                    {"x": 3, "y": 5},
                    {"x": 4, "y": 5},
                    {"x": 5, "y": 5},
                    {"x": 5, "y": 4},
                    {"x": 6, "y": 4},
                    {"x": 6, "y": 5},
                    {"x": 6, "y": 6},
                    {"x": 5, "y": 6},
                    {"x": 4, "y": 6},
                    {"x": 3, "y": 6},
                    {"x": 2, "y": 6},
                    {"x": 1, "y": 6},
                    {"x": 1, "y": 6},
                ],
                "head": {"x": 0, "y": 5},
                "length": 36,
                "shout": "",
                "squad": "",
            }
        ],
        "food": [{"x": 3, "y": 3}, {"x": 6, "y": 0}],
        "hazards": [],
    },
    "you": {
        "id": "gs_R3FTmRbx6HQMvMBfr3KWJ6w7",
        "name": "snake1",
        "latency": "301",
        "health": 100,
        "body": [
            {"x": 0, "y": 5},
            {"x": 0, "y": 4},
            {"x": 0, "y": 3},
            {"x": 0, "y": 2},
            {"x": 1, "y": 2},
            {"x": 1, "y": 1},
            {"x": 1, "y": 0},
            {"x": 2, "y": 0},
            {"x": 2, "y": 1},
            {"x": 2, "y": 2},
            {"x": 3, "y": 2},
            {"x": 3, "y": 1},
            {"x": 4, "y": 1},
            {"x": 5, "y": 1},
            {"x": 6, "y": 1},
            {"x": 6, "y": 2},
            {"x": 6, "y": 3},
            {"x": 5, "y": 3},
            {"x": 5, "y": 2},
            {"x": 4, "y": 2},
            {"x": 4, "y": 3},
            {"x": 4, "y": 4},
            {"x": 3, "y": 4},
            {"x": 3, "y": 5},
            {"x": 4, "y": 5},
            {"x": 5, "y": 5},
            {"x": 5, "y": 4},
            {"x": 6, "y": 4},
            {"x": 6, "y": 5},
            {"x": 6, "y": 6},
            {"x": 5, "y": 6},
            {"x": 4, "y": 6},
            {"x": 3, "y": 6},
            {"x": 2, "y": 6},
            {"x": 1, "y": 6},
            {"x": 1, "y": 6},
        ],
        "head": {"x": 0, "y": 5},
        "length": 36,
        "shout": "",
        "squad": "",
    },
}

data = {
    "game": {
        "id": "c9cce9c3-c0ca-4291-97f9-2f76e637b1fd",
        "ruleset": {
            "name": "solo",
            "version": "v1.0.22",
            "settings": {
                "foodSpawnChance": 15,
                "minimumFood": 1,
                "hazardDamagePerTurn": 0,
                "royale": {"shrinkEveryNTurns": 0},
                "squad": {
                    "allowBodyCollisions": False,
                    "sharedElimination": False,
                    "sharedHealth": False,
                    "sharedLength": False,
                },
            },
        },
        "timeout": 500,
        "source": "challenge",
    },
    "turn": 148,
    "board": {
        "height": 7,
        "width": 7,
        "snakes": [
            {
                "id": "gs_VrJvPpFFHfKcGg7wyXvGgqgQ",
                "name": "snake1",
                "latency": "234",
                "health": 92,
                "body": [
                    {"x": 5, "y": 3},
                    {"x": 4, "y": 3},
                    {"x": 4, "y": 2},
                    {"x": 4, "y": 1},
                    {"x": 4, "y": 0},
                    {"x": 3, "y": 0},
                    {"x": 3, "y": 1},
                    {"x": 3, "y": 2},
                    {"x": 3, "y": 3},
                    {"x": 2, "y": 3},
                    {"x": 1, "y": 3},
                    {"x": 1, "y": 2},
                    {"x": 0, "y": 2},
                    {"x": 0, "y": 3},
                    {"x": 0, "y": 4},
                    {"x": 1, "y": 4},
                    {"x": 2, "y": 4},
                    {"x": 3, "y": 4},
                    {"x": 4, "y": 4},
                    {"x": 5, "y": 4},
                    {"x": 5, "y": 5},
                    {"x": 5, "y": 6},
                    {"x": 6, "y": 6},
                    {"x": 6, "y": 5},
                    {"x": 6, "y": 4},
                ],
                "head": {"x": 5, "y": 3},
                "length": 25,
                "shout": "",
                "squad": "",
            }
        ],
        "food": [
            {"x": 3, "y": 6},
            {"x": 0, "y": 1},
            {"x": 5, "y": 0},
            {"x": 4, "y": 5},
            {"x": 2, "y": 6},
            {"x": 0, "y": 0},
        ],
        "hazards": [],
    },
    "you": {
        "id": "gs_VrJvPpFFHfKcGg7wyXvGgqgQ",
        "name": "snake1",
        "latency": "234",
        "health": 92,
        "body": [
            {"x": 5, "y": 3},
            {"x": 4, "y": 3},
            {"x": 4, "y": 2},
            {"x": 4, "y": 1},
            {"x": 4, "y": 0},
            {"x": 3, "y": 0},
            {"x": 3, "y": 1},
            {"x": 3, "y": 2},
            {"x": 3, "y": 3},
            {"x": 2, "y": 3},
            {"x": 1, "y": 3},
            {"x": 1, "y": 2},
            {"x": 0, "y": 2},
            {"x": 0, "y": 3},
            {"x": 0, "y": 4},
            {"x": 1, "y": 4},
            {"x": 2, "y": 4},
            {"x": 3, "y": 4},
            {"x": 4, "y": 4},
            {"x": 5, "y": 4},
            {"x": 5, "y": 5},
            {"x": 5, "y": 6},
            {"x": 6, "y": 6},
            {"x": 6, "y": 5},
            {"x": 6, "y": 4},
        ],
        "head": {"x": 5, "y": 3},
        "length": 25,
        "shout": "",
        "squad": "",
    },
}
first_shortest_path_to_food: [
    {"x": 5, "y": 3},
    {"x": 6, "y": 3},
    {"x": 6, "y": 4},
    {"x": 6, "y": 5},
    {"x": 6, "y": 6},
    {"x": 5, "y": 6},
    {"x": 4, "y": 6},
    {"x": 3, "y": 6},
]

choose_move(data)