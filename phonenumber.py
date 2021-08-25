#!/usr/bin/env python3

# Import modules
import argparse
import phonenumbers
from phonenumbers import carrier, geocoder

class Details:
	def __init__(self,phonenumber):
		# Parsing phone number
		self.parse_phonenumber = phonenumbers.parse("+"+phonenumber)
		
	def main(self,phonenumber):
		print(self.parse_phonenumber)
		print(f"Network provider: {carrier.name_for_number(self.parse_phonenumber,'en')}")
		print(f"Location: {geocoder.description_for_number(self.parse_phonenumber,  'en')}")
		
		# Saving results to a text file
		if args.output:
			with open(f"{phonenumber}.txt", "w") as file:
				file.write(f"{self.parse_phonenumber}\n{carrier.name_for_number(self.parse_phonenumber,'en')}\n{geocoder.description_for_number(self.parse_phonenumber,  'en')}")
		
if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Get phone number details")
	parser.add_argument("phonenumber", help="target phone number")
	parser.add_argument("-O","--output-results",help="save results to a file",dest="output",action="store_true")
	args = parser.parse_args()
	phonenumber = args.phonenumber
	output = args.output
	try:
		Details(phonenumber).main(phonenumber)
		
	except Exception as e:
		print(e)
