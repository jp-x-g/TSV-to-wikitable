#! /usr/bin/python
# -*- coding: utf-8 -*-
# JPxG, 2023 January 14
# Takes a TSV as input and outputs a simple, sortable wikitable.
import sys
import os

def convert(
	input       = "input.txt",
	output      = "output.txt",
	classes     = "wikitable sortable",
	style       = None,
	headerstyle = None,
	cellstyle   = None,
	rotate      = False
	):
	
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

	helpstring = "";
	helpstring += "\nconvert(input_file, output_file, classes, style, headerstyle, cellstyle, rotate)"
	helpstring += "\n    Converts input file to Wikitable."
	helpstring += "\n    Each row of the TSV (linebreak-separated) will be a row of the table."
	helpstring += "\n    Defaults are input.txt and output.txt."
	helpstring += "\n    Usage should be like this:"
	helpstring += "\npython3 main.py uglytext.txt nicetable.txt"
	helpstring += "\n"
	helpstring += "\n    If calling convert(), there are optional additional keyword arguments:"
	helpstring += "\nclasses     - Classes to apply to whole table (default is 'wikitable sortable')"
	helpstring += "\nstyle       - Style to apply to the whole table"
	helpstring += "\nheaderstyle - Style to apply to the header row"
	helpstring += "\ncellstyle   - Style to apply to each cell"
	helpstring += "\nrowstyle    - Style to apply to each row"
	helpstring += "\nalternate   - Style for every other row (switches with rowstyle or default)"
	helpstring += "\nrotate      - Transpose (top left stays put, rows become columns and vice versa)"


	if len(sys.argv) == 1:
		convert()
		exit()
	else:
		if (sys.argv[1] == "-h") or (sys.argv[1] == "--help") or (sys.argv[1] == "help"):
			print(helpstring)
			exit()
		else:
			if len(sys.argv) == 2:
				convert(str(sys.argv[1]))
				exit()
			if len(sys.argv) == 3:
				convert(str(sys.argv[1]), str(sys.argv[2]))
				exit()
			print("Error: too many arguments provided.")
			print(helpstring)
			exit()


