def perfect(n):
    divisors_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i
        return divisors_sum == n

    n = int(input("enter a number = "))
    print(perfect(n))
