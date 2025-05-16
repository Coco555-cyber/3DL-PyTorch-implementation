import polyscope as ps
import numpy as np
import colorsys
import time
import color_maps

from pathlib import Path
from model_reader import read_obj, read_off
from gaussian_curvature import discrete_gaussian_curvature

model_name = 'bumpy'
file = Path(f'../objects/{model_name}.npy')
V = VN = F = FN = None

if Path(f'../objects/{model_name}.obj').is_file():
    V, VN, F, FN = read_obj(f'{model_name}.obj')
elif Path(f'../objects/{model_name}.off'):
    V, F = read_off(f'{model_name}.off')

if file.is_file():
    angles = np.load(f'../objects/{model_name}.npy')
else:
    angles = discrete_gaussian_curvature(V, F)
    np.save("../objects/" + model_name, np.array(angles))

colors = np.empty((V.shape[0], 3))
angles = (angles + abs(np.min(angles))) / (np.max(angles) + abs(np.min(angles)))
for i, angle in enumerate(angles):
    # colors[i] = np.array(color_maps.viridis_cm[int(angle[0] * 255)])
    colors[i] = np.array(colorsys.hsv_to_rgb((1 - angle[0]) * 0.75, 1, 1))

ps.init()
ps_mesh = ps.register_surface_mesh("my mesh", V, F, smooth_shade=False)
ps_mesh.add_color_quantity("rand colors", colors, enabled=True)
ps_mesh.set_material("candy")
ps.show()