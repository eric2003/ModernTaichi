import taichi as ti

ti.init(arch=ti.cpu)

f_0d = ti.field(ti.f32, shape=( ))  # 0D field
f_0d[ None ] = 10.0

print( "f_0d =", f_0d )
print( "f_0d[ None ] =", f_0d[ None ] )
print( "type(f_0d) =", type(f_0d) )
print( "type(f_0d[ None ]) =", type(f_0d[ None ]) )

print( "f_0d.shape =", f_0d.shape )
print( "f_0d.dtype =", f_0d.dtype )
print( "type(f_0d.shape ) =", type(f_0d.shape ) )
print( "type(f_0d.dtype ) =", type(f_0d.dtype ) )
print()
print()
v_0d = ti.Vector.field( 2, ti.f32, shape=() )
v_0d[ None ] = ti.Vector( [1.1, 2.3] )
print( "v_0d =", v_0d )
print( "v_0d[ None ] =", v_0d[ None ] )
print( "type(v_0d) =", type(v_0d) )
print( "type(v_0d[ None ]) =", type(v_0d[ None ]) )
print( "v_0d.shape =", v_0d.shape )
print( "v_0d.dtype =", v_0d.dtype )

print( "type(v_0d.shape ) =", type(v_0d.shape ) )
print( "type(v_0d.dtype ) =", type(v_0d.dtype ) )

