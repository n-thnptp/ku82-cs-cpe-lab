ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'Ad31n15Tr@t012'

user = input("Username: ")
pw = input("Password: ")

if user == ADMIN_USERNAME and pw == ADMIN_PASSWORD:
    print("Welcome, admin.")
else:
    print("You are not admin.")