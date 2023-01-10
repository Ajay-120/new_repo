import mysql.connector
import xlrd
conn=mysql.connector.connect(host="localhost",user="root",passwd="root",database="portfolioproject")
cur=conn.cursor()
loc=("C:\\Users\\ajay\\Downloads\\CovidDeaths.xlsx")
a=xlrd.open_workbook(loc)
l=list()
sheet=a.sheet_by_index(0)
sheet.cell_value(0,0)
for i in range(1,85172):
    l.append(tuple(sheet.row_values(i)))
cur.execute(l)
conn.commit()
conn.close()
