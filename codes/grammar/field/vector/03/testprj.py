import taichi as ti

ti.init(arch=ti.cpu)

v1s0d = ti.Vector.field( 1, ti.f32, shape=() )

print( "type(v1s0d) =", type(v1s0d) )
print( "v1s0d.__dict__ =", v1s0d.__dict__ )
print( "v1s0d.ndim =", v1s0d.ndim )
print( "v1s0d.n    =", v1s0d.n )
print( "v1s0d.m    =", v1s0d.m )
print( "v1s0d      =\n", v1s0d )

print( "v1s0d[ None ] =", v1s0d[ None ] )
print( "type(v1s0d[ None ]) =", type(v1s0d[ None ]) )

print( "v1s0d[ None ].__dict__ =", v1s0d[ None ].__dict__ )
print( "v1s0d[ None ].ndim =", v1s0d[ None ].ndim )
print( "v1s0d[ None ].n =", v1s0d[ None ].n )
print( "v1s0d[ None ].m =", v1s0d[ None ].m )

v1s1d = ti.Vector.field( 1, ti.f32, shape=(9) )

print( "type(v1s1d) =", type(v1s1d) )
print( "dir(v1s1d) =", dir(v1s1d) )
print( "v1s1d.__doc__ =", v1s0d.__doc__ )
print( "v1s1d.__dict__ =", v1s0d.__dict__ )
print( "v1s1d.vars =", v1s1d.vars )
print( "v1s1d.shape =", v1s1d.shape )
print( "v1s1d.dtype =", v1s1d.dtype )
print( "v1s1d.ndim =", v1s1d.ndim )
print( "type(v1s1d.shape) =", type(v1s1d.shape) )
print( "len(v1s1d.shape) =", len(v1s1d.shape) )
print( "v1s1d.n    =", v1s1d.n )
print( "v1s1d.m    =", v1s1d.m )
print( "v1s1d      =\n", v1s1d )

print( "v1s1d[ 0 ] =", v1s1d[ 0 ] )
print( "type(v1s1d[ 0 ]) =", type(v1s1d[ 0 ]) )

print( "v1s1d[ 0 ].__dict__ =", v1s1d[ 0 ].__dict__ )
print( "v1s1d[ 0 ].ndim =", v1s1d[ 0 ].ndim )
print( "v1s1d[ 0 ].n =", v1s1d[ 0 ].n )
print( "v1s1d[ 0 ].m =", v1s1d[ 0 ].m )


