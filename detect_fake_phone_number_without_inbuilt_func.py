# fake phone number dection star with +91 , 0 ,7,9,8 if star with +91 then in format +91 00000 000000
# if star with 0 the in format 0XXXXX XXXXX and only digit 
def detect_fake_phone_number(n):
    try:
        if  n =="":
            print("please enter the phone number")
            return False
        def check_digit(n):
            digit=['1','2','3','4','5','6','7','8','9','0']
            for ch in n :
                if ch == " ":
                    continue
                found = False
                for d in digit:
                    if d == ch:
                        found=True
                        break
                if not found :
                    return False
            return True
        
        if n[0]=="+":
            result=check_digit(n[1:])
        else:
            result=check_digit(n)
        
        if result == True:
            pn=n
            length=len(pn)
            if pn[0:3]=="+91":
                if length!=15:
                    print("phone number must contain 10 digit or fromat is of +91 XXXXX XXXXX please note the space")
                elif not (pn[3]==" " and pn[9]==" "):
                    print("fromat is of +91 XXXXX XXXXX please note the space")  
                else:
                    print(f"valid number :{pn}")
            elif pn[0]=="0":
                if length!=12:
                    print("phone number must contain 10 digit or fromat is of +91 XXXXX XXXXX please note the space")
                elif pn[6]!=" ":
                    print("fromat is of 0XXXXX XXXXX please note the space")  
                else:
                    print(f"valid number :{pn}")
                    
            elif pn[0] in ['7','8','9']:
                if length!=10:
                    print("phone number must contain 10 digit")
                else:
                    print(f"valid number :{pn}")
            else:
                print("invalid")
          
        else :
            print("Enter the digit only")
            
    except Exception as e:
        print(f"error:{e}")

detect_fake_phone_number("+91 85910 63904")
