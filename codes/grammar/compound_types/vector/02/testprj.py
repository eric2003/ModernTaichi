import taichi as ti

ti.init(arch=ti.cpu)
vec3f = ti.types.vector( 3, ti.f32 )
a = vec3f( 0.0 )
print( " a =", a )
print( " type(a) =", type(a) )

b = vec3f( 0.0, 1.0, 2.0 )
print( " b =", b )

c = vec3f( [1.0, 2.0, 3.0] )
print( " c =", c )

