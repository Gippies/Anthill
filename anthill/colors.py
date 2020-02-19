WHITE = 255, 255, 255
RED = 255, 0, 0
GREEN = 0, 255, 0
SAND_YELLOW = 255, 191, 0
BROWN = 117, 69, 23


def get_color_by_vertices(vertex_count, r, g, b):
    rgb_list = []
    for i in range(vertex_count):
        rgb_list.extend([r, g, b])
    return 'c3B', tuple(rgb_list)
