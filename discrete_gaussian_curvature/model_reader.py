import numpy as np

def read_obj(file_name: str):
    vertices: list[tuple[float]] = []
    normals: list[tuple[float]] = []
    faces: list[tuple[float]] = []
    face_normals: list[tuple[float]] = []

    with open(f'../objects/{file_name}', 'r') as file:
        for line in file:
            line = line.strip()
            
            if line.startswith('#'):
                continue
            coords = line.split()

            if coords[0] == 'v':
                vertices += [[float(c) for c in coords[1:]]]
            elif coords[0] == 'vn':
                normals += [[float(c) for c in coords[1:]]]
            elif coords[0] == 'f':
                if '/' in coords[1]:
                    faces += [[int(c.split('/')[0]) - 1 for c in coords[1:]]]
                    face_normals += [int(coords[1].split('/')[2])]
                else:
                    faces += [[int(c) - 1 for c in coords[1:]]]

    return np.array(vertices), np.array(normals), np.array(faces), np.array(face_normals)

def read_off(file_name: str):
    vertices: list[tuple[float]] = []
    faces: list[tuple[float]] = []
    start_line = 0

    with open(f'../objects/{file_name}', 'r') as file:
        lines = file.readlines()

    if lines[0].strip() == 'OFF':
        start_line = 1
    num = lines[start_line].strip().split()
    num_vert, num_face, num_edge = [int(n) for n in num]
    start_line += 1

    for i in range(start_line, start_line + num_vert):
        coords = lines[i].strip().split()
        vertices += [[float(c) for c in coords]]

    for i in range(start_line + num_vert, start_line + num_vert + num_face):
        coords = lines[i].strip().split()
        faces += [[int(c) for c in coords[1:]]]

    return np.array(vertices), np.array(faces)