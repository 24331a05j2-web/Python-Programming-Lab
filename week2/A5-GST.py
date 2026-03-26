print("GST Calculator:")
price=int(input("Enter the price of the product: "))
gst=float(input("Enter the GST percentage of the product: "))
tgst=price*(gst/100)
Total=price+tgst
print("The GST of the given product is: ",tgst)
print("The total price of the given product is: ",Total)