from home_work.A.Rectangle.rectangle import Rectangle


def main() -> None:
    rect = Rectangle(3, 4)
    print(rect)  # Rectangle(w=3, h=4)
    print("Area:", rect.area())  # Area: 12
    print("Perimeter:", rect.perimeter())  # Perimeter: 14

if __name__ == "__main__":
    main()