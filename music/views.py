from django.shortcuts import *
from music.models import *
from django.template import RequestContext
from .forms import TopUpForm,UserForm,UserAccountForm
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login

def home(request):
    artist = Artist.objects.all()
    return render(request,'home.html', {'artist': artist, })


def register(request):
    #get the request context
    context = RequestContext(request)

    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        user_ac_form = UserAccountForm(data=request.POST)

        if user_form.is_valid() and user_ac_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)

            user_ac_form.save()
            user.save()
            registered = True
        else:
            print(user_form.errors, user_ac_form.errors)
    else:
        user_form = UserForm()
        user_ac_form = UserAccountForm()
    return render_to_response('register.html',
                              {'user_form': user_form,
                               'user_ac_form': user_ac_form
                               , 'registered': registered},
                              context
                              )

def user_login(request):
    context = RequestContext(request)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user =authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("YOUR ACCOUNT IS DORMANT CONTACT HITS254 ADMIN TO ACTIVATE.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    else:
        return render_to_response("login.html", {}, context)
def topup(request):
    if request.method == 'POST':
        form =TopUpForm(request.POST)
        if form.is_valid():

            form.save()
    else:
        form = TopUpForm()
    args ={}
    args.update(csrf(request))
    args['form'] = form
    return render(request, 'topup.html', args)


def transaction_log(request):
    username = request.user
    if username is not None:
        log = AirtimeTopUp.objects.filter(username=request.user)
        return render(request,'logs.html', {'log': log})
    else:
        message="cannot show transaction log for this user"
        return render(request, 'logs.html', {'message': message})