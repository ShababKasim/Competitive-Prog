
def gcd(a,b):
    while b != 0:
        remainder = a % b
        a,b = b,remainder 
    return a

def rec_gcd(a,b):
    return a if b == 0 else rec_gcd(b, a % b) 

if __name__ == '__main__':
    x,y = 400,124
    res = rec_gcd(x,y)
    print(res)    