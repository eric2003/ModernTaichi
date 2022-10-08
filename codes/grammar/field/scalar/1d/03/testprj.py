import taichi as ti

ti.init(arch=ti.cpu)

# Declare a 1D scalar field whose data type is f32
f_1d = ti.field(ti.i32, shape=9)  # 1D field
for i in range( 9 ):
    f_1d[ i ] = i

print( "type(f_1d) =", type(f_1d) )
print( "f_1d.__dict__ =", f_1d.__dict__ )
print( "f_1d      =\n", f_1d )

print( "f_1d[ 3 ] =", f_1d[ 3 ] )
print( "type(f_1d[ 3 ]) =", type(f_1d[ 3 ]) )

print( "f_1d.shape =", f_1d.shape )
print( "f_1d.dtype =", f_1d.dtype )

print( "type(f_1d.shape ) =", type(f_1d.shape ) )
print( "type(f_1d.dtype ) =", type(f_1d.dtype ) )

print( "dir(f_1d) =", dir(f_1d) )

