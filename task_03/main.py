def move(source, target, rods):
    # видаляємо і повертаємо останній елемент
    disk = rods[source].pop()
    
    # --> target
    rods[target].append(disk)

    print(f"Перемістити диск {disk}: {source} -> {target}")
    print(f"Проміжний стан: {rods}")

def hanoi(n, source, target, auxiliary, rods):
    """
        n: кількість дисків
        source: звідки переносимо
        target: куди переносимо
        auxiliary: допоміжний стрижень
    """
    if n == 1:
        # Базовий випадок
        move(source, target, rods)
    else:
        #  Переносимо --> auxiliary
        hanoi(n - 1, source, auxiliary, target, rods)
        
        # Переносимо --> target
        move(source, target, rods)
        
        # Переносимо --> source
        hanoi(n - 1, auxiliary, target, source, rods)

def main():
    n = int(input("Введіть кількість дисків: "))
    
    initial_state = {
        'A': list(range(n, 0, -1)),
        'B': [],
        'C': []
    }
    
    print(f"Початковий стан: {initial_state}")
    
    hanoi(n, 'A', 'C', 'B', initial_state)
    
    print(f"Фінальний стан: {initial_state}")

if __name__ == "__main__":
    main()