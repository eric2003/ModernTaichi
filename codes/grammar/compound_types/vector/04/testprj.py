import taichi as ti

ti.init(arch=ti.cpu)

vec0f = ti.types.vector( 0, ti.f32 )
x = vec0f( 0.0 )
print( " x =", x )
print( " type(x) =", type(x) )

vec1f = ti.types.vector( 1, ti.f32 )
a = vec1f( 0.0 )
print( " a =", a )
print( " type(a) =", type(a) )

vec2f = ti.types.vector( 2, ti.f32 )
b = vec2f( 0.0 )
print( " b =", b )
print( " type(b) =", type(b) )

vec3f = ti.types.vector( 3, ti.f32 )
c = vec3f( 0.0 )
print( " c =", c )
print( " type(c) =", type(c) )

