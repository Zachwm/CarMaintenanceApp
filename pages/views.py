from django.shortcuts import render

def home_view(request):
    return render(request, "home.html")

def sign_in(request):
    return render(request, "sign_in.html")

def sign_up(request):
    return render(request, "sign_up.html")

def signing_up(request):
    return render(request, "vehicles.html")

def vehicles(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        return render(request, 'vehicles.html', {'username': username})
    else:
        return render(request, 'signup.html')
    
def new_vehicle(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        return render(request, 'new_vehicle.html', {'username': username})
    else:
        return render(request, 'new_vehicle.html')
    
def adding_new_vehicle(request):
    if request.method == 'POST':
        username = request.POST.get('username') 
        oil_change_date = request.POST.get('oil_change_date') 
        oil_change_miles = request.POST.get('oil_change_miles') 
        brake_pads_date = request.POST.get('brake_pads_date') 
        brake_pads_miles = request.POST.get('brake_pads_miles')  
        air_filter_date = request.POST.get('air_filter_date')  
        battery_check_date = request.POST.get('battery_check_date')

        new_vehicle = {
            'oil_change_date': oil_change_date,
            'oil_change_miles': oil_change_miles,
            'brake_pads_date': brake_pads_date,
            'brake_pads_miles': brake_pads_miles,
            'air_filter_date': air_filter_date,
            'battery_check_date': battery_check_date
        }

        vehicles = []

        vehicles.append(new_vehicle)

        return render(request, 'vehicles.html', {
            'username': username,
            'vehicles': vehicles
        })
    else:
        return render(request, 'signup.html')
