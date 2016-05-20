# convert from cvs to xls
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),'xlwte'))
import glob
import csv
import xlwte

for csvfile in glob.glob(os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)),"StkHis"),'*.csv')):
    wb = xlwte.Workbook()
    ws = wb.add_sheet('data')
    print('Converting %s' % csvfile )
    with open(csvfile, 'rb') as f:
        reader = csv.reader(f)
        for r, row in enumerate(reader):
            for c, col in enumerate(row):
                ws.write(r, c, col)
    wb.save(csvfile.split('.c')[0] + '.xls')
    os.remove(csvfile)
