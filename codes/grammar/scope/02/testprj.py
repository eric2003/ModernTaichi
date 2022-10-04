import taichi as ti

ti.init(arch=ti.cpu)

#Python scope
#Everything in a normal python script is in the Python-scope

def foo() :
    print( "This is a normal python function" )
   
foo()

