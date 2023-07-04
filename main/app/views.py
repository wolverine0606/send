from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
import stripe

@csrf_exempt
@require_POST
def stripe_webhook(request):
    payload = request.body
    # import pdb
    # pdb.set_trace()

    event = None

    try:
        event = stripe.Event.construct_from(
            json.loads(payload), 'sk_test_51NNZ45FcZHEL6zHAuKQTq99kmAaQUn7V17ravCBMB7dxv17ZjFGpzT6MIyP6u3tY25HHFv2ABKZbtxPv55bCQOnv00bzALwigR'
        )
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)
    if event.type == 'charge.succeeded':   
        payment_intent = event.data.object.billing_details.email
        print(payment_intent)
        # email = SendGridEmailMessage('Subject', 'Body', 'dimaspotapov0606@gmail.com', ['Dmytro.Potapov@muuvr.io'])
        # email.send() 
    elif event.type == 'payment_intent.failed':
        pass
    else:
        return JsonResponse({'status': 'success', 'message': 'Unhandled event'})
    return JsonResponse({'status': 'success'})
def home(request):
    return(render(request, 'index.html'))


