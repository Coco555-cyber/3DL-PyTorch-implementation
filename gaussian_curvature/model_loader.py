import polyscope as ps
from obj_reader import read_obj

V, VN, F = read_obj('plane.obj')
ps.init()
ps.register_surface_mesh("my mesh", V, F, smooth_shade=True)
ps.show()