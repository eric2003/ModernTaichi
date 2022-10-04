import taichi as ti

ti.init(arch=ti.cpu)

# Declare a 0D scalar field whose data type is f32
f_0d = ti.field(ti.f32, shape=())  # 0D field

f_0d[ None ] = 10.0

print( "f_0d[ None ]=", f_0d[ None ] )