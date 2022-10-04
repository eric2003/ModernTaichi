import taichi as ti

ti.init(arch=ti.cpu)

vec3 = ti.types.vector(3, ti.f32)
sphere = ti.types.struct(center=vec3, radius=float)
s = sphere(center=vec3([0., 0., 0.]), radius=1.0)

print( "s =\n", s )
print( " type(s) =", type(s) )

