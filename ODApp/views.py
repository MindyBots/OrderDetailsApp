import openai
import re
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # Only for demonstration; make sure to use proper CSRF protection in production
def extract_orders(request):
    print(request.method)
    if request.method == "POST":
        try:
            # Get the message content from the POST request body
            request_data = json.loads(request.body.decode("utf-8"))
            message = request_data.get("message", "")

            # Initialize OpenAI API key (usually done outside the view)
            openai.api_key = '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'

            # Preprocess the message
            message = re.sub(r'\n+', ' ', message)
            message = re.sub(r'\s+', ' ', message)

            # Create messages for the OpenAI chat
            messages = [{"role": "system", "content": "You just analyze the text and give order details one by one"}]
            if message:
                messages.append({"role": "user", "content": message})

            # Call OpenAI API
            chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
            reply = chat.choices[0].message.content

            # Return the reply as JSON response
            return JsonResponse({"reply": reply})

        except Exception as e:
            # Handle any exceptions
            return JsonResponse({"error": str(e)})

    else:
        return JsonResponse({"error": "Only POST requests are allowed for this view"})
