# email detection 

def validated_email(e):
    if ' ' in e:
        print("email should not contain blank space")
        return False
        
    if e =="":
        print("please write email")
        return False
    
    def check_a(e):
        count=0
        for ch in e:
            if ch == "@":
                count=count+1
        return count
    if check_a(e) != 1:
        print("email should contain @")
        return False
    # end_check=".com"
    if (e[-10:]!="@gmail.com") and (e[-10:]!="@yahoo.com"):
        print("mail should end with @gmail.com or @yahoo.com")
        return False
  
    return True

print(validated_email("p@yahoo.com"))