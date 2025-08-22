from django.http import JsonResponse

def test_api(request):
	if request.method == 'GET':
		return JsonResponse({'message': 'Test API response'})
	return JsonResponse({'error': 'Method not allowed'}, status=405)
