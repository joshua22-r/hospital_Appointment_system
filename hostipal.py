class Patient:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"Patient: {self.name}, Age: {self.age}, Gender: {self.gender}"


class Doctor:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization

    def __str__(self):
        return f"Doctor: {self.name}, Specialization: {self.specialization}"


class Appointment:
    def __init__(self, patient, doctor, date, time):
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time

    def __str__(self):
        return f"Appointment - Date: {self.date}, Time: {self.time}\n{self.patient}\n{self.doctor}"


class Hospital:
    def __init__(self, name):
        self.name = name
        self.appointments = []

    def schedule_appointment(self, patient, doctor, date, time):
        appointment = Appointment(patient, doctor, date, time)
        self.appointments.append(appointment)
        return appointment

    def list_appointments(self):
        print(f"Appointments at {self.name}:\n")
        for appointment in self.appointments:
            print(appointment)
            print("\n" + "-" * 30)


if __name__ == "__main__":
    hospital = Hospital("City Hospital")

    while True:
        print("\nOptions:")
        print("1. Schedule Appointment")
        print("2. List Appointments")
        print("Type 'exit' to exit.")

        choice = input("Enter your choice: ")

        if choice.lower() == 'exit':
            break

        if choice == '1':
            patient_name = input("Enter patient name: ")
            patient_age = int(input("Enter patient age: "))
            patient_gender = input("Enter patient gender: ")

            doctor_name = input("Enter doctor name: ")
            doctor_specialization = input("Enter doctor specialization: ")

            appointment_date = input("Enter appointment date (YYYY-MM-DD): ")
            appointment_time = input("Enter appointment time: ")

            patient = Patient(patient_name, patient_age, patient_gender)
            doctor = Doctor(doctor_name, doctor_specialization)

            hospital.schedule_appointment(patient, doctor, appointment_date, appointment_time)
            print("Appointment scheduled successfully!")

        elif choice == '2':
            hospital.list_appointments()

        else:
            print("Invalid choice. Please try again.")
