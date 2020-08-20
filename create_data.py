import csv

new_file = open('training/basic/scatter/data_result.csv', 'w', encoding='utf-8')
csv_writer = csv.writer(new_file)

with open('test_results.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        line = []
        # keep echart format
        line.append('['+row[1])
        line.append(row[2]+']')
        line.append('')
        csv_writer.writerow(line)