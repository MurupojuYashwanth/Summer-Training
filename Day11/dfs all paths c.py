def dfs_paths(d, x, path=[]):
    path = path + [x]
    if x == 2:
        return [path]
    paths = []
    for i in d[x]:
        if i not in path:
            new_paths = dfs_paths(d, i, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths

d = {5: [7, 3], 7: [5, 4, 3], 4: [7, 8, 2], 3: [5, 7, 8], 8: [3, 4, 2], 2: [4, 8]}
paths = dfs_paths(d, 5)
for path in paths:
    print(path)
