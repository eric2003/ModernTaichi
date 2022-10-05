import taichi as ti

ti.init(arch=ti.cpu)

# Declare a 1D scalar field whose data type is f32
f_1d = ti.field(ti.i32, shape=9)  # 1D field
for i in range( 9 ):
    f_1d[ i ] = i
print( "f_1d =", f_1d )
print( "f_1d[ 3 ] =", f_1d[ 3 ] )
print( "type(f_1d) =", type(f_1d) )
