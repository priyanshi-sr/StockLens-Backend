
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import StockIndex


class IndexData(APIView):
    def get(self, request, *args, **kwargs):
        name = request.GET.get('id')
        print(name)
        stock_indices = StockIndex.objects.filter(name=name)
        print(stock_indices)
        data = {}
        if stock_indices.exists():
            for index in stock_indices:
                data = {
                    'name': index.name,
                    'image_url': index.image.url,
                    'api_url': index.url
                }
        else:
            data['error'] = 'Not found'
        return Response(data)