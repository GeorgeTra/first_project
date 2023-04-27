def longest_common_prefix(strs: list[str]) -> str:
    result = ""
    strs = sorted(strs)
    print(strs)
    first = strs[0]
    last = strs[-1]
    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            return result
        result = result + first[i]
    return result


print(longest_common_prefix(['корыто', 'корова', 'корзина']))


