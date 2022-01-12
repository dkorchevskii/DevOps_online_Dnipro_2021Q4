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