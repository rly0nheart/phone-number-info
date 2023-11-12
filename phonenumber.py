import argparse

import phonenumbers
from phonenumbers import carrier, geocoder
from rich.markdown import Markdown
from rich_argparse import RichHelpFormatter


def parse_phonenumber(phonenumber: str):
    parsed_phonenumber = phonenumbers.parse("+" + phonenumber)
    print(f"[+] {parsed_phonenumber}")
    print(f"[+] Network provider: {carrier.name_for_number(parsed_phonenumber,'en')}")
    print(f"[+] Location: {geocoder.description_for_number(parsed_phonenumber,  'en')}")

    if args.output:
        with open(f"{phonenumber}.txt", "w") as file:
            file.write(
                f"{parsed_phonenumber}\n"
                f"{carrier.name_for_number(parsed_phonenumber,'en')}\n"
                f"{geocoder.description_for_number(parsed_phonenumber,  'en')}"
            )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=Markdown(
            """
# Phone Number Info
> Simple script to get phone number information.""",
            style="argparse.text",
        ),
        epilog=Markdown(
            """
# by [Richard Mwewa](https://about.me/rly0nheart)
```
MIT License

Copyright (c) 2021-2023 Richard Mwewa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```"""
        ),
        formatter_class=RichHelpFormatter,
    )
    parser.add_argument("phonenumber", help="target phone number")
    parser.add_argument(
        "-o", "--output", help="save results to a file", action="store_true"
    )
    args = parser.parse_args()
    try:
        print(
            """
┏┓┓         ┳┓     ┓       ┳  ┏  
┃┃┣┓┏┓┏┓┏┓  ┃┃┓┏┏┳┓┣┓┏┓┏┓  ┃┏┓╋┏┓
┣┛┛┗┗┛┛┗┗   ┛┗┗┻┛┗┗┗┛┗ ┛   ┻┛┗┛┗┛"""
        )
        parse_phonenumber(phonenumber=args.phonenumber)
    except Exception as e:
        print(f"An error occurred: {e}")
