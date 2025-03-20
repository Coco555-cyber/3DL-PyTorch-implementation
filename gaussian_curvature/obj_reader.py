def read_obj(file_name: str):
    vertices: list[tuple[float]] = []
    normals: list[tuple[float]] = []
    faces: list[tuple[float]] = []

    with open('../objects/' + str(file_name), 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('#'):
                continue
            coords = line.split(' ')
            if coords[0] == 'v':
                vertices.append([float(c) for c in coords[1:]])
            elif coords[0] == 'vn':
                normals.append([float(c) for c in coords[1:]])
            elif coords[0] == 'f':
                faces.append([int(c.split('/')[0]) - 1 for c in coords[1:]])
    
    return vertices, normals, faces



