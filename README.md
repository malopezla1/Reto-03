# Reto-03

En este reto se usaran las bases vistas en clase como herencia, composición y encapsulamiento en la programación orientada a objetos. 

# Ejercicio 1
1. Cree la clase Rectangle y la clase Line.
   
2. El rectángulo debe inicializarse utilizando cualquiera de estos 3 métodos:

  - **Método 1**: Esquina inferior izquierda (Punto) + ancho y alto
  - **Método 2**: Centro(Punto) + ancho y alto
  - **Método 3**: Dos esquinas opuestas (puntos), por ejemplo, inferior izquierda y superior derecha.
    ancho , alto , centro: atributos de instancia

  - **compute_area()**: debe devolver el área del rectángulo
  - **compute_perimeter()**: debe devolver el perímetro del rectángulo

3. Cree una clase **Square()** que herede los atributos y métodos necesarios de Rectangle.
   
4. Cree un método llamado **compute_interference_point(Point)** que devuelva si un punto está dentro de un rectángulo.

5. La linea debe inicializarse con las siguientes carácteristicas y metodos.

  - **length, slope, start, end**: atributos de instancia, dos de ellos son puntos (por lo que una línea se compone al menos de dos           puntos).
  - **compute_length()**: debe devolver la longitud de la línea
  - **compute_slope()**: debe devolver la pendiente de la línea desde la horizontal en grados.
  - **compute_horizontal_cross()**: debe devolver si existe la intersección con el eje x
  - **compute_vertical_cross()**: debe devolver si existe la intersección con el eje y
    
6. Redefinir la clase **Rectángulo**, agregando un nuevo método de inicialización utilizando 4 Líneas (la composición en su mejor expresión, un rectángulo se compone de 4 líneas).

# Código:

``` Python
class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

class Line(Point):
    def __init__(self, start: Point, end: Point) -> None:
        super().__init__(start.x, start.y)
        self.start = start
        self.end = end

    def compute_length(self) -> float:
        length = ((self.end.x - self.start.x) ** 2 + (self.end.y - self.start.y) ** 2) **0.5
        return length
    
    def compute_slope(self) -> float:
        if self.end.x == self.start.x:
            return None
        slope = (self.end.y - self.start.y) / (self.end.x - self.start.x)
        return slope

    def compute_horizontal_cross(self) -> float:
        slope = self.compute_slope()
        if slope is None:
            return self.start.x
        if slope == 0:
            return None
        x_intercept = self.start.x - self.start.y / slope
        return x_intercept
    
    def compute_vertical_cross(self) -> float:
        slope = self.compute_slope()
        if slope is None:
            return None
        y_intercept = self.start.y - slope * self.start.x
        return y_intercept

    def __str__(self) -> str:
        return (
            f"Longitud: {self.compute_length()}, "
            f"Pendiente: {self.compute_slope()}, "
            f"Corte Horizontal: {self.compute_horizontal_cross()}, "
            f"Corte Vertical: {self.compute_vertical_cross()}"
        )
        
class rectangle:
    #Método 2: Desde el centro, ancho y alto
    def __init__(self, width: float, height: float, center: Point):
        self.width = width
        self.height = height
        self.center = center

    @classmethod
    def from_bottom_left(cls, bottom_left: Point, width: float, height: float):
        center_x = bottom_left.x + width / 2
        center_y = bottom_left.y + height / 2
        return cls(width, height, Point(center_x, center_y))

    @classmethod
    def from_corners(cls, p1: Point, p2: Point):
        width = abs(p1.x - p2.x)
        height = abs(p1.y - p2.y)
        center_x = (p1.x + p2.x) / 2
        center_y = (p1.y + p2.y) / 2
        return cls(width, height, Point(center_x, center_y))

    @classmethod
    def from_lines(cls, line1: Line, line2: Line, line3: Line, line4: Line):
        puntos = [line1.start, line1.end, line2.start, line2.end, line3.start, line3.end, line4.start, line4.end]
        xs = [p.x for p in puntos]
        ys = [p.y for p in puntos]
        width = abs(max(xs) - min(xs))
        height = abs(max(ys) - min(ys))
        center = Point((max(xs) + min(xs)) / 2, (max(ys) + min(ys)) / 2)
        return cls(width, height, center)
    
    def bounds(self):
        half_width = self.width / 2
        half_height = self.height / 2

        center_x = self.center.x
        center_y = self.center.y

        x_min = center_x - half_width
        y_min = center_y - half_height
        x_max = center_x + half_width
        y_max = center_y + half_height

        return {"x_min": x_min, "y_min": y_min, "x_max": x_max, "y_max": y_max}

    def corners(self):
        bounds = self.bounds()
        x_min = bounds["x_min"]
        y_min = bounds["y_min"]
        x_max = bounds["x_max"]
        y_max = bounds["y_max"]

        bottom_left = (x_min, y_min)
        bottom_right = (x_max, y_min)
        top_left = (x_min, y_max)
        top_right = (x_max, y_max)

        return {
            "Inferior_Izquierdo": bottom_left,
            "Inferior_Derecho": bottom_right,
            "Superior_Izquierdo": top_left,
            "Superior_Derecho": top_right
        }
    
    def compute_interference_point(self, point: Point) -> bool:
        bounds = self.bounds()
        x_min = bounds["x_min"]
        y_min = bounds["y_min"]
        x_max = bounds["x_max"]
        y_max = bounds["y_max"]
        return (x_min <= point.x <= x_max) and (y_min <= point.y <= y_max)

    def computer_area(self):
        return self.width * self.height
    
    def computer_perimeter(self):
        return 2 * (self.width + self.height)
    
class square(rectangle):
    def __init__ (self, side_length: float, center: Point):
        super().__init__(side_length, side_length, center)

    def computer_area(self):
        return self.width ** 2
    
    def computer_perimeter(self):
        return 4 * self.width

#Límites, esquinas, área y perímetro del rectángulo
print("--- Rectángulo ---")
print("Elige el método para crear el rectángulo:")
print("1. Esquina inferior izquierda + ancho y alto")
print("2. Centro + ancho y alto")
print("3. Dos esquinas opuestas")
print("4. Cuatro líneas\n")

opcion = input("Ingresa 1, 2, 3 o 4: ")

if opcion == "1":
    datos = input("\nIngresa (x,y) de la esquina inferior izquierda, ancho y alto (separados por espacios): ").split()
    esquina = Point(float(datos[0]), float(datos[1]))
    ancho = float(datos[2])
    alto = float(datos[3])
    rect = rectangle.from_bottom_left(esquina, ancho, alto)

elif opcion == "2":
    datos = input("\nIngresa ancho, alto, (x,y) del centro (separados por espacios): ").split()
    ancho = float(datos[0])
    alto = float(datos[1])
    centro = Point(float(datos[2]), float(datos[3]))
    rect = rectangle(ancho, alto, centro)

elif opcion == "3":
    datos = input("\nIngresa (x,y) de la primera esquina y (x,y) de la segunda esquina (separados por espacios): ").split()
    p1 = Point(float(datos[0]), float(datos[1]))
    p2 = Point(float(datos[2]), float(datos[3]))
    rect = rectangle.from_corners(p1, p2)

elif opcion == "4":
    print("\nIngresa los puntos de las 4 líneas (cada línea: x1 y1 x2 y2):")
    lineas = []
    for i in range(4):
        datos = input(f"Línea {i+1}: ").split()
        p1 = Point(float(datos[0]), float(datos[1]))
        p2 = Point(float(datos[2]), float(datos[3]))
        lineas.append(Line(p1, p2))
    rect = rectangle.from_lines(lineas[0], lineas[1], lineas[2], lineas[3])

else:
    print("Opción no válida.")
    rect = None

if rect:
    bounds_rectangle = rect.bounds()
    print(f"Los límites del rectángulo son: {bounds_rectangle}")
    corners_rectangle = rect.corners()
    print(f"Las esquinas del rectángulo son: {corners_rectangle}")
    area_rectangle = rect.computer_area()
    print(f"El área del rectángulo es: {area_rectangle}")
    perimeter_rectangle = rect.computer_perimeter()
    print(f"El perímetro del rectángulo es: {perimeter_rectangle}")

    # Comprobar si un punto está dentro del rectángulo
    user_point1 = input("Ingrese las coordenadas del primer punto (x y): ").split()
    user_point2 = input("Ingrese las coordenadas del segundo punto (x y): ").split()

    point1 = Point(float(user_point1[0]), float(user_point1[1]))
    point2 = Point(float(user_point2[0]), float(user_point2[1]))

    print(f"¿El punto {point1.x, point1.y} está dentro del rectángulo?: {rect.compute_interference_point(point1)}")
    print(f"¿El punto {point2.x, point2.y} está dentro del rectángulo?: {rect.compute_interference_point(point2)}")
        
# Límites, esquinas, área y perímetro del cuadrado
print("\n--- Cuadrado ---")
user2 = input("Ingrese el lado y centro del cuadrado (x,y), separados por espacios: ").split()
side_sq = float(user2[0])
center_sq = Point(float(user2[1]), float(user2[2]))
sq = square(side_sq, center_sq)

bounds_square = sq.bounds()
print(f"Los límites del cuadrado son: {bounds_square}")
corners_square = sq.corners()
print(f"Las esquinas del cuadrado son: {corners_square}")
area_square = sq.computer_area()
print(f"El área del cuadrado es: {area_square}")
perimeter_square = sq.computer_perimeter()
print(f"El perímetro del cuadrado es: {perimeter_square}") 
```

