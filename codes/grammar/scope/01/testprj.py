import taichi as ti

ti.init(arch=ti.cpu)

d = 1

def foo() :
    d_python = d
    print( "d_python = ", d_python )
    
@ti.kernel
def bar() :
    d_taichi = d
    print( "d_taichi = ", d_taichi )
    
d = d + 1
foo()
bar()

d = d + 1
foo()
bar()
