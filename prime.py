try:
    def prime(n):
        if n <= 1:
            print(f"{n} is not a prime number")
        else:
            for i in range(2,n):
                if n % i == 0:
                    print(f"{n} is not a prime number")
                    return
            print(f"{n} is a prime number")
    prime(4)
except Exception as e:
    print(f"error is {e}")