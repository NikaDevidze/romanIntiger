def romanToInteger(roman):
    # I = 1
    # V = 5
    # X = 10
    # L = 50
    # C = 100
    # D = 500
    # M = 1000
    I = roman.count("I")
    V = roman.count("V")
    X = roman.count("X")
    L = roman.count("L")
    C = roman.count("C")
    D = roman.count("D")
    M = roman.count("M")
    ans = I*1 + V*5 + X*10 + L*50 + C*100 + D*500 + M*1000
    return ans

#print(romanToInteger("DMCV"))