
import unittest
import main


class TestCalculator(unittest.TestCase):
	
	def setUp(self):
		main.app.testing = True
		self.app = main.app.test_client()

	def test_add1(self):
		#case 1, A is n integer B is an integer
		solution = self.app.get('/add?A=18&B=4')
		self.assertEqual(b'22.0', solution.data)

	def test_add2(self):

		#case 2, A is rational number and B is rational number p/q form
		solution = self.app.get('/add?A=3/4&B=1/4')
		self.assertEqual(b'1.0', solution.data)

	def test_add3(self):

		#case 3, A is a float and B is a float
		solution = self.app.get('/add?A=125.33&B=2.007')
		self.assertEqual(b'127.337', solution.data)

	def test_add4(self):

		#case 4, when A is float and B is integer
		solution = self.app.get('/add?A=23.333&B=89')
		self.assertEqual(b'112.333', solution.data)

	def test_add5(self):

		#case 5, when A is integer and B is float
		solution = self.app.get('/add?A=125&B=69.9')
		self.assertEqual(b'194.9', solution.data)

	def test_add6(self):

		#case 6, when A is fraction p/q and B is an integer
		solution = self.app.get('/add?A=1/4&B=55')
		self.assertEqual(b'55.25', solution.data)

	def test_add7(self):

		#case 7, when A is an integer and B is a fraction p/q
		solution = self.app.get('/add?A=80&B=5/10')
		self.assertEqual(b'80.5', solution.data)

	def test_add8(self):

		#case 8, when A input is an alphabet(non integer) and B is integer
		solution = self.app.get('/add?A=slice&B=33')
		self.assertEqual(b'33.0', solution.data)#non integer type considered as not valid , in this case which is zero

	def test_add9(self):

		#case 9, when A input is an integer and B input is an alphabet
		solution = self.app.get('/add?A=44&B=rock')
		self.assertEqual(b'44.0', solution.data)
		#when one input is alphabet and other input be any number, whether rational , integer, fraction ultimately the result will be the input which was an integer

	def test_add10(self):

		#case 10, when A input is of the form p/q where q=0 and B input be any number
		solution = self.app.get('add?A=5/0&B=4')
		self.assertEqual(b"None", solution.data)
		#according to the script if q=0 in p/q form then it should display an error but it is resolved using zerodivision module 

	def test_add11(self):

		#case 11, when A input is any number and B=p/q form where q=0
		solution = self.app.get('add?A=18&B=5/0')
		self.assertEqual(b"None", solution.data)

	def test_sub1(self):
		#case 1, A is n integer B is an integer
		solution = self.app.get('/sub?A=4&B=3')
		self.assertEqual(b'1.0', solution.data)

	def test_sub2(self):

		#case 2, A is rational number and B is rational number p/q form
		solution = self.app.get('/sub?A=3/4&B=1/4')
		self.assertEqual(b'0.5', solution.data)

	def test_sub3(self):

		#case 3, A is a float and B is a float
		solution = self.app.get('/sub?A=8.5&B=2.005')
		self.assertEqual(b'6.495', solution.data)

	def test_sub4(self):

		#case 4, when A is float and B is integer
		solution = self.app.get('/sub?A=44.444&B=4')
		self.assertEqual(b'40.444', solution.data)

	def test_sub5(self):

		#case 5, when A is integer and B is float
		solution = self.app.get('/sub?A=12&B=1.111')
		self.assertEqual(b'10.889', solution.data)

	def test_sub6(self):

		#case 6, when A is fraction p/q and B is an integer
		solution = self.app.get('/sub?A=1/4&B=12')
		self.assertEqual(b'-11.75', solution.data)

	def test_sub7(self):

		#case 7, when A is an integer and B is a fraction p/q
		solution = self.app.get('/sub?A=3&B=2/10')
		self.assertEqual(b'2.8', solution.data)

	def test_sub8(self):

		#case 8, when A input is an alphabet(non integer) and B is integer
		solution = self.app.get('/sub?A=good&B=10')
		self.assertEqual(b'-10.0', solution.data)#non integer type considered as not valid , which is zero

	def test_sub9(self):

		#case 9, when A input is an integer and B input is an alphabet
		solution = self.app.get('/sub?A=22&B=rock')
		self.assertEqual(b'22.0', solution.data)
		#when one input is alphabet and other input be any number, whether rational , integer, fraction ultimately the result will be the input which was an integer

	def test_sub10(self):

		#case 10, when A input is of the form p/q where q=0 and B input be any number
		solution = self.app.get('sub?A=1/0&B=2')
		self.assertEqual(b"None", solution.data)
		#according to the script if q=0 in p/q form then it should display an error

	def test_sub11(self):

		#case 11, when A input is any number and B=p/q form where q=0
		solution = self.app.get('sub?A=12&B=2/0')
		self.assertEqual(b"None", solution.data)

	def test_mul1(self):
		#case 1, A is n integer B is an integer
		solution = self.app.get('/mul?A=33&B=3')
		self.assertEqual(b'99.0', solution.data)

	def test_mul2(self):

		#case 2, A is rational number and B is rational number p/q form
		solution = self.app.get('/mul?A=7/2&B=2/6')
		self.assertEqual(b'1.1666666666666667', solution.data)

	def test_mul3(self):

		#case 3, A is a float and B is a float
		solution = self.app.get('/mul?A=0.9&B=10.12')
		self.assertEqual(b'9.108', solution.data)

	def test_mul4(self):

		#case 4, when A is float and B is integer
		solution = self.app.get('/mul?A=22.22&B=2')
		self.assertEqual(b'44.44', solution.data)

	def test_mul5(self):

		#case 5, when A is integer and B is float
		solution = self.app.get('/mul?A=10&B=9.9')
		self.assertEqual(b'99.0', solution.data)

	def test_mul6(self):

		#case 6, when A is fraction p/q and B is an integer
		solution = self.app.get('/mul?A=11.22&B=1')
		self.assertEqual(b'11.22', solution.data)

	def test_mul7(self):

		#case 7, when A is an integer and B is a fraction p/q
		solution = self.app.get('/mul?A=1&B=4/9')
		self.assertEqual(b'0.4444444444444444', solution.data)

	def test_mul8(self):

		#case 8, when A input is an alphabet(non integer) and B is integer
		solution = self.app.get('/mul?A=rock&B=22')
		self.assertEqual(b'0.0', solution.data)#non integer type considered as not valid , in this case which is zero

	def test_mul9(self):

		#case 9, when A input is an integer and B input is an alphabet
		solution = self.app.get('/mul?A=22&B=rock')
		self.assertEqual(b'0.0', solution.data)
		#when one input is alphabet and other input be any number, whether rational , integer, fraction ultimately the result will be the input which was an integer

	def test_mul10(self):

		#case 10, when A input is of the form p/q where q=0 and B input be any number
		solution = self.app.get('mul?A=1/0&B=2')
		self.assertEqual(b"None", solution.data)
		#according to the script if q=0 in p/q form then it should display an error but it is resolved using zerodivision module

	def test_mul11(self):

		#case 11, when A input is any number and B=p/q form where q=0
		solution = self.app.get('mul?A=12&B=2/0')
		self.assertEqual(b"None", solution.data)

	def test_div1(self):
		#case 1, A is n integer B is an integer
		solution = self.app.get('/div?A=10&B=2')
		self.assertEqual(b'5.0', solution.data)

	def test_div2(self):

		#case 2, A is rational number and B is rational number p/q form
		solution = self.app.get('/div?A=3/2&B=1/2')
		self.assertEqual(b'3.0', solution.data)

	def test_div3(self):

		#case 3, A is a float and B is a float
		solution = self.app.get('/div?A=0.89&B=12.22')
		self.assertEqual(b'0.07283142389525368', solution.data)

	def test_div4(self):

		#case 4, when A is float and B is integer
		solution = self.app.get('/div?A=22.22&B=22')
		self.assertEqual(b'1.01', solution.data)

	def test_div5(self):

		#case 5, when A is integer and B is float
		solution = self.app.get('/div?A=10&B=1.1')
		self.assertEqual(b'9.090909090909092', solution.data)

	def test_div6(self):

		#case 6, when A is fraction p/q and B is an integer
		solution = self.app.get('/div?A=12&B=1')
		self.assertEqual(b'12.0', solution.data)

	def test_div7(self):

		#case 7, when A is an integer and B is a fraction p/q
		solution = self.app.get('/div?A=12&B=2/3')
		self.assertEqual(b'18.0', solution.data)

	def test_div8(self):

		#case 8, when A input is an alphabet(non integer) and B is integer
		solution = self.app.get('/div?A=rock&B=12')
		self.assertEqual(b'0.0', solution.data)#non integer type considered as not valid , in this case which is zero

	def test_div9(self):

		#case 9, when A input is an integer and B input is an alphabet
		solution = self.app.get('/div?A=22&B=rock')
		self.assertEqual(b'None', solution.data)
		#when one input is alphabet and other input be any number, whether rational , integer, fraction ultimately the result will be the input which was an integer

	def test_div10(self):

		#case 10, when A input is of the form p/q where q=0 and B input be any number
		solution = self.app.get('div?A=1/0&B=2')
		self.assertEqual(b'None', solution.data)
		#according to the script if q=0 in p/q form then it should display an error

	def test_div11(self):

		#case 11, when A input is any number and B=p/q form where q=0
		solution = self.app.get('div?A=12&B=2/0')
		self.assertEqual(b'None', solution.data)


if __name__ == '__main__':
	unittest.main()