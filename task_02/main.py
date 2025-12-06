import turtle

def koch_curve(t, order, size):
    """
    t: об'єкт turtle для малювання
    order: рівень рекурсії
    size: довжина лінії
    """
    if order == 0:
        t.forward(size)
    else:
        koch_curve(t, order - 1, size / 3)
        # ліворуч на 60
        t.left(60)
        koch_curve(t, order - 1, size / 3)
        # праворуч на 120
        t.right(120)
        koch_curve(t, order - 1, size / 3)
        # ліворуч на 60
        t.left(60)
        koch_curve(t, order - 1, size / 3)
        

def main():
    try:
        order = int(input("Введіть рівень рекурсії (рекомендовано 0-5): "))
    except ValueError:
        print("Будь ласка, введіть ціле число.")
        return

    window = turtle.Screen()
    window.bgcolor("white")
    window.title("Сніжинка Коха")

    t = turtle.Turtle()

    # центтруемо
    t.penup()
    t.goto(-150, 90) # Зсув ліворуч і вгору
    t.pendown()

    size = 300 

    for _ in range(3):
        koch_curve(t, order, size) 
        t.right(120)

    window.mainloop()

if __name__ == "__main__":
    main()