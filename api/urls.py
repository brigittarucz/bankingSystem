from django.urls import path
from .views import CurrencyList, SymbolList, RateList
from .views import api_rate, api_currency_detail, api_rate_historical_from, api_rate_historical_range, api_convert
from .views import api_rate_historical_post, api_currency_update

app_name = 'api'

urlpatterns = [
    path('symbols/', SymbolList.as_view()),
    path('latest/', CurrencyList.as_view()),
    path('latest/<str:currency_code>/', api_currency_detail, name="detail"),
    path('rates/', RateList.as_view()),
    path('create/', api_rate_historical_post, name="create"),
    path('update/<str:currency_code>/', api_currency_update, name="edit"),
    path('rates/<str:rate_code>/', api_rate),
    path('rates/<str:rate_code>/<int:rate_from>/', api_rate_historical_from),
    path('rates/<str:rate_code>/<int:rate_from>/<int:rate_to>/', api_rate_historical_range),
    path('convert/<str:rate_code_from>/<str:rate_code_to>/<int:amount>/', api_convert),
]