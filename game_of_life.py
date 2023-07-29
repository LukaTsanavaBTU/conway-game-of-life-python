import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

height = 100
width = 100

space = np.zeros((height, width))


def space_cycle():
    global paused
    if not paused:
        to_activate = []
        to_deactivate = []
        for i in range(0, height):
            for j in range(0, width):
                if space[i, j] == 1:
                    to_activate += check_cells_around(i, j)
                    if check_around(i, j) not in (2, 3):
                        to_deactivate += [(i, j)]
        for cell in to_activate:
            space[cell[0], cell[1]] = 1
        for cell in to_deactivate:
            space[cell[0], cell[1]] = 0


def check_around(i, j):
    cell_sum = 0
    for a in [-1, 0, 1]:
        for b in [-1, 0, 1]:
            if (a, b) != (0, 0):
                if not (i + a < 0 or i + a > (height - 1) or j + b < 0 or j + b > (width - 1)):
                    cell_sum += space[i + a, j + b]
    return cell_sum


def check_cells_around(i, j):
    to_activate = []
    for a in [-1, 0, 1]:
        for b in [-1, 0, 1]:
            if (a, b) != (0, 0):
                if not (i + a < 0 or i + a > (height - 1) or j + b < 0 or j + b > (width - 1)):
                    if check_around(i+a, j+b) == 3:
                        to_activate.append((i+a, j+b))
    return to_activate


def update(frames):
    space_cycle()
    im.set_data(space)
    return im,


def onclick(event):
    if event.inaxes is not None:
        if space[int(event.ydata), int(event.xdata)] == 1:
            space[int(event.ydata), int(event.xdata)] = 0
        else:
            space[int(event.ydata), int(event.xdata)] = 1


def pause(event):
    global paused
    if event.key == "control":
        paused = not paused


fig, ax = plt.subplots()
im = plt.imshow(space)
anim = animation.FuncAnimation(fig, update, cache_frame_data=False)
paused = False
fig.canvas.mpl_connect("button_press_event", onclick)
fig.canvas.mpl_connect("key_press_event", pause)
plt.show()
