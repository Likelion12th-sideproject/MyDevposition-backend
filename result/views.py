from django.http import JsonResponse
from .models import TestResult
from rest_framework.views import APIView
import json



class ResultView(APIView):
    def post(self, request):
        try:
            data = json.loads(request.body)
            result = data.get('result')
            
            if result not in [choice[0] for choice in TestResult._meta.get_field('result').choices]:
                return JsonResponse({'status': 'error', 'message': 'Invalid result value'}, status=400)
            test_result = TestResult.objects.create(result=result)
            print('success')
            return JsonResponse({'result': test_result.result}, status=201)
        
        except Exception as e:
            print('failed')
            return JsonResponse({'message': str(e)}, status=400)
