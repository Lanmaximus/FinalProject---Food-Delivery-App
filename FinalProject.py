import json
class Foodapp:
    def __init__(self,name):
        self.appname = name
        self.foods = {}
        self.food_id = 0
        self.user_reg = {}
        self.ordered_item = []

    def add_food_item(self):
     try:    
        name = input("Enter the food name :")
        quantity = float(input("Enter the quantity :"))
        price = float(input("Enter the price :"))  
        discount = float(input("Enter the dicount:"))
        stock = float(input("Enter the available stock :"))
        food_item = {"Name":name , "Quantity":quantity , "Price":price ,"Discount":discount, "Stock":stock}
        self.food_id = len(self.foods)+1
        self.foods[self.food_id] = food_item
        print("\nFood item Added successfully")
     except Exception as ex:
        print("\nSome error")

    def view_food_items(self):
        if len(self.foods)!= 0:
            for i in self.foods:
                print(f"food id : {i}")
                for j in self.foods[i]:
                    print(j, ":",self.foods[i][j])
               
                print() 
        else:
            print("No food available") 

    def edit_food_item(self):
     try:
        id = int(input("Enter the food id:"))
        print("Edit the food") 
        print("1.Food name \n2.Quantity \n3.Price \n4.Discount\n5.Stock")
        y = input("Enter the key:")
        if id in self.foods.keys():
            if y == '1':
                self.foods[id]["Name"] = input("Edit the food name:")
                print("Food item edited successfully")
            elif y == '2':
                self.foods[id]["Quantity"] = float(input("Edit the Quantity:"))
                print("Food item edited successfully")
            elif y == '3':
                self.foods[id]["Price"] = float(input("Edit the price:"))
                print("Food item edited successfully")
            elif y == '4':
                self.foods[id]["Discount"] = float(input("Edit the Discount:"))
                print("Food item edited successfully")
            elif y == '5':
                self.foods[id]["Stock"] = float(input("Edit the stock:"))
                print("Food item edited successfully")
            else:
                print("Invalid key")
        else:
            print("Invalid Food id Please Try Again")
     except Exception:
          print("\nSomething went wrong")
    def remove_food(self):
        id = int(input("Enter the food id:"))
        if id in self.foods.keys():
            del self.foods[id]
            print("Food item removed successfully")
            print("\nUpdated Food List : \n",self.foods)
        else:
            print("No food id available")

    def register_user(self):
     try:
        while True:
            username = str(input("Enter the name:"))
            email = input("Enter the email:")
            password = (input("Enter the password:"))
            address = (input("Enter the address:"))
            phone_num = int(input("Enter the phn number:"))

            user_reg = {"Name":username , "Email":email , "Password":password , "Address":address , "Phone number":phone_num}
            self.user_id = len(self.user_reg)+1
            self.user_reg[self.user_id] = user_reg
            print("Registered Successfully\n")
            for i in self.user_reg:
                    print(i, ":", self.user_reg[i])
            print()
            break
        print("user registered")
     except Exception:
        print("Something wrong")

    def user_login(self):
        try:
            while True:
                print(f"Welcome TO {self.appname} \n\n")
                email = input("Enter Your Email ID : ")
                password = input("Enter Your Password : ")
                if len(self.user_reg) != 0:
                 for values in self.user_reg.values():
                  if email == values["Email"] and password == values["Password"]:
                    print("\n Login successfully")
                    while True:
                        print("\nEnter the Below Options\n")
                        print("1. Place New Order\n2. Check Order History\n3. Update Your Profile Details\n4. Exit")
                        a = input("Entrer the key: ")
                        if a == "1":
                            self.place_order()
                        elif a == "2":
                            self.ordered_history()
                        elif a == "3":
                            self.update_details()
                        elif a == "4":
                            break
                     
                  else:
                    print("\n** Incorrect Email or Password**\n")
                break
        except Exception as e:
            print("\n Something went wrong please try again")

    def place_order(self):
        try:
            if len(self.foods) != 0:
                menu = []
                for item in self.foods:
                    menu.append([self.foods[item]["Name"], self.foods[item]["Quantity"], self.foods[item]["Price"]])
                    
                    print("Foods Available" )
                    if len(self.foods)!= 0:
                        for i in self.foods:
                          print(f"food id : {i}")
                          for j in self.foods[i]:
                           print(j, ":",self.foods[i][j])
               
                          print() 
                    else:
                     print("No food available")
                    
                
                while True:
               
                    print("\n1. Place the Order \n2. Exit")
                    x = input("Enter a Key: ")
                 
                    if x == "1":
                        y = input("Enter the Food Items :").split(",")
                        if y in menu:
                            print("Your Order has placed Successfully")
                        for i in y:
                            a = int(i)
                            if a <= len(menu):
                                self.ordered_item.append(menu[a - 1])
                            else:
                                print(" : ", a)
                        print("****Your Order has Placed Successfully***** \n******Enter 1 to Order Again or Just Enter 2 to Exit*****")
                       
                    elif x == "2":
                        break
                    
            else:
                print("\nNo Food Items are available\n")
        except Exception as e:
            print("\n!! Something went wrong try again !!")

    def ordered_history(self):
        print("\n***Your Ordered Items*** ")
        for i in self.ordered_item:
            print(i)

    def update_details(self):
        try:
            
                id = int(input("Enter the user id number:"))
                print("Edit the Details")
                print("Enter the Option Below>\n")
                print("\n1) Name\n2) Phone number\n3) Email ID\n4) Password\n5) Address\n6) Exit\n")
                a = input("Enter the Key : ")
                if id in self.user_reg.keys():
                 if a == "1":
                    self.user_reg[id]["Name"] = input("Enter your updated full name : ")
                    print("\nUpdated Successfully\n")
                 elif a == "2":
                    self.user_reg[id]["Phone Number"] = int(input("Enter your updated 10 digit phone number : "))
                    print("\nUpdated Successfully\n")
                 elif a == "3":
                    self.user_reg[id]["Email"] = input("Enter your updated email id : ")
                    print("\n  Updated Successfully")

                 elif a == "4":
                    self.user_reg[id]["Password"] = input("Enter your updated password : ")
                    print("\n Updated Successfully\n")

                 elif a == "5":
                    self.user_reg[id]["Address"] = input("Enter your updated address with area PIN code ")
                    print("\nUpdated Successfully\n")

                
                 else:
                    print("\n Invalid Number Entered \n")
                else:
                    print("Wrong User ID Try again")
                if a in ["1", "2", "3", '4', "5"]:
                    for i in self.user_reg:
                        print(i, ":", self.user_reg[i])
        except Exception as e:
            print("\nSomething went wrong please try again\n ")

