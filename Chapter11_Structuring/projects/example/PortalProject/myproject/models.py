



class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    #  One_to_one relationship
    # A student only has one teacher, thus uselist is False.
    # Strong assumption of 1 teacher per 1 student and vice versa.
    teacher = db.relationship('Teacher', backref="student", uselist=False)

    def __init__(self, name):
        # მხოლოდ გვჭირდება ამ ბაზის მოდელისთვის უნიკალური წევრის ატრიბუტის აღწერა
        self.name = name

    def __repr__(self):
        if self.teacher:
            return f"სტუდენტი {self.name}-ს მასწავლებელი არის {self.teacher.name}."
        else:
            return f"სტუდენტ {self.name}-ს არ ჰყავს მასწავლებელი."


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Connect the teacher to the Student that "owns" it.
    # We use student.id because __tablename__='student'
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    name = db.Column(db.String)

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def __repr__(self):
        return f"მასწავლებლის სახელი: {self.name}"
