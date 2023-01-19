from flask import render_template, request, flash, redirect, url_for
from app import app, db
from app.forms import LoginForm, AddEmployeeForm, AddDepartmentForm, UpdateEmployeeForm, UpdateDepartmentForm, DeleteEmployeeForm, DeleteDepartmentForm
from app.models import Department, Employee

titles = {"junior":2, "senior":3, "lead":4, "manager": 5}
employees = [
        {
            "name": "Ahmed Ahmed",
            "title": "Manager",
            "experience_years": 10,
            "salary": 5000,
            "department": "R&D"
        },
        {
            "name": "Ali Ali",
            "title": "Lead",
            "experience_years": 6,
            "salary": 4000,
            "department": "R&D"
        }
    ]


@app.route('/')
@app.route('/employees')
def employees():
    emps = Employee.query.all()
    return render_template('employees.html', title='Home', employees=emps)

@app.route('/departments')
def departments():
    deps = Department.query.all()
    return render_template('departments.html', title='Departments', departments=deps)

@app.route('/add_employee', methods=['GET', 'POST'])
def add_employee():
    form = AddEmployeeForm()
    if form.validate_on_submit():
        try:
            title = request.form['employee_title'].lower()
            if title in titles:
                factor = titles[title]
            else:
                flash('Not a proper title, choosing junior as title')
                title = 'junior'
                factor = titles[title]
            exp_yrs = int(request.form['employee_experience'])
            salary = exp_yrs*factor*300

        except:
            salary = 0
            title = 'junior'
            flash('Experience Years must be a whole numeric value')
            return render_template('/add_employee.html', title='Add New Employee', form=form)
        
        e = Employee(
            name=request.form['employee_name'],
            title=title.lower(),
            exp_yrs=exp_yrs,
            salary=salary,
            department=request.form['employee_department']
            )


        try:
            deps = Department.query.all()
            for dep in deps:
                if dep.name == e.department:
                    db.session.add(e)
                    db.session.commit()
                    flash('Employee added: {}'.format(form.employee_name.data))
                    return redirect(url_for('employees'))
            flash('Wrong department use a valid department')
            return render_template('add_employee.html', title='Add New Employee', form=form)
           

        except:
            flash('ERROR IN SQL QUERY TRY ADDING AGAIN')
            return render_template('/add_employee.html', title='Add New Employee', form=form)
        
        
    return render_template('/add_employee.html', title='Add New Employee', form=form)

@app.route('/add_department', methods=['GET', 'POST'])
def add_department():
    form = AddDepartmentForm()
    if form.validate_on_submit():
        name = request.form['department_name']
        manager = request.form['department_manager']
        d = Department(name=name,
                       dep_manager=manager
            )

        try:
            db.session.add(d)
            db.session.commit()

        except:
            flash('ERROR IN SQL QUERY TRY ADDING AGAIN')
            return render_template('add_department.html', title='Add New Department', form=form)

        flash('Department added: {}'.format(
            form.department_name.data))
        
        
        return redirect(url_for('departments'))
    return render_template('add_department.html', title='Add New Department', form=form)

@app.route('/update_employee', methods=['GET', 'POST'])
def update_employee():
    form = UpdateEmployeeForm()
    if form.validate_on_submit():
        try:
            title = request.form['employee_title'].lower()
            if title in titles:
                factor = titles[title]
            else:
                flash('Not a proper title, choosing junior as title')
                title = 'junior'
                factor = titles[title]
            exp_yrs = int(request.form['employee_experience'])
            salary = exp_yrs*factor*300

        except:
            salary = 0
            title = 'junior'
            flash('Experience Years must be a whole numeric value')
            return render_template('update_employee.html', title='Update an Employee', form=form)
        
        
        try:
            deps = Department.query.all()
            e = Employee.query.filter_by(id= int(request.form['employee_id'])).first()
            e.name = request.form['employee_name']
            e.title=title.lower()
            e.exp_yrs=exp_yrs
            e.salary = salary
            e.department=request.form['employee_department']

            for dep in deps:
                if dep.name == e.department:
                    db.session.commit()
                    flash('Employee Updated: {}'.format(form.employee_name.data))
                    return redirect(url_for('employees'))
            flash('Wrong department, use a valid department')
            return render_template('update_employee.html', title='Update an Employee', form=form)
           

        except:
            flash('ERROR IN SQL QUERY TRY UPDATING AGAIN')
            return render_template('update_employee.html', title='Update an Employee', form=form)
        
        
    return render_template('update_employee.html', title='Update an Employee', form=form)

@app.route('/update_department', methods=['GET', 'POST'])
def update_department():
    form = UpdateDepartmentForm()
    if form.validate_on_submit():
        dep_name = request.form['department_name']
        manager = request.form['department_manager']
        
        try:
            d = db.get_or_404(Department, dep_name)
            d.dep_manager= manager
            db.session.commit()

        except:
            flash('ERROR IN SQL QUERY TRY UPDATING AGAIN')
            return render_template('update_department.html', title='Update a Department', form=form)

        flash('Department added: {}'.format(
            form.department_name.data))
        
        return redirect(url_for('departments'))
    return render_template('update_department.html', title='Update a Department', form=form)

@app.route('/delete_employee', methods=['GET', 'POST'])
def delete_employee():
    form = DeleteEmployeeForm()
    if form.validate_on_submit():
    
        try:
            e = Employee.query.filter_by(id= int(request.form['employee_id'])).first()
            name = e.name
            db.session.delete(e)
            db.session.commit()
            flash('Employee Removed: {}'.format(name))
            return redirect(url_for('employees'))
            
        except:
            flash('ERROR IN SQL QUERY TRY UPDATING AGAIN')
            return render_template('delete_employee.html', title='Remove an Employee', form=form)
        
        
    return render_template('delete_employee.html', title='Remove an Employee', form=form)


@app.route('/delete_department', methods=['GET', 'POST'])
def delete_department():
    form = DeleteDepartmentForm()
    if form.validate_on_submit():
        dep_name = request.form['department_name']
        try:
            d = db.get_or_404(Department, dep_name)
            db.session.delete(d)
            db.session.commit()
            flash('Department Removed: {}'.format(dep_name))
            return redirect(url_for('departments'))
            
        except:
            flash('ERROR IN SQL QUERY TRY UPDATING AGAIN')
            return render_template('delete_department.html', title='Remove a Department', form=form)
        
        
    return render_template('delete_department.html', title='Remove a Department', form=form)