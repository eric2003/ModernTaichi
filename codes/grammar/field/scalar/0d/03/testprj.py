import taichi as ti

ti.init(arch=ti.cpu)

# Declare a 0D scalar field whose data type is f32
f_0d = ti.field(ti.f32, shape=())  # 0D field
f_0d[ None ] = 10.0

print( "type(f_0d) =", type(f_0d) )
print( "f_0d.__dict__ =", f_0d.__dict__ )
print( "f_0d      =\n", f_0d )

print( "type(f_0d[ None ]) =", type(f_0d[ None ]) )

print( "f_0d.shape =", f_0d.shape )
print( "f_0d.dtype =", f_0d.dtype )

print( "type(f_0d.shape ) =", type(f_0d.shape ) )
print( "type(f_0d.dtype ) =", type(f_0d.dtype ) )

