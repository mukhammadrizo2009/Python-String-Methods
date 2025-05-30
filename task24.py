email = input("Emailingizni kiriting: ")

result = not email.startswith("@") and email.endswith(".com")


print(result)