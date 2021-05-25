from settings import *
import json
from flask_migrate import Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Student(db.Model):
    __tablename__='student_table'
    student_id=db.Column(db.Integer,primary_key=True)
    student_name=db.Column(db.String(20),nullable=False)
    student_age=db.Column(db.Integer,nullable=False)
    student_section=db.Column(db.String(6),nullable=False)
    student_gender=db.Column(db.String(6),nullable=False)

    def json(self):
        return {'id':self.student_id,'name':self.student_name,'age':self.student_age,
                'section':self.student_section,'gender':self.student_gender}

    # def __init__(self,name,age,section,gender):
    #     self.name=name
    #     self.age=age
    #     self.section=section
    #     self.gender=gender
    def add_student(name,age,section,gender):
        new_student=Student(student_name=name,student_age=age,student_section=section,student_gender=gender)
        db.session.add(new_student)
        db.session.commit()


    def get_all_students():
            return [Student.json(student) for student in Student.query.all()]


    def update_Student(id,name,age,section,gender):
        updateStudent=Student.query.filter_by(student_id=id).first()
        updateStudent.student_name=name
        updateStudent.student_age=age
        updateStudent.student_section=section
        updateStudent.student_gender=gender
        db.session.commit()

    def get_student_by_id(id):


        return [Student.json(Student.query.filter_by(student_id=id).first())]



    def delete_student(id):

        Student.query.filter_by(student_id=id).delete()
        db.session.commit()






