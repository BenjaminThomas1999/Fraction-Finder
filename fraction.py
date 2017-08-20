import time

class Fraction:
	def __init__(self, num = 1, denom = 1):
		self.num = num
		self.denom = denom
	def value(self):
		return self.num/self.denom
	def show(self):
		print("\n"+ str(self.num) +"\n— = "+str(self.value())+"\n" + str(self.denom))
		
		
def findRationalFraction(target):
	trialFraction = Fraction()
	closest = Fraction()
	print("Ctrl-C to stop")
	
	#~ smallestDiff = float('inf')
	
	while trialFraction.value() != target:
		if trialFraction.value() < target:
			trialFraction.num += 1
		elif trialFraction.value() > target:
			trialFraction.denom += 1
		
		#~ if abs(trialFraction.value()-target) < smallestDiff:
			#~ closest = Fraction(trialFraction.num, trialFraction.denom)
			#~ closest.show()
			#~ smallestDiff = abs(trialFraction.value()-target)
			
			
	return trialFraction
	
findRationalFraction(float(input("Enter number to rationalise: "))).show()