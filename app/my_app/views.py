from django.shortcuts import render
from django.template.defaulttags import comment
from django.views import View

from my_app.forms import WriteLineForm
from my_app.models import Customer


class MainView(View):

    def get(self, request):
        context = {
            'form': WriteLineForm(),
            'title': "Форма для ввода данных",
        }
        return render(request, 'form.html', context)

    def post(self, request, firstname, lastname, age, comment):
        form = WriteLineForm(request.POST)
        if form.is_valid():
            Customer.objects.create(
                firstname=form.cleaned_data.get("firstname"),
                lastname=form.cleaned_data.get("lastname"),
                age=form.cleaned_data.get("age"),
                comment=form.cleaned_data.get("comment"),
            )
            context = {
                "users": Customer.objects.all(),
                "title": "Profile"
            }
            print(f'{firstname} | {lastname} | {age} | {comment}')
            return render(request, "form.html", context)
