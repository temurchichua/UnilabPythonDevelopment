from models import db, Teacher, Student, Books

tengo = Student("tengo")
mariami = Student("mariami")

# Add puppies to database
db.session.add_all([tengo,mariami])
db.session.commit()