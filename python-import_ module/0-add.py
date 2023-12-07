from add_0 import add

def main():
    global a, b
    a = 1
    b = 2
    result = add(a, b)
    print("{} + {} = {}".format(a, b, result))

if __name__ == "__main__":
    main()


