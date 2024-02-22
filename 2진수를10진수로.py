def dec_to_bi(n): 
    binary = "0."
    
    r = n * 2
    if r >= 1:
        binary += "1"
        n = r - 1
    else:
        binary += "0"
        n = r
    
    return binary

print(dec_to_bi(0.625))