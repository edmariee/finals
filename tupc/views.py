from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from .forms import SignUpUser, OrgInfoForm, OfficersInfoForm, ActivitiesInfoForm, ReportsInfoForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def home(request):
	organizationID = OrganizationInfo.objects.all()
	context = {'organizationID': organizationID}
	return render(request, 'Home.html', context)

#FOR ADMIN (ORGANIZATION)
@login_required(login_url='login')
def organization(request):
	form = OrgInfoForm()
	if request.method == 'POST':
		form = OrgInfoForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/History')
		
	context = {'form':form}

	return render(request, 'org.html', context)

@login_required(login_url='login')
#Update
def update(request, pk):
	organizationID = OrganizationInfo.objects.get(id=pk)
	form = OrgInfoForm(instance=organizationID)

	if request.method == 'POST':
		form = OrgInfoForm(request.POST, instance=organizationID)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'org.html', context)



#-----------------------------------------------


def loginPage(request):

	if request.user.is_authenticated:
		return redirect('login')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('signup')
			else:
				messages.info(request, 'The email and password you entered did not match our records. Please double-check and try again.')

		context = {}
		return render(request, 'login.html', context)



def signup(request):
	if request.user.is_authenticated:
		return redirect('org')
	else:
		form = SignUpUser()
		if request.method == 'POST':
			form = SignUpUser(request.POST)
			if form.is_valid():
				form.save()
				return redirect('/org')
		
	context = {'form':form}

	return render(request, 'signup.html', context)



#ADMIN ACCESS
#CRUD
@login_required(login_url='login')
def history (request):
	studentID = OfficersInfo.objects.all()
	context = {'studentID': studentID}
	return render(request, 'History.html', context)


#ADMIN ACCESS
#Activities Data
#@login_required(login_url='login')
def editable (request):
	activityView = ActivitiesInfo.objects.all()
	context = {'activityView': activityView}
	return render(request, 'Editable.html', context)


#ADMIN ACCESS
#View for Reports List
#@login_required(login_url='login')
def table (request):
	reportsView = ReportsInfo.objects.all()
	context = {'reportsView': reportsView}
	return render(request, 'table.html', context)

#--------------------------------------------------------

#Form For Officers
def form(request):
	form = OfficersInfoForm()
	if request.method == 'POST':
		form = OfficersInfoForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('crud')
	context = {'form':form}

	return render(request, 'FormOfficers.html', context)

#CRUD
@login_required(login_url='login')
def crud (request):
	studentID = OfficersInfo.objects.all()
	context = {'studentID': studentID}
	return render(request, 'CRUD.html', context)


#Activities Form
def nextpage(request):

	form = ActivitiesInfoForm()
	if request.method == 'POST':
		form = ActivitiesInfoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/Data')
	context = {'form':form}
	return render(request, 'Activities.html', context)


@login_required(login_url='login')
#Activities Data
def data (request):
	activityView = ActivitiesInfo.objects.all()
	context = {'activityView': activityView}
	return render(request, 'Data.html', context)


#View for Actiivties Data
def view_data(request, pk):
	activityView = ActivitiesInfo.objects.get(id=pk)
	form = ActivitiesInfoForm(instance=activityView)

	if request.method == 'POST':
		form = ActivitiesInfoForm(request.POST, instance=activityView)
		if form.is_valid():
			form.save()
			return redirect('/Data')

	context = {'form':form}
	return render(request, 'Activities.html', context)

#Reports Form
def activity(request):
	form = ReportsInfoForm()
	if request.method == 'POST':
		form = ReportsInfoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/View')
	context = {'form':form}

	return render(request, 'Reports.html', context)

#View for Reports List
@login_required(login_url='login')
def view (request):
	reportsView = ReportsInfo.objects.all()
	context = {'reportsView': reportsView}
	return render(request, 'View.html', context)


#About US
def report(request):
	form = ()
	context =  {'form':form}
	return render(request, 'AboutUS.html', context)




def logoutUser(request):
	logout(request)
	return redirect('login')
