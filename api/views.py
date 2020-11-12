from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
import requests

from .serializers import CategorySerializer, ProductsSerializer, OrderSerializer, TrdelnikSerializer
from .models import Category, Products, Order, Trdelnik
# Create your views here.


class OrderView(APIView):
    def post(self, request):
        order = 'Заказ: ' + '\n' + str(request.data["order"]) + '\n'
        adress = 'Адресс: ' + str(request.data["adress"]) + '\n'
        name = 'Имя: ' + str(request.data["name"]) + '\n'
        mobile = 'Телефон: ' + str(request.data["mobile"]) + '\n'
        networth = 'Сумма: ' + str(request.data["networth"]) + "тг" + '\n'
        body = order + adress + name + mobile + networth
        url = f'http://api.telegram.org/bot1182982253:AAGIDEpYjzsbXd1z0k8oXdbCSuXSgiKwhPw/sendMessage?chat_id=@Eliks_BOOT&text=' + body
        requests.get(url).content
        return Response(status=201)

    def get(self, request):
        order = Order.objects.all()
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)


class TrdelnikView(APIView):
    def get(self, request):
        trdelnik = Trdelnik.objects.all()
        serializer = TrdelnikSerializer(trdelnik, many=True)
        return Response(serializer.data)

    def post(self, request):
        trdelnik = TrdelnikSerializer(data=request.data)
        name = 'Имя: ' + str(request.data["name"]) + '\n'
        mobile = 'Номер: ' + str(request.data["mobile"]) + '\n'
        trdelnik_type = 'Тип: ' + str(request.data["trdelnik_type"]) + '\n'
        pomazka_type = 'Помазка: ' + str(request.data["pomazka_type"]) + '\n'
        posypka_type = 'Посыпка: ' + str(request.data["posypka_type"]) + '\n'
        nachinka_type = 'Начинка: ' + str(request.data["nachinka_type"]) + '\n'
        iceCream_type = 'Мороженое: ' + \
            str(request.data["iceCream_type"]) + '\n'
        Topping_type = 'Топпинг: ' + str(request.data["Topping_type"]) + '\n'
        Decorations_type = 'Украшения: ' + \
            str(request.data["Decorations_type"]) + '\n'
        Adress_type = 'Адресс: ' + str(request.data["Adress_type"]) + '\n'
        body = name + mobile + trdelnik_type + pomazka_type + posypka_type + nachinka_type + \
            iceCream_type + Topping_type + Decorations_type + Adress_type
        url = f'http://api.telegram.org/bot1182982253:AAGIDEpYjzsbXd1z0k8oXdbCSuXSgiKwhPw/sendMessage?chat_id=@Eliks_BOOT&text=' + body
        requests.get(url).content
        if trdelnik.is_valid():
            trdelnik.save()
        return Response(status=201)


class CategoryListApiView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ProductsListApiView(ListAPIView):
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()


class CategoryDetail(RetrieveAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'id'
