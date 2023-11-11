DIGITS = '9876543210'
AVAILABLE_OPERATIONS = {
    '0': '',
    '1': '+',
    '2': '-',
    # '3': '*',
    # '4': '/'
}

from functools import reduce

def _convert_to_str(number: int, new_base: int, digit_limit: int):
    '''
    Конвертирование числа `number` в системе счисления по модулю `new_base`
    в строку без потери порядка символов
    '''
    
    op_list = []
    
    while number:
        op_list.append(str(number % new_base))
    
        number = number // new_base
    
    # Заполняем пустые места нулями чтобы потом применить zip()
    length = len(op_list)
    if length < digit_limit - 1:
        op_list.append('0' * (digit_limit - length - 1))
        
    return reduce(lambda acc, el: el + acc, op_list)

def solve(string: str, available_operations: dict, target_value: int = 200) -> list:
    current_base = len(available_operations.items())
    res = []

    # Перебор всех возможных позиций знаков
    max_op = int(str(current_base - 1) * (len(string) - 1), current_base)
    available_positions = range(max_op + 1)

    for iteration in available_positions:
        operations = _convert_to_str(iteration, current_base, len(string))
        
        print(f'Iteration #{iteration} out of {max_op}')
        
        expr = string[0]
        
        # Проходимся по zip, где каждому элементу сопоставлен код операции и сама цифра
        for digit, operation_code in zip(string[1:], operations):
            expr += available_operations[operation_code] + digit
        
        try:
            if eval(expr) == target_value:
                res.append(f'{expr} == {target_value}')
        except ZeroDivisionError:
            pass

    return res

def main():

    result = solve(DIGITS, AVAILABLE_OPERATIONS)
    
    print('\n\n\nResult:')
    print(
        *result,
        sep='\n'
    ) if result != [] else print('Возможных вариантов решения не найдено')

if __name__ == '__main__':
    main()

    