from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash
from sqlalchemy import or_
from app import db
from app.models import Employee

employee_bp = Blueprint('employee', __name__)

@employee_bp.route('/')
def list_employees():
    employees = Employee.query.all()
    return render_template('employees.html', employees=employees)

@employee_bp.route('/register_employee', methods=['GET', 'POST'])
def register_employee():
    if request.method == 'POST':
        name = request.form['name']
        cpf = request.form['cpf']
        email = request.form['email']
        password = request.form['password']
        phone = request.form['phone']
        birthdate = request.form['birthdate']
        position = request.form['position']
        salary = float(request.form['salary'])
        access_key = request.form['access_key']

        existing = Employee.query.filter(or_(Employee.cpf == cpf, Employee.access_key == access_key)).first()
        if existing:
            flash('CPF ou chave de acesso já cadastrados.', 'danger')
            return redirect(url_for('employee.register_employee'))

        try:
            new_employee = Employee(
                name=name,
                cpf=cpf,
                email=email,
                password=generate_password_hash(password),
                phone=phone,
                birthdate=birthdate,
                position=position,
                salary=salary,
                access_key=access_key
            )
            db.session.add(new_employee)
            db.session.commit()
            flash('Funcionário cadastrado com sucesso!', 'success')
            return redirect(url_for('employee.list_employees'))
        except Exception as e:
            db.session.rollback()
            flash(f'Erro ao cadastrar funcionário: {str(e)}', 'danger')
            return redirect(url_for('employee.register_employee'))

    return render_template('register_employee.html')

@employee_bp.route('/delete_employee/<int:employee_id>', methods=['POST'])
def delete_employee(employee_id):
    employee = Employee.query.get_or_404(employee_id)
    try:
        db.session.delete(employee)
        db.session.commit()
        flash('Funcionário excluído com sucesso.', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Erro ao excluir funcionário: {str(e)}', 'danger')
    return redirect(url_for('employee.list_employees'))

@employee_bp.route('/edit_employee/<int:employee_id>', methods=['POST'])
def edit_employee(employee_id):
    employee = Employee.query.get_or_404(employee_id)

    if request.method == 'POST':
        try:
            employee.name = request.form['name']
            employee.cpf = request.form['cpf']
            employee.email = request.form['email']
            employee.phone = request.form['phone']
            employee.birthdate = request.form['birthdate']
            employee.position = request.form['position']
            employee.salary = float(request.form['salary'])
            employee.access_key = request.form['access_key']
            db.session.commit()
            flash('Funcionário atualizado com sucesso.', 'success')
            return redirect(url_for('employee.list_employees'))
        except Exception as e:
            db.session.rollback()
            flash(f'Erro ao atualizar funcionário: {str(e)}', 'danger')
            return redirect(url_for('employee.edit_employee', employee_id=employee_id))

    return render_template('edit_employee.html', employee=employee)

