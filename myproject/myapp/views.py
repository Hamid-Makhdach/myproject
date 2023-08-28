from django.shortcuts import render
from django.views import View
import pickle
# Create your views here.

class PredictionView(View):
    template_name = 'result.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        new_text = request.POST.get('text')
        paragraphs = new_text.split('.')

        predictions = []
        for paragraph in paragraphs:
            # Effectuer la prédiction
            model = pickle.load(open('ml_model/fakenews.pkl', 'rb'))
            prediction = model.predict([paragraph])[0]
            predictions.append(prediction)

        context = {'paragraphs': paragraphs, 'predictions': predictions}
        return render(request, self.template_name, context)




