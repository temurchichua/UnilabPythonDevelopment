from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

password = "bestkeptsecret"

hashed_pass = bcrypt.generate_password_hash(password=password)

print(f'Hashed_Pass: {hashed_pass}')

check = bcrypt.check_password_hash(hashed_pass, 'wrongPassword')

print(f'result: {check}')

check = bcrypt.check_password_hash(hashed_pass, 'bestkeptsecret')

print(f'result: {check}')
