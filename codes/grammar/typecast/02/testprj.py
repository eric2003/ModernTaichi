import taichi as ti

ti.init(arch=ti.cpu)
#implicit casts
#static types within the Taichi scope

def foo() :
    a = 1
    print( "python foo:type(a) =", type(a) )
    a = 2.7
    print( "python foo:type(a) =", type(a) )
    print( "python foo:a =", a )
    
@ti.func
def myfunc():  # a Taichi function
    b = 1
    print( "taichi func myfunc:type(b) =", type(b) )
    b = 2.7
    print( "taichi func myfunc:type(b) =", type(b) )
    print( "taichi func myfunc:b =", b )
    
    
@ti.kernel    
def bar() :
    b = 1
    print( "taichi bar:type(b) =", type(b) )
    b = 2.7
    print( "taichi bar:type(b) =", type(b) )
    print( "taichi bar:b =", b )
  
foo()
myfunc();
bar()

