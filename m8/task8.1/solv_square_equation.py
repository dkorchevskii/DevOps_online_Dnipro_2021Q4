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
	
