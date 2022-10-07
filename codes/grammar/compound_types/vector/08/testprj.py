import taichi as ti

ti.init(arch=ti.cpu)

vec0f = ti.types.vector( 0, ti.f32 )
x0 = vec0f( 0.0 )
print( " x0 =", x0 )
print( "type(x0) =", type(x0) )

print( "x0.__dict__ =", x0.__dict__ )
print( "x0.n =", x0.n )
print( "x0.m =", x0.m )
print( )
print( )

vec1f = ti.types.vector( 1, ti.f32 )
x1 = vec1f( 0.0 )
print( "ti.lang.matrix.Vector.__dict__ =", ti.lang.matrix.Vector.__dict__ )
print( )
print( )
print( "x1.__dict__ =", x1.__dict__ )
print( "x1.n =", x1.n )
print( "x1.m =", x1.m )

