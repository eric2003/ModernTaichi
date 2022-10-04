import taichi as ti

ti.init(arch=ti.cpu)
vec3f = ti.types.vector( 3, ti.f32 )
a = vec3f( 0.0 )
print( " a =", a )
print( " type(a) =", type(a) )
