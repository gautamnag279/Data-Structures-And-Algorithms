def solve(s):
    ans = ''.join(sorted(s))
    if ans == 'Timru':
        print("YES")
    else:
        print("NO")

# I HAVE NO IDEA WHY THE FOLOWING FUNCTION DOES NOT WORK
# def solve2(n, s):
#     ans = 'YES'
#     letters = [84, 105, 109, 117, 114]
#     if n != 5:
#         ans = "NO"
#     else:
#         for i in s:
#             if ord(i) not in letters:
#                 ans = "NO"
#                 break
#     print(ans)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        solve(s)

        