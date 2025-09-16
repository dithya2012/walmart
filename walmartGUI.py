# 1 - import packages and define classes
import pygame, pygwidgets, sys


#2 - define constants
BLACK = (0,0,0)
WHITE = (255,255,255)
WHITISH = (210,210,210)
LIGHT_BLUE = (142, 202, 230)
TEAL = (33, 158, 188)
DARK_BLUE = (2, 48, 71)
BLUE = (20,48,71)
YELLOW = (255, 183, 3)
ORANGE = (251, 133, 0)
RED = (255,0,0)
GREEN = (100,255,10)
WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 850
FPS = 30

#3 - initialise the world
pygame.init()
pygame.display.set_caption("walmart")
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
clock = pygame.time.Clock()

title = pygwidgets.DisplayText(window,(600,50), "WALMART",fontSize=40, textColor=DARK_BLUE, justified="center")
add = pygwidgets.TextButton(window,(100,250), "Add To Cart",170,50,YELLOW,DARK_BLUE,TEAL,BLUE,fontSize=25)
remove_button = pygwidgets.TextButton(window,(300,250),"Remove From Cart",170,50,BLACK,YELLOW,ORANGE,ORANGE,fontSize=25)
clear_button = pygwidgets.TextButton(window,(900,250),"Clear Cart",170,50,YELLOW,DARK_BLUE,TEAL,BLUE,fontSize=25)
quit_button = pygwidgets.TextButton(window,(1100,250),"Checkout",170,50,BLACK,YELLOW,ORANGE,ORANGE,fontSize=25)

indextext = pygwidgets.DisplayText(window,(200,150), "What is the product index:",fontSize=35, textColor=DARK_BLUE, justified="center",height=50)
quantitytext = pygwidgets.DisplayText(window,(700,150), "What is the quantity:",fontSize=35, textColor=DARK_BLUE, justified="center",height=50)
productindex = pygwidgets.InputText(window,(200,200),"",fontSize=25, width=300, textColor=YELLOW, backgroundColor=BLACK)
productquantity = pygwidgets.InputText(window,(700,200),"",fontSize=25, width=300, textColor=YELLOW, backgroundColor=BLACK)

error = pygwidgets.DisplayText(window,(490,400),"",fontSize=35, textColor=RED, justified="center")
message = pygwidgets.DisplayText(window,(440,450),"",fontSize=35, textColor=TEAL, justified="center")

product_panel = pygame.Rect(20,330,400,500)
cart_pannel = pygame.Rect(900,330,470,500)

product_panel_title = pygwidgets.DisplayText(window,(100,350), "Products:",fontSize=30, textColor=DARK_BLUE, justified="center")
cart_title = pygwidgets.DisplayText(window,(1100,350), "Your Cart:",fontSize=30, textColor=DARK_BLUE, justified="center")

paid_button = pygwidgets.TextButton(window,(550,600),"Bill Paid",170,50,BLACK,ORANGE,YELLOW,YELLOW,fontSize=25)
admin_button = pygwidgets.TextButton(window,(550,250),"Enter Admin Mode",170,50,BLACK,ORANGE,YELLOW,YELLOW,fontSize=25)
password = pygwidgets.InputText(window,(500,525),"",fontSize=25, width=300, textColor=YELLOW, backgroundColor=BLACK)
passwordtext = pygwidgets.DisplayText(window,(500,425), "Admin Password:",fontSize=35, textColor=DARK_BLUE, justified="center",height=50)
checkpw =   pygwidgets.TextButton(window,(550,650),"Enter",170,50,BLACK,ORANGE,YELLOW,YELLOW,fontSize=25)


# admin mode
product_text_admin = pygwidgets.DisplayText(window,(80,150), "What is the product name you want to add:",fontSize=25, textColor=DARK_BLUE, justified="center",height=50)
quantity_text_admin = pygwidgets.DisplayText(window,(600,150), "What is the quantity of product:",fontSize=25, textColor=DARK_BLUE, justified="center",height=50)
price_text_admin = pygwidgets.DisplayText(window,(1000,150), "What is the price of single item:",fontSize=25, textColor=DARK_BLUE, justified="center",height=50)

product_textinput_admin = pygwidgets.InputText(window,(80,200),"",fontSize=25, width=300, textColor=YELLOW, backgroundColor=BLACK)
quantity_textinput_admin = pygwidgets.InputText(window,(600,200),"",fontSize=25, width=300, textColor=YELLOW, backgroundColor=BLACK)
price_textinput_admin= pygwidgets.InputText(window,(1000,200),"",fontSize=25, width=300, textColor=YELLOW, backgroundColor=BLACK)


