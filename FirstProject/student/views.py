from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
# Cette fonction permet d'ajouter et d'afficher les informations des étudiants
def add_show(request):
    if request.method =='POST':
        fm =StudentRegistration(request.POST)
        if fm.is_valid():
            nom=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pwd=fm.cleaned_data['password']
            reg=User( name=nom, email=em,password=pwd)
            reg.save()
            fm = StudentRegistration()  #Renvoyer les valeurs de champs au formulaire 
            
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'student/addandshow.html', {'form':fm, 'stu':stud})
# cette fonction permet de modifier les informations 
def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance = pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk = id)
        fm = StudentRegistration(instance=pi)
    return render(request, "student/updatestudent.html", {"form":fm})

# Cette fonction permet de supprimer les données 
def delete_data(request, id):
    if request.method =="POST":
        pi = User.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect("/")

# Fait par AFOUDAH Melchissedeck