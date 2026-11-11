import math
import unittest

try:
    from L20_Polimorphyzm.Shape import Shape
    from L20_Polimorphyzm.Circle import Circle
    from L20_Polimorphyzm.Square import Square
    from L20_Polimorphyzm.Triangle import Triangle
except ModuleNotFoundError:
    from Shape import Shape
    from Circle import Circle
    from Square import Square
    from Triangle import Triangle


class TestShape(unittest.TestCase):
    """Тестирование базового класса Shape."""

    def test_shape_inheritance(self):
        """Проверка, что конкретные фигуры наследуются от Shape."""
        circle = Circle(5)
        square = Square(4)
        triangle = Triangle(3, 4, 5)

        self.assertIsInstance(circle, Shape)
        self.assertIsInstance(square, Shape)
        self.assertIsInstance(triangle, Shape)


class TestCircle(unittest.TestCase):
    """Тестирование класса Circle."""

    def setUp(self):
        self.radius = 5.0
        self.circle = Circle(self.radius)

    def test_init_and_properties(self):
        """Проверка инициализации, имени и радиуса."""
        self.assertEqual(self.circle.name, "Circle")
        self.assertEqual(self.circle.radius, self.radius)

    def test_str(self):
        """Проверка строкового представления."""
        self.assertEqual(str(self.circle), f"this is Circle with {self.radius} cm.")

    def test_perimeter(self):
        """Проверка вычисления длины окружности (периметра)."""
        expected_perimeter = 2 * math.pi * self.radius
        self.assertAlmostEqual(self.circle.perimeter(), expected_perimeter, places=5)

    def test_area(self):
        """Проверка вычисления площади круга."""
        expected_area = math.pi * (self.radius ** 2)
        self.assertAlmostEqual(self.circle.area(), expected_area, places=5)

    def test_radius_setter_valid(self):
        """Проверка обновления радиуса через сеттер на корректное значение."""
        self.circle.radius = 10.0
        self.assertEqual(self.circle.radius, 10.0)
        self.assertAlmostEqual(self.circle.perimeter(), 2 * math.pi * 10.0, places=5)
        self.assertAlmostEqual(self.circle.area(), math.pi * 100.0, places=5)

    def test_radius_setter_invalid(self):
        """Проверка, что сеттер игнорирует некорректные (<= 0) значения."""
        self.circle.radius = -3
        self.assertEqual(self.circle.radius, self.radius)

        self.circle.radius = 0
        self.assertEqual(self.circle.radius, self.radius)

    def test_init_invalid_radius(self):
        """Проверка создания круга с отрицательным радиусом."""
        invalid_circle = Circle(-5)
        # Атрибут _Circle__radius не должен быть установлен
        with self.assertRaises(AttributeError):
            _ = invalid_circle.radius


class TestSquare(unittest.TestCase):
    """Тестирование класса Square."""

    def setUp(self):
        self.side = 4.0
        self.square = Square(self.side)

    def test_init_and_properties(self):
        """Проверка инициализации, имени и стороны квадрата."""
        self.assertEqual(self.square.name, "Square")
        self.assertEqual(self.square.side, self.side)

    def test_str(self):
        """Проверка строкового представления."""
        self.assertEqual(str(self.square), f"Square with side: {self.side} cm.")

    def test_perimeter(self):
        """Проверка вычисления периметра квадрата (4 * side)."""
        self.assertEqual(self.square.perimeter(), 4 * self.side)

    def test_area(self):
        """Проверка вычисления площади квадрата (side * side)."""
        self.assertEqual(self.square.area(), self.side * self.side)

    def test_side_setter_valid(self):
        """Проверка обновления стороны через сеттер."""
        self.square.side = 7.0
        self.assertEqual(self.square.side, 7.0)
        self.assertEqual(self.square.perimeter(), 28.0)
        self.assertEqual(self.square.area(), 49.0)

    def test_side_setter_invalid(self):
        """Проверка, что сеттер не принимает отрицательные или нулевые значения."""
        self.square.side = -2
        self.assertEqual(self.square.side, self.side)

        self.square.side = 0
        self.assertEqual(self.square.side, self.side)

    def test_init_invalid_side(self):
        """Проверка создания квадрата с отрицательной стороной."""
        invalid_square = Square(-4)
        # Атрибут _Square__side не должен быть установлен
        with self.assertRaises(AttributeError):
            _ = invalid_square.side


