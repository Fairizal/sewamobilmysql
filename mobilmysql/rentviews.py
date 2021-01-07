from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Rent
from .forms import RentForm
from django.views.generic import ListView, DetailView
from django.db.models import F

class IndexView(ListView):
    template_name = 'rent/index.html'
    context_object_name = 'rent_list'

    def get_queryset(self):
        # rent = Rent.objects.select_related('idCars').annotate(carsName=F('idCars__carsName')).values('id', 'carsName', 'rentDate', 'rentDateBack', 'statusRent').all()
        rent = Rent.objects.all()
        # print(rent)
        return rent
        # return Rent.objects.all()

class RentDetailView(DetailView):
    model = Rent
    template_name = 'rent/detail.html'

def create(request):
    if request.method == 'POST':
        form = RentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('rentindex')
    form = RentForm()

    return render(request,'rent/create.html',{'form': form})

def detail(request, pk, template_name='rent/detail.html'):
    rent = get_object_or_404(Rent, pk=pk)
    form = RentForm(request.POST or None, instance=rent)
    if form.is_valid():
        form.save()
        return redirect('rentindex')
    return render(request, template_name, {'form':form})

def edit(request, pk, template_name='rent/edit.html'):
    rent = get_object_or_404(Rent, pk=pk)
    form = RentForm(request.POST or None, instance=rent)
    if form.is_valid():
        form.save()
        return redirect('rentindex')
    return render(request, template_name, {'form':form})

def delete(request, pk, template_name='rent/confirm_delete.html'):
    rent = get_object_or_404(Rent, pk=pk)
    if request.method=='POST':
        rent.delete()
        return redirect('rentindex')
    return render(request, template_name, {'object':rent})