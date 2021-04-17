# Hackathon project for the Maple High School Hackathon, Done with Avi Walia, Daniel Truong, and Ameya Soman
import time
import random

print("Welcome to the Smiley Smoothie Management Program \n")

ingredients = ["Strawberries", "Yogurt", "Milk", "Ice Cubes", "Mangoes",
               "Frozen Berries"]  # stores ingredients in the variable
items = ["Strawberry Smoothie", "Mango Smoothie", "Berry Blast Smoothie"]  # stores items in the variable
inventory = {}  # creates empty dictionary that gets added later in the code
menu = {}  # creates empty dictionary that gets added later in the code

dishes = {"Strawberry Smoothie": ("Strawberries", "Yogurt", "Milk", "Ice Cubes"),
          "Mango Smoothie": ("Mangoes", "Yogurt", "Milk", "Ice Cubes"),
          "Berry Blast Smoothie": ("Frozen Berries", "Yogurt", "Milk", "Ice Cubes")}

balance = float(input("What is the new starting balance? "))

print("")

num_employees = int(input("How many employees do you have? "))

print("")
print("An input of 1 represents the amount required to make one smoothie.")
time.sleep(1.5)
print("For example, if a smoothie requires 8 strawberries, an input of 1 represents 8 strawberries.")
time.sleep(1.5)
print("""Dollar signs are not required when inputting costs.\n""")
time.sleep(1.5)

for i in ingredients:  # adds quantities and costs of ingredients to the inventory dictionary
    quantity = float(input("How much of this ingredient do you have?: {} ".format(i)))
    cost = float(input("How much does each portion of {} cost? ".format(i)))
    l = [quantity, cost]
    inventory[i] = l
    print("")

print("")

for i in items:  # adds menu prices to the menu dictionary
    cost = float(input("How much does the {} cost? ".format(i)))
    menu[i] = cost

straw_sold = random.randint(325, 575) # generates random values for sales
berry_sold = random.randint(325, 575)
mango_sold = random.randint(275, 525)

straw_revenue = straw_sold * menu["Strawberry Smoothie"]
berry_revenue = berry_sold * menu["Berry Blast Smoothie"]
mango_revenue = mango_sold * menu["Mango Smoothie"]

straw_expense = 0
berry_expense = 0
mango_expense = 0

for i in dishes["Strawberry Smoothie"]:
    item_cost = straw_sold * inventory[i][1]
    straw_expense += item_cost

for i in dishes["Berry Blast Smoothie"]:
    item_cost = berry_sold * inventory[i][1]
    berry_expense += item_cost

for i in dishes["Mango Smoothie"]:
    item_cost = mango_sold * inventory[i][1]
    mango_expense += item_cost

total_revenue = straw_revenue + berry_revenue + mango_revenue
total_expense = straw_expense + berry_expense + mango_expense
total_profits = total_revenue - total_expense

# function that determines whether or not the user is eligible for each loan/subsidy
def loan_eligibility(revenue, expense, employees):
  el = []
  not_el = []
  if revenue >= 5000 and employees >= 10:
      el.append("RBC")
  else:
      not_el.append("RBC")

  if 1500 <= revenue <= 3000 and employees >= 10:
      el.append("TD")
  else:
      not_el.append("TD")

  if revenue >= 7000 and num_employees >= 5:
      el.append("CIBC")
  else:
      not_el.append("CIBC")

  if expense <= 1000 and revenue >= 2000:
      el.append("SCOTIABANK")
  else:
      not_el.append("SCOTIABANK")

  if expense <= 1500 and revenue >= 7000:
      el.append("BMO")
  else:
      not_el.append("BMO")

  return el, not_el


expenses = 0
chosen_loan = ""

loan_paid = 0

while True:  # will repeat code if invalid input is entered
  time.sleep(1)  # prevents user from accidentally choosing an option while inputting values
  print("""\n Please choose an option: \n
 1. Check current balance \n
 2. Check inventory \n
 3. Purchase more inventory \n
 4. Remove unusable inventory \n
 5. Display expenses made on inventory items \n
 6. Report current sales \n
 7. View loans and subsidies\n
 8. Calculate loan repayment \n
 9. Display menu \n
 10. End program """)
  option = input("\n")  # stores their chosen option in variable

  if option == '1': # if 1 is chosen, displays the balance
      print('Balance: $%.2f' % balance)

  elif option == '2': # if 2 is chosen, displays the quantity of each inventory item
      for i in ingredients:
          print("{}: {}".format(i, inventory[i][0]))

