import taichi as ti

ti.init(arch=ti.cpu)
x = 1.0
a = ti.cast( x, ti.i32 )
print( " a =", a )
print( " type(a) =", type(a) )

