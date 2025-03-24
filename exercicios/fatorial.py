def fatorial_recursivo(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial_recursivo(n - 1)

num = int(input("Digite um número para calcular o fatorial: "))
print(f"{num}! = {fatorial_recursivo(num)}")
