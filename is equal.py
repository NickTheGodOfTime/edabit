def is_equal(obj_one, obj_two):
  if obj_one == obj_two:
      return True
  else:
      return False

first_obj_one = {
  "name": "Benny",
  "phone": "3325558745",
  "email": "benny@edabit.com"
}

first_obj_two = {
  "name": "Jason",
  "phone": "9853759720",
  "email": "jason@edabit.com"
}

e = is_equal(first_obj_one, first_obj_two)
print(e)

second_obj_one = {
  "name": "Jason",
  "phone": "9853759720",
  "email": "jason@edabit.com"
}

second_obj_two = {
  "name": "Jason",
  "phone": "9853759720",
  "email": "jason@edabit.com"
}

e = is_equal(second_obj_one, second_obj_two)
print(e)