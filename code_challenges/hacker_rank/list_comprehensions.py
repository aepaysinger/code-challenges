def create_cuboids(x, y, z, n):
    cuboids = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n]
    print(cuboids)

if __name__ == '__main__':
    x = 1
    y = 1
    z = 1
    n = 2
    create_cuboids(x, y, z, n)