import taichi as ti

ti.init(arch=ti.cpu)

v2s2d = ti.Vector.field( 2, ti.f32, shape=(4,3) )

print( "type(v2s2d) =", type(v2s2d) )
print( "v2s2d.shape =", v2s2d.shape )
print( "v2s2d.dtype =", v2s2d.dtype )
print( "v2s2d.ndim =", v2s2d.ndim )
print( "type(v2s2d.shape) =", type(v2s2d.shape) )
print( "len(v2s2d.shape) =", len(v2s2d.shape) )
print( "v2s2d.n    =", v2s2d.n )
print( "v2s2d.m    =", v2s2d.m )
print( "v2s2d      =\n", v2s2d )

print( "v2s2d[ 0 , 0 ] =", v2s2d[ 0 , 0 ] )
print( "type(v2s2d[ 0 , 0 ]) =", type(v2s2d[ 0 , 0 ]) )

print( "v2s2d[ 0 , 0 ].__dict__ =", v2s2d[ 0 , 0 ].__dict__ )
print( "v2s2d[ 0 , 0 ].ndim =", v2s2d[ 0 , 0 ].ndim )
print( "v2s2d[ 0 , 0 ].n =", v2s2d[ 0 , 0 ].n )
print( "v2s2d[ 0 , 0 ].m =", v2s2d[ 0 , 0 ].m )
