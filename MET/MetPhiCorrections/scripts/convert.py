import json
import gzip
import sys

args = sys.argv

if len(args)<3: 
    print("Please provide additional arguments \n"\
          "python convert.py outfile.json.gz input1.json.gz input2.json.gz ...")
    
output_file = args[1]
input_files = args[2:]

data = []

filestring = ''

# Load JSON data from the input file
for infile in input_files:
    with gzip.open(infile, 'rt', encoding='utf-8') as f:
        data.append(json.load(f))
    filestring += infile + ' '


data[0]['description'] = 'Merged from ' + filestring

for i in range(len(data)-1):
    data[0]['corrections'] += data[i+1]['corrections']

# Write JSON data to a gzipped file
with gzip.open(output_file, 'wt', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f'Conversion from to {output_file} completed.')