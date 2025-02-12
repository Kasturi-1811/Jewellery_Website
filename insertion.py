import pyodbc

# Establish a connection to the database
cnxn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=KASTURI\SQLEXPRESS;DATABASE=jewellery_website;Trusted_Connection=yes'
)

# Create a cursor object
cursor = cnxn.cursor()

# Open the image file in binary mode
with open('images\ear1.jpg', 'rb') as file:
    image_data = file.read()

# Convert the image to binary data
binary_data = bytearray(image_data)

# Insert the image into the database
query = "INSERT INTO J_table (id, image) VALUES (?, ?)"
data = (1, binary_data)

try:
    cursor.execute(query, data)
    cnxn.commit()
    print("Image inserted successfully")
except Exception as e:
    print(f"Error inserting image: {e}")

# Close the cursor and connection
cursor.close()
cnxn.close()