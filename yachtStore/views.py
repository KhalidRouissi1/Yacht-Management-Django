from django.shortcuts import render
from django.contrib.auth.decorators import login_required



def index(req):
    is_authenticated = req.user.is_authenticated
    return render(req,"store/home.html", {'is_authenticated': is_authenticated})

@login_required
def buyYacht(req):
    return render(req,"store/index.html")



@login_required
def shOwYachts(req):
    return render(req,"store/addpage.html")


@login_required
def editYacht(req):
    return render(req,"store/adminActions/edit.html")


def addd(request):
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

