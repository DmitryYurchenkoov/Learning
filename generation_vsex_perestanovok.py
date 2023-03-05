def generate_numbers(N:int, M:int, prefix = None):
    """Генерирует все числа (с лидирующими нулями)
        в N-ричной системе счисления (N<= 10)
        длины M"""
    prefix = prefix or [] ##Проверяет prefix - получает None - это ложь соответсвенно prefix = [] равносильно созданию пустого списка//
    if M == 0:
        print(prefix) ##вспомнить древо
        return
    for digit in range(N):
        prefix.append(digit)
        generate_numbers(N, M-1, prefix)
        prefix.pop()

generate_numbers(2,3)