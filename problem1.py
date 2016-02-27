def sumOfAllMultiplicant(limit):
	countOfThree = (limit-1)/3
	countOfFive = (limit-1)/5
	countOfFiften = (limit-1)/15
	sumOfThree = 3*(countOfThree*(countOfThree+1))/2
	sumOfFive = 5*(countOfFive*(countOfFive+1))/2
	sumOfFiften = 15*(countOfFiften*(countOfFiften+1))/2
	return  sumOfThree+sumOfFive - sumOfFiften 


print sumOfAllMultiplicant(1000)