import sys

sys.stdin = open('5185_input.txt')
def dec_bi(n):
    if n == 0:
        return '0000'
    
    b_str = ''
    while n > 0:
        b_str = str(n % 2) + b_str
        n //= 2
    if len(b_str) != 4:
           b_str = '0' * (4 - len(b_str)) + b_str
    return b_str
   
dict_hexa = {'A': '1010', 'B': '1011' , 'C': '1100', 'D': '1101', 'E': '1110','F':'1111'}

for tc in range(1,1+int(input())):
    N, hexa = input().split()
    lst = []
    for h in hexa :
        if h.isdigit():
            lst.append(dec_bi(int(h)))
        else:
            lst.append(dict_hexa[h])
    print(f'#{tc}', ''.join(lst))
   
   
    
    