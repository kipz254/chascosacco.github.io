from django.shortcuts import render, redirect

from Chasco.forms import MemberForm, ManagementForm
from Chasco.models import Management, Member


# Create your views here.


def index(request):
    data = Management.objects.all()
    context = {'Team': data}
    return render(request, 'index.html', context)

def membership(request):
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('membership')
    else:
        form = MemberForm()
    return render(request, 'membership.html', {'form': form})

def staff(request):
    if request.method == 'POST':
        form = ManagementForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('staff')
    else:
        form = ManagementForm()
    return render(request, 'staff.html', {'form': form})
