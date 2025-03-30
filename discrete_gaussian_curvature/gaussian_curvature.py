import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import math
import numpy as np
import numpy.ma as ma

# def discrete_gaussian_curvature(V, F):
#     vertices = torch.from_numpy(V)
#     faces = torch.from_numpy(F)
#     curvature = []
#     for i, vertex in enumerate(vertices):
#         print(i/vertices.size()[0])
#         angular_deficit = 2 * math.pi
#         for face in faces:
#             if i in face:
#                 incident_vertices = face[(face != i).nonzero(as_tuple=False)]
#                 vector_1 = vertices[incident_vertices[0]] - vertex
#                 vector_2 = vertices[incident_vertices[1]] - vertex
#                 product = torch.dot(vector_1[0], vector_2[0])
#                 mag = (magnitude(vector_1) * magnitude(vector_2)).item()
#                 angular_deficit -= torch.acos(product / mag)
#         curvature.append(angular_deficit)
#     return curvature

def discrete_gaussian_curvature(V, F):
    vertices = torch.from_numpy(V)
    faces = torch.from_numpy(F)
    curvature = np.full((V.shape[0], 1), 2 * math.pi)
    for face in faces:
        for i, vertex in enumerate(face):
            vector_1 = vertices[face[i - 1]] - vertices[vertex]
            vector_2 = vertices[face[i - 2]] - vertices[vertex]
            product = torch.dot(vector_1, vector_2)
            mag = (magnitude(vector_1) * magnitude(vector_2))
            curvature[vertex] -= torch.acos(product / mag).item()
    return curvature

def magnitude(vector):
    return torch.sqrt(torch.sum(vector ** 2))
