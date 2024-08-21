from rest_framework.response import Response
from rest_framework import status
from analysis.service import DataSerializerService


class DataResponseService(object):
    def __init__(self, csv, *args, **kwargs):
        self.csv = csv
        self.data_serializer = DataSerializerService(csv)

    def get_conversion_rates(self):
        try:
            data = self.data_serializer.serialize_conversion_rates()
            return Response(
                data, 
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {'error': str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def get_status_distributions(self):
        try:
            data = self.data_serializer.serialize_status_distributions()
            return Response(
                data, 
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {'error': str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def get_category_type_performance(self):
        try:
            data = self.data_serializer.serialize_category_type_performance()
            return Response(
                data, 
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {'error': str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def get_averages_per_customer(self):
        try:
            data = self.data_serializer.serialize_averages_per_customer()
            return Response(
                data, 
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {'error': str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )