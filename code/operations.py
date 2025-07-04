import write
def show_producttable(products):
    """
    -------------------------------------------------------------------------
    Displays the list of products in a tabular format.
    -------------------------------------------------------------------------

    Parameters:
        products (list): 
            A list of dictionaries, each representing a product.

    -------------------------------------------------------------------------
    Returns:
        None
        This function does not return anything.
    -------------------------------------------------------------------------
    """

    print("Available Products\n")
    print(" S.N  Product              Brand        Stock  C.P       S.P        Origin")
    print("-------------------------------------------------------------------------------")

    for p in products:
        sell_price = p['cost_price'] * 2

        serialno = str(int(p['S.N']))
        if len(serialno) < 6:
            serialno = serialno + ' ' * (6 - len(serialno))

        name = p['name']
        if len(name) < 20:
            name = name + ' ' * (20 - len(name))

        brand = p['brand']
        if len(brand) < 15:
            brand = brand + ' ' * (15 - len(brand))

        stock = str(p['quantity'])
        if len(stock) < 6:
            stock = stock + ' ' * (6 - len(stock))

        cost = str(int(p['cost_price']))
        if len(cost) < 11:
            cost = cost + ' ' * (11 - len(cost))

        selling = str(int(sell_price))
        if len(selling) < 11:
            selling = selling + ' ' * (11 - len(selling))

        origin = p['origin']

        print(serialno + name + brand + stock + cost + selling + origin)

def selling_products(products):
    
    while True:
        user_input = input("Enter the Product ID (S.N): ")
        if user_input.isdigit():
            found = False
            for product in products:
                if product['S.N'] == user_input:
                    found = True
                    while True:
                        qty_input = input("How many products do you want to buy? ")
                        if qty_input.isdigit():
                            total_needed = int(qty_input)
                            free_items = total_needed // 3
                            total_with_offer = total_needed + free_items
                            if total_with_offer <= product['quantity']:
                                product['quantity'] -= total_with_offer

                                # Ask if user wants to buy more
                                more = input("Do you want to buy more? (yes/no): ").lower()
                                if more != 'yes':
                                    #  Only return when user finishes shopping
                                    return product, total_needed, free_items
                                else:
                                    # Continue the loop again for another product
                                    break
                            else:
                                print("Not enough stock. Try a smaller quantity.")
                        else:
                            print("Enter a valid number.")
                    break
            if not found:
                print("Product ID not found.")
        else:
            print("Enter a valid number.")

      
def restock_product(filename, products):
    restock_invoice = []

    vendor = input("Enter vendor name: ")  # Ask vendor name once at the beginning

    while True:
        try:
            restock_id = int(input("Enter the Product ID to restock: "))
            found = False

            for p in products:
                if int(p['S.N']) == restock_id:
                    found = True
                    current_qty = p['quantity']
                    print("Current quantity of '" + p['name'] + "': " + str(current_qty))

                    added_quantity = input("Quantity to add: ")
                    if added_quantity.isdigit():
                        added_quantity = int(added_quantity)
                        p['quantity'] += added_quantity

                        cost_price = p['cost_price']
                        total_cost = added_quantity * cost_price

                        restock_invoice.append({
                            "product": p['name'],
                            "restocked_qty": added_quantity,



                            
                            "cost_price": cost_price,
                            "total_cost": total_cost,
                            "vendor": vendor  # Add vendor to invoice
                        })

                        print(p['name'] + " restocked successfully. New quantity: " + str(p['quantity']))
                        write.save_products(filename, products)
                    else:
                        print("Invalid quantity input. Must be a number.")

                    break

            if not found:
                print("Invalid Product ID. Please try again.")

        except ValueError:
            print("Invalid input. Please enter a numeric Product ID.")

        another_restock = input("Do you want to restock another product? (Y/N): ").upper()
        if another_restock != 'Y':
            break

    if restock_invoice:
        write.create_restock_invoice(restock_invoice)
        write.display_restock_invoice()
    else:
        print("\nNo products were restocked, so no restock invoice was created.\n")
