def polynomial_input(polynomail, x_and_k):
    holder =[]
    for i in polynomial:
        holder.append(i.replace("x",x_and_k[1]))
    # for i in holder:
    #     int(i)
    holder.pop()
    return holder

        




if __name__ == "__main__":
    x_and_k = ['1', '4']
    x = x_and_k[0]
    polynomial = ['x**3', 'x**2', 'x', '1']
    print(polynomial_input(polynomial, x_and_k))