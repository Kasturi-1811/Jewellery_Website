import pyodbc
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import io

# Establish a connection to the database
cnxn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=KASTURI\SQLEXPRESS;DATABASE=jewellery_website;Trusted_Connection=yes'
)

# Create a cursor object
cursor = cnxn.cursor()

# Retrieve the image from the database
query = "SELECT image FROM J_table WHERE id = ?"
data = (1,)
cursor.execute(query, data)
image_data = cursor.fetchone()[0]

# Convert the image data to a bytes object
image_bytes = bytes(image_data)

# Create a BytesIO object from the image bytes
image_stream = io.BytesIO(image_bytes)

# Open the image using PIL
image = Image.open(image_stream)

# Display the image
image.show()

# Alternatively, you can display the image using matplotlib
# image_array = np.array(image)
# plt.imshow(image_array)
# plt.show()

# Close the cursor and connection
cursor.close()
cnxn.close()