# Reto-03:

1. Escenario de restaurante: desea diseñar un programa para calcular la factura del pedido de un cliente en un restaurante.
 
  - **Definir una clase base MenuItem**: Esta clase debe tener atributos como nombre, precio y un método para calcular el precio total.
  - **Cree subclases para diferentes tipos de elementos de menú**: herede de MenuItem y defina propiedades específicas para cada tipo         (por ejemplo, Bebida, Aperitivo, Plato principal).
  - **Definir una clase Order**: Esta clase debe tener una lista de objetos MenuItem y métodos para agregar artículos, calcular el monto      total de la factura y potencialmente aplicar descuentos específicos según la composición del pedido.

Cree un diagrama de clases con todas las clases y sus relaciones. El menú debe tener al menos 10 elementos. El código debe seguir las reglas PEP8.

# Diagrama: 

```mermaid
--- 
config:
  theme: dark
---
classDiagram
direction TB
    class MenuItem {
	    +name: String
	    +price: float
	    +calculate_total() : float
    }
    class Beverage {
	    +size: String
		+type: String 
	    +calculate_total() : float
    }
    class Appetizer {
	    +is_vegetarian: bool
		+is_vegan: bool
		+regular_appetizer: bool
	    +calculate_total() : float
    }
    class MainCourse {
	    +pork: String
		+beef: String
		+chicken: String
		+fish: String
		+vegetarian: String
	    +calculate_total() : float
    }
    class Order {
	    +items: List~MenuItem~
	    +add_item(item: MenuItem)
	    +calculate_total() : float
	    +apply_discount() : float
    }

    MenuItem <|-- Beverage
    MenuItem <|-- Appetizer
    MenuItem <|-- MainCourse
    Order "1" --* "*" MenuItem : contiene
```

# Código:

El siguiente codigo, muestra el funcionamiento de el diagrama de clases acerca de un escenario real de un restaurante.

```Python
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
```
