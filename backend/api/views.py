from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['POST'])
def calculate_sum(request):
    numbers = request.data.get('numbers', [])
    total = sum(numbers)
    return Response({'sum': total})

    
