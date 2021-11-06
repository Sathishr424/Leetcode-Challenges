from test import Test

prices = {
"Strawberries" : "$1.50",
"Banana" : "$0.50",
"Mango" : "$2.50",
"Blueberries" : "$1.00",
"Raspberries" : "$1.00",
"Apple" : "$1.75",
"Pineapple" : "$3.50"
}

class Smoothie:
	# Write code here!
	def __init__(self, ingred):
		self.ingredients = ingred
	
	def intToDollers(self, x):
		if len(str(round(x,2))) == 3: return '$' + str(round(x,2)) + '0'
		return '$' + str(round(x,2))
	
	def get_cost(self):
		ret = 0
		for i in self.ingredients:
			ret+=float(prices.get(i)[1:])
		return self.intToDollers(ret)
		
	def get_price(self):
		tmp = float(self.get_cost()[1:])
		ret = tmp+(tmp*1.5)
		return self.intToDollers(ret)
		
	def get_name(self):
		tmp = self.ingredients
		tmp.sort()
		ret = ''
		for i in tmp:
			if i[-7:] == 'berries':
				ret+=i[:-7]+'berry '
			else: ret+=i + ' '
		if len(tmp) > 1:
			return ret + 'Fusion'
		return ret + 'Smoothie'
			
		
s1 = Smoothie(['Banana'])
s2 = Smoothie(['Raspberries', 'Strawberries', 'Blueberries'])
s3 = Smoothie(['Mango', 'Apple', 'Pineapple'])
s4 = Smoothie(['Pineapple', 'Strawberries', 'Blueberries', 'Mango'])
s5 = Smoothie(['Blueberries'])

print(s1.get_cost())

Test.assert_equals(s1.ingredients, ['Banana'])
Test.assert_equals(s1.get_cost(), '$0.50')
Test.assert_equals(s1.get_price(), '$1.25')
Test.assert_equals(s1.get_name(), 'Banana Smoothie')
Test.assert_equals(s2.ingredients, ['Raspberries', 'Strawberries', 'Blueberries'])
Test.assert_equals(s2.get_cost(), '$3.50')
Test.assert_equals(s2.get_price(), '$8.75')
Test.assert_equals(s2.get_name(), 'Blueberry Raspberry Strawberry Fusion')
Test.assert_equals(s3.ingredients, ['Mango', 'Apple', 'Pineapple'])
Test.assert_equals(s3.get_cost(), '$7.75')
Test.assert_equals(s3.get_price(), '$19.38')
Test.assert_equals(s3.get_name(), 'Apple Mango Pineapple Fusion')
Test.assert_equals(s4.ingredients, ['Pineapple', 'Strawberries', 'Blueberries', 'Mango'])
Test.assert_equals(s4.get_cost(), '$8.50')
Test.assert_equals(s4.get_price(), '$21.25')
Test.assert_equals(s4.get_name(), 'Blueberry Mango Pineapple Strawberry Fusion')
Test.assert_equals(s5.ingredients, ['Blueberries'])
Test.assert_equals(s5.get_cost(), '$1.00')
Test.assert_equals(s5.get_price(), '$2.50')
Test.assert_equals(s5.get_name(), 'Blueberry Smoothie')
			
