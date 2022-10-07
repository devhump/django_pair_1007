from multiprocessing import context
from django.shortcuts import redirect, render
from reviews.forms import ReviewsForm
from .models import Reviews

# Create your views here.
def index(request):

    reviews = Reviews.objects.all()

    context = {
        'reviews' : reviews,
    }

    return render(request, 'reviews/index.html', context)

def create(request):

    if request.method == "POST":
        reviews_form = ReviewsForm(request.POST)
        if reviews_form.is_valid():
            reviews_form.save()
            return redirect('reviews:index')
    else:
        reviews_form = ReviewsForm()

    context = {
        'reviews_form' : reviews_form,
    }

    return render(request, 'reviews/create.html', context)


def detail(request, pk):

    review = Reviews.objects.get(pk=pk)

    context = {
        'review' : review,
    }

    return render(request, 'reviews/detail.html', context)


def update(request, pk):

    review = Reviews.objects.get(pk=pk)

    if request.method == 'POST':
        reviews_form = ReviewsForm(request.POST, instance=review)
        if reviews_form.is_valid():
            reviews_form.save()
            return redirect('reviews:detail', review.pk)
    else:
        reviews_form  = ReviewsForm(instance=review)

    context = {
        'reviews_form' : reviews_form,
    }

    return render(request, 'reviews/update.html', context)


#get으로 구현, post로 변경 필요
def delete(request, pk):

    review = Reviews.objects.get(pk=pk)
    review.delete()

    return redirect('reviews:index')
