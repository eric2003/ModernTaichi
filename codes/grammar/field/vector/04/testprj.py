import taichi as ti

ti.init(arch=ti.cpu)

v1s1d = ti.Vector.field( 1, ti.f32, shape=(9) )

print( "type(v1s1d) =", type(v1s1d) )
#print( "dir(v1s1d) =", dir(v1s1d) )
print( "v1s1d.__doc__ =", v1s1d.__doc__ )
print( "v1s1d.__dict__ =", v1s1d.__dict__ )
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


v2s1d = ti.Vector.field( 2, ti.f32, shape=(9) )

print( "type(v2s1d) =", type(v2s1d) )
#print( "dir(v2s1d) =", dir(v2s1d) )
print( "v2s1d.shape =", v2s1d.shape )
print( "v2s1d.dtype =", v2s1d.dtype )
print( "v2s1d.ndim =", v2s1d.ndim )
print( "type(v2s1d.shape) =", type(v2s1d.shape) )
print( "len(v2s1d.shape) =", len(v2s1d.shape) )
print( "v2s1d.n    =", v2s1d.n )
print( "v2s1d.m    =", v2s1d.m )
print( "v2s1d      =\n", v2s1d )

print( "v2s1d[ 0 ] =", v2s1d[ 0 ] )
print( "type(v2s1d[ 0 ]) =", type(v2s1d[ 0 ]) )

print( "v2s1d[ 0 ].__dict__ =", v2s1d[ 0 ].__dict__ )
print( "v2s1d[ 0 ].ndim =", v2s1d[ 0 ].ndim )
print( "v2s1d[ 0 ].n =", v2s1d[ 0 ].n )
print( "v2s1d[ 0 ].m =", v2s1d[ 0 ].m )



