import csv

with open('mei.ext_index.txt') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    next(reader, None)  # skip the header line
    # Your code goes here!


def enso_classification(year):
    classification = ''
    intensity = ''

    # Your code goes here!

    return classification, intensity