# if 3 is chosen, asks the user how much of a certain ingredient they want to purchase and whether or not they can afford it
  elif option == '3':
      for i in ingredients:
          extra_purchase = float(input("How much of this ingredient would you like to purchase?: {} ".format(i)))
          cost_purchase = extra_purchase * inventory[i][1]
          while True:
              if cost_purchase < balance:
                  break
              else:
                  print("You don't have sufficient funds to make this purchase")
                  extra_purchase = float(input("How many {} would you like to purchase: ".format(i)))
                  cost_purchase = extra_purchase * inventory[i][1]
          inventory[i][0] += extra_purchase
          balance -= cost_purchase
          expenses += cost_purchase
  
  # if 4 is chosen, allows the user to remove a certain amount of a specific inventory item.
  elif option == "4":
    while True:
      counter = 1
      for i in ingredients:
        print("{}: {}: {}".format(counter, i, inventory[i][0]))
        counter += 1
      print("")
      del_option = input("Which ingredient would you like to remove inventory from? (input the corresponding number represented to the left of the ingredient name. If none, type '0') ")
      if del_option == "1":
        del_quantity = float(input("How many portions of Strawberries would you like to remove? "))
        inventory["Strawberries"][0] -= del_quantity
      elif del_option == "2":
        del_quantity = float(input("How many portions of Yogurt would you like to remove? "))
        inventory["Yogurt"][0] -= del_quantity
      elif del_option == "3":
        del_quantity = float(input("How many portions of Milk would you like to remove? "))
        inventory["Milk"][0] -= del_quantity
      elif del_option == "4":
        del_quantity = float(input("How many Ice Cubes would you like to remove? "))
        inventory["Ice Cubes"][0] -= del_quantity
      elif del_option == "5":
        del_quantity = float(input("How many portions Mangoes would you like to remove? "))
        inventory["Mangoes"][0] -= del_quantity
      elif del_option =="6":
        del_quantity = float(input("How many portions of Frozen berries would you like to remove? "))
        inventory["Frozen Berries"][0] -= del_quantity
      elif del_option == "0":
        print("None selected")
        break
      else:
        print("Invalid option")

# if 5 is chosen, shows the user how much they have spent on purchasing inventory
  elif option == "5":
      print("Expenses on Inventory: $%.2f" % expenses)

# if 6 is chosen, allows the user to report any sales that they make. Balance will increase and inventory will decrease based on how many products are sold. If they do not have the inventory to make the sale, it will state that they cannot do so
  elif option == "6":
      strawberry_sales = int(input("How many strawberry smoothies have you sold: "))

      for i in dishes["Strawberry Smoothie"]:
          while True:
              if inventory[i][0] >= strawberry_sales:
                  break
              else:
                  print("You don't have enough inventory to do that!")
                  strawberry_sales = int(input("How many strawberry smoothies have you sold: "))
          inventory[i][0] -= strawberry_sales

      print("")

      mango_sales = int(input("How many mango smoothies have you sold: "))

      for i in dishes["Mango Smoothie"]:
          while True:
              if inventory[i][0] >= mango_sales:
                  break
              else:
                  print("You don't have enough inventory to do that!")
                  mango_sales = int(input("How many mango smoothies have you sold: "))
          inventory[i][0] -= mango_sales

      print("")

      berry_sales = int(input("How many berry smoothies have you sold: "))

      for i in dishes["Berry Blast Smoothie"]:
          while True:
              if inventory[i][0] >= berry_sales:
                  break
              else:
                  print("You don't have enough inventory to do that!")
                  berry_sales = int(input("How many berry smoothies have you sold: \n"))
          inventory[i][0] -= berry_sales

      balance += strawberry_sales * (menu["Strawberry Smoothie"])
      balance += mango_sales * (menu["Mango Smoothie"])
      balance += berry_sales * (menu["Berry Blast Smoothie"])

      total_sales = strawberry_sales * (menu["Strawberry Smoothie"]) + mango_sales * (menu["Mango Smoothie"]) + berry_sales * (menu["Berry Blast Smoothie"])

      print ("Your total sales are: $%.2f" % total_sales)

