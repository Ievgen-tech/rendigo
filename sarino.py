def greet(name: str) -> str:
    return f"Привіт, {name}!"


def sum_numbers(a: int, b: int) -> int:
    return a + b


def main() -> None:
    name = input("Введіть ім'я: ")
    print(greet(name))

    a = int(input("Введіть перше число: "))
    b = int(input("Введіть друге число: "))
    print(f"Сума: {sum_numbers(a, b)}")

    print("П'ять рядків: ")
    for i in range(1, 6):
        print(f"Рядок {i}")


if __name__ == "__main__":
    main()
