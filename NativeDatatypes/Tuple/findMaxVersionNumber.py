if __name__ == '__main__':
    for i in range(1, int(input("Enter the number of elements\n")) + 1):
        version = tuple(input("%s : "%(i)).split('.'))
        if i == 0:
            max = version
        if version > max:
            max = version
print("\t\tMax version is : %s"%('.'.join(max)))
