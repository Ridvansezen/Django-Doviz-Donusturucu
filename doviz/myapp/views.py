from django.shortcuts import render
import requests
from django.views.decorators.csrf import csrf_exempt

api_key = "your-api"

url = "http://data.fixer.io/api/latest?access_key=" + api_key

@csrf_exempt
def index(request):
    if request.method == "POST":
        firstCurrency = request.POST.get("firstCurrency") # USD
        secondCurrency = request.POST.get("secondCurrency") # TRY

        amount = request.POST.get("amount") # 15
        response = requests.get(url)
        infos =  response.json()

        firstValue = infos["rates"][firstCurrency] # 1.231066
        secondValue = infos["rates"][secondCurrency] # 4.690815

        result = (secondValue / firstValue) * float(amount)

        currencyInfo = dict()

        currencyInfo["firstCurrency"] = firstCurrency
        currencyInfo["secondCurrency"] = secondCurrency
        currencyInfo["amount"] = amount
        currencyInfo["result"] = result

        return render(request, "index.html", {"info": currencyInfo})
    else:
        return render(request, "index.html" )
