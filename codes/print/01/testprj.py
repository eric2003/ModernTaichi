import taichi as ti

ti.init(arch=ti.gpu)

@ti.kernel
def kernel_print():
    for i in range( 10 ) :
        print( i )

def main():
    kernel_print()

if __name__ == '__main__':
    main()
