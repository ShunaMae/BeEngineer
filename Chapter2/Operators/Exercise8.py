
def main():
    A = int(input())
    N = int(input())
    r = float(input()) / 100

    ans = A
    to_return = (ans * r * (1+r)**N) // (1+r)**N-1
    for _ in range(3):
        
        print(to_return)
        ans -= to_return
    print(ans)

main()
