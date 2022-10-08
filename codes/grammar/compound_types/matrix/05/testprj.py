import taichi as ti

ti.init(arch=ti.cpu)

#<class 'taichi.lang.matrix.Matrix'>

MAT0x0 = ti.types.matrix(0, 0, ti.f32)
m0x0 = MAT0x0( [] )

print( "type(m0x0) =", type(m0x0) )
print( "m0x0.__dict__ =", m0x0.__dict__ )
print( "m0x0.ndim =", m0x0.ndim )
print( "m0x0.n    =", m0x0.n )
print( "m0x0.m    =", m0x0.m )
print( "m0x0      =\n", m0x0 )

