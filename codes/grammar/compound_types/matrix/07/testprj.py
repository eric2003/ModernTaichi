import taichi as ti

ti.init(arch=ti.cpu)

#<class 'taichi.lang.matrix.Matrix'>
def myprint( name, var ) :
    print( "type(%s) ="%name, type(var) )
    print( "%s.__dict__ =" %name, var.__dict__ )
    print( "%s.ndim ="%name, var.ndim )
    print( "%s.n    ="%name, var.n )
    print( "%s.m    ="%name, var.m )
    print( "%s      =\n"%name, var )
    
MAT0x0 = ti.types.matrix(0, 0, ti.f32)
m0x0 = MAT0x0( [] )

myprint( "m0x0", m0x0 )

#print( "m0x0.dtype =", m0x0.dtype )
print( "dir(m0x0) =", dir(m0x0) )

#print( "ti.lang.matrix.Matrix.__dict__ =", ti.lang.matrix.Matrix.__dict__ )
