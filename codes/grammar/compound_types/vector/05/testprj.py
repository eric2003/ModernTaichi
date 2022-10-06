import taichi as ti

ti.init(arch=ti.cpu)

vec0f = ti.types.vector( 0, ti.f32 )
x = vec0f( 0.0 )
print( " x =", x )

x1 = ti.Vector([])
print( " x1 =", x1 )

vec1f = ti.types.vector( 1, ti.f32 )
a = vec1f( 0.0 )
print( " a =", a )

a1 = ti.Vector([0.0])
print( " a1 =", a1 )

vec2f = ti.types.vector( 2, ti.f32 )
b = vec2f( 0.0 )
print( " b =", b )

b1 = ti.Vector([0.0, 0.0])
print( " b1 =", b1 )

vec3f = ti.types.vector( 3, ti.f32 )
c = vec3f( 0.0 )
print( " c =", c )

c1 = ti.Vector([0.0, 0.0, 0.0])
print( " c1 =", c1 )

