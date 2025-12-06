from functools import lru_cache

file_path = "input2.txt"

@lru_cache(maxsize=None)
def get_ans(number: str, digits: int) -> int:
    if digits == 0:
        return 0

    if len(number) == digits:
        return int(number)

    # use number[0]
    ans1 = (int(number[0]) * 10 ** (digits - 1)) + get_ans(number[1:], digits - 1)

    # do not use number[0]
    ans2 = get_ans(number[1:], digits)
    return max(ans1, ans2)


with open(file_path, 'r') as file:
    ans = 0
    for line in file:
        line = line.strip()
        ans += get_ans(line, 12)

    print(ans)