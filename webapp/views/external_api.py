import requests
from django.shortcuts import render, redirect
from django.views import View

API_BASE_URL = "http://127.0.0.1:8001/"
API_USERNAME = 'olesia'      
API_PASSWORD = 'python1111' 

class ExternalAirportListView(View):
    template_name = 'webapp/external_airports.html'

    def get(self, request):
        try:
            response = requests.get(f"{API_BASE_URL}airports/", auth=(API_USERNAME, API_PASSWORD))
            if response.status_code == 200:
                airports = response.json()
            else:
                airports = []
        except requests.exceptions.RequestException:
            airports = []

        return render(request, self.template_name, {'airports': airports})

    def post(self, request):
        airport_id = request.POST.get('airport_id')
        
        if airport_id:
            try:
                delete_url = f"{API_BASE_URL}airports/{airport_id}/"
                requests.delete(delete_url, auth=(API_USERNAME, API_PASSWORD))
            except requests.exceptions.RequestException:
                pass 
        return redirect('webapp:external-airport-list')