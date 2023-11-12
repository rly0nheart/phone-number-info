import argparse
import phonenumbers
from phonenumbers import carrier, geocoder

def parse_phone_number(phonenumber: str):
	parsed_number = phonenumbers.parse("+" + self.phonenumber)
	print(parsed_number)
	print(f"Network provider: {carrier.name_for_number(self.parse_phonenumber,'en')}")
	print(f"Location: {geocoder.description_for_number(self.parse_phonenumber,  'en')}")
		
	if args.output:
		with open(f"{phonenumber}.txt", "w") as file:
			file.write(
				f"{self.parse_phonenumber}\n"
				f"{carrier.name_for_number(self.parse_phonenumber,'en')}\n"
				f"{geocoder.description_for_number(self.parse_phonenumber,  'en')}"
			)
		

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Simple script to get phone number information.")
	parser.add_argument("phonenumber", help="target phone number")
	parser.add_argument("-o","--output", help="save results to a file", action="store_true")
	args = parser.parse_args()
	try:
		parse_phone_number(phonenumber=args.phonenumber)
	except Exception as e:
		print(f"An error occurred: {e}")
