from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404,redirect
from .forms import YakhtForm  # Import your form
from .models import Yacht


def index(req):
    is_authenticated = req.user.is_authenticated
    return render(req,"store/home.html", {'is_authenticated': is_authenticated})








def add(request):
    if request.method == "POST":
        form = YakhtForm(request.POST)
        if form.is_valid():
            yakht = Yacht(
                description=form.cleaned_data['description'],
                title=form.cleaned_data['title'],
                image=form.cleaned_data[' image'],
                price =form.cleaned_data['price']
            )
            yakht.save()
            return redirect('/show')
    else:
        form = YakhtForm()
    return render(request, 'addpage.html', {'yakhtf': form})


@staff_member_required
def editYacht(request, id):
    yakht = get_object_or_404(Yacht, id=id)
    if request.method == "POST":
        form = YakhtForm(request.POST, request.FILES, instance=yakht)
        if form.is_valid():
            form.save()
            return redirect('/buy')
    else:
        form = YakhtForm(instance=yakht)

    return render(request, 'store/adminActions/edit.html', {'Yakht': yakht, 'form': form})
@staff_member_required
def delete (request,id):
    yakhtid=Yacht.objects.get(id=id)
    yakhtid.delete()
    return redirect('/buy')



@staff_member_required
def add(request):
    if request.method == "POST":
        form = YakhtForm(request.POST, request.FILES)  # Note the use of request.FILES for handling image upload
        if form.is_valid():
            yakht = form.save(commit=False)
            # You may want to set additional fields or perform additional logic here before saving

            yakht.save()
            return redirect('/show')  # Adjust the redirect URL as needed
    else:
        form = YakhtForm()

    return render(request, 'store/adminActions/addpage.html', {'form': form})


def getById(request,yid):
    yacht = get_object_or_404(Yacht, id=yid)
    return render(request, 'store/yachtDetails.html', {'Yakht': yacht})
def show(request):
    all_yakhts = Yacht.objects.all()
    
    return render(request, 'store/showAll.html',{"data":all_yakhts})