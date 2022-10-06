import taichi as ti

ti.init(arch=ti.cpu)

mat2x2 = ti.types.matrix(2, 2, ti.f32)  # 2x2 matrix type
M = mat2x2( [[1., 2.], [3., 4.]] )  # an instance of this type
M1 = ti.Matrix( [[1., 2.], [3., 4.]] );

print( "M =\n", M )
print( "M1 =\n", M1 )



