test_data_1 = {
    "game": {
        "id": "d2f41a62-9064-4e1c-9c1b-8009b7c8a7c7",
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
    "turn": 101,
    "board": {
        "height": 7,
        "width": 7,
        "snakes": [
            {
                "id": "gs_MFdGvJSdjTXtmWm43vDvFTX6",
                "name": "snake2",
                "latency": "196",
                "health": 100,
                "body": [
                    {"x": 4, "y": 3},
                    {"x": 4, "y": 4},
                    {"x": 4, "y": 5},
                    {"x": 3, "y": 5},
                    {"x": 2, "y": 5},
                    {"x": 1, "y": 5},
                    {"x": 1, "y": 4},
                    {"x": 1, "y": 3},
                    {"x": 2, "y": 3},
                    {"x": 2, "y": 2},
                    {"x": 2, "y": 1},
                    {"x": 2, "y": 0},
                    {"x": 3, "y": 0},
                    {"x": 4, "y": 0},
                    {"x": 5, "y": 0},
                    {"x": 5, "y": 1},
                    {"x": 5, "y": 2},
                    {"x": 4, "y": 2},
                    {"x": 4, "y": 1},
                    {"x": 3, "y": 1},
                    {"x": 3, "y": 1},
                ],
                "head": {"x": 4, "y": 3},
                "length": 21,
                "shout": "",
                "squad": "",
            }
        ],
        "food": [{"x": 3, "y": 2}],
        "hazards": [],
    },
    "you": {
        "id": "gs_MFdGvJSdjTXtmWm43vDvFTX6",
        "name": "snake2",
        "latency": "196",
        "health": 100,
        "body": [
            {"x": 4, "y": 3},
            {"x": 4, "y": 4},
            {"x": 4, "y": 5},
            {"x": 3, "y": 5},
            {"x": 2, "y": 5},
            {"x": 1, "y": 5},
            {"x": 1, "y": 4},
            {"x": 1, "y": 3},
            {"x": 2, "y": 3},
            {"x": 2, "y": 2},
            {"x": 2, "y": 1},
            {"x": 2, "y": 0},
            {"x": 3, "y": 0},
            {"x": 4, "y": 0},
            {"x": 5, "y": 0},
            {"x": 5, "y": 1},
            {"x": 5, "y": 2},
            {"x": 4, "y": 2},
            {"x": 4, "y": 1},
            {"x": 3, "y": 1},
            {"x": 3, "y": 1},
        ],
        "head": {"x": 4, "y": 3},
        "length": 21,
        "shout": "",
        "squad": "",
    },
}
# valid path not found
# chase tail
# [9 8 7 6 5 4 5]
# [10 17 18 19 20  3  4]
# [11 16  3  2 21  2  3]
# [12 15 14  1  0  1  2]
# [13 14 13  2  5  6  3]
# [14 13 12  3  4  7  4]
# [13 12 11 10  9  8  5]
# ==========================
#
# path_to_tail:[[{'x': 4, 'y': 3}, {'x': 3, 'y': 3}, {'x': 3, 'y': 2}, {'x': 3, 'y': 1}]]
# turn:101, direction:left
# =======================
#
# issue:
# no valid path to food
# then chase tail, but a food exists on path to tail


test_data_2 = {
    "game": {
        "id": "a84b5676-1bd7-426c-8c11-9dcf09d1b897",
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
    "turn": 114,
    "board": {
        "height": 7,
        "width": 7,
        "snakes": [
            {
                "id": "gs_vjPYCyDrySqx3mcY9MXBBc6K",
                "name": "snake2",
                "latency": "200",
                "health": 100,
                "body": [
                    {"x": 1, "y": 5},
                    {"x": 1, "y": 4},
                    {"x": 1, "y": 3},
                    {"x": 1, "y": 2},
                    {"x": 1, "y": 1},
                    {"x": 2, "y": 1},
                    {"x": 2, "y": 2},
                    {"x": 2, "y": 3},
                    {"x": 3, "y": 3},
                    {"x": 3, "y": 2},
                    {"x": 3, "y": 1},
                    {"x": 3, "y": 0},
                    {"x": 4, "y": 0},
                    {"x": 4, "y": 1},
                    {"x": 4, "y": 2},
                    {"x": 4, "y": 3},
                    {"x": 4, "y": 4},
                    {"x": 4, "y": 5},
                    {"x": 4, "y": 6},
                    {"x": 3, "y": 6},
                    {"x": 2, "y": 6},
                    {"x": 1, "y": 6},
                    {"x": 0, "y": 6},
                    {"x": 0, "y": 6},
                ],
                "head": {"x": 1, "y": 5},
                "length": 24,
                "shout": "",
                "squad": "",
            }
        ],
        "food": [{"x": 6, "y": 5}],
        "hazards": [],
    },
    "you": {
        "id": "gs_vjPYCyDrySqx3mcY9MXBBc6K",
        "name": "snake2",
        "latency": "200",
        "health": 100,
        "body": [
            {"x": 1, "y": 5},
            {"x": 1, "y": 4},
            {"x": 1, "y": 3},
            {"x": 1, "y": 2},
            {"x": 1, "y": 1},
            {"x": 2, "y": 1},
            {"x": 2, "y": 2},
            {"x": 2, "y": 3},
            {"x": 3, "y": 3},
            {"x": 3, "y": 2},
            {"x": 3, "y": 1},
            {"x": 3, "y": 0},
            {"x": 4, "y": 0},
            {"x": 4, "y": 1},
            {"x": 4, "y": 2},
            {"x": 4, "y": 3},
            {"x": 4, "y": 4},
            {"x": 4, "y": 5},
            {"x": 4, "y": 6},
            {"x": 3, "y": 6},
            {"x": 2, "y": 6},
            {"x": 1, "y": 6},
            {"x": 0, "y": 6},
            {"x": 0, "y": 6},
        ],
        "head": {"x": 1, "y": 5},
        "length": 24,
        "shout": "",
        "squad": "",
    },
}

test_data_3 = {'game': {'id': '05b21bf4-133b-4f5d-8cc9-f9166981d6a7', 'ruleset': {'name': 'solo', 'version': 'v1.0.22', 'settings': {'foodSpawnChance': 15, 'minimumFood': 1, 'hazardDamagePerTurn': 0, 'royale': {'shrinkEveryNTurns': 0}, 'squad': {'allowBodyCollisions': False, 'sharedElimination': False, 'sharedHealth': False, 'sharedLength': False}}}, 'timeout': 500, 'source': 'challenge'}, 'turn': 190,
               'board': {'height': 7, 'width': 7, 'snakes': [{'id': 'gs_cXpM8DVrwfQ6BTjCjRPTj7kc', 'name': 'snake1', 'latency': '202', 'health': 95, 'body': [{'x': 2, 'y': 4}, {'x': 1, 'y': 4}, {'x': 0, 'y': 4}, {'x': 0, 'y': 3}, {'x': 1, 'y': 3}, {'x': 2, 'y': 3}, {'x': 2, 'y': 2}, {'x': 2, 'y': 1}, {'x': 3, 'y': 1}, {'x': 4, 'y': 1}, {'x': 5, 'y': 1}, {'x': 5, 'y': 0}, {'x': 6, 'y': 0}, {'x': 6, 'y': 1}, {'x': 6, 'y': 2}, {'x': 5, 'y': 2}, {'x': 4, 'y': 2}, {'x': 3, 'y': 2}, {'x': 3, 'y': 3}, {'x': 4, 'y': 3}, {'x': 5, 'y': 3}, {'x': 6, 'y': 3}, {'x': 6, 'y': 4}, {'x': 6, 'y': 5}, {'x': 6, 'y': 6}, {'x': 5, 'y': 6}, {'x': 4, 'y': 6}, {'x': 3, 'y': 6}, {'x': 2, 'y': 6}, {'x': 1, 'y': 6}, {'x': 0, 'y': 6}, {'x': 0, 'y': 5}, {'x': 1, 'y': 5}], 'head': {'x': 2, 'y': 4}, 'length': 33, 'shout': '', 'squad': ''}], 'food': [{'x': 5, 'y': 5}, {'x': 4, 'y': 4}, {'x': 4, 'y': 0}, {'x': 4, 'y': 5}, {'x': 3, 'y': 5}, {'x': 5, 'y': 4}, {'x': 3, 'y': 4}, {'x': 2, 'y': 0}], 'hazards': []},
               'you': {'id': 'gs_cXpM8DVrwfQ6BTjCjRPTj7kc', 'name': 'snake1', 'latency': '202', 'health': 95, 'body': [{'x': 2, 'y': 4}, {'x': 1, 'y': 4}, {'x': 0, 'y': 4}, {'x': 0, 'y': 3}, {'x': 1, 'y': 3}, {'x': 2, 'y': 3}, {'x': 2, 'y': 2}, {'x': 2, 'y': 1}, {'x': 3, 'y': 1}, {'x': 4, 'y': 1}, {'x': 5, 'y': 1}, {'x': 5, 'y': 0}, {'x': 6, 'y': 0}, {'x': 6, 'y': 1}, {'x': 6, 'y': 2}, {'x': 5, 'y': 2}, {'x': 4, 'y': 2}, {'x': 3, 'y': 2}, {'x': 3, 'y': 3}, {'x': 4, 'y': 3}, {'x': 5, 'y': 3}, {'x': 6, 'y': 3}, {'x': 6, 'y': 4}, {'x': 6, 'y': 5}, {'x': 6, 'y': 6}, {'x': 5, 'y': 6}, {'x': 4, 'y': 6}, {'x': 3, 'y': 6}, {'x': 2, 'y': 6}, {'x': 1, 'y': 6}, {'x': 0, 'y': 6}, {'x': 0, 'y': 5}, {'x': 1, 'y': 5}], 'head': {'x': 2, 'y': 4}, 'length': 33, 'shout': '', 'squad': ''}}
