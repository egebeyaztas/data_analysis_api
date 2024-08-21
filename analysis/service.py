from enum import Enum
from analysis.data_processing import DataProcessor
import json


class DataSerializerService(object):
    
    class FilterType(Enum):
        CONVERSION = "CONVERSION"
        AWARENESS = "AWARENESS"
        ENGAGEMENT = "ENGAGEMENT"

    def __init__(
            self, csv, 
            filter_type=FilterType.CONVERSION, 
            *args, **kwargs):
        self.csv = csv
        self.processing = DataProcessor(csv)
        self.filter_type = filter_type.value

    def serialize_conversion_rates(self):
        data = self.processing.calculate_conversion_rates()
        conversion_rates = data.get(
            'group_conversion_rate', 
            None
        )
        serialized_conversion_rates = json.loads(
            conversion_rates.to_json()
        )
        result = {
            "highest_conversion_rate": {
                "customer_id": data.get(
                    'highest_conversion_customer', 
                    None
                ),
                "conversion_rate": data.get(
                    'highest_conversion_rate_value', 
                    None
                )
            },
            "lowest_conversion_rate": {
                "customer_id": data.get(
                    'lowest_conversion_customer', 
                    None
                ),
                "conversion_rate": data.get(
                    'lowest_conversion_rate_value', 
                    None
                )
            }
        }
        data = {
            "conversion_rates": serialized_conversion_rates,
            **result
        }
        return data

    def process_status_distribution(self, status_distribution):
        result = {"statuses": {}}
        for _, row in status_distribution.iterrows():
            status = row['status']
            type_ = row['type']
            category = row['category']
            count = row['count']
            
            if status not in result["statuses"]:
                result["statuses"][status] = {}
            
            if type_ not in result["statuses"][status]:
                result["statuses"][status][type_] = {"category": {}}
            
            result["statuses"][status][type_]["category"][category] = {
                "count": count
            }
        return result

    def serialize_status_distributions(self):
        status_distribution, status_totals = self.processing.calculate_status_distribution()
        result = self.process_status_distribution(status_distribution)
        status_totals = json.loads(status_totals.to_json())
        status_totals_dict = {"status_totals": status_totals}
        data = result | status_totals_dict
        return data
    
    def process_category_type_performance(self, performance):
        performance_dict = {}
        for _, row in performance.iterrows():
            category = row['category']
            type_ = row['type']
            revenue = row['revenue']
            conversions = row['conversions']
            
            if category not in performance_dict:
                performance_dict[category] = {}
                
            if type_ not in performance_dict[category]:
                performance_dict[category][type_] = {}
                
            performance_dict[category][type_] = {
                'revenue': revenue,
                'conversions': conversions
            }
        final_json = {'performance_summary': performance_dict}
        return final_json

    def serialize_category_type_performance(self):
        performance, top_performance = self.processing.calculate_category_type_performance()
        result = self.process_category_type_performance(
            performance
        )
        top_performance = json.loads(
            top_performance.to_json()
        )
        top_category_type_dict = {
            "top_category_and_type": top_performance
        }
        data = result | top_category_type_dict
        return data

    def process_averages_per_customer(self, col):
        filtered_data = self.processing.filter_by_type(self.filter_type)
        average_per_customer = filtered_data.groupby(
            'customer_id'
        ).agg({col: 'mean'}).reset_index()
        return average_per_customer

    def serialize_averages_per_customer(self):
        average_revenues = self.process_averages_per_customer(
            'revenue'
        )
        average_conversions = self.process_averages_per_customer(
            'conversions'
        )
        revenues_dict = average_revenues.set_index(
            'customer_id'
        )['revenue']
        conversions_dict = average_conversions.set_index(
            'customer_id'
        )['conversions']

        data = {
            "average_conversions": json.loads(
                conversions_dict.to_json()
            ),
            "average_revenues": json.loads(
                revenues_dict.to_json()
            )
        }     
        return data
