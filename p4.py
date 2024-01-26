#using the class Pokemon as a model

class Favorite_animal:

	

	def __init__(self,name,length_of_arms,length_of_legs,number_of_eyes,has_a_tail,is_furry):
		self.name = name
		self.length_of_arms = length_of_arms
		self.length_of_legs = length_of_legs
		self.number_of_eyes = number_of_eyes
		self.has_a_tail = has_a_tail
		self.is_furry = is_furry 

#import the class


from animalclass import Favorite_animal
def main():
    Bear = Favorite_animal('Bear', length_of_arms = 0, length_of_legs = 35.5, number_of_eyes = 2, has_a_tail = True, is_furry = True)

    print('My favorite animal is a', Bear.name)
    print('Length of Arms:', Bear.length_of_arms)
    print('Length of Legs:', Bear.length_of_legs, 'inches')
    print('Number of Eyes:', Bear.number_of_eyes)
    print('Has a tail:', Bear.has_a_tail)
    print('Is furry:', Bear.is_furry)

if __name__ == '__main__':
    main()
    