# if 7 is chosen, it will display revenue and expenses. It will then show which loans/subsidy the user is eligible for and allows them to choose one, affecting their balance and interest on expenses
  elif option == "7":
      print("The following displays monthly averages NOT including this month's sales \n")
      print("Strawberry Smoothies sold:", straw_sold, "\n")
      print("Berry Blast Smoothies sold:", berry_sold, "\n")
      print("Mango Smoothies sold:", mango_sold, "\n")
      print("Total Revenue: $%.2f" % total_revenue, "\n")
      print("Total Expenses: $%.2f" % total_expense, "\n")
      print("Gross Profits : $%.2f" % (total_profits), "\n")

      loans_and_subsidies = loan_eligibility(total_revenue, total_expense, num_employees)
      eligible = loans_and_subsidies[0]
      not_eligible = loans_and_subsidies[1] 

      time.sleep(3)

      print("Below are the loans and subsidies made available by your local banks \n")
      print("RBC Maple Businesses Subsidy")
      print("- Requires at least $5000 in revenue per month.")
      print("- Employs at least 10 people.")
      print("This loan will provide you with $20,000. \n")
      time.sleep(3)

      print("TD Extreme Financial Need Loan")
      print("- $1500-$3000 in revenue per month.")
      print("- Employs at least 10 people.")
      print("This loan will provide you with $10,000 with a 1% interest compounded annually. \n")
      time.sleep(3)

      print("CIBC Financial Need Loan")
      print("- $7000 in revenue per month.")
      print("- Employs at least 5 people.")
      print("This loan will provide you with $100,000 with a 2.1% interest compounded annually. \n")
      time.sleep(3)

      print("Scotiabank Entrepreneurship Loan")
      print("- Average expenses must not exceed $1000 a month.")
      print("- $2000 in revenue per month.")
      print("- Owners donʼt need to employ anyone.")
      print("This loan will provide you with $100,000 with a 3.2% interest compounded annually. \n")
      time.sleep(3)

      print("BMO “Operation Small Business” Subsidy")
      print(" - Average expenses must not exceed $1500 a month.")
      print(" - $7000 in revenue per month.")
      print(" - In the restaurant or small business industry")
      print("This loan will provide you with $70,000. \n")

      if len(eligible) != 0:
          time.sleep(3)
          print("You are eligible for these loans and subsidies:")
          for i in eligible:
              print("- " + i + "\n")

      if len(not_eligible) != 0:
          time.sleep(3)
          print("You are not eligible for these loans and subsidies:")
          for i in not_eligible:
              print("- " + i + "\n")

      if len(eligible) == 0:
          time.sleep(3)
          print("You are not eligible for any of the listed loans.")
      else:
          time.sleep(3)
          print("Which of these eligible loans would you like to choose from (Input bank name or type '0' for none)? ")
          for i in eligible:
              print("- " + i)

          chosen_loan = input("")
          chosen_loan = chosen_loan.upper()

          while True:
              if chosen_loan in eligible or chosen_loan == "0":
                  break
              else:
                  print("Invalid Option, make sure spelling is correct \n")
                  chosen_loan = input("Which of these eligible loans would you like to choose from (Input bank name "
                                      "or type '0' for none)? ")
                  for i in eligible:
                      print("- " + i)

          if chosen_loan == "RBC":
              print("Congratulations, you have qualified for a $20,000 subsidy")
              balance += 20000
              loan_expense = 20000
          elif chosen_loan == "TD":
              print("Congratulations, you have qualified for a $10,000 loan")
              balance += 10000
              loan_expense = 10000
          elif chosen_loan == "CIBC":
              print("Congratulations, you have qualified for a $100,000 loan")
              balance += 100000
              loan_expense = 100000
          elif chosen_loan == "SCOTIABANK":
              print("Congratulations, you have qualified for a $100,000 loan")
              balance += 100000
              loan_expense = 100000
          elif chosen_loan == "BMO":
              print("Congratulations, you have qualified for a $70,000 subsidy")
              balance += 70000
              loan_expense = 70000
          elif chosen_loan == "0":
              print("You have not selected a loan/subsidy")

