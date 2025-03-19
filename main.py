#! /usr/bin/python
# -*- coding: utf-8 -*-
# JPxG, 2023 January 14
# Takes a TSV as input and outputs a simple, sortable wikitable.
import sys
import os

def convert(
	inputtext   = None,
	output      = None,
	rotate      = False,
	classes     = "wikitable sortable",
	attrs       = None,
	headerattrs = None,
	rowattrs    = None,
	altattrs    = None
	):
	
	data = inputtext.strip().split("\n")
	if not data:
		print("Error: Couldn't read data.")
		return "Error: Couldn't read data."

	table_data = [row.split("\t") for row in data]

	#if rotate:
	#	table_data = list(map(list, zip(*table_data)))  # Transpose table
	rows, cols = len(table_data), len(table_data[0])
	if rotate:
		data = [[table_data[row][col] for row in range(rows)] for col in range(cols)]
		cols, rows = rows, cols

	print(f"Processing input: {rows} rows of {cols} columns.")
	
	stringy  = '{|class="wikitable sortable"\n'
	for n in range(0,len(table_data[0])):
		stringy += f'! {str(n)}\n'

	stringy += "|-\n"
	
	for item in data:
		items = item.split("\t")
		strangy = "|-\n"
		for thing in items:
			strangy += f"| {thing.strip()}\n"
		stringy += strangy

	stringy += "|}"

	#print(stringy)
	
	if output is not None:
		f = open(output, "w")
		f.write(str(stringy))
		f.close()
		print("")
		print(f"Saved to: {output}")
		exit()

if (__name__ == "__main__"):
	print("TSV to Wikitable V2.0, JPxG March 2025")

	helpstring = """
    convert(input_file, output_file, classes, style, headerstyle, cellstyle, rotate)
Converts input file to Wikitable.
Each row of the TSV (linebreak-separated) will be a row of the table.
Defaults are input.txt and output.txt.
Usage should be like this:
    python3 main.py uglytext.txt nicetable.txt

If calling convert(), there are optional additional keyword arguments:
    rotate      - Transpose (top left stays put, rows become cols & vice versa)
    classes     - Classes to apply to whole table (default 'wikitable sortable')
    attrs       - Attribute string, of any sort, to apply to the whole table
                  (e.g. "style="hoomba: baroomba;" baba="booey"")
    headerattrs - Same, but to apply to each cell in the header row
    rowattrs    - Or to apply to each row of the rest of the table
    altattrs    - Or to every-other-row (alternates with rowattrs or default)
"""


	if len(sys.argv) == 1:
		with open("input.txt", "r") as f:
			data = f.read()
		convert(data, "output.txt")
		exit()
	else:
		if (sys.argv[1] == "-h") or (sys.argv[1] == "--help") or (sys.argv[1] == "help"):
			print(helpstring)
			exit()
		else:
			if len(sys.argv) == 2:
				with open(str(sys.argv[1]), "r") as f:
					data = f.read()
				convert(data, "output.txt")
				exit()
			if len(sys.argv) == 3:
				with open(str(sys.argv[1]), "r") as f:
					data = f.read()
				convert(data, str(sys.argv[2]))
				exit()
			print("Error: too many arguments provided.")
			print(helpstring)
			exit()


