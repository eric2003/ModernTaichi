import taichi as ti

ti.init(arch=ti.cpu)

@ti.kernel
def foo() :
    a = ti.Vector( [0.0] )
    print( a )
    d = ti.Vector( [0.0, 1.0, 0.0] )
    print( d )
    B = ti.Matrix( [ [1.5, 1.4], [1.3, 1.2] ] )
    print( "B =\n", B )
    r = ti.Struct( ro = a, rd = d, l  = 1 )
    print( "r.ro =", r.ro )
    print( "r.rd =", r.rd )

foo()