exit_admin_button = pygwidgets.TextButton(window,(550,250),"Exit Admin Mode",170,50,BLACK,ORANGE,YELLOW,YELLOW,fontSize=25)
add_admin = pygwidgets.TextButton(window,(300,250),"Add Product",170,50,BLACK,ORANGE,YELLOW,YELLOW,fontSize=25)
cart_items = []
cart_quantity = []
cart_prices = []
product_names = ["T-shirt", "Jeans", "Sneakers", "Cap", "Socks"]
product_prices = [20.0, 50.0, 100.0, 15.0, 5.0]
product_stock = [10, 5, 3, 20, 30]
cart_text = []
product_text = []
total_text = []

start_x = 50
start_y = 400
start_x_stock = 910
line_height = 40
total_bill = 0

index_value = 0
qty = 0
state = "shopping"
admin_password = ""
is_admin = False
cart_total = pygwidgets.DisplayText(window,(start_x_stock,start_y + len(cart_items)*line_height + 40 ), f"Total Bill Amount: ${total_bill}",fontSize=30, textColor=DARK_BLUE, justified="center")
admin_price = ""
admin_qty = ""
admin_name = ""

#4 - load assets, images, sound

#5 - loop forever

def main():
    global admin_button, is_admin, cart_items, cart_prices, cart_quantity, state, error, message, start_x_stock, admin_password, cart_total
    while True:
        #6 - check for handle events
        for event in pygame.event.get():
            #quit the screen and sys
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if productindex.handleEvent(event):
                index_value = productindex.getValue()
            if productquantity.handleEvent(event):
                qty = productquantity.getValue()
           
            if add.handleEvent(event) and state == "shopping":
                message.setText("")
                error.setText("")
                try:
                    index_value = int(productindex.getValue())
                    qty = int(productquantity.getValue())
                    add_to_cart(index_value, qty)
                except ValueError:
                    error.setText("Index and Quantity must be numbers.")
                index_value = 0
                qty = 0
                productindex.clearText()
                productquantity.clearText()

            if remove_button.handleEvent(event)and state == "shopping":
                message.setText("")
                error.setText("")
                try:
                    index_value = int(productindex.getValue())
                    qty = int(productquantity.getValue())
                    remove_from_cart(index_value,qty)
                except ValueError:
                     error.setText("Index and Quantity must be numbers.")
                index_value = 0
                qty = 0
                productindex.clearText()
                productquantity.clearText()
        
            
            if clear_button.handleEvent(event)and state == "shopping":
                message.setText("")
                error.setText("")
                clear_cart()
                index_value = 0
                qty = 0
                total_bill = 0
                cart_total = pygwidgets.DisplayText(window,(start_x_stock,start_y + len(cart_items)*line_height + 40 ), f"Total Bill Amount: ${total_bill}",fontSize=30, textColor=DARK_BLUE, justified="center")

                productindex.clearText()
                productquantity.clearText()

            
            if quit_button.handleEvent(event) and total_bill > 0:
                message.setText("")
                error.setText("")
                checkout_quit(total_bill)
                state = "paying"

            if paid_button.handleEvent(event) and state == "paying":
                cart_total.setText("")
                state = "shopping"
                total_bill = 0
                qty = 0
                index_value = 0 
                cart_items.clear()
                cart_quantity.clear()
                cart_prices.clear()
                message.setText("")
                error.setText("")

            #Admin mode code
            if admin_button.handleEvent(event):
                message.setText("")
                error.setText("")
                state = "admincheck"
            password.handleEvent(event)
                
            if checkpw.handleEvent(event): 
                admin_password = password.getValue()
                if admin_password == "123456":
                    state = "admin"
                    admin_password = ""
                    password.setText("")
                else:
                    error.setText("acess restricted")
                    state = "shopping"
                    

            if price_textinput_admin.handleEvent(event):
                admin_price = price_textinput_admin.getValue()
            if product_textinput_admin.handleEvent(event):
                admin_name = product_textinput_admin.getValue()
            if quantity_textinput_admin.handleEvent(event):
                admin_qty = quantity_textinput_admin.getValue()
            if add_admin.handleEvent(event):
                admin_price = float(price_textinput_admin.getValue())
                admin_qty = int(quantity_textinput_admin.getValue())
                admin_name = product_textinput_admin.getValue()
                if admin_name == "" or admin_qty == "" or admin_price == "":
                    error.setText("fill out all empty fields")
                else:
                    product_names.append(admin_name)
                    product_stock.append(admin_qty)
                    product_prices.append(admin_price)
                    error.setText(f"{admin_name} added to stock!")
                admin_price = 0.0
                admin_name = "" 
                admin_qty = 0
                price_textinput_admin.setText("")
                quantity_textinput_admin.setText("")
                product_textinput_admin.setText("")


            if exit_admin_button.handleEvent(event):
                message.setText("")
                error.setText("")
                state = "shopping"
            
            #Exit Admin Mode


             



        #7 - Do any per frame actions
     
            
        
                    
        cart_text.clear()
        product_text.clear()
        cart_text.clear()
        total_bill = 0
        for i in range(len(cart_items)):
            
            price = cart_prices[i]
            stock = cart_quantity[i]
           
            
        
        for i, (items, stock, price) in enumerate(zip(cart_items, cart_quantity, cart_prices)):
            y = start_y + i * line_height
            if stock >= 5:
                
                dic = (stock * price)*0.95
                total_bill += dic
                text = pygwidgets.DisplayText(window, (start_x_stock, y), f"{i} : {items} - ${price} X {stock} (applied 5% discount) = ${dic}", fontSize=25, textColor=DARK_BLUE, justified="left") 
                cart_text.append(text)

            else:
                dic = stock * price
                total_bill += dic
                text = pygwidgets.DisplayText(window, (start_x_stock, y), f"{i} : {items} - ${price} X {stock} = ${dic}", fontSize=25, textColor=DARK_BLUE, justified="left") 
                cart_text.append(text)
            cart_total = pygwidgets.DisplayText(window,(start_x_stock,start_y + len(cart_items)*line_height + 40 ), f"Total Bill Amount: ${total_bill}",fontSize=30, textColor=DARK_BLUE, justified="center")

    

        for i, (name, price, stock) in enumerate(zip(product_names, product_prices, product_stock)):
            y = start_y + i * line_height
            txt = pygwidgets.DisplayText(window, (start_x, y), f"{i} : {name}   - ${price}  [{stock} left]", fontSize=25, textColor=DARK_BLUE, justified="left")
            product_text.append(txt)

        if state == "shopping":
            paid_button.hide()
            password.hide()
            passwordtext.hide()
            checkpw.hide()
            price_textinput_admin.hide()
            quantity_textinput_admin.hide()
            product_textinput_admin.hide()
            price_text_admin.hide()
            quantity_text_admin.hide()
            product_text_admin.hide()
            productquantity.show()
            productindex.show()
            quantitytext.show()
            indextext.show()
            exit_admin_button.hide()
            add_admin.hide()
            add.show()
            remove_button.show()
            clear_button.show()
            quit_button.show()
            admin_button.show()
            

        if state == "paying":
            paid_button.show()
            password.hide()
            passwordtext.hide()
            checkpw.hide()
            price_textinput_admin.hide()
            quantity_textinput_admin.hide()
            product_textinput_admin.hide()
            price_text_admin.hide()
            quantity_text_admin.hide()
            product_text_admin.hide()
            productquantity.show()
            productindex.show()
            quantitytext.show()
            indextext.show()
            exit_admin_button.hide()
            add_admin.hide()
        
        
        if state == "admincheck":
            paid_button.hide()
            password.show()
            passwordtext.show()
            checkpw.show()
            price_textinput_admin.hide()
            quantity_textinput_admin.hide()
            product_textinput_admin.hide()
            price_text_admin.hide()
            quantity_text_admin.hide()
            product_text_admin.hide()
            productquantity.show()
            productindex.show()
            quantitytext.show()
            indextext.show()
            exit_admin_button.hide()
            add_admin.hide()


        if state == "admin":
            productindex.hide()
            productquantity.hide()
            indextext.hide()
            quantitytext.hide()
            password.hide()
            passwordtext.hide()
            checkpw.hide()
            price_textinput_admin.show()
            quantity_textinput_admin.show()
            product_textinput_admin.show()
            price_text_admin.show()
            quantity_text_admin.show()
            product_text_admin.show()
            productquantity.hide()
            remove_button.hide()
            quit_button.hide()
            add.hide()
            clear_button.hide()
            admin_button.hide()
            exit_admin_button.show()
            add_admin.show()
           


        

        #8 - clear the window
        window.fill(WHITISH)

        
    

        #9 - Draw all window elements
        pygame.draw.rect(window,WHITE,product_panel)
        pygame.draw.rect(window,WHITE,cart_pannel)
        title.draw()
        add.draw()
        remove_button.draw()
       
        clear_button.draw()
        quit_button.draw()
        productindex.draw()
        productquantity.draw()
        quantitytext.draw()
        indextext.draw()
        product_panel_title.draw()
        for txt in product_text:
            txt.draw()
        for text in cart_text:
            text.draw()
      
        cart_title.draw()
        error.draw()
        message.draw()
        paid_button.draw()
        password.draw()
        passwordtext.draw()
        cart_total.draw()
        checkpw.draw()
        admin_button.draw()
        price_text_admin.draw()
        product_text_admin.draw()
        quantity_text_admin.draw()
        product_textinput_admin.draw()
        quantity_textinput_admin.draw()
        price_textinput_admin.draw()
        exit_admin_button.draw()
        add_admin.draw()
        #10 - update the window
        pygame.display.update()


        #11 - slow things down using frames
        clock.tick(FPS)




