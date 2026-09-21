def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    romanSymbol = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    romanTotal = 0
    first_symbol = ""
    
    if not (len(s) >= 1 and len(s)) <= 15: # 1 -> 15 length
        return
    for romanNumeral in s:
        if not(romanNumeral in romanSymbol): # s contains only valid roman numerals
            return
        value = romanSymbol[romanNumeral]
        print(f"RS: {romanNumeral}\nV:{value}")
        if first_symbol == "I" and (romanNumeral == "V" or romanNumeral == "X"):
            romanTotal += value - 2
            first_symbol = romanNumeral
        elif first_symbol == "X" and (romanNumeral == "L" or romanNumeral == "C"):
            romanTotal += value - 20
            first_symbol = romanNumeral
        elif first_symbol == "C" and (romanNumeral == "D" or romanNumeral == "M"):
            romanTotal += value - 200
            first_symbol = romanNumeral
        else:
            first_symbol = romanNumeral
            romanTotal += value
        print(romanTotal)
        
    if romanTotal >= 1 and romanTotal <= 3999:
        return romanTotal

# Testing
s = "EE"
romanToInt(s)

s = "IV"
romanToInt(s)
# Notes