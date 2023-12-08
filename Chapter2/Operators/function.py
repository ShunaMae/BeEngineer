def show_score(eng_score: int, math_score: int, jpn_score=100) -> int:
    print("eng_score:", eng_score, "math_score:", math_score, "jpn_score:", jpn_score)


def collatz(n: int) -> list:
    li = []
    while True:
        li.append(n)
        if n == 1:
            break
        if not n%2:
            n //= 2
        else:
            n = 3*n + 1
    print(*li)
    return

collatz(3)
        

    