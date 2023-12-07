def no_c(my_string):
    return ''.join([i for i in my_string if i not in 'cC'])

if __name__ == "__main__":
    print(no_c("Holberton School"))
    print(no_c("aya"))
    print(no_c("C is fun!"))