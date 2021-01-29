def bubble_sort(data):
    
    n = len(data)
    
    for i in range(n-1):
        for j in range(n-i-1):
            if data[j] < data[j+1]:
                temp = data[j]
                data[j] = data[j+1]
                data[j+1] = temp

data = [4,5,0,1,2,7,6,3]

bubble_sort(data)
print(data)
