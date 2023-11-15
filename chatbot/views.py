from django.shortcuts import render
from django.http import JsonResponse
from bardapi import Bard
# Create your views here.
def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = "Thanks for choosing YD chatbot!"
        bard = Bard(token='xxxxx') # Your token here
        response = bard.get_answer(message)['content']
        return JsonResponse({'message':message,'response': response})
    return render(request, 'chatbot.html')
    
def retrain(request):
    return JsonResponse({'message':'Retraining is in progress!'})