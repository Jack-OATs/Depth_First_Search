import numpy as np
from os.path import join


def find_path_DFS(map, current, goal, explored, path, depth=0):
    if (current[0], current[1]) not in explored:
        explored.append(current)
        if (current[0], current[1]) == explored[0]:
            path.append(current)

    if current == goal:
        return path, explored

    if len(map) > current[0]+1 and (current[0]+1, current[1]) not in explored and map[current[0]+1][current[1]] == 0:
        current = (current[0]+1, current[1])
        path.append(current)
        find_path_DFS(map, current, goal, explored, path)

    elif len(map[0]) > current[1]+1 and (current[0], current[1]+1) not in explored and map[current[0]][current[1]+1] == 0:
        current = (current[0], current[1]+1)
        path.append(current)
        find_path_DFS(map, current, goal, explored, path)

    elif 0 <= current[0]-1 and (current[0]-1, current[1]) not in explored and map[current[0]-1][current[1]] == 0:
        current = (current[0]-1, current[1])
        path.append(current)
        find_path_DFS(map, current, goal, explored, path)

    elif 0 <= current[1]-1 and (current[0], current[1]-1) not in explored and map[current[0]][current[1]-1] == 0:
        current = (current[0], current[1]-1)
        path.append(current)
        find_path_DFS(map, current, goal, explored, path)

    else:
        del path[-1]
        if not path:
            return None, explored
        current = path[-1]
        find_path_DFS(map, current, goal, explored, path)

    if not path:
        return None, explored

    return path, explored


if __name__ == "__main__":
    m = np.load(join('Maps', 'Map2.npy'))
    start = (0, 0)
    end = (4, 4)
    # print(len(m))
    path, explored = find_path_DFS(m, start, end, [], [])
    print(path, "\n", explored)