def add_to_cart(index_value, qty):
    # validating for item index
    if index_value < 0 or index_value >= len(product_names):
        error.setText("Invalid product index value")
        return

    #validating for product quantity 
    if qty < 1 or qty > product_stock[index_value]:
        error.setText("Invalid product quantity")
        return

    # checks if item is in cart already them just increases it quantity
    if product_names[index_value] in cart_items:
        idx = cart_items.index(product_names[index_value])
        if cart_quantity[idx] + qty > product_stock[index_value] + cart_quantity[idx]:
            error.setText("Exceeds available stock.")
            return
        cart_quantity[idx] +=  qty
    # otherwise add name, qty, price in cart items
    else:
        cart_items.append(product_names[index_value])
        cart_quantity.append(qty)
        cart_prices.append(product_prices[index_value])
    
    # removes the qty added by user from stock
    product_stock[index_value] -= qty

    error.setText("")
    message.setText(f"Added {qty} x {product_names[index_value]} to cart.")
    
 




def remove_from_cart(index_value, qty):
    if index_value < 0 or index_value >= len(cart_items):
        error.setText("Invalid product index value")
        message.setText("")
        return
    
    if qty < 1 or qty > cart_quantity[index_value]:
        error.setText("Invalid product quantity")
        message.setText("")
        return

    current_qty = cart_quantity[index_value]

    if qty < 1 or qty > current_qty:
        error.setText(f"Invalid quanitiy. Enter 1-{current_qty} to remove.")
        message.setText("")
        return


    #figure out which product this is 
    product_name = cart_items[index_value]

    #find its slot in the inventory list = in product names give me the index of jeans
    stock_idx = product_names.index(product_name)

    #restore that much in stock
    product_stock[stock_idx]  = product_stock[stock_idx] + qty


    if current_qty == qty:
        cart_items.pop(index_value)
        cart_quantity.pop(index_value)
        cart_prices.pop(index_value)
        message.setText(f"{product_name} X {qty} have been removed form cart")
        error.setText("")
    else:
        cart_quantity[index_value] = cart_quantity[index_value] - qty 
        message.setText(f"{product_name} X {qty} have been removed form cart")
        error.setText("")
        
        


