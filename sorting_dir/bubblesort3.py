def bubble_sort(a):
    for _ in range(len(a)):
        for i in range(1, len(a)):
            if a[i]<a[i-1]:
                a[i-1], a[i] = a[i], a[i-1]                

names = ['pretzels', 'carrots', 'arugula', 'bacon']
bubble_sort(names)
print(names)
