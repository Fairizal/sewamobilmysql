from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cars
from .forms import CarsForm
from django.views.generic import ListView, DetailView

class IndexView(ListView):
    template_name = 'car/index.html'
    context_object_name = 'cars_list'

    def get_queryset(self):
        return Cars.objects.all()

class CarDetailView(DetailView):
    model = Cars
    template_name = 'car/detail.html'

def create(request):
    if request.method == 'POST':
        form = CarsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('carsindex')
    form = CarsForm()

    return render(request,'car/create.html',{'form': form})

def detail(request, pk, template_name='car/detail.html'):
    cars = get_object_or_404(Cars, pk=pk)
    form = CarsForm(request.POST or None, instance=cars)
    if form.is_valid():
        form.save()
        return redirect('carsindex')
    return render(request, template_name, {'form':form})

def edit(request, pk, template_name='car/edit.html'):
    cars = get_object_or_404(Cars, pk=pk)
    form = CarsForm(request.POST or None, instance=cars)
    if form.is_valid():
        form.save()
        return redirect('carsindex')
    return render(request, template_name, {'form':form})

def delete(request, pk, template_name='car/confirm_delete.html'):
    cars = get_object_or_404(Cars, pk=pk)
    if request.method=='POST':
        cars.delete()
        return redirect('carsindex')
    return render(request, template_name, {'object':cars})