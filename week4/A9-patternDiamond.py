print("Diamond design printer:")
n=int(input("Enter the number of rows of the pattern to be printed(only odd numbers): "))

if n%2!=0 :
    mid = n // 2

    for i in range(n):
        if i <= mid:
            spaces = mid - i
            stars = 2*i + 1
        else:
            spaces = i - mid
            stars = 2*(n - i) - 1

        print(" " * spaces + "*" * stars)
else:
    print("Enter only odd numbers!")