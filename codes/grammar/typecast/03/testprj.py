import taichi as ti

ti.init(arch=ti.cpu)
    
@ti.kernel    
def foo() :
    a = 1.7
    b = ti.cast( a, ti.i32 )
    c = ti.cast( b, ti.f32 )
    print( "b =", b )
    print( "c =", c )
  
foo()

