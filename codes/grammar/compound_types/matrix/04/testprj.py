import taichi as ti

ti.init(arch=ti.cpu)

MAT1x2 = ti.types.matrix(1, 2, ti.f32)
m1x2 = MAT1x2( [[1., 2.]] )
print( "type(m1x2) =", type(m1x2) )
print( "m1x2.__dict__ =", m1x2.__dict__ )
print( "m1x2 =\n", m1x2 )

MAT2x1 = ti.types.matrix(2, 1, ti.f32)
m2x1 = MAT2x1( [[1.],[2.]] )
print( "type(m2x1) =", type(m2x1) )
print( "m2x1.__dict__ =", m2x1.__dict__ )
print( "m2x1 =\n", m2x1 )

MAT2x2 = ti.types.matrix(2, 2, ti.f32)
m2x2 = MAT2x2( [[1., 2.], [3., 4.]] )
print( "type(m2x2) =", type(m2x2) )
print( "m2x2.__dict__ =", m2x2.__dict__ )
print( "m2x2 =\n", m2x2 )

MAT2x3 = ti.types.matrix(2, 3, ti.f32)
m2x3 = MAT2x3( [[1., 2.], [3., 4.], [5., 6.]] )
print( "type(m2x3) =", type(m2x3) )
print( "m2x3.__dict__ =", m2x3.__dict__ )
print( "m2x3 =\n", m2x3 )





