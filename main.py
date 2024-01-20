import dotenv
import os

def check_creds(un, pw):
    dotenv.load_dotenv()

    user1 = os.getenv('user1')
    password1 = os.getenv('password1')

    if un == user1 and pw == password1:
        print('You logged in correctly')
    else:
        print("Incorrect username or password")

def main():
    
    user_name = input("Login Name: ")
    user_password = input("Please enter password: ")
    
    check_creds(user_name, user_password)   
     
if __name__ == '__main__':
    main()
