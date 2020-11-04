from werkzeug.security import generate_password_hash, check_password_hash

password = "bestkeptsecret"

# პაროლის ჰეშირება
hashed_pass = generate_password_hash(password)
print(f'Hashed_Pass: {hashed_pass}')

# პაროლის შემოწმება
password = 'wrongpassword'
check = check_password_hash(hashed_pass, password)
print(f'Result: {check}')

password = 'bestkeptsecret'

check = check_password_hash(hashed_pass, password)
print(f'Result: {check}')
