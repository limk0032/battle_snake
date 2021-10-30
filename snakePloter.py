import matplotlib.pyplot as plt
import numpy as np
from matplotlib.table import Table


def get_symbol_snake_body(front, back):
    if front is None:
        # this is head
        return "\u25FC\u25FC"
    elif front["x"] > back["x"] and front["y"] == back["y"]:
        return "\u25B6"  # going right
    elif front["x"] < back["x"] and front["y"] == back["y"]:
        return "\u25C0"  # going left
    elif front["x"] == back["x"] and front["y"] > back["y"]:
        return "\u25B2"  # going up
    elif front["x"] == back["x"] and front["y"] < back["y"]:
        return "\u25BC"  # going down
    else:
        # unknown
        return "?"


def plot_snake(data):
    fig, ax = plt.subplots()
    ax.set_axis_off()
    tb = Table(ax, bbox=[0, 0, 1, 1])
    ax.add_table(tb)
    max_y = 7
    max_x = 7

    for y in range(8):
        for x in range(8):
            tb.add_cell(
                max_y - y,
                x,
                width=10,
                height=10,
                text=f"{x},{y}",
                facecolor="yellow",
                loc="center",
            )

    for snake in data["board"]["snakes"]:
        print(snake["body"])
        for i in range(len(snake["body"])):
            if i == 0:
                front = None
                back = snake["body"][i]
            else:
                front = snake["body"][i - 1]
                back = snake["body"][i]
            # print(tb[max_y - back["y"], back["x"]].get_text().get_text())
            cell = tb[max_y - back["y"], back["x"]]
            cell.set_text_props(
                text=f'{tb[max_y - back["y"], back["x"]].get_text().get_text()} {get_symbol_snake_body(front, back)}',
                # text=get_symbol_snake_body(front, back),
                backgroundcolor="pink",
            )
    plt.show()
    