def clear_cart():
    # runs a loop and deleted everything from cart and add it back to stock
    for i in range(len(cart_items)):
        name = cart_items[i]
        quantity = cart_quantity[i]
        product_index = product_names.index(name)
        product_stock[product_index] += quantity
 
    # make all var to its original values
    total_bill = 0
    index_value = 0
    qty = 0

    cart_items.clear()
    cart_quantity .clear()
    message.setText("Cart is cleared!")
    error.setText("")


def checkout_quit(total_bill):
    if total_bill == 0:
        error.setText("No items in cart yet! Start Shopping")
        message.setText("")
    else:
   
        after_disc_price=[]
        for i in range(len(cart_items)): 
            name = cart_items[i]
            quantitiy = cart_quantity[i]
            price = cart_prices[i]
            total_price = price*quantitiy
            
          
            if quantitiy >= 5:
                total = total_price*0.95
                after_disc_price.append(total)
                
            else:
                total = total_price
                after_disc_price.append(total)
            
        total_bill = sum(after_disc_price)
        
        print(f"totalbill:{total_bill}")
        print(f"final list:{after_disc_price}")
        
        order_dic = 0
        # if total bill is more than 200, 10% discount
        if total_bill >= 200:
            order_dic = total_bill*0.1
        
         # if total bill is more than 100, 5% discount
        elif total_bill >=100:
            order_dic = total_bill*0.05
            
        total_bill = total_bill - order_dic
        print(total_bill)

        if order_dic > 0 :
            message.setText(f"Order discount : -${order_dic:.2f} \n Final Cart Total after discount: ${total_bill:.2f} \n Thank you for shopping at list mart!")
          
        else:
            message.setText(f"Final Cart Total : ${total_bill:.2f} \n Thank you for shopping at list mart!")
        
           
    
main()


