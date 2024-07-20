from analysis import sum_to_n, arithmetic_sum


def test_sum():
    integers = [0, 1, 2, 3]
    expected_sums = [0, 1, 3, 6]

    for i, expected_sum in zip(integers, expected_sums):
        assert sum_to_n(i)[0] == expected_sum
        assert arithmetic_sum(i)[0] == expected_sum
