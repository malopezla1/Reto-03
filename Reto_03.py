# Clase base
class MenuItem:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def calculate_total(self, quantity: int) -> float:
        if quantity < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        return self.price * quantity

    def __str__(self) -> str:
        return f"{self.name}: ${self.price}"


class Order:
    def __init__(self):
        self.items = []

    def calculate_total_price(self) -> float:
        return sum(item.calculate_total(quantity) for item, quantity in self.items)

    def add_item(self, item: MenuItem, quantity: int) -> None:
        self.items.append((item, quantity))

    def apply_discount(self, discount_percentage: float) -> float:
        total = self.calculate_total_price()
        discount_percentage = max(0, min(discount_percentage, 100))
        discount_amount = total * (discount_percentage / 100)
        return total - discount_amount

    def __str__(self) -> str:
        items_str = "\n".join(
            f"{item.name} x {quantity} - ${item.calculate_total(quantity)}"
            for item, quantity in self.items
        )
        return (
            f"Items:\n{items_str}\n"
            f"Total Price: ${self.calculate_total_price()}"
        )


class Beverage(MenuItem):
    def __init__(self, name: str, price: float, size: str, drink_type: str):
        super().__init__(name, price)
        self.size = size
        self.drink_type = drink_type

    def __str__(self) -> str:
        return super().__str__() + f" (Size: {self.size}, Type: {self.drink_type})"

    def calculate_total(self, quantity: int) -> float:
        size_multiplier = {"small": 1, "medium": 1.5, "large": 2}
        type_multiplier = {"soda": 1, "juice": 1.2, "water": 0.6}
        multiplier = size_multiplier.get(self.size.lower(), 1) * type_multiplier.get(self.drink_type.lower(), 1)
        return super().calculate_total(quantity) * multiplier


class Appetizer(MenuItem):
    def __init__(self, name: str, price: float, is_vegetarian: bool, is_vegan: bool, regular_appetizer: bool):
        super().__init__(name, price)
        self.is_vegetarian = is_vegetarian
        self.is_vegan = is_vegan
        self.regular_appetizer = regular_appetizer

    def calculate_total(self, quantity: int) -> float:
        if self.is_vegan:
            discount = 0.2
            total = super().calculate_total(quantity)
            total -= total * discount
            return total
        
        if self.is_vegetarian:
            discount = 0.1
            total = super().calculate_total(quantity)
            total -= total * discount
            return total

        if self.regular_appetizer:
            return super().calculate_total(quantity)

        return super().calculate_total(quantity)


class MainCourse(MenuItem):
    def __init__(self, name: str, price: float, pork: bool, beef: bool, chicken: bool, fish: bool, vegetarian: bool):
        super().__init__(name, price)
        self.pork = pork
        self.beef = beef
        self.chicken = chicken
        self.fish = fish
        self.vegetarian = vegetarian

    def calculate_total(self, quantity: int) -> float:
        if self.pork:
            surcharge = 0.15
            total = super().calculate_total(quantity)
            total += total * surcharge
            return total

        if self.beef:
            surcharge = 0.2
            total = super().calculate_total(quantity)
            total += total * surcharge
            return total

        if self.chicken:
            surcharge = 0.1
            total = super().calculate_total(quantity)
            total += total * surcharge
            return total

        if self.fish:
            surcharge = 0.12
            total = super().calculate_total(quantity)
            total += total * surcharge
            return total

        if self.vegetarian:
            return super().calculate_total(quantity)

        return super().calculate_total(quantity)
# Uso de las clases
if __name__ == "__main__":
    beverage1 = Beverage("Coca-cola", 2.0, "Large", "Soda")
    beverage2 = Beverage("Orange Juice", 3.0, "Medium", "Juice")
    beverage3 = Beverage("Water", 1.0, "Small", "Water")
    beverage4 = Beverage("Lemonade", 2.5, "Large", "Juice")
    appetizer1 = Appetizer("Bruschetta", 5.0, False, False, True)
    appetizer2 = Appetizer("Vegan Salad", 6.0, True, True, False)
    appetizer3 = Appetizer("Garlic Bread", 4.0, True, False, False)
    main_course1 = MainCourse("Pork Roll", 15.0, True, False, False, False, False)
    main_course2 = MainCourse("Beef Steak", 18.0, False, True, False, False, False)
    main_course3 = MainCourse("Grilled Chicken", 12.0, False, False, True, False, False)
    main_course4 = MainCourse("Salmon Fillet", 20.0, False, False, False, True, False)
    main_course5 = MainCourse("Vegetarian Pasta", 10.0, False, False, False, False, True)

    order = Order()
    order.add_item(beverage1, 2)
    order.add_item(appetizer1, 1)
    order.add_item(main_course1, 1)

    print(order)