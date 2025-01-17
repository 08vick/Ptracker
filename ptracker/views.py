from datetime import timedelta, datetime

from django.shortcuts import render, get_object_or_404, redirect

from .forms import PregnancyForm
from .models import Pregnancy



# Create your views here.

def index(request):
    pregnancy_info = None
    error = None

    if request.method == 'POST':
        form = PregnancyForm(request.POST)
        if form.is_valid():
            # Save the pregnancy object if the form is valid
            pregnancy = form.save()

            # Calculate pregnancy info (due date, trimester, etc.)
            pregnancy_info = calculate_pregnancy_info(pregnancy.lmp_date)

            # Optionally, redirect to another page after successful submission
            return redirect('pregnancy_list')  # Example: redirect to the pregnancy list page
        else:
            error = "Please correct the errors below."

    else:
        form = PregnancyForm()

    return render(request, 'index.html', {'form': form, 'pregnancy_info': pregnancy_info, 'error': error})



def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        # Handle form submission (e.g., store the data in the database or send email)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # You can store the data or send an email here
        return render(request, 'contact.html', {'message': 'Thanks for reaching out!'})

    return render(request, 'contact.html')


def calculate_pregnancy_info(lmp_date):
    # Convert the input string date into a datetime object
    current_date = datetime.now().date()  # Get only the date part
    days_pregnant = (current_date - lmp_date).days
    due_date = lmp_date + timedelta(days=280)
    weeks_pregnant = days_pregnant // 7
    if weeks_pregnant < 13:
        trimester = "First Trimester"
    elif weeks_pregnant < 27:
        trimester = "Second Trimester"
    else:
        trimester = "Third Trimester"

    return {
        "weeks_pregnant": weeks_pregnant,
        "due_date": due_date.strftime("%B %d, %Y"),
        "trimester": trimester
    }


def pregnancy_list(request):
    pregnancies = Pregnancy.objects.all()  # Get all pregnancies from the database
    return render(request, 'pregnancy_list.html', {'pregnancies': pregnancies})



def immunization_schedule(request, pregnancy_id):
    # Get the Pregnancy object based on the provided pregnancy_id
    pregnancy = get_object_or_404(Pregnancy, id=pregnancy_id)

    # Call the get_immunization_schedule method of the pregnancy instance
    immunization_schedule = pregnancy.get_immunization_schedule()

    # If no immunization schedule, handle this gracefully (e.g., return an error or message)
    if immunization_schedule is None:
        return render(request, 'error.html', {'message': 'No birth date available for immunization schedule'})

    # Render the immunization schedule template with data
    return render(request, 'immunization_schedule.html', {
        'pregnancy': pregnancy,
        'immunization_schedule': immunization_schedule
    })


def update_pregnancy(request, pregnancy_id):
    # Get the pregnancy record by its ID
    pregnancy = get_object_or_404(Pregnancy, id=pregnancy_id)

    # If it's a POST request, update the pregnancy record
    if request.method == "POST":
        form = PregnancyForm(request.POST, instance=pregnancy)  # Populate the form with existing data
        if form.is_valid():
            form.save()  # Save the updated data to the database
            return redirect('pregnancy_list')  # Redirect to the pregnancy list page after successful update
    else:
        form = PregnancyForm(instance=pregnancy)  # Pre-fill the form with existing data

    # Render the form for updating the pregnancy record
    return render(request, 'update_pregnancy.html', {'form': form, 'pregnancy': pregnancy})


def delete_pregnancy(request, pregnancy_id):
    # Get the pregnancy record by its ID
    pregnancy = get_object_or_404(Pregnancy, id=pregnancy_id)

    # If it's a POST request, delete the pregnancy record
    if request.method == "POST":
        pregnancy.delete()  # Delete the pregnancy record from the database
        return redirect('pregnancy_list')  # Redirect to the pregnancy list page after successful deletion

    return render(request, 'confirm_delete.html', {'pregnancy': pregnancy})





