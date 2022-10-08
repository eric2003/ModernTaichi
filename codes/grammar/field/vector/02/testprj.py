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


v2s0d = ti.Vector.field( 2, ti.f32, shape=() )

print( "type(v2s0d) =", type(v2s0d) )
print( "v2s0d.__dict__ =", v2s0d.__dict__ )
print( "v2s0d.ndim =", v2s0d.ndim )
print( "v2s0d.n    =", v2s0d.n )
print( "v2s0d.m    =", v2s0d.m )
print( "v2s0d      =\n", v2s0d )

print( "v2s0d[ None ] =", v2s0d[ None ] )
print( "type(v2s0d[ None ]) =", type(v2s0d[ None ]) )

print( "v2s0d[ None ].__dict__ =", v2s0d[ None ].__dict__ )
print( "v2s0d[ None ].ndim =", v2s0d[ None ].ndim )
print( "v2s0d[ None ].n =", v2s0d[ None ].n )
print( "v2s0d[ None ].m =", v2s0d[ None ].m )

v3s0d = ti.Vector.field( 3, ti.f32, shape=() )

print( "type(v3s0d) =", type(v3s0d) )
print( "v3s0d.__dict__ =", v3s0d.__dict__ )
print( "v3s0d.ndim =", v3s0d.ndim )
print( "v3s0d.n    =", v3s0d.n )
print( "v3s0d.m    =", v3s0d.m )
print( "v3s0d      =\n", v3s0d )

print( "v3s0d[ None ] =", v3s0d[ None ] )
print( "type(v3s0d[ None ]) =", type(v3s0d[ None ]) )

print( "v3s0d[ None ].__dict__ =", v3s0d[ None ].__dict__ )
print( "v3s0d[ None ].ndim =", v3s0d[ None ].ndim )
print( "v3s0d[ None ].n =", v3s0d[ None ].n )
print( "v3s0d[ None ].m =", v3s0d[ None ].m )





