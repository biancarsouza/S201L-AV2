
def primo(n):
    divisores = 0

    for i in range(1, n):
        if n % i == 0:
            divisores = divisores + 1
            
    if(divisores > 2):
        return False
    
    return True

n = int(input())
print(primo(n))