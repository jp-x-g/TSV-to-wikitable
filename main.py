#! /usr/bin/python
# -*- coding: utf-8 -*-
# JPxG, 2023 January 14
# Takes a TSV as input and outputs a simple, sortable wikitable.
import sys
import os

def convert(input="input.txt", output="output.txt"):
	
	f = open(input, "r")
	data = f.read()
	f.close()
	
	
	# For processing words only. Converts linebreaks to spaces and strips all alphanumerics.
	data_len = len(data)
	# This should make it do words instead of letters.
	data = data.split("\n")
	
	print("Processing input: " + str(data_len) + " chars" + ", " + str(len(data)) + " items")
	
	#time.sleep(2)
		
	columns = len(data[0].split("\t"))
	
	stringy  = '{|class="wikitable sortable"\n'
	for n in range(0,columns):
		stringy += f'! {str(n)}\n'

	stringy += "|-\n"
	
	for item in data:
		items = item.split("\t")
		strangy = "|-\n"
		for thing in items:
			strangy += f"| {thing.strip()}\n"
		stringy += strangy

	stringy += "|}"

	print(stringy)
	
	f = open(output, "w")
	f.write(str(stringy))
	f.close()
	print("")
	print(f"Saved to: {output}")
	exit()

if (__name__ == "__main__"):
	print("TSV to Wikitable V1.0, JPxG January 2023")

	if len(sys.argv) == 1:
		convert()
		exit()
	else:
		if (sys.argv[1] == "-h") or (sys.argv[1] == "--help") or (sys.argv[1] == "help"):
			print("> convert(input_file, output_file)")
			print("  Converts input file to Wikitable.")
			print("  Defaults are input.txt and output.txt.")
			print("  Usage should be like this:")
			print("   python3 main.py uglytext.txt nicetable.txt")
			print("")
			exit()
		else:
			if len(sys.argv) == 2:
				convert(str(sys.argv[1]))
				exit()
			if len(sys.argv) == 3:
				convert(str(sys.argv[1]), str(sys.argv[2]))
				exit()
			print("Error: too many arguments provided.")
			print("")
			print("> convert(input_file, output_file)")
			print("  Converts input file to Wikitable.")
			print("  Defaults are input.txt and output.txt.")
			print("  Usage should be like this:")
			print("   python3 main.py uglytext.txt nicetable.txt")
			print("")
			exit()


