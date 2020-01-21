#!/usr/bin/python3

import to_do_list_functions as tdl

if __name__ == '__main__':
	import sys
	to_do_list = tdl.initialize_list()
	while True:
		selection = input("U: Continue \nQ: Quit\n").lower()
		if selection == "q":
			print("Quitting")
			sys.exit()
		if selection == "u":
			tdl.to_do_list_main(to_do_list)
