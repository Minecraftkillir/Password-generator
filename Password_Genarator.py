import random

numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

string = numbers + lower_case + upper_case
password_lenght = 10

password = "".join(random.sample(string, password_lenght))
print(f"Your password is: {password}")