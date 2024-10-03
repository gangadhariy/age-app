def new_func():
    while True:
      age = input("enter your age: ")
      if age == "":
          print("please enter valid age")
          continue
      elif age.isalpha():  # age.isdigit() checks if all characters are digits
            print("Please enter a valid numeric age.")
            continue
      else:
          age = int(age)
          if age < 13:
              return"child"
              break
          elif age <= 18:
              return"adult"
              break
          else:
              return"senior"
              break
text = new_func()
if text == "child":
    print("He should be in school")
elif text == "adult":
    print("he should be in collage")
else:
    print("he should be in job or buisiness")