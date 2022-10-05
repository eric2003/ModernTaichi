import taichi as ti

ti.init(arch=ti.cpu)

f_0d = ti.field(ti.f32, shape=( ))  # 0D field
f_1d = ti.field(ti.i32, shape=(9))  # 1D field
f_2d = ti.field(int, shape=(3, 6))  # 2D field
print( "f_0d.shape =", f_0d.shape )
print( "f_0d.dtype =", f_0d.dtype )

print( "f_1d.shape =", f_1d.shape )
print( "f_1d.dtype =", f_1d.dtype )

print( "f_2d.shape =", f_2d.shape )
print( "f_2d.dtype =", f_2d.dtype )
