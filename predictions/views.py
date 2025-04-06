from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Match, Prediction
from datetime import datetime

def home(request):
    return render(request, 'predictions/home.html')

@csrf_exempt
def predict(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            team1 = data.get('team1')
            team2 = data.get('team2')
            
            # 임시 예측 로직 (실제로는 머신러닝 모델을 사용해야 함)
            prediction = {
                'team1_win_probability': 0.6,
                'team2_win_probability': 0.4,
                'predicted_winner': team1
            }
            
            # 데이터베이스에 저장
            match = Match.objects.create(
                team1=team1,
                team2=team2,
                date=datetime.now()
            )
            
            Prediction.objects.create(
                match=match,
                team1_win_probability=prediction['team1_win_probability'],
                team2_win_probability=prediction['team2_win_probability'],
                predicted_winner=prediction['predicted_winner']
            )
            
            return JsonResponse(prediction)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)