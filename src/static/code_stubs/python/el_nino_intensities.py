import csv

with open('mei.ext_index.txt') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    next(reader, None)  # skip the header line
    # Your code goes here!


def enso_classification(two_year_period):
    classification = ''
    intensity = ''
    mei = 0.0

    # Your code goes here!

    return classification, intensity, mei
