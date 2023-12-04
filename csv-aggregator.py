import pandas as pd

class Item:  
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price  

    def format_price(self):
        self.price = float(self.price.replace('$', '').replace(',', ''))
        
    def total_price(self):
        return self.quantity * self.price

    def update_item(self, new_quantity):
        self.quantity = new_quantity
    
# Read csv file and create objects
def read_invoice(items, filename):
    df = pd.read_csv(filename)

    for index, row in df.iterrows():
         # Find the corresponding item in the items list
        matching_item = next((i for i in items if i.name == row['Description']), None)
        
        if matching_item:
            # If the item exists, update it
            print(f"Item: {row['Description']} exists, updating quantity")
            matching_item.update_item(row['Quantity'])
        else:
            # If it doesn't exist, create it
            item = Item(row['Description'], row['Quantity'], row['Price'])
            item.format_price()
            items.append(item)

    return items

def update_items_from_csv(items, update_filename):
    update_df = pd.read_csv(update_filename)

    for index, row in update_df.iterrows():
        # Find the corresponding item in the items list
        matching_item = next((p for p in items if p.name == row['Description']), None)

        # If matching item is found, update quantity and price
        if matching_item:
            matching_item.update_item(row['Quantity'], row['Price'])
            matching_item.format_price()


invoiceAPath = './Invoice A.csv'
invoiceBPath = './Invoice B.csv'
# invoiceA = read_invoice(invoiceAPath)
# invoiceB = read_invoice(invoiceBPath)
invoices = [invoiceAPath, invoiceBPath]
items = []

for invoice in invoices:
    print(invoice)
    items = read_invoice(items, invoice)

# Print details for each Item object
for item in items:
    total_price = item.total_price()
    print(f"{item.name} - Quantity: {item.quantity}, Total Price: ${total_price}")

