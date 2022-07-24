
def fibonacci(prev,now,turn,arr):
    if turn == 0:
        return arr
    new = prev + now
    next_turn = turn - 1
    arr.append(now)
    fibonacci(now,new,next_turn,arr)
    
    return arr


if __name__ == '__main__':

    length_of_fibonacci = 10
    lof = length_of_fibonacci

    value = fibonacci(0,1,lof,[0])
    print(value)