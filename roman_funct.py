valors = {
    5000: "V*",
    4000: "IV*",
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I"
}

def to_roman(n):

    result = ""
    
    for number in valors:
        
        if n >= 5000:
            n = n - 5000
            result = valors[5000] + result
        elif n >= 4000:
            n = n - 4000
            result = valors[4000] + result
        elif n >= 1000:
            n = n - 1000
            result = valors[1000] + result
        elif n >= 900:
            n = n - 900
            result = result + valors[900]
        elif n >= 500:
            n = n - 500
            result = result + valors[500]
        elif n >= 400:
            n = n - 400
            result = result + valors[400]
        elif n >= 100:
            n = n - 100
            result = result + valors[100]   
        elif n >= 90:
            n = n - 90
            result = result + valors[90]
        elif n >= 50:
            n = n - 50
            result = result + valors[50]
        elif n >= 40:
            n = n - 40
            result = result + valors[40]  
        elif n >= 10:
            n = n - 10
            result = result + valors[10]
        elif n >= 9:
            n = n - 9
            result = result + valors[9]
        elif n >= 5:
            n = n - 5
            result = result + valors[5] 
        elif n >= 4:
            n = n - 4
            result = result + valors[4]
        elif n >= 1:
            n = n - 1
            result = result + valors[1]
        elif n <= 0:
          break
           
        else:
            result 

    
    return result

print(to_roman(5125))