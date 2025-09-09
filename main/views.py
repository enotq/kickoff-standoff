from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'store' :   'Kickoff Standoff',
        'npm'   :   '2306275941',
        'name'  :   'Ahmad Aqeel Saniy',
        'class' :   'PBP A'
    }
    return render(request, 'main.html', context)