import math
from typing import Dict, List


class MoverMaxFreeSpace(object):
    def __init__(self):
        pass
        
    def avoid_my_neck(
        self, my_head: Dict[str, int], my_body: List[dict], possible_moves: List[str]
    ) -> List[str]:
        if {
            "x": my_head["x"],
            "y": my_head["y"] + 1,
        } in my_body and "up" in possible_moves:
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
        self,
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

    def get_foods_sorted_by_distance_asc(
        self, my_head: Dict[str, int], foods: List[dict]
    ):
        length_food_list = []
        for food in foods:
            distance = math.sqrt(
                (food["x"] - my_head["x"]) ** 2 + (food["y"] - my_head["y"]) ** 2
            )
            length_food_list.append({"distance": distance, "food": food})
        length_food_list_sorted = sorted(length_food_list, key=lambda x: x["distance"])
        food_list_sorted = list(map(lambda x: x["food"], length_food_list_sorted))
        return food_list_sorted

    def get_preferred_directions_to_food(
        self, my_head: Dict[str, int], food: Dict[str, int], possible_moves: List[str]
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

    def combine_preferred_directions_with_possible_moves(
        self, preferred_directions: List[str], possible_moves: List[str]
    ):
        result = []
        for preferred_direction in preferred_directions:
            if preferred_direction in possible_moves:
                result.append(preferred_direction)
        return result

    def possible_move_to_index(self, possible_move: str, my_head: Dict[str, int]):
        if possible_move == "up":
            return {"x": my_head["x"], "y": my_head["y"] + 1}
        if possible_move == "down":
            return {"x": my_head["x"], "y": my_head["y"] - 1}
        if possible_move == "right":
            return {"x": my_head["x"] + 1, "y": my_head["y"]}
        if possible_move == "left":
            return {"x": my_head["x"] - 1, "y": my_head["y"]}

    def re_prioritize_preferred_directions_based_on_free_connected_tile(
        self,
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

    def get_number_of_connected_tile(
        self,
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
        self,
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

    def get_move_with_max_free_space(self, data):
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
            nearest_food = get_foods_sorted_by_distance_asc(
                my_head, data["board"]["food"]
            )[0]
            print(f"nearest_food:{nearest_food}")
            possible_moves_prioritized = get_preferred_directions_to_food(
                my_head, nearest_food, possible_moves
            )
            print(
                f"possible_moves_prioritized based on food:{possible_moves_prioritized}"
            )
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