import taichi as ti

ti.init(arch=ti.cpu)

#Taichi scope
#Everything decorated by @ti.kernel or @ti.func is in the Taichi-scope

@ti.kernel
def foo() :
    print( "This is now a Taichi kernel" )
   
foo()

