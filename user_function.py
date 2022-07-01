import random
import json
from function import*
import datetime as date

class User:
    user_details={}
    user_info=[]
    functions_obj=Admin()
    
    def __init(self,name,phone_no,address,mail,password):        
        self.name=name
        self.phone_no=phone_no
        self.address=address
        self.email=mail
        self.password=password

    def user_registration(self):
        key=random.randint(1,100)
        User.user_info=[]
        self.name=input("Enter your full Name")
        User.user_info.append(self.name)
        self.phone_no=int(input("Enter your contact no"))
        User.user_info.append(self.phone_no)
        self.address=input("Enter your address:")
        User.user_info.append(self.address)
        self.email=input("Enter your email ID")
        User.user_info.append(self.email)
        self.password=input("Enter your password")
        User.user_info.append(self.password)
        User.user_details[key]=User.user_info
        if key:
            print("User registration completed successfully!!!")
        
        else:
            print("something went wrong!!!")

        self.file=open("userdata.json","r")
        self.json_obj = json.load(self.file)
        self.json_obj.update(User.user_details)

        self.file=open("userdata.json","w")
        json.dump(self.json_obj,self.file)
     
    def show_user(self):
        for k,v in User.user_details.items():
            print("User ID:",k,"User details",v)

    def user_login(self):
        flag=False
        self.user_id=input("Enter your user ID")
        self.file = open("userdata.json","r")
        self.data=json.load(self.file)
        if self.user_id in self.data.keys():
            self.pw=input("Enter your password")
            for i in self.data.get(self.user_id):
                if self.pw==i:
                    flag=True

            if flag==True:
                print("Successfully logged in!!!")
            else:
                print("Incorrect password!!!")
        else:
            print("Not a valid user ID!!!")

    def order_food(self):
        self.total=0
        self.cntn=1
        self.flag=False
        self.order_list=[]
        User.functions_obj.food()
        while self.cntn==1:
            self.order=[]
            item=int(input("Enter the Food ID of item you want to order"))
            for i in User.functions_obj.food_list:
                for j in range(len(i)-1):
                    if item==User.functions_obj.food_list[j][0]:
                        self.flag=True

            if self.flag==False:
                print("Selected item not Available")

            else:
                self.quantity=int(input("Enter the quantity"))
                User.functions_obj.set_food_list(item,self.quantity)
                self.order.append(User.functions_obj.food_list[item-1][1])
                self.order.append(self.quantity)
                self.order.append((User.functions_obj.food_list[item-1][3])*self.quantity)
                self.order_list.append(self.order)
                self.total=self.total+self.order[2]
                self.cntn=int(input("Enter 1 to add more items else Enter 0 to see list of selected food items"))
                if self.cntn!=1:
                    print(["Food item","Quantity","Price"])
                    for i in range(len(self.order_list)):
                        print(self.order_list[i])
                    print("---------------")
                    print("Payable Amount:",self.total)
                    self.order_list.append(self.total)
                    self.order_list.append(str(date.datetime.now()))
                    self.final=int(input("Press 1 to place order or press 0 to exit"))
                    if self.final==1:
                        print("Order placed successfully!!!")
                        self.orders()
                    else:
                        print("Order Cancelled")

    def orders(self):
        key=random.randint(1,100)
        all_orders={}
        my_orders={}
        orders={}
        orders[key]=self.order_list
        file=open("orders.json","r")
        all_orders=json.load(file)
        my_orders=all_orders.get(self.user_id)
        if my_orders:   
            my_orders.update(orders)
        else:
            my_orders=orders
        all_orders[self.user_id]=my_orders
        file.close()
        file=open("orders.json","w")
        json.dump(all_orders,file)
        

    def update_profile(self):
        self.name=input("Enter your full Name")
        User.user_info.append(self.name)
        self.phone_no=int(input("Enter your contact no"))
        User.user_info.append(self.phone_no)
        self.address=input("Enter your address:")
        User.user_info.append(self.address)
        self.email=input("Enter your email ID")
        User.user_info.append(self.email)
        self.password=input("Enter your password")
        User.user_info.append(self.password)
        self.data[self.user_id]=User.user_info
        file=open("userdata.json","w")
        json.dump(self.data,file)
        print("Profile updated successfully")

    def view_profile(self):
        file=open("userdata.json","r")
        alldata=json.load(file)
        data=alldata.get(self.user_id)
        print("ID:",self.user_id)
        print("NAME:",data[0])
        print("MOBILE NO:",data[1])
        print("ADDRESS:",data[2])
        print("EMAIL ID:",data[3])
        print("PASSWORD:",data[4])
       


    def order_history(self):
        file=open("orders.json","r")
        data=json.load(file)
        mydata=data.get(self.user_id)
        for k,v in mydata.items():
            print(k)   
            print('["Food item","Quantity","Price"]')     
            for i in v:
                print(i)
