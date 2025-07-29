# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
total_height = height ** 2
BMI = float(weight/total_height)

if BMI >= 35:
  res = "you are clinically obese."
elif BMI >= 30 and BMI < 35 :
  res = "you are obese."
elif BMI >= 25 and BMI < 30 :
  res = "you are slightly overweight."
elif BMI >= 18.5 and BMI < 25 :
  res = "you have a normal weight."
else : 
  res = "you are underweight."

print(f"Your BMI is {BMI}, {res} ")
