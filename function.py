class Admin:
    def __init__(self):
        self.food_list=[[1,"noodles","250 gms", 100, 20, 10],\
        [2,"rice  ","150 gms ", 90, 10, 8],\
        [3,"Burger","   1  ", 130  , 30   , 15],\
        [4,"Pizza   "," 1    ",180,40,10],\
        [5,"Sandwich"," 1    ",170,20,10]]

    def admin(self,id,pw):
        self.admin_id="admin"
        self.password="I am admin"
        if id==self.admin_id and pw==self.password:
            return True
        else:
            return False

    def food(self):
        l=len(self.food_list)
        Menu=["Food id","Food Item","Quantity/plate","Price","Discount","Stock Available"]
        for i in Menu:
            print(i, end="      ")
        print("  ")

        for item in self.food_list:
            for i in item:
                print(i,end="            ")
            print(" ")

    def set_food_list(self,id,quantity):
        self.food_list[id-1][5]-=quantity
 
    def edit(self):
        l=len(self.food_list)
        status=False
        food_id=int(input("Enter the food id of item you want to edit"))
        for i in range(0,l):
            if food_id==self.food_list[i][0]:
                status=True
                self.food_list[i][1]=input("Name of food item")
                self.food_list[i][2]=input("Quantity")
                self.food_list[i][3]=int(input("Price"))
                self.food_list[i][4]=int(input("Discount"))
                self.food_list[i][5]=int(input("stock"))
        if status==False:
                print("This food id does not exist")
        print("Item modified successfully")
        print("updated menu list")      

    def add(self):
        list=[]
        l=len(self.food_list)
        temp=self.food_list[l-1][0]+1
        list.append(temp)
        temp=input("Enter the name of food item")
        list.append(temp)
        temp=input("Quantity/plate:")
        list.append(temp)
        temp=int(input("Price:"))
        list.append(temp)
        temp=int(input("Discount:"))
        list.append(temp)
        temp=int(input("Available stock:"))
        list.append(temp)
        self.food_list.append(list)
        print("Item added to list successfully")
    

    def remove(self):
        l=len(self.food_list)
        food_id=int(input("Enter the food id of item you want to remove from list"))
        for i in range(0,l):
            if food_id==self.food_list[i][0]:
                list.pop(self.food_list[food_id-1])
                flag=1
                print("Item removed successfully!!!")

        
            else:
                flag=0
        if flag==0:
            print("Not a valid food ID!!!")      
