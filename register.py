# views.py
from django.http import JsonResponse
from .models import User
from .utils import hash_password, connect_to_db, disconnect_from_db

async def register(request):
    if request.method == 'POST':
        # Assuming JSON data is sent in the request body
        json_data = json.loads(request.body)

        # Connect to the database
        connect_to_db()

        # Check if user already exists
        if User.objects.filter(email=json_data['email']).exists():
            return JsonResponse({'message': 'User exists!'}, status=200)

        # Hash the password
        hashed_password = hash_password(json_data['password'])

        # Create a new user object
        new_user = User(
            firstname=json_data['firstname'],
            lastname=json_data['lastname'],
            password=hashed_password,
            email=json_data['email'],
            street=json_data['street'],
            city=json_data['city'],
            country=json_data['country'],
            phone=json_data['phone']
        )

        try:
            # Save the new user object to the database
            new_user.save()
            return JsonResponse({'message': 'Data saved successfully!'}, status=201)
        except Exception as e:
            # Handle database save errors
            return JsonResponse({'message': 'Something went wrong! ' + str(e)}, status=500)
        finally:
            # Disconnect from the database
            disconnect_from_db()
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)
