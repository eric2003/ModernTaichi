import taichi as ti

ti.init(arch=ti.cpu)

vec0f = ti.types.vector( 0, ti.f32 )
x = vec0f( 0.0 )
print( " x =", x )
print( "type(x) =", type(x) )

print( "x.__dict__ =", x.__dict__ )

print( )
print( )

print( "ti.lang.matrix.Vector.__dict__ =", ti.lang.matrix.Vector.__dict__ )

print( "x.n =", x.n )
print( "x.m =", x.m )
print( 'getattr(x, "n") =', getattr(x, "n") )
print( "x.__dict__ =", x.__dict__ )
print( )
print( )
print( "dir(x) =", dir(x) )

print( "ti.Vector.__dict__ =", ti.Vector.__dict__ )