def main():
  try:  
        a = Foodapp("FOOD APP")
        print("\nWelcome to Food App\n")
        while True:
            print("1:Admin \n2.User \n3.Exit")
            key = input("Enter a key:")
            if key == '1':
             ab = open("admin.json","r")
             abc = json.load(ab)
             username = input("\nEnter Username:")
             password = input("Enter the password:")
             if abc["username"] == username and abc["password"] == password:
               
              while True:
                print("\nEnter the Option")
                print("\n1.Add food  \n2.View food \n3.Edit food \n4.Remove food \n5.Exit")
                key_1 = input("Enter a key:")
                if key_1 == '1':
                   a.add_food_item()
                elif key_1 == '2':
                   a.view_food_items()
                elif key_1 == '3':
                   a.edit_food_item()
                elif key_1 == '4':
                   a.remove_food()
                elif key_1 == '5':
                    break
             else:
                print("\nWrong password or username(try again)")
            
            elif key == "2":
             while True:
                    print("\n1.Register new user \n2.Login user \n3.Exit")
                    key_a = input("\nEnter a key:")
                    if key_a == "1":
                        a.register_user()
                    elif key_a == "2":
                        a.user_login()
                    
                    elif key_a == "3":
                      break 
            elif key == '3':
                print("//////THANKYOU VISIT AGAIN//////")
                break          

  except Exception:
        print("\nsome error occurs") 
         
         
if __name__ == '__main__':
    main()