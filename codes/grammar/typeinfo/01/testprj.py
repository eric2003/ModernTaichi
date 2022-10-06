import taichi as ti

ti.init(arch=ti.cpu)

def print_is_int( vartype ) :
    print( vartype, " is_integral = ", ti.types.is_integral(vartype) )
    print( vartype, " is_real = ", ti.types.is_real(vartype) )

print( "type(ti.types.f16) =", type(ti.types.f16) )
print( "type(ti.types.f32) =", type(ti.types.f32) )
print_is_int(ti.types.f16)
print( "ti.types.is_real(ti.types.f16) =", ti.types.is_real(ti.types.f16) )
print( "ti.types.is_integral(ti.types.f16) =", ti.types.is_integral(ti.types.f16) )
print( "ti.types.is_signed(ti.types.i32) =", ti.types.is_signed(ti.types.i32) )
print( "ti.types.is_signed(ti.types.u32) =", ti.types.is_signed(ti.types.u32) )
print( "ti.types.is_real(ti.types.f32) =", ti.types.is_real(ti.types.f32) )
print( "ti.types.is_tensor(ti.types.f32) =", ti.types.is_tensor(ti.types.f32) )

