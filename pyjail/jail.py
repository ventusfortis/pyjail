#!/bin/python3
GREEN = '\033[92m'
WARNING = '\033[93m'
ERROR = '\033[91m'
ENDC = '\033[0m'

def main():
	text = input('>>> ')
	for keyword in ['eval', 'exec', 'import', 'open', 'os', 'read', 'system', 'write', 'subprocess']:
		if keyword in text:
			print(f"{ERROR}Nope, {WARNING}{keyword}{ERROR} is banned!{ENDC}")
			return
	exec(text)
	return


if __name__ == "__main__":
	print(f"{WARNING}Hi and welcome the most secure python console! Enter your commands.{ENDC}")
	print('-' * 80)
	while 1:
		try:
			main()
		except Exception as e:
			print(f"Oops, something broke: \n{ERROR}{e}{ENDC}")

