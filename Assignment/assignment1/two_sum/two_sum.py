def solution(n):

    if n > 99 or n < -99:
        raise ValueError("The number must be a two-digit integer or its negative equivalent.")

    n = abs(n)
    digit_sum = 0
    for digit in str(n):
        digit_sum += int(digit)

    return digit_sum

test = solution(-91)

print(test)
