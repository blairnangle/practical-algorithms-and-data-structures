import time


def sum_to_n(n: int) -> (int, float):
    start = time.time()

    total: int = 0
    for number in range(n + 1):
        total = total + number

    end = time.time()

    return total, end - start


def arithmetic_sum(n: int) -> (int, float):
    start = time.time()

    total: int = (n * (n + 1)) // 2

    end = time.time()

    return total, end - start


if __name__ == "__main__":
    output_template = "{}({}) = {:15d} ({:8.7f} seconds)"
    for _ in range(5):
        print(output_template.format("sum_to_n", 1000000, *sum_to_n(1000000)))

    for i in range(1, 10):
        print(output_template.format("sum_to_n", i * 1000000, *sum_to_n(i * 1000000)))

    for _ in range(5):
        print(output_template.format("arithmetic_sum", 1000000, *arithmetic_sum(1000000)))

    for i in range(1, 10):
        print(output_template.format("arithmetic_sum", i * 1000000, *arithmetic_sum(i * 1000000)))
