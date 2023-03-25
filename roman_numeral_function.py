# Initialisation of function with one parameter which will be the roman numeral
def RomanToNum(s):
    
    # Key with all primary symbol values of roman numerals
    roman = {"M":1000, "CM":900, "D":500, "CD":400, "C":100, "XC":90, "L":50, "XL":40, "X":10, "IX":9, "V":5, "IV":4, "I":1}

    # Iteration value
    i = 0

    # Converted tally of roman numeral
    num = 0

    # Iteration through length of parameter 
    while i < len(s):

        # Iteration through each roman numeral whilst checking if the numeral next to it and itself is within the key
        if i + 1 < len(s) and s[i:i+2] in roman:

            # If the double numeral is within the key the value will be added to the tally 
            # eg if the double numeral is IX; I = first i:i. X = +2 
            print(s[i:i+2])
            num += roman[s[i:i+2]]

            # Iteration will be +2 since the double numeral equates to a single value 
            i += 2

        # If not a double numeral value 
        else:
            
            # Add value of single numeral to tally
            num += roman[s[i]]

            # Iterate to next number
            i += 1

    # Return the tallied result 
    return num

# Converted result using the function will be saved in this variable
solution = RomanToNum("MMXIXIII")

# Print result 
print(solution)