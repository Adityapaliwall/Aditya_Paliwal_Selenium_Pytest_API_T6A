import openpyxl

def test_fun1():
    wb = openpyxl.load_workbook('../sample.xlsx')
    ws = wb["sheet1"]

    data = []
    for row in ws.iter_rows(min_row=2 ,values_only=True):
        data.append(row)

    return data