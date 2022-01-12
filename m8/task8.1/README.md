# Python Essentials

Реализовать скрипт, который решает квадратное уравнение вида:
	ax^2+bx+c=0 
Параметры квадратного уравнения (𝑎, 𝑏, 𝑐) задаются вводом или через аргументы командной строки. В скрипте реализовать несколько функций, которые декомпозируют задачу решения квадратного уравнения. В эти функции должны передаваться параметры. Также на эти функций написать UnitTests.

Основной скрипт solv_square_equation.py должен иметь следующие функции:

* main()
* validate_param(int) - проверяет, что введено число, повторяет ввод 3 раза если не число (использовать exception)
* **discriminant(a, b, c)**
* **roots(d, a, b, c)**
* **solv_square(a, b, c) -> roots**
* square_print(a, b, c, roots) – выводит на экран результат
	
На выделенные написать UnitTest (discriminant, roots, solv_square).

Не использовать глобальные переменные.

\* Реализовать возврат exit_code из скрипта, в котором должна кодироваться ошибка. Количество возможных ошибок определить самостоятельно. Разрешено использовать глобальные переменные (константы), которые записываются большими буквами и слова разделены “_” (Пример: SUCCESS_EXIT=0). Эти переменные можно использовать только в методе main().

solv_square_equation.py:
```
import sys
from math import sqrt as m_sqrt
from cmath import sqrt as cm_sqrt


INVALID_INPUT_EXIT = 1
SUCCESS_EXIT = 0

def validate_param(input_str):
  for attempt in range(3):  # 3 input attempts
    try:
      return int(input_str)
    except ValueError:
      input_str = input("input a number(now)! ")
      continue
  # raise ValueError("input should be a number.")
  return None

def discriminant(a, b, c):
  return b**2 - 4*a*c

def roots(d, a, b, c):
  if a == 0:
    return None
  if d != discriminant(a, b, c):
    raise Exception("haha, cheeky one! (discriminant is wrong)")
  if d < 0: 
    sqrt = cm_sqrt  # complex roots support
  else: 
    sqrt = m_sqrt
  x1 = (-b + sqrt(d)) / (2 * a)
  x2 = (-b - sqrt(d)) / (2 * a)
  return (x1, x2)

def solv_square(a, b, c):
  d = discriminant(a, b, c)
  return roots(d, a, b, c)

def square_print(a, b, c, solution):
  print(f"Quadratic equation roots are: {solution}")

def main():
  # Equation: ax^2 + bx + c = 0
  a = validate_param(input("input a: "))
  if a in (None, 0):
    print ("a=0 makes it non-quadratic, also can't divide by zero.")
    sys.exit(INVALID_INPUT_EXIT)
  b = validate_param(input("input b: "))
  if b is None: 
    sys.exit(INVALID_INPUT_EXIT)
  c = validate_param(input("input c: "))
  if c is None: 
    sys.exit(INVALID_INPUT_EXIT)

  solution = solv_square(a, b, c)
  if solution is None:
    sys.exit(INVALID_INPUT_EXIT)
  square_print(a, b, c, solution)
  sys.exit(SUCCESS_EXIT)

if __name__ == "__main__":
	main()
	
```

![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m8/task8.1/Screenshots/1.jpg?raw=true)

![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m8/task8.1/Screenshots/2.jpg?raw=true)


solv_square_equation_test.py:

```
import unittest
import solv_square_equation

class test_solv_square_equation(unittest.TestCase):
	
	# cases for d=0; d<0; d>0
	def test_discriminant(self):
	  self.assertEqual(solv_square_equation.discriminant(0, 0, 0), 0)
	  self.assertEqual(solv_square_equation.discriminant(1, 1, 1), -3)
	  self.assertEqual(solv_square_equation.discriminant(-1, 7, 8), 81)
	
	# cases for int roots; float roots; complex roots
	def test_roots(self):
	  self.assertEqual(solv_square_equation.roots(0, 0, 0, 0), None)
	  self.assertEqual(solv_square_equation.roots(121, 3, 7, -6), (0.6666666666666666, -3.0))
	  self.assertEqual(solv_square_equation.roots(-3, 1, 1, 1), ((-0.5+0.8660254037844386j), (-0.5-0.8660254037844386j)))
	# same cases as for roots()
	def test_solv_square(self):
	  self.assertEqual(solv_square_equation.solv_square(0, 0, 0), None)
	  self.assertEqual(solv_square_equation.solv_square(3, 7, -6), (0.6666666666666666, -3.0))
	  self.assertEqual(solv_square_equation.solv_square(1, 1, 1), ((-0.5+0.8660254037844386j), (-0.5-0.8660254037844386j)))

if __name__ == "__main__":
  unittest.main()
```

![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m8/task8.1/Screenshots/3.jpg?raw=true)

