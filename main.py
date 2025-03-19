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
	
	with open(input, "r") as f:
		data = f.read().strip().split("\n")
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
    classes     - Classes to apply to whole table (default is 'wikitable sortable')
    style       - Style to apply to the whole table
    headerstyle - Style to apply to the header row
    cellstyle   - Style to apply to each cell
    rowstyle    - Style to apply to each row
    alternate   - Style for every other row (switches with rowstyle or default)
    rotate      - Transpose (top left stays put, rows become columns and vice versa)
"""


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


