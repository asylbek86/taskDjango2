from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView

from .models import Car, CommentCar
from .forms import CarForm, CommentFrom
from django.http import HttpResponse



# Форма добавление коментарии

class CarCommentView(CreateView):
    template_name = 'car_comment.html'
    form_class = CommentFrom
    queryset = Car.objects.all()
    success_url = '/cars/'
    def get_object(self, **kwargs):
        car_id = self.kwargs.get('id')
        return get_object_or_404(CommentCar, id=car_id)


    def form_valid(self, form):
        print(form.clean)
        return super(CarCommentView, self).form_valid(form=form)


#**************************************************************************

def car_list_view(request):
    cars = Car.objects.all()
    return render(request, 'car_list.html', {'cars': cars})



def car_detail_view(request, id):
    car_detail = get_object_or_404(Car, id=id)
    return render(request, 'car_detail.html', {'car_detail': car_detail})


# добавление машины

def car_create_view(request):
    method = request.method
    if method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h2>Машина успешно добавленно</h2>')
    else:
        form = CarForm()
    return render(request, 'car_create.html', {'form': form})

# изменение и обновление машин

def update_object_view(request, id):
    car_object = get_object_or_404(Car, id=id)
    if request.method == 'POST':
        form = CarForm(instance=car_object, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Машина успешно обновлено</h1>')
    else:
        form = CarForm(instance=car_object)
        return render(request, 'update_car.html', {'form': form,
                                                                        'object': car_object
                                                                        })


# Удаление машины


def delete_object_view(request, id):
    car_object = get_object_or_404(Car, id=id)
    car_object.delete()
    return HttpResponse('<h1>Машина успешно удалено</h1>')










