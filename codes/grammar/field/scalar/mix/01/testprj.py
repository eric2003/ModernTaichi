import taichi as ti

ti.init(arch=ti.cpu)

# Declare a 2D scalar field whose data type is int
f_2d = ti.field(int, shape=(3, 6))  # 2D field
for i in range( 3 ):
    for j in range( 6 ):
        f_2d[i, j] = i * 10 + j
print( "f_2d =\n", f_2d )
print( "f_2d[ 2, 3 ] =", f_2d[ 2, 3 ] )
print( "type(f_2d) =", type(f_2d) )
print( "f_2d.shape =", f_2d.shape )
print( "f_2d.dtype =", f_2d.dtype )

fv_2d = ti.field(0, int, shape=(3, 6))  # 2D field
for i in range( 3 ):
    for j in range( 6 ):
        fv_2d[i, j] = i * 10 + j
print( "fv_2d =\n", fv_2d )
print( "fv_2d[ 2, 3 ] =", fv_2d[ 2, 3 ] )
print( "type(fv_2d) =", type(fv_2d) )
print( "fv_2d.shape =", fv_2d.shape )
print( "fv_2d.dtype =", fv_2d.dtype )

