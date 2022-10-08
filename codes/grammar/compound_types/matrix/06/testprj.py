import taichi as ti

ti.init(arch=ti.cpu)

#<class 'taichi.lang.matrix.Matrix'>
def myprint( name, var ) :
    #print( "type(%s) ="%name, type(var) )
    #print( "%s.__dict__ =" %name, var.__dict__ )
    print( "%s.ndim ="%name, var.ndim )
    print( "%s.n    ="%name, var.n )
    print( "%s.m    ="%name, var.m )
    print( "%s      =\n"%name, var )
    
MAT0x0 = ti.types.matrix(0, 0, ti.f32)
m0x0 = MAT0x0( [] )

MAT1x0 = ti.types.matrix(1, 0, ti.f32)
m1x0 = MAT1x0( [] )

MAT1x1 = ti.types.matrix(1, 1, ti.f32)
m1x1 = MAT1x1( [1.0] )

MAT2x1 = ti.types.matrix(2, 1, ti.f32)
m2x1 = MAT2x1( [1.0,2.0] )

MAT3x1 = ti.types.matrix(3, 1, ti.f32)
m3x1 = MAT3x1( [1.0,2.0,3.0] )

MAT4x1 = ti.types.matrix(4, 1, ti.f32)
m4x1 = MAT4x1( [1.0,2.0,3.0,4.0] )

MAT2x2 = ti.types.matrix(2, 2, ti.f32)
m2x2 = MAT2x2( [1.0,2.0,3.0,4.0] )

MAT3x2 = ti.types.matrix(3, 2, ti.f32)
m3x2 = MAT3x2( [1.0,2.0,3.0,4.0,5.0,6.0] )

MAT4x2 = ti.types.matrix(4, 2, ti.f32)
m4x2 = MAT4x2( [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0] )

MAT1x2 = ti.types.matrix(1, 2, ti.f32)
m1x2 = MAT1x2( [1.0,2.0] )

MAT1x3 = ti.types.matrix(1, 3, ti.f32)
m1x3 = MAT1x3( [1.0,2.0,3.0] )

MAT1x4 = ti.types.matrix(1, 4, ti.f32)
m1x4 = MAT1x4( [1.0,2.0,3.0,4.0] )

MAT2x3 = ti.types.matrix(2, 3, ti.f32)
m2x3 = MAT2x3( [1.0,2.0,3.0,4.0,5.0,6.0] )

MAT2x4 = ti.types.matrix(2, 4, ti.f32)
m2x4 = MAT2x4( [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0] )

myprint( "m0x0", m0x0 )
myprint( "m1x0", m1x0 )
myprint( "m1x1", m1x1 )
myprint( "m2x1", m2x1 )
myprint( "m3x1", m3x1 )
myprint( "m4x1", m4x1 )
myprint( "m2x2", m2x2 )
myprint( "m3x2", m3x2 )
myprint( "m4x2", m4x2 )

myprint( "m1x1", m1x1 )
myprint( "m1x2", m1x2 )
myprint( "m1x3", m1x3 )
myprint( "m1x4", m1x4 )
myprint( "m2x3", m2x3 )
myprint( "m2x4", m2x4 )

myprint( "m2x3", m2x3 )
myprint( "m3x2", m3x2 )

myprint( "m2x4", m2x4 )
myprint( "m4x2", m4x2 )
