from student import *

@app.route("/addStdeunt/details" ,methods=['POST'])
def add_student():
    student_data=request.get_json()
    Student.add_student(student_data["name"],student_data["age"],student_data["section"],student_data["gender"])
    response=Response("student added",200, mimetype='application/json')
    return response

@app.route('/getAllStudents', methods=['GET'])
def get_all_students():
    return jsonify({'Students': Student.get_all_students()})

@app.route("/hello")
def display():
    return {"hello":"bhuvanesh"}

@app.route("/updateStudent/<id>",methods=['PUT'])
def update_Student(id):
    student_data=request.get_json()
    Student.update_Student(id,student_data["name"],student_data["age"],student_data["section"],student_data["gender"])
    response = Response("student updated", 200, mimetype='application/json')
    return response

@app.route("/find/student/id/<id>",methods=['GET'])
def get_student_by_id(id):
    student=Student.get_student_by_id(id)
    return jsonify(student)

@app.route("/delete/by/id/<id>",methods=['DELETE'])
def delete_student(id):
    Student.delete_student(id)
    response=Response("student deleted",status=200)
    return response


if __name__ == '__main__':
    app.run(port=80,debug=True)

