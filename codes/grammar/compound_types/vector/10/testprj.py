import taichi as ti

ti.init(arch=ti.cpu)

vec0f = ti.types.vector( 0, ti.f32 )
x0 = vec0f( 0.0 )
print( "type(x0) =", type(x0) )
print( "x0.__dict__ =", x0.__dict__ )
print( "dir(x0) =", dir(x0) )
print( "x0      =", x0 )
print( "x0.ndim =", x0.ndim )
print( "x0.n    =", x0.n )
print( "x0.m    =", x0.m )
print( )
print( )
