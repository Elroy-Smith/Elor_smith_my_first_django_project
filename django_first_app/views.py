from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from django_first_app.models import Book

# Create your views here.
number = 10
products = []


def index(request):
    login = request.POST.get("login", "")
    password = request.POST.get("password", "")
    return render(request, "django_first_app/index.html",
                  {"names": ["Ala", "Ela", "Ola"],
                   "login": login,
                   "password": password})


def main(request):
    name = request.GET.get("name")
    name_list = request.GET.getlist("name")
    return HttpResponse(
        "<a href='/hello/?name=Jan'>Hello Jan</a>Witaj w Django! Pierwszy widok napisany!" + str(name) + str(name_list))


def hello(request):
    name = request.GET.get("name", "")
    return HttpResponse("Hello " + name)


def game(request):
    message = ""
    try:
        guess = request.GET.get("guess")
        guessNumber = int(guess)
        if guessNumber > number:
            message = "twoja liczba jest za duża"
        elif guessNumber < number:
            message = "twoja liczba jest za mała"
        else:
            message = "zgadłeś"
    except:
        pass
    return HttpResponse("<form><input name='guess' placeholder='zgadnij liczbę (1-100)'></form>" + message)


def article(request, id):
    return HttpResponse(str(id))


def form(request):
    if request.method == "GET":
        return render(request, "django_first_app/form.html")

    if request.method == "POST":
        product = request.POST.get("product")
        products.append(product)
        return redirect("/product/")


def show_products(request):
    return render(request, "django_first_app/products.html", {"products": products})


class BookAddView(View):
    def get(self, request):
        return render(request, "django_first_app/book_form.html")

    def post(self, request):
        title = request.POST.get("title")
        author = request.POST.get("author")
        description = request.POST.get("description")
        rating = request.POST.get("rating")
        price = request.POST.get("price")
        page_count = request.POST.get("page_count")
        Book.objects.create(title=title, author=author, description=description, rating=rating, price=price, page_count=page_count)
        return redirect("/book/")

def show_all_books(request):
    books = Book.objects.all()

    return render(request, "django_first_app/book_list.html", {"books":books})

def fizz_buzz(request):
    n = int(request.GET.get("n"))
    fizbuzlista = list(range(1, n))
    data = []
    fizz = 3
    buzz = 7
    for element in fizbuzlista:
        if element % (fizz * buzz) == 0:
            data.append("FizzBuzz")
        elif element % fizz == 0:
            data.append("Fizz")
        elif element % buzz == 0:
            data.append("Buzz")
        else:
            data.append(element)
    return render(request, "django_first_app/fizzbuzz.html", {"data": data})