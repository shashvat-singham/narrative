import csv
from django.shortcuts import render
from .models import StudentData

def upload_csv(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']
        decoded_file = csv_file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)

        for row in reader:
            name = f"{row['First Name']} {row['Last Name']}"
            school = row['School']
            location = row['Location']
            state = 'MA' if 'Boston' in location else 'CA'  # Example mapping logic

            for class_key in ['Class 1', 'Class 2']:
                StudentData.objects.create(
                    name=name,
                    class_name=row[class_key],
                    school=school,
                    state=state
                )
        return render(request, 'uploader/upload_success.html')

    return render(request, 'uploader/upload.html')
