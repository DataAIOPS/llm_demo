import sqlite3

conn = sqlite3.connect('llm_demo.db')

cursor = conn.cursor()

#create a table
table ="""CREATE TABLE llm_demo(River_Name VARCHAR(255), Length_km INTEGER, 
Origin VARCHAR(255), Mouth VARCHAR(255), States_Flowing_Through VARCHAR(255));"""

cursor.execute(table)

cursor.execute('''
    INSERT INTO llm_demo (River_Name, Length_km, Origin, Mouth, States_Flowing_Through) VALUES
        ('Ganga', 2525, 'Gangotri Glacier', 'Bay of Bengal', 'Uttarakhand, Uttar Pradesh, Bihar, Jharkhand, West Bengal'),
        ('Yamuna', 1376, 'Yamunotri Glacier', 'Ganga at Allahabad', 'Uttarakhand, Haryana, Delhi, Uttar Pradesh'),
        ('Godavari', 1465, 'Triambakeshwar, Maharashtra', 'Bay of Bengal', 'Maharashtra, Telangana, Andhra Pradesh'),
        ('Krishna', 1400, 'Mahabaleshwar, Maharashtra', 'Bay of Bengal', 'Maharashtra, Karnataka, Telangana, Andhra Pradesh'),
        ('Brahmaputra', 2900, 'Angsi Glacier, Tibet', 'Bay of Bengal', 'Assam, Arunachal Pradesh')
''')

print("below rows are inserted into database")
data = cursor.execute('''select * from llm_demo''')
for row in data:
    print(row)

conn.commit()
conn.close()