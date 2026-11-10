import csv
from pathlib import Path

def read_csv(file_path):
    records = []
    '''
    Opens the CSV for reading:
     - 'r' made for reading
     - newline='' lets the file to handle line endings
     - encoding= specifies the character encoding of the file
    '''
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        # Reads each CSV row as a dictionary using the headers as keys
        reader = csv.DictReader(file)
        for row in reader:
            records.append(row)

        return records

def main():
    file_path = Path('data/sample_sales.csv')
    records = read_csv(file_path)

    print('DataPipeline - CSV Reader')
    print('-------------------------')

    for record in records:
        print(record)

    print(f'\nTotal records: {len(records)}')

if __name__ == '__main__':
    main()

