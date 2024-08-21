from django.urls import path
from api.views import (
    ConversionRateView,
    StatusDistributionView,
    CategoryTypePerformanceView,
    FilteredAggregationView
)

urlpatterns = [
    path(
        'conversion-rate/', 
        ConversionRateView.as_view(), 
        name='conversion-rate'
    ),
    path(
        'status-distribution/', 
        StatusDistributionView.as_view(), 
        name='status-distribution'
    ),
    path(
        'category-type-performance/', 
        CategoryTypePerformanceView.as_view(), 
        name='category-type-performance'
    ),
    path(
        'filtered-aggregation/', 
        FilteredAggregationView.as_view(), 
        name='filtered-aggregation'
    ),
]