class TestTriangle(unittest.TestCase):
    """Тестирование класса Triangle."""

    def setUp(self):
        self.a, self.b, self.c = 3.0, 4.0, 5.0
        self.triangle = Triangle(self.a, self.b, self.c)

    def test_init_and_properties(self):
        """Проверка инициализации, имени и сторон треугольника."""
        self.assertEqual(self.triangle.name, "Triangle")
        self.assertEqual(self.triangle.side_of_triangle1, self.a)
        self.assertEqual(self.triangle.side_of_triangle2, self.b)
        self.assertEqual(self.triangle.side_of_triangle3, self.c)

    def test_str(self):
        """Проверка строкового представления."""
        expected_str = f"Triangle with three sides: {self.a} x {self.b} x {self.c}"
        self.assertEqual(str(self.triangle), expected_str)

    def test_perimeter(self):
        """Проверка формата и значения периметра треугольника."""
        expected_perimeter = self.a + self.b + self.c
        expected_output = f"Perimetr of triangle is {expected_perimeter:.2f} sm"
        self.assertEqual(self.triangle.perimeter(), expected_output)

    def test_area(self):
        """Проверка вычисления площади по формуле Герона."""
        p = (self.a + self.b + self.c) / 2
        s = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        expected_output = f"Square of triangle is {s:.2f} sm2"
        self.assertEqual(self.triangle.area(), expected_output)

    def test_init_invalid_line_raises_value_error(self):
        """Проверка вызова исключения при нарушении неравенства треугольника."""
        # Сумма двух сторон меньше или равна третьей (вырожденный треугольник / прямая)
        with self.assertRaises(ValueError):
            Triangle(1, 2, 5)

        with self.assertRaises(ValueError):
            Triangle(2, 2, 4)

    def test_side_setters_valid(self):
        """Проверка успешного обновления сторон через сеттеры."""
        self.triangle.side_of_triangle1 = 6.0
        self.assertEqual(self.triangle.side_of_triangle1, 6.0)

        self.triangle.side_of_triangle2 = 7.0
        self.assertEqual(self.triangle.side_of_triangle2, 7.0)

        self.triangle.side_of_triangle3 = 8.0
        self.assertEqual(self.triangle.side_of_triangle3, 8.0)

    def test_side_setters_invalid(self):
        """Проверка, что сеттеры отклоняют отрицательные значения и некорректные типы."""
        self.triangle.side_of_triangle1 = -1
        self.assertEqual(self.triangle.side_of_triangle1, self.a)

        self.triangle.side_of_triangle2 = "invalid"
        self.assertEqual(self.triangle.side_of_triangle2, self.b)

        self.triangle.side_of_triangle3 = 0
        self.assertEqual(self.triangle.side_of_triangle3, self.c)


class TestPolymorphism(unittest.TestCase):
    """Тестирование полиморфизма — ключевой концепции урока L20."""

    def test_polymorphic_iteration(self):
        """
        Проверка полиморфной обработки: различные фигуры помещаются в один список
        и обрабатываются единым образом через интерфейс Shape (perimeter() и area()).
        """
        shapes = [
            Circle(3),
            Square(5),
            Triangle(3, 4, 5)
        ]

        perimeters = []
        areas = []

        for shape in shapes:
            # Все объекты являются экземплярами Shape
            self.assertIsInstance(shape, Shape)
            # Каждый объект имеет имя
            self.assertTrue(hasattr(shape, "name"))
            # Каждый объект полиморфно реализует perimeter() и area()
            perimeters.append(shape.perimeter())
            areas.append(shape.area())

        self.assertEqual(len(perimeters), 3)
        self.assertEqual(len(areas), 3)

        # Проверка значений из полиморфного вызова
        self.assertAlmostEqual(perimeters[0], 2 * math.pi * 3, places=5)
        self.assertEqual(perimeters[1], 20)
        self.assertEqual(perimeters[2], "Perimetr of triangle is 12.00 sm")

        self.assertAlmostEqual(areas[0], math.pi * 9, places=5)
        self.assertEqual(areas[1], 25)
        self.assertEqual(areas[2], "Square of triangle is 6.00 sm2")


if __name__ == "__main__":
    unittest.main()
