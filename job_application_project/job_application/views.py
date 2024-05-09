from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import ApplicantForm, EducationForm, ExperienceForm

def job_application(request):
    if request.method == 'POST':
        applicant_form = ApplicantForm(request.POST)
        education_form = EducationForm(request.POST)
        experience_form = ExperienceForm(request.POST)
        if all([applicant_form.is_valid(), education_form.is_valid(), experience_form.is_valid()]):
            applicant = applicant_form.save()
            # Create an Applicant instance from the form data but don't save it yet
            education = education_form.save(commit=False)
            #Create an Education instance but don't save it yet
            education.applicant = applicant
            #Assign the applicant to the education instanc
            education.save()
            experience = experience_form.save(commit=False)
            experience.applicant = applicant
            experience.save()
            return redirect('success')
    else:
        applicant_form = ApplicantForm()
        education_form = EducationForm()
        experience_form = ExperienceForm()
    return render(request, 'application_form.html', {
        'applicant_form': applicant_form,
        'education_form': education_form,
        'experience_form': experience_form
    })

def success_view(request):
    return render(request, 'success.html')
