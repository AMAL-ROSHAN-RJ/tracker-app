import csv

def export_rows(rows, path):
    with open(path, 'w') as f:
        csv.writer(f).writerows(rows)
