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
print( "f_2d.shape[ 0 ] =", f_2d.shape[ 0 ] )
print( "f_2d.shape[ 1 ] =", f_2d.shape[ 1 ] )

