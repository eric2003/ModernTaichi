import taichi as ti

ti.init(arch=ti.cpu)
#implicit casts
#static types within the Taichi scope

def foo() :
    a = 1
    a = 2.7
    print( "python foo:a =", a )
    
@ti.kernel    
def bar() :
    b = 1
    b = 2.7
    print( "taichi bar:b =", b )
  
foo()
bar()

