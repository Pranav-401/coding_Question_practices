try:
    def equilibrium(input_array):
        length=len(input_array)
        if length>1:
            # sort_array=sorted(input_array)
            for i in range(length):
                left_side=sum(input_array[:i])
                right_side=sum(input_array[i+1:])
                
                if left_side == right_side:
                    return i
            return -1     
        else:
            print(f"array is {length} it should greater than 2")
except Exception as e:
    print(f"Error:{e}")

input_array=list(map(int,input("enter the elment : ").split()))
index=equilibrium(input_array)
print(f"array is : {input_array} , index is {index}")