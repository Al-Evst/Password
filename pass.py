print("Введи пароль: ")
password = str(input())

def is_very_long(password):
    if len(password) >= 12:
        return True
    else:
        return False

def has_digit(password):
  for frm in password:
    if frm.isdigit(password):
      return True
  return False

# def raiting(password):
#   score = 0
#   if is_very_long(password):
#     score += 2
#   elif has_digit(password):
#     score += 2
#   elif has_letters(password):
#     score += 2
#   elif has_upper_letters(password):
#     score += 2
#   elif has_lower_letters(password):
#     score += 2
#   return score
  
def has_letters(password):
  for lt in password:
    if lt.isalpha():
      return True
  return False

def has_upper_letters(password):
  for up in password:
    if up.isupper():
      return True
  return False

def has_lower_letters(password):
  for lw in password:
    if lw.islower():
      return True
  return False

# is_very_long()
# has_digit()
# has_letters()
# has_upper_letters()
# has_lower_letters()

def call_fun():
    some_func = [is_very_long, has_digit, has_letters, has_upper_letters,has_lower_letters]
    score = 0
    for func in some_func:
        if func(password):
            score += 2

print(call_fun())