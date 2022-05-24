check_days = int(input())
doctor = 7
treated_patients = 0
untreated_patients = 0
for i in range(1, check_days + 1):
    patients = int(input())
    if i % 3 == 0 and untreated_patients > treated_patients:
        doctor += 1
    if patients >= doctor:
        treated_patients = treated_patients + doctor
    else:
        treated_patients = treated_patients + patients
    if (patients - doctor) > 0:
        untreated_patients = patients - doctor + untreated_patients
    else:
        untreated_patients = untreated_patients
print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")
