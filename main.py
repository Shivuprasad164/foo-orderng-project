from function import*
from user_function import*
from datetime import datetime as date

if __name__=="__main__":
    print("1.Enter 1 To login as Admin")
    print("2.Enter 2 To login as User")
    choice=int(input("Enter:"))
    if choice==1:
        admin_id=input("Enter admin Id")
        admin_pw=input("Enter Password")
        obj=Admin()
        
        status=obj.admin(admin_id,admin_pw)
        if status==True:
            flag=1
            while flag==1:
                print("Welcome to the delicious Food Cafe, you have logged in as Admin successfully")
                print("Enter 1. Show food Menu list")
                print("2. Edit food item in Menu list\n 3. Add a food item to Menu list")
                print("4.Remove food item from Menu list")
                choice=int(input())

                if choice==1:
                    obj.food()

                elif choice==2:
                    obj.edit()

                elif choice==3:
                    obj.add()

                elif choice==4:
                    obj.remove()
                
                else:
                    print("you have entered invalid option")

                    print("")

                flag=int(input("Do you wish to continue: enter '1' to continue and '0' to exit"))
                    
        else:
            print("you have entered incorrect login details")


    elif choice==2:
        user_obj=User()
        login=int(input("Enter 1.To register as a new user\n2.To login to your account"))
        if login==1:
            user_obj.user_registration()
            user_obj.show_user()
            user_obj.user_login()
            choice=int(input("Enter 1.Place new Order\n2.Order History\n3.Update Profile"))
            if choice==1:
                user_obj.order_food()
            if choice==2:
                pass
            if choice==3:
                pass
        
        
        elif login==2:
            result=user_obj.user_login()
            if result==True:
                status=1
                while status==1:
                    choice=int(input("Enter 1.Place new Order\n2.Order History\n3.Update Profile\n4.View Profile"))
                    if choice==1:
                        user_obj.order_food()

                    elif choice==2:
                        user_obj.order_history()

                    elif choice==3:
                        user_obj.update_profile()

                    elif choice==4:
                        user_obj.view_profile()

                    status=int(input("Enter 1 to continue or 0 to exit"))

                    if status!=1:
                        print("Thankyou for visiting us!!!")

                    else:
                        print("Not a valid option") #Modify