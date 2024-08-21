import pandas as pd


class DataProcessor(object):
    def __init__(self, csv, *args, **kwargs):
        self.df = pd.read_csv(csv)

    def calculate_conversion_rates_by_customer(
            self, *args, **kwargs):
        try:
            grouped = self.df.groupby('customer_id').sum()
            grouped['conversion_rate'] = (
                grouped['conversions'] / grouped['revenue']
            ) * 100
        except Exception as e:
            return e
        return grouped

    def calculate_conversion_rates(self, *args, **kwargs):
        try:
            grouped = self.calculate_conversion_rates_by_customer()
            group_conversion_rate = grouped['conversion_rate']
            highest_conversion_customer = group_conversion_rate.idxmax()
            lowest_conversion_customer = group_conversion_rate.idxmin()
            highest_conversion_rate_value = float(
                grouped.loc[
                    highest_conversion_customer, 
                    'conversion_rate'
                ]
            )
            lowest_conversion_rate_value = float(
                grouped.loc[
                    lowest_conversion_customer, 
                    'conversion_rate'
                ]
            )
        except Exception as e:
            return e
        return {
            'group_conversion_rate': group_conversion_rate,
            'highest_conversion_rate_value':highest_conversion_rate_value, 
            'lowest_conversion_rate_value':lowest_conversion_rate_value,
            'highest_conversion_customer':highest_conversion_customer,
            'lowest_conversion_customer':lowest_conversion_customer
        }
    
    def calculate_status_distribution(self, *args, **kwargs):
        try:
            status_distribution = self.df.groupby(
                ['status', 'type', 'category']
            ).size().reset_index(name="count")
            status_totals = self.df.groupby(
                'status'
                ).agg(
                    {
                        'revenue': 'sum', 
                        'conversions': 'sum'
                    }
                )
        except Exception as e:
            return e
        return status_distribution, status_totals
    
    def calculate_category_type_performance(self, *args, **kwargs):
        try:
            category_type_performance = self.df.groupby(
                ['category', 'type']
            ).agg(
                {'revenue': 'sum', 'conversions': 'sum'}
            ).reset_index()
            max_conversions_combination = category_type_performance.loc[
                category_type_performance['conversions'].idxmax()
            ]
        except Exception as e:
            return e
        return category_type_performance, max_conversions_combination
    
    def filter_by_type(self, type, *args, **kwargs):
        try:
            filtered_data = self.df[self.df['type'] == type]
        except Exception as e:
            return e
        return filtered_data
