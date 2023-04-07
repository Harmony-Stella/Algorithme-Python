def sontInvOuOpp():
    a = float(input("Entrez le premier nombre : "))
    b = float(input("Entrez le deuxième nombre : "))
    
    if a + b == 0:
        message = f"{a} et {b} sont opposés."
        return True, message
    elif a * b == 1:
        message = f"{a} et {b} sont inverses."
        return True, message
    else:
        message = f"{a} et {b} ne sont ni inverses ni opposés."
        return False, message
