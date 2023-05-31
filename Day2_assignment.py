current_year = int(2023)

year_of_birth = int(input('Enter Year Of Birth: '))

age = int(0)

age = int(current_year - year_of_birth)

mytext = 'You are %s years old.'

print(mytext % age)

if age < 18 :

  print('NOT VALID AGE!')

elif age > 100:

    print('NOT VALID AGE!')

else:

  print('Welcome To The Portal.')

  age_value = age;

 

gender = input("Enter F for female, M for male and O for others :--> ")

if gender == 'F' or gender =='f':

   print ("Female")

   gender_value = "f"

elif gender == 'M' or gender == 'm':

      print ("Male")

      gender_value = "m"

else:

   print ("Not valid Gender!")

 

principal = float(input("Input you current prinicpal amount  "))

import locale

locale.setlocale(locale.LC_ALL, '')

print(locale.currency(principal, grouping=True))

 

interest = int(0)

if gender_value == "f" and age > 59 :

   interest = principal * 8

   if gender_value == "f" and age < 60 :

      interest = principal * 6

   elif gender_value == "m" and age > 59 :

      interest = principal * 7

   elif gender_value == "m" and age < 59 :

      interest = principal * 5

 

import locale

locale.setlocale(locale.LC_ALL, '')

interest_amount = (locale.currency(interest, grouping=True))

 

print("Your Gender is: " + gender_value)

print("Your age is: " + age + "Your Principal amount is: " + principal + " Interest Amount: " + interest)