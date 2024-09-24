def check_age_and_send_message(age):
    if 10 <= age <= 20:
        print ("You're in the prime age range! Keep fighting!")
    else:
        print("Stay strong and keep pushing forward!")

# Example usage:
age = int(input("Enter your age: "))
message = check_age_and_send_message(age)
print(message)
