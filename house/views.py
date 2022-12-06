from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import Paginator
from django.urls import reverse
from django.http import HttpResponseRedirect
from house.choices import price_choices, bedroom_choices, city_choices, area_choices
from .models import Listing
from .forms import ListingForm, ListingFormSet
from accounts.models import Profile

def create(request, pk):
    profile= Profile.objects.get(id=pk)
    form = ListingForm()
    if request.method == 'POST':
      form =ListingForm(request.POST, request.FILES)
      if form.is_valid():
          new_question = form.save(commit=False)
          question_formset = ListingFormSet(request.POST, instance=new_question)
          if question_formset.is_valid():
              form.save()
              question_formset.save()
              return HttpResponseRedirect(reverse('polls:detail',args=(new_question.pk,)))
      else:
          print(form.errors)
    else:
        form = ListingForm()
        question_formset = ListingFormSet(instance=Listing())
    return render(request, "listings/listing_create.html", {'form':form, 'question_formset':question_formset,})

def listing_create(request):
    form = ListingForm()
    if request.method == "POST":
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.lessor = request.user.Profile
            instance.save()
            return redirect('/listings')
    context={
        "form": form
    }
    return render(request,"listings/listing_create.html",context)

def listing_list(request):
    listings=Listing.objects.order_by('-list_date')
    paginator = Paginator(listings,6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context={
        'listings':paged_listings
    }
    return render(request, "listings/listings.html",context)

def listing_retrieve(request,listing_id):
    listing= Listing.objects.get(pk=listing_id)
    listings2=Listing.objects.order_by('-list_date')[:6]
    context={
        "listing":listing,
        "listings2": listings2
    }
    return render(request, "listings/detail.html",context)



def search(request):
    queryset_list = Listing.objects.order_by('price','area','-list_date')
    #pagnination
    
    # Keywords 
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(address__icontains=keywords) |  queryset_list.filter(description__icontains=keywords)
    
    # city 
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact = city)

    # bedrooms 
    if 'area' in request.GET:
        area = request.GET['area']
        if area:
            queryset_list = queryset_list.filter(area__lte = area)
    
    # price 
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte= price)
    #Page
    paginator = Paginator(queryset_list,6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context =  {
        
        "city_choices": city_choices,
        "price_choices":price_choices,
        "area_choices":area_choices,
        "bedroom_choices":bedroom_choices,
        "listings":paged_listings,
        "values":request.GET,
    }
    return render(request,'listings/search.html',context)


