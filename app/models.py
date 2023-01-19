from app import db

class Department(db.Model):
    name = db.Column(db.String(100), primary_key=True)
    dep_manager = db.Column(db.String(100))
    employees = db.relationship("Employee", cascade='all,delete')

    def __repr__(self):
        return '<Department {}>'.format(self.name)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    title = db.Column(db.String(100))
    exp_yrs = db.Column(db.Integer)
    salary = db.Column(db.Integer)
    department = db.Column(db.String(100), db.ForeignKey('department.name'), nullable=True)
    
    def __repr__(self):
        return '<Employee {}, Title {}, Exp Yrs {}, Salary {}, Department {}>'.format(
            self.name, self.title, self.exp_yrs, self.salary, self.department)
