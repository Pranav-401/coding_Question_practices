try:
    def check_magic_number(n):
        original = n
        while n>9:
            arr=list(str(n))
            l=len(arr)
            total=0
            for i in range(l):
                total += int(arr[i])
            n=total
            
        if total == 1:
            print(f"{original} is a magic number")
        else:
            print(f"{original} is a not magic number")

    check_magic_number(1274)   
except Exception as e:
    print(f"error is :{e}")

