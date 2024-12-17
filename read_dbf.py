from dbfread import DBF

# Path to your DBF file
dbf_path = "PURTRAN.DBF"

# Open the DBF file
table = DBF(dbf_path)

# Counter to keep track of the number of rows
row_count = 0

# Iterate over records and print the first 5 rows
for record in table:
    print(f"TYPE: {record['TYPE']}, GROUP: {record['GROUP']}")
    row_count += 1
    if row_count >= 5:
        break
