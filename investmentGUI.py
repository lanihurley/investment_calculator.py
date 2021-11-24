"""
Program: investmentGUI.py
Author: Lani Hurley 11/15/2021

Compute an investment report that takes input from the user and displays the investment summary in tabular format along with the totals.
*** Note: the file breezypythongui.py MUST be in the same directory as the file for the application to work.***
"""

from breezypythongui import EasyFrame
from tkinter.font import Font

class TextAreaDemo(EasyFrame):
	"""An investment calculator that demonstrates the use of a multi-line text area widget."""

	def __init__(self):
		"""Sets the window and the widgets."""
		EasyFrame.__init__(self, title = "INVESTMENT CALCULATOR", background = "steelblue")
		self.addLabel(text = "Initial Amount", row = 0, column = 0, background = "steelblue", font = Font(family = "courier new", size = 11))
		self.addLabel(text = "Number of Years", row = 1, column = 0, background = "steelblue",  font = Font(family = "courier new", size = 11))
		self.addLabel(text = "Interest Rate in %", row = 2, column = 0, background = "steelblue",  font = Font(family = "courier new", size = 11))
		self.amount = self.addFloatField(value = 0.0, row = 0, column = 1)
		self.period = self.addIntegerField(value = 0, row = 1, column = 1)
		self.rate = self.addIntegerField(value = 0, row = 2, column = 1)
		self.outputArea = self.addTextArea(text = "", row = 4, column = 0, columnspan = 2, width = 50, height = 15)
		self.button = self.addButton(text = "Compute", row = 3, column = 0, columnspan = 2, command = self.compute) 
		# change that button color!
		self.button["background"] = "orange"
		self.button["padx"] = "10"
		self.button["pady"] = "5"

	# Event handling method
	def compute(self):
		"""Computes the investment schedule based on the inputs and outputs the full report"""
		# Obtain and validate the input
		startBalance = self.amount.getNumber()
		years = self.period.getNumber()
		rate = self.rate.getNumber()

		# If any of the inputs are a zero, just exit the function
		if startBalance == 0 or rate == 0 or years == 0:
			self.outputArea["state"] = "normal"
			self.outputArea.setText("Please make sure that no inputs \ncontain a ZERO!")
			self.outputArea["state"] = "disabled"
			return 
		# calculation phase 
		# convert the rate to a decimal number
		rate = rate / 100

		#Initialize the accumulator for the interest
		totalInterest = 0.0

		# Displays the header for the table in tabular notation
		result = "%4s%18s%10s%16s\n" % ("Year", "Starting Balance", "Interest", "Ending Balance")
		

		# Compute and append the results for each year
		for year in range(1, years + 1):
			interest = startBalance * rate
			endBalance = startBalance + interest
			result += "%4d%18.2f%10.2f%16.2f\n" % (year, startBalance, interest, endBalance)
			startBalance = endBalance
			totalInterest += interest 

		# Append the totals to the result string for the entire report
		result += "Ending balance: $%0.2f\n" % endBalance
		result += "Total interest earned: $%0.2f\n" % totalInterest

		# Output the result while preserving read-only status
		self.outputArea["state"] = "normal"
		self.outputArea.setText(result)
		self.outputArea["state"] = "disabled"
		self.outputArea["fg"] = "indigo"

# definition of the main() function for program entry
def main():
	"""Instantiates and pops up the window."""
	TextAreaDemo().mainloop()

# global call to trigger the main() function
if __name__ == "__main__":
	main()
