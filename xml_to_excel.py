import xml.etree.ElementTree as ET
import pandas as pd
import requests

# Download and parse the XML file
url = 'your_xml_link_here.xml'
response = requests.get(url)
response.encoding = 'utf-8'
root = ET.fromstring(response.text)

# List to store product data
products = []

# Iterate through each product in the XML file
for product in root.findall('product'):
    try:
        product_data = {
            'ProductID': product.find('ProductID').text.strip(),
            'Name': product.find('Name').text.strip(),
            'Price': product.find('Price').text.strip(),
            'Description': product.find('Description').text.strip() if product.find('Description') is not None else None
        }
        products.append(product_data)
    except AttributeError as e:
        print(f"Error processing product: {e}")

# Create a DataFrame from the product list
df = pd.DataFrame(products)

# Save the DataFrame to an Excel file
df.to_excel('products.xlsx', index=False)

print("XML data has been successfully exported to products.xlsx")
