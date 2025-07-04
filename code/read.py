def read_data(filename):
    """
    -------------------------------------------------------------------------
    Reads product data from a file and returns it as a list of dictionaries.
    -------------------------------------------------------------------------

    Parameters:
        filename (str): 
            The name of the file containing product data.

    -------------------------------------------------------------------------
    Returns:
        products (list): 
            A list of dictionaries, each representing a product with keys such as
            'Product Id', 'Product Name', 'Brand', 'Quantity', 'Price', and 'Country'.
    -------------------------------------------------------------------------
    """
    
# Create an empty list to store all products read from the file
    products = []
    '''
Open the file to read product data,
read all lines into a list,
then close the file to free resources.
    '''
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()

    

    for line in lines:
        index = line.split(',')
        if len(index) == 6:
            serialno = index[0]
            name = index[1]
            brand = index[2]
            quantity = int(index[3])
            cost_price = float(index[4])
            origin = index[5].replace("\n", "")

            product = {
                'S.N': serialno,
                'name': name,
                'brand': brand,
                'quantity': quantity,
                'cost_price': cost_price,
                'origin': origin
            }
            products.append(product)
    return products
