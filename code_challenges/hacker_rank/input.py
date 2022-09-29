def polynomial_input(polynomial, x_and_k):

    polynomial = " ".join(polynomial)
    polynomial = polynomial.replace("x", x_and_k[0])
    polynomial = polynomial.split(" ")
    total = 0
    
    for equation in polynomial:
        total += eval(equation)
    
    return total == int(x_and_k[1])
        
    

        




if __name__ == "__main__":
    x_and_k = ['1', '4']
    x = x_and_k[0]
    polynomial = ['x**3', 'x**2', 'x', '1']
    print(polynomial_input(polynomial, x_and_k))