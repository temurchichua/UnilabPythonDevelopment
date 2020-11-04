from werkzeug.security import generate_password_hash, check_password_hash

hashed_pass = generate_password_hash('bestkeptsecret')
print(f'Hashed_Pass: {hashed_pass}')

check = check_password_hash(hashed_pass, 'wrongpass')
print(f'Result: {check}')

check = check_password_hash(hashed_pass, 'bestkeptsecret')
print(f'Result: {check}')
