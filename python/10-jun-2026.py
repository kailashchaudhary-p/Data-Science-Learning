"""
 Movie Ticket Pricing Calculator
Write a program that determines the ticket price for a 
movie theater based on a customer's age and whether they 
have a student ID. The Rules: Children under 5 roll for 
free (0 Rs.).Retiring seniors (65 Rs.  and older) get a 
discounted rate of 7 Rs. Regular tickets cost 12.If a 
regular customer (ages 5 to 64) provides a student ID
, they get a 3 Rs .  discount (making the ticket 9 Rs . ).
"""
age = int(input("enter your age: "))
student_id = input("do you have a student id? (yes/no): ").lower()
if age < 5:
    print("Your ticket is free (0 Rs.)")
elif age >= 65:
    print("You get a discounted rate of 7 Rs.")
elif age >= 5 and age < 65:
    if student_id == "yes":
        print("You get a 3 Rs. discount, making the ticket 9 Rs.")
    else:
        print("Regular ticket costs 12 Rs.")