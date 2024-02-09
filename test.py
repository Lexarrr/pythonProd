import pymysql as pyms

connection = pyms.connect(host='172.20.10.13', user='obmen', password='123456', database='bank', port=3306)
cursor = connection.cursor()
cursor.execute('ALTER TABLE bank.valute_rate MODIFY COLUMN rate varchar(10) CHARACTER SET latin1 COLLATE latin1_swedish DEFAULT NULL NULL')

data = cursor.fetchall()

print(data)
