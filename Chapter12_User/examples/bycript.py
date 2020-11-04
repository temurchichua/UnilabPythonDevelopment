from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

password = "bestkeptsecret"

# პაროლის ჰეშირება
hashed_password = bcrypt.generate_password_hash(password=password)
print(f'Hashed Pass: {hashed_password}')

# პაროლის შემოწმება
password = 'wrongpassword'
check = bcrypt.check_password_hash(hashed_password, password)
print(f'Result: {check}')

password = 'bestkeptsecret'
check = bcrypt.check_password_hash(hashed_password, password)
print(f'Result: {check}')
