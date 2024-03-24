def calcula_fibonacci(valor):
    fib = [0, 1]
    cur_index = 0

    while (fib[len(fib)-1] < valor) or (len(fib) < 20):    
        next_fib = fib[cur_index] + fib[cur_index + 1]
    
        fib.append(next_fib)
    
        cur_index += 1
        
    return fib

num = int(input("Insira um valor inteiro: "))
fib = calcula_fibonacci(num)
print(f"Sequência de Fibonacci calculada: {fib}")
print(f"O valor {num} {'' if num in fib else 'não '}pertence à sequência de Fibonacci.")