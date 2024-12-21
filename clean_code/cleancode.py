def average_rgb(pixels):
    r = [x[0] for x in pixels]
    g = [x[1] for x in pixels]
    b = [x[2] for x in pixels]
    n = len(r)
    return ((sum(r)/n), (sum(g)/n), (sum(b)/n))
 #   return (int(sum(r)/n), int(sum(g)/n), int(sum(b)/n))

print(average_rgb([(0,0,0),(256,128,0),(32,64,33)]))

def unit_test_avg():
    print('Test average...')
    print(average_rgb([(0,0,0)]))
    print(average_rgb([(0, 0, 0),(0,0,0)]))
    print(average_rgb([(0,0,0)])==average_rgb([(0, 0, 0), (0, 0, 0)]))
def unit_test_type():
    print('Test type...')
    for i in range(3):
        print(average_rgb([(1, 2, 3), (4, 5, 6), (7, 8, 9)])[i])
        print(type(average_rgb([(1,2,3),(4,5,6),(7,8,9)])[i]) == int)
        print([(1, 2, 3), (4, 5, 6), (7, 8, 9)][i])

unit_test_avg()
unit_test_type()