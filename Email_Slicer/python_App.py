def main():
    print("Welcome to the Email_Slicer!!")
    print(" ")
    
    email_input = input("Enter your email : ")
    
    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")
    
    print("Username : " , username)
    print("Domain : " , domain)
    print("Extension : " , extension)
    
while True:   
    main()