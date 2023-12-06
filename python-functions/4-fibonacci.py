def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

if __name__ == "__main__":
    print(fibonacci_sequence(6))
    print(fibonacci_sequence(1))
    print(fibonacci_sequence(0))
    print(fibonacci_sequence(20))