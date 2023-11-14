#https://replit.com/join/eowxkqnlrb-javiergarza12

def salary():
  person = input("Are you a seller? (yes/no)")
  if person == "no":
    print("Goodbye!")
  if person == "yes":
    print("Give me your base salary:")
    base_salary_one_person = float(input())
    print("And how many clients did you had?")
    clients_one_person = int(input())
    
    if clients_one_person < 3500:
      print("You got a 7% comission!")
      almost_total_salary_one_person = ((float(base_salary_one_person))*(float(7/100)))
      total_salary_one_person = ((float(base_salary_one_person))+(float(almost_total_salary_one_person)))
      print("Your total salary is now",total_salary_one_person)
    
    elif clients_one_person <= 3500 or clients_one_person <= 7000:
      print("You got a 10% comission!")
      almost_total_salary_one_person = ((float(base_salary_one_person))*(float(10/100)))
      total_salary_one_person = ((float(base_salary_one_person))+(float(almost_total_salary_one_person)))
      print("Your total salary is now",total_salary_one_person)

    elif clients_one_person > 7000:
      print("You got a 15% comission!")
      almost_total_salary_one_person = ((float(base_salary_one_person))*(float(15/100)))
      total_salary_one_person = ((float(base_salary_one_person))+(float(almost_total_salary_one_person)))
      print("Your total salary is now",total_salary_one_person)

    more_sellers = input("Is there more sellers? (yes/no)")
    if more_sellers == "no":
      print("Goodbye!")
    elif more_sellers == "yes":
      print("How many?")
      sellers_number = int(input())

      for plátanos in range(sellers_number):
        seller_list = []
        print("Give me the name of the seller:")
        seller = input()
        print("Give me the salary of the person:")
        salary_of_seller = float(input())
        print("And how many clients does he/she/it/they/them/her/him/we/us/etc/walmartbag had?")
        clients_of_seller = int(input())
        if clients_of_seller < 3500:
          almost_total_salary_seller = ((float(salary_of_seller))*(float(7/100)))
          total_salary_of_seller = ((float(salary_of_seller))+(float(almost_total_salary_seller)))
          print("The total salary is",total_salary_of_seller)
          
        elif clients_of_seller <= 3500 or clients_of_seller <= 7000:
          almost_total_salary_seller = ((float(salary_of_seller))*(float(10/100)))
          total_salary_of_seller = ((float(salary_of_seller))+(float(almost_total_salary_seller)))
          print("The total salary is",total_salary_of_seller)

        elif clients_of_seller > 7000:
          almost_total_salary_seller = ((float(salary_of_seller))*(float(15/100)))
          total_salary_of_seller = ((float(salary_of_seller))+(float(almost_total_salary_seller)))
          print("The total salary is",total_salary_of_seller)
      
salary()
