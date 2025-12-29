Shopping_cart=[]
def add_cart():
    item_name=input("Enter the item name: ")
    price=int(input("Enter the price of the item: "))
    if price>0:
     a=[item_name,price]
     Shopping_cart.append(a)
     print("\tITEM ADDED SUCCESSFULLY..!")
     print("----------------------------------")
    else:
       print("Enter the valid price")
def remove_cart():
    item=int(input("Enter the item:"))
    print(Shopping_cart.pop(item))
    print("\tITEM REMOVED SUCCESSFULLY\n")
    print("----------------------------------")
while True:
 print("\t|--------------------------------|")
 print("\t| WELCOME TO THE SHOPPING CART\t |")
 print("\t|--------------------------------|")
 print("1.Add item")
 print("2.Remove item")
 print("3.View cart")
 print("4.Exit")
 choice=int(input("\nEnter the choice:"))
 if choice==1:
    add_cart()
    print("\n")
 elif choice==2:
       if Shopping_cart==[]:
        print("\tSHOPPING CART IS EMPTY\n")
        print("-------------------------------")
       else:
         remove_cart()
 elif choice==3:
    print("The Length of Shopping Cart is",len(Shopping_cart))
    if Shopping_cart==[]:
       print("\tCART IS EMPTY\n")
       print("-------------------------------")
    else:
     print("\n|------------------------|")
     print("|        CART MENU       |")
     print("|------------------------|")
     for a in Shopping_cart:
       print("|\t",a,"\t|")
     print("|------------------------|\n")
 elif choice==4:
    print("\tTHANK YOU..!")
    print("\t\tEXITING....!")
    print("----------------------------------")
    break
 else:
    print("\t\tENTER THE VALID CHOICE........!\n\n")