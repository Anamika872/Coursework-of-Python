from read import read_data
from write import save_products, create_restock_invoice, display_restock_invoice
from operations import show_producttable, selling_products, restock_product
import datetime

def main():
    """
    -------------------------------------------------------------------------
    Main function to run the WeCare Skin Products Management system.
    -------------------------------------------------------------------------

    Description:
        This function serves as the entry point for the application. It loads 
        product data, displays a menu to the user, and handles user choices 
        for showing products, selling products, restocking, and exiting the 
        program. It also manages invoice creation and product stock updates.

    -------------------------------------------------------------------------
    Parameters:
        None

    -------------------------------------------------------------------------
    Returns:
        None
        This function does not return anything.
    -------------------------------------------------------------------------
    """
   
    filename = "products.txt"
    products = read_data(filename)
    """
This function reads data from a file,
processes each line to extract product details,
and returns a list of product dictionaries.
"""

    
    

    while True:
        print("\n==== WeCare Skin Products Management ====")
        print("1. Show Products")
        print("2. Sell Product")
        print("3. Restock Product")
        print("4. Exit")
        print("==========================================")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_producttable(products)

        elif choice == "2":
            sold_product, bought_qty, free_items = selling_products(products)

            customer_name = input("Enter customer name: ")

            total_price = bought_qty * sold_product['cost_price'] * 2
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            invoice_text = []  # Initialize invoice_text as a list

            invoice_text.append("======================================================= INVOICE =================================================\n")
            invoice_text.append("Date & Time: " + current_time + "\n")
            invoice_text.append("-----------------------------------------------------------------------------------------------------------------\n")
            invoice_text.append("Customer Name: " + customer_name + "\n")
            invoice_text.append("------------------------------------------------------------------------------------------------------------------------\n")
            invoice_text.append("Product: " + sold_product['name'] + "\n")
            invoice_text.append("Brand: " + sold_product['brand'] + "\n")
            invoice_text.append("Origin: " + sold_product['origin'] + "\n")
            invoice_text.append("Quantity Purchased: " + str(bought_qty) + "\n")
            invoice_text.append("Free Items: " + str(free_items) + "\n")
            invoice_text.append("Price per unit: Rs. " + str(sold_product['cost_price'] * 2) + "\n")
            invoice_text.append("Total Price: Rs. " + str(total_price) + "\n")
            invoice_text.append("==============================================================================================================================\n")

            # Show on screen
            for line in invoice_text:
                print(line, end='')

            # Save to file
            with open("invoice.txt", "w") as invoice_file:
                invoice_file.write("".join(invoice_text))

            # Save product stock update
            save_products(filename, products)

        elif choice == "3":
            restock_product(filename, products)

        elif choice == "4":
            print("Thank you for visiting . Have a great day.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

main()
