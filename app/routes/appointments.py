from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models import Appointment, Customer, Employee
from datetime import datetime

appointments_bp = Blueprint('appointments', __name__)

@appointments_bp.route('/')
def list_appointments():
    appointments = Appointment.query.order_by(Appointment.date.desc()).all()
    return render_template('appointments.html', appointments=appointments)

@appointments_bp.route('/new', methods=['GET', 'POST'])
def create_appointment():
    if request.method == 'POST':
        try:
            date = datetime.strptime(request.form['date'], '%Y-%m-%dT%H:%M')
            description = request.form['description']
            appt_type = request.form.get('type')  
            customer_id = request.form.get('customer_id') or None
            employee_id = request.form.get('employee_id') or None

            appointment = Appointment(
                type=appt_type,
                date=date,
                description=description,
                customer_id=customer_id,
                employee_id=employee_id
            )
            db.session.add(appointment)
            db.session.commit()
            flash('Consulta agendada com sucesso.', 'success')
            return redirect(url_for('appointments.list_appointments'))
        except Exception as e:
            db.session.rollback()
            flash(f'Erro ao agendar consulta: {str(e)}', 'danger')
            return redirect(url_for('appointments.create_appointment'))
    customers = Customer.query.all()
    employees = Employee.query.all()
    return render_template('new_appointment.html', customers=customers, employees=employees)

@appointments_bp.route('/cancel/<int:appointment_id>', methods=['POST'])
def cancel_appointment(appointment_id):
    appointment = Appointment.query.get_or_404(appointment_id)
    appointment.status = 'Cancelada'
    db.session.commit()
    flash('Consulta cancelada.', 'info')
    return redirect(url_for('appointments.list_appointments'))
