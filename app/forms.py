from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class AddEmployeeForm(FlaskForm):
    employee_name = StringField('Employee Name', validators=[DataRequired()])
    employee_title = StringField('Employee Title', validators=[DataRequired()])
    employee_experience = StringField('Exprience Years', validators=[DataRequired()])
    employee_department = StringField('Employee Department', validators=[DataRequired()])
    submit = SubmitField('Add Employee')

class AddDepartmentForm(FlaskForm):
    department_name = StringField('Department Name', validators=[DataRequired()])
    department_manager = StringField('Department Manager')
    submit = SubmitField('Add Department')

class UpdateEmployeeForm(FlaskForm):
    employee_id = StringField('Employee ID to update', validators=[DataRequired()])
    employee_name = StringField('Employee Name update')
    employee_title = StringField('Employee Title update')
    employee_experience = StringField('Exprience Years update')
    employee_department = StringField('Employee Department update')
    submit = SubmitField('Update Employee')

class UpdateDepartmentForm(FlaskForm):
    department_name = StringField('Department Name to update', validators=[DataRequired()])
    department_manager = StringField('Department Manager')
    submit = SubmitField('Update Department')


class DeleteEmployeeForm(FlaskForm):
    employee_id = StringField('Employee ID to remove', validators=[DataRequired()])
    submit = SubmitField('Remove Employee')

class DeleteDepartmentForm(FlaskForm):
    department_name = StringField('Department Name to remove', validators=[DataRequired()])
    submit = SubmitField('Remove Department')