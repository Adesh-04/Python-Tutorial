
def count_str(item, string):
    count = 0
    for i in string:
        if i == item:
            count+=1
        else:
            continue
    return count
        

if __name__ == '__main__':
    value = count_str('f','sdjadfafbedvasdfa')
    print(value)