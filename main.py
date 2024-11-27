rec_total_calls = 0
rec_calls_per_n = {}

def fibonacci(n):
    global rec_total_calls
    rec_total_calls += 1
    n_count = rec_calls_per_n.get(n, 0)
    rec_calls_per_n[n] = n_count + 1

    if n == 0 or n == 1:
        return n

    return (fibonacci(n - 1) +
        fibonacci(n - 2))

print(fibonacci(5))
print(f"{rec_total_calls=}")
print(f"{rec_calls_per_n=}")