# if 8 is chosen, the program allows the user to pay off part of their loan based on how many years it been since their acquired it.
  elif option == "8":
      if chosen_loan == "":
        print("Please go to option 7 and pick a loan/subsidy")
      elif chosen_loan == "RBC" or chosen_loan == "BMO":
        print("You do not have to repay any loans")
      elif chosen_loan == "DONE":
        print("You already repaid your loan!")
      else:
        
        years = int(input("How many FULL years have passed since you received your loan? ")) 
        if chosen_loan == "TD": 
            amount_due = round((10000*(1 + 0.01)**years - loan_paid), 2)
            while True:
              loan_repay = input("At the current time, your loan repayment is $%d. Would you like to pay some of it back right now? Type '1' for YES or '0' for NO: " % amount_due)
              if loan_repay == "1":
                payment = float(input("How much do you want to pay? ")) 
                if balance >= payment:
                  balance -= payment
                  print ("Payment successful. Your balance is now $%.2f" % balance)
                  loan_paid += payment
                  if payment == amount_due:
                    chosen_loan = "DONE"
                else:
                  print ("You do not have sufficient funds.")
                break
              elif loan_repay == "0":
                print ("The loan was not repaid")
                break
              else:
                print ("Invalid input")
        elif chosen_loan == "CIBC":
            amount_due = round((100000*(1 + 0.021)**years - loan_paid), 2)
            while True:
              loan_repay = input("At the current time, your loan repayment is $%. Would you like to pay some of it back right now? Type '1' for YES or '0' for NO: " % amount_due)
              if loan_repay == "1":
                payment = float(input("How much do you want to pay? ")) 
                if balance >= payment:
                  balance -= payment
                  print ("Payment successful. Your balance is now $%.2f" % balance)
                  loan_paid += payment
                  if payment == amount_due:
                    chosen_loan = "DONE"
                else:
                  print ("You do not have sufficient funds.")
                break
              elif loan_repay == "0":
                print ("The loan was not repaid")
                break
              else:
                print ("Invalid input")
        elif chosen_loan == "SCOTIABANK":
            amount_due = round((100000*(1 + 0.032)**years - loan_paid), 2)
            while True:
              loan_repay = input("At the current time, your loan repayment is $%.2f. Would you like to pay some of it back right now? Type '1' for YES or '0' for NO: " % amount_due)
              if loan_repay == "1":
                payment = float(input("How much do you want to pay? ")) 
                if balance >= payment:
                  balance -= payment
                  print ("Payment successful. Your balance is now $%.2f" % balance)
                  loan_paid += payment
                  if payment == amount_due:
                    chosen_loan = "DONE"
                else:
                  print ("You do not have sufficient funds.")
                break
              elif loan_repay == "0":
                print ("The loan was not repaid")
                break
              else:
                print ("Invalid input")

  elif option == "9": # if 9 is chosen, it displays the menu
      print("""\nSmiley Smoothies Menu:""")
      print("|  Strawberry Smoothie  |   Mango Smoothie   | Berry Blast Smoothie |")
      print("| - Strawberries        | - Mangoes          | - Frozen Berries     |")
      print("| - Yogurt              | - Yogurt           | - Yogurt             |")
      print("| - Milk                | - Milk             | - Milk               |")
      print("| - Ice Cubes           | - Ice Cubes        | - Ice Cubes          |")
      print("""\nInventory List:""")
      print("| 1. Strawberries       | 2. Yogurt          | 3. Milk              |")
      print("| 4. Ice Cubes          | 5. Mangoes         | 6. Frozen Berries    |")

  elif option == "10": # if 10 is chosen, the program ends
      print("Goodbye.")
      break

  else: # if the user inputs an invalid option, ask to input again
      print("Invalid input, please select a listed option")
