from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from decouple import config
from api.service import DataResponseService

csv = config('CSV_FILE')
service = DataResponseService(csv)


class ConversionRateView(APIView):
    def get(self, request, *args, **kwargs):
        return service.get_conversion_rates()


class StatusDistributionView(APIView):
    def get(self, request, *args, **kwargs):
        return service.get_status_distributions()


class CategoryTypePerformanceView(APIView):
    def get(self, request, *args, **kwargs):
        return service.get_category_type_performance()


class FilteredAggregationView(APIView):
    def get(self, request, *args, **kwargs):
        return service.get_averages_per_customer()
