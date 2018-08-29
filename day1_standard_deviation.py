import math
def mean(data):
    return sum(data) / len(data)

def stddev(data, size):
    sum = 0
    for i in range(size):
        sum = sum + (data[i] - mean(data)) ** 2
    return math.sqrt(sum / size)
size = int(input())
numbers = list(map(int, input().split()))
print(round(stddev(numbers, size), 1))