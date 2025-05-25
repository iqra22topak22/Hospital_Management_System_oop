# Hospital Management System with Billing

# Base Class
class Person:
    def __init__(self, name, age, gender, contact):
        self.name = name
        self.age = age
        self.gender = gender
        self.contact = contact

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Contact: {self.contact}")

# Doctor Class (inherits from Person)
class Doctor(Person):
    def __init__(self, name, age, gender, contact, doctor_id, specialization):
        super().__init__(name, age, gender, contact)
        self.doctor_id = doctor_id
        self.specialization = specialization

    def display_info(self):
        super().display_info()
        print(f"Doctor ID: {self.doctor_id}")
        print(f"Specialization: {self.specialization}")

# Patient Class (inherits from Person)
class Patient(Person):
    def __init__(self, name, age, gender, contact, patient_id, disease):
        super().__init__(name, age, gender, contact)
        self.patient_id = patient_id
        self.disease = disease

    def display_info(self):
        super().display_info()
        print(f"Patient ID: {self.patient_id}")
        print(f"Disease: {self.disease}")

# Appointment Class
class Appointment:
    def __init__(self, appointment_id, doctor, patient, date_time):
        self.appointment_id = appointment_id
        self.doctor = doctor
        self.patient = patient
        self.date_time = date_time

    def display_info(self):
        print(f"\n--- Appointment Details ---")
        print(f"Appointment ID: {self.appointment_id}")
        print(f"Date & Time: {self.date_time}")
        print("\nDoctor Info:")
        self.doctor.display_info()
        print("\nPatient Info:")
        self.patient.display_info()

# Billing Class
class Billing:
    def __init__(self, appointment, consultation_fee, medicine_charges, room_charges=0):
        self.appointment = appointment
        self.consultation_fee = consultation_fee
        self.medicine_charges = medicine_charges
        self.room_charges = room_charges
        self.total_amount = 0

    def calculate_total(self):
        self.total_amount = self.consultation_fee + self.medicine_charges + self.room_charges

    def display_bill(self):
        self.calculate_total()
        print(f"\n--- Billing Details ---")
        print(f"Appointment ID: {self.appointment.appointment_id}")
        print(f"Patient Name: {self.appointment.patient.name}")
        print(f"Doctor: {self.appointment.doctor.name}")
        print(f"Consultation Fee: Rs. {self.consultation_fee}")
        print(f"Medicine Charges: Rs. {self.medicine_charges}")
        print(f"Room Charges: Rs. {self.room_charges}")
        print(f"Total Amount: Rs. {self.total_amount}")

# Example Usage
if __name__ == "__main__":
    # Creating Doctor
    doc = Doctor("Dr. Asim", 45, "Male", "0300-1267", "D001", "Cardiology")

    # Creating Patient
    pat = Patient("Ali Raza", 30, "Male", "0312-987", "P100", "Heart Pain")

    # Creating Appointment
    app = Appointment("A500", doc, pat, "2025-06-01 11:00 AM")

    # Display Appointment Info
    app.display_info()

    # Creating and Displaying Billing Info
    bill = Billing(app, consultation_fee=1500, medicine_charges=800, room_charges=2000)
    bill.display_bill()
