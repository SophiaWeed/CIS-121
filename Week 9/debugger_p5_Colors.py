class ColorRGB:
	def __init__(self,_red, _green, _blue):
		self.red = _red
		self.green = _green
		self.blue = _blue
	
	def get_red(self):
		return self.red
	
	def set_red(self, red):
		self.red = red
	
	def get_green(self):
		return self.green
	
	def set_green(self, green):
		self.green = green
	
	def get_blue(self):
		return self.blue
	
	def set_blue(self, blue):
		self.blue = blue
	
	def to_grayscale(self):
		return 0.5 * self.red + 0.59 * self.green + 0.11 * self.blue
	
colors = ColorRGB(0.5,0.7,0.1)
Nathan = ColorRGB(0.0,0.1,0.7)
Sophia = ColorRGB(0.4,0.5,0.1)

print(ColorRGB.to_greyscale())

colors.set_blue(0)
colors.set_red(0)
colors.set_green(0)

print(colors.get_red())
print(colors.get_blue())
print(colors.get_green())

