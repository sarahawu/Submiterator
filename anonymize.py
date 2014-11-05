#!/usr/bin/env python

import csv
import sys

workers = {}
def symb(workerid):
	if workerid in workers:
		return workers[workerid]
	else:
		id_number = str(len(workers))
		workers[workerid] = id_number
		return id_number

original_data_filename = sys.argv[1]
new_data_filename = original_data_filename.split(".results")[0] + "_anonymized.results"
new_rows = []

with open(original_data_filename, "rb") as csvfile:
	csvreader = csv.reader(csvfile, delimiter="\t")
	is_header = True
	workerIndex = 0
	for row in csvreader:
		if is_header:
			workerIndex = row.index("workerid")
			is_header = False
		else:
			row[workerIndex] = symb(row[workerIndex])
		new_rows.append("\t".join(row))

w = open(new_data_filename, "w")
w.write("\n".join(new_rows))
w.close()

print workers