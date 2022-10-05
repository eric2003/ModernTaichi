import taichi as ti

ti.init(arch=ti.cpu)
vec3f = ti.types.vector(3, ti.f32)
mat2f = ti.types.matrix(2, 2, ti.f32)
ray   = ti.types.struct(ro=vec3f, rd=vec3f, l=ti.f32)

@ti.kernel
def foo() :
    a = vec3f( 0.0 )
    print( a )
    d = vec3f( 0.0, 1.0, 0.0 )
    print( d )
    B = mat2f( [ [1.5, 1.4], [1.3, 1.2] ] )
    print( "B =\n", B )
    r = ray( ro = a, rd = d, l  = 1 )
    print( "r.ro =", r.ro )
    print( "r.rd =", r.rd )
    
foo()


