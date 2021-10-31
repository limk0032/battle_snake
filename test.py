import test_data
import snakePloter
import server_logic
import cProfile
import re

# snakePloter.plot_snake(test_data.test_data_1)
# chosen_move = server_logic.choose_move(test_data.test_data_1)
# print(f"chosen_move:{chosen_move}")
# assert chosen_move == "right"

# snakePloter.plot_snake(test_data.test_data_4)
# chosen_move = server_logic.choose_move(test_data.test_data_4)
# print(f"chosen_move:{chosen_move}")
# assert chosen_move == "down"

cProfile.run('server_logic.choose_move(test_data.test_data_4)')
