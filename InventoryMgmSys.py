# ================================
#     INVENTORY MANAGEMENT SYSTEM
# ================================
# 1. Add Product
# 2. View Inventory
# 3. Search Product
# 4. Update Stock
# 5. Delete Product
# 6. Exit

# Enter your choice:

def display_inventory():
    inventory = []

    while True:
        print('=' * 30)
        print("Inventory Management System")
        print('=' * 30)
        print('1. Add Items')
        print('2. View Items')
        print('3. Search Items')
        print('4. Update Items')
        print('5. Delete Items')
        print('6. Exit')

        choice = input("Enter your choice : ")

        if choice == '1':
            print('Add Items Selected')
            prod_id = int(input('Enter product id : '))

            found = False

            for prod in inventory:
                if prod['id'] == prod_id:
                    found = True
                    break
            if found:
                print('product already exist.')
            else:
                name = input('Enter product name : ')
                price = int(input('Enter product price : '))
                quantity = int(input('Enter quantity: '))
                prod_dict = {
                    'id':prod_id,
                    'name':name,
                    'price':price,
                    'quantity':quantity
                }
                inventory.append(prod_dict)
                print('Product aded successfully into inventory')



        elif choice == '2':
            print('View Inventiry selected.')

            if len(inventory)==0:
                print('No items found')

            else:
                for prod in inventory:
                    print(f"Product Name : {prod['name']} | Product id {prod['id']}, | Product Price {prod['price']} | Product Quantity {prod['quantity']}")


        elif choice == '3':
            print('Search items Selected')
            search_id = int(input('Enter product id : '))

            for prod in inventory:
                if prod['id'] == search_id:
                    print('Product Found Successfully')
                    print(f"Product Name : {prod['name']} | Product id {prod['id']}, | Product Price {prod['price']} | Product Quantity {prod['quantity']}")
                    break
            else:
                print('No product found')



        elif choice == '4':
            print('Update Product Selected')
            search_id = int(input('Enter product id : '))

            for prod in inventory:
                if prod['id'] == search_id:
                    print('Product Found Successfully')
                    update_price = int(input('Enter Updated price'))
                    update_quant = int(input('Enter updated amount'))
                    prod['price'] = update_price
                    prod['quantity'] = update_quant 
                    print('Product Updated SUccessfully.')
                    break
            else:
                print('Noo Product Found')             


        elif choice == '5':
            print("Product Delete Started")
search_id = int(input('Enter product id : '))

            for prod in inventory:
                if prod['id'] == search_id:
                    print('Product Found Successfully')

        elif choice == "6":
            print('Exiting the program')
            break
        else:
            print('Invalid choice')




display_inventory()