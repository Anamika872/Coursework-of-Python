def save_products(filename, products):
    """
    -------------------------------------------------------------------------
    Saves the updated list of products to the specified file.
    -------------------------------------------------------------------------

    Parameters:
        filename (str): 
            The name of the file where product data will be saved.
        products (list): 
            A list of dictionaries, each representing a product.

    -------------------------------------------------------------------------
    Returns:
        None
        This function does not return anything.
    -------------------------------------------------------------------------
    """
    # Function code remains unchanged

    file = open(filename, 'w')
    for p in products:
        line = p['S.N'] + ',' + p['name'] + ',' + p['brand'] + ',' + str(p['quantity']) + ',' + str(p['cost_price']) + ',' + p['origin'] + '\n'
        file.write(line)
    file.close()

def create_restock_invoice(restock_invoice):
    """
    -------------------------------------------------------------------------
    Creates a restock invoice for a product that has been restocked.
    -------------------------------------------------------------------------

    Parameters:
        product (dict): 
            A dictionary containing the product details with keys such as:
                - 'Product Id' (int): Unique identifier of the product
                - 'Product Name' (str): Name of the product
                - 'Brand' (str): Brand of the product
                - 'Quantity' (int): Current quantity before restocking
                - 'Price' (int or float): Price per unit of the product
                - 'Country' (str): Country of manufacture

        restock_quantity (int): 
            The quantity of the product that has been added to the stock.

        supplier_name (str): 
            The name of the supplier providing the restocked items.

        invoice_date (str or datetime): 
            The date when the restock invoice is created. Can be a string or datetime object.

    -------------------------------------------------------------------------
    Returns:
        invoice_text (str): 
            A formatted string representing the restock invoice, including product details,
            restock quantity, supplier information, date, and total cost.

    -------------------------------------------------------------------------
    Description:
        This function generates a detailed restock invoice for record-keeping and 
        accounting purposes. The invoice includes product information, restock quantity, 
        supplier details, date of restocking, and the total cost calculated as 
        restock_quantity multiplied by the product price.
    -------------------------------------------------------------------------
    """
    # Function implementation here

    import datetime
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file = open("restock_bill.txt", "w")
    file.write("=============== Restock Invoice ====================\n")
    file.write("Date & Time: " + current_time + "\n")
    file.write("=====================================================\n")
    if restock_invoice:
            file.write("Vendor Name: " + restock_invoice[0]['vendor'] + "\n")  # Use vendor from the first product
    file.write("======================================================\n")

    for item in restock_invoice:
        file.write("Product: " + item["product"] + "\n")
        file.write("Quantity Restocked: " + str(item["restocked_qty"]) + "\n")
        file.write("Cost Price per Unit: " + str(item["cost_price"]) + "\n")
        file.write("Total Restock Cost: " + str(item["total_cost"]) + "\n")
        file.write("--------------------------\n")

    file.write("==========================\n")
    file.close()

def display_restock_invoice():
    """
    -------------------------------------------------------------------------
    Displays the restock invoice details to the console or user interface.
    -------------------------------------------------------------------------

    Parameters:
        invoice_text (str): 
            A formatted string representing the restock invoice. This string 
            usually contains product details, restock quantity, supplier information, 
            date of restocking, and total cost.

    -------------------------------------------------------------------------
    Returns:
        None
        This function does not return any value. It outputs the invoice text 
        directly to the console or display.
    -------------------------------------------------------------------------

    Description:
        This function takes a restock invoice string and prints it in a readable 
        format for record-keeping or user confirmation. It helps in verifying 
        restock transactions by showing all relevant details clearly.
    -------------------------------------------------------------------------
    """
    # Example implementation
    print(invoice_text)

    print("\n==== Restock Invoice ====")
    print("==========================")
    file = open("restock_bill.txt", "r")
    print(file.read())
    file.close()
