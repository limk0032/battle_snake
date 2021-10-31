import random
from typing import Dict, List

import mover_max_free_space
import numpy as np
import tree_node

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
            sub_tree_node = tree_node.TreeNode()
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


def get_shortest_paths_to_target(
    body, other_snakes, board_height, board_width, target, foods
):
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
    shortest_paths_tree_root_node = tree_node.TreeNode()
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
        shortest_paths_valid = []
        #
        for shortest_path in shortest_paths:
            number_of_food_picked_up_along_path = 0
            for food in foods:
                if food in shortest_path:
                    number_of_food_picked_up_along_path =number_of_food_picked_up_along_path+1
            body_after_moving_to_parent = body[: -len(shortest_path) + number_of_food_picked_up_along_path + 1 +1]
            # 1 for head, 1 for tail
            if shortest_path[-1] not in body_after_moving_to_parent:
                shortest_paths_valid.append(shortest_path)
        return (min_step_to_reach_matrix, shortest_paths_valid)
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
    mmfs = MoverMaxFreeSpace()
    foods_sorted_by_distance = mmfs.get_foods_sorted_by_distance_asc(
        head, foods
    )
    for food in foods:
        (
            min_step_to_reach_matrix_head_to_food,
            shortest_paths_head_to_food,
        ) = get_shortest_paths_to_target(
            body, other_snakes, board_height, board_width, food, foods
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
                foods,
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
        print("no first_shortest_path_to_food")
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
            data["board"]["food"],
        )
        print_min_step_to_reach_matrix(min_step_to_reach_matrix)
        print(f"path_to_tail:{paths_to_tail}")
        if len(paths_to_tail)==0:
            return None
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


def choose_move(data: dict) -> str:
    print(f'\n\nturn:{data["turn"]}\n, data:{data}')
    # return get_move_with_max_free_space(data)
    direction = get_move_in_shortest_path_to_food(data)
    if direction == None:
        mmfs = MoverMaxFreeSpace()
        direction = mmfs.get_move_with_max_free_space(data)
    print(f'turn:{data["turn"]}, direction:{direction}')
    print("=======================\n\n")
    return direction