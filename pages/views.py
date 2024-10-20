from django.shortcuts import render
import pyrebase
from django.contrib import auth

config={
    "apiKey": "AIzaSyDKBnDqbSJ7DTDjriTSon4rCDQiCatiKhs",
    "authDomain": "car-maintenenance-web-app.firebaseapp.com",
    "databaseURL": "https://car-maintenenance-web-app-default-rtdb.firebaseio.com",
    "projectId": "car-maintenenance-web-app",
    "storageBucket": "car-maintenenance-web-app.appspot.com",
    "messagingSenderId": "6873408904",
    "appId": "1:6873408904:web:9903a858b5f5814d4c463d",
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()

def home_view(request):
    return render(request, "home.html")

def sign_in(request):
    return render(request, "sign_in.html")

def sign_up(request):
    return render(request, "sign_up.html")

def postsignin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = authe.sign_in_with_email_and_password(username, password)
        except:
            message = "Invalid credentials"
            return render(request, "sign_in.html", {"messg": message})

        uid = user['localId']
        name = database.child(uid).child('name').get().val()

        return render(request, 'vehicles.html', {'uid': uid, 'name': name})
    else:
        return render(request, 'sign_in.html')
    
def postsignup(request):
    name = request.POST.get('name')
    username = request.POST.get('username')
    password = request.POST.get('password')

    try:
        user = authe.create_user_with_email_and_password(username, password)
    except:
        message = "Error creating user"
        return render(request, "sign_up.html", {"messg": message})
    
    uid = user['localId']

    authe.sign_in_with_email_and_password(username, password)

    database.child(uid).child('name').set(name)

    return render(request, "vehicles.html", {'uid': uid, 'name': name})
    
def forgotPassword(request):
    return render(request, 'accountRecovery.html')

    
def new_vehicle(request):
    if request.method == 'POST':
        uid = request.POST.get('uid')
        name = request.POST.get('name')
        return render(request, 'new_vehicle.html', {'uid': uid, 'name': name})
    else:
        return render(request, 'new_vehicle.html')
    
def adding_new_vehicle(request):
    if request.method == 'POST':
        uid = request.POST.get('uid')
        name = request.POST.get('name')
        manufacturer = request.POST.get('manufacturer')
        model = request.POST.get('model')
        year = request.POST.get('year')
        oil_change_date = request.POST.get('oil_change_date') 
        oil_change_miles = request.POST.get('oil_change_miles') 
        brake_pads_date = request.POST.get('brake_pads_date') 
        brake_pads_miles = request.POST.get('brake_pads_miles')  
        air_filter_date = request.POST.get('air_filter_date')  
        battery_check_date = request.POST.get('battery_check_date')

        vehicle_data = {
            'manufacturer': manufacturer,
            'model': model,
            'year': year,
            'oil_change_date': oil_change_date,
            'oil_change_miles': oil_change_miles,
            'brake_pads_date': brake_pads_date,
            'brake_pads_miles': brake_pads_miles,
            'air_filter_date': air_filter_date,
            'battery_check_date': battery_check_date
        }

        vehicles_ref = database.child(uid).child('vehicles')
        vehicles_ref.push(vehicle_data)

        return render(request, 'vehicles.html', {'uid': uid, 'name': name})
    else:
        return render(request, 'sign_in.html')

    
def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return render(request, 'home.html')

def deleteaccount(request):
    uid = request.POST.get('uid')
    print(uid)
    database.child(uid).remove()

    user = authe.current_user
    authe.delete_user_account(user['idToken']) 
    
    return render(request, 'home.html')