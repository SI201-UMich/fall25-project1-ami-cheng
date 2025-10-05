# Amelia Cheng
# amicheng
# 2504 8424
# I worked on this project independently

import os
import unittest

class Superstore():
    def __init__(self, filename):
        self.base_path = os.path.abspath(os.path.dirname(__file__))

        self.full_path = os.path.join(self.base_path, filename)

        self.file_obj = open(self.full_path, 'r')

        self.raw_data = self.file_obj.readlines()

        self.file_obj.close()

        self.data_dict = {
            'Ship Mode': [],
            'Mode': [],
            'Segment': [],
            'Country': [],
            'City': [],
            'State': [],
            'Postal Code': [],
            'Region': [],
            'Category': [],
            'Sub-Category': [],
            'Sales': [],
            'Quantity': [],
            'Discount': [],
            'Profit': []
        }

    def build_data_dict(self):

        for i in self.raw_data[1:]:

            item = i.strip().split(',')

            self.data_dict['Ship Mode'].append(item[0])
            self.data_dict['Segment'].append(item[1])
            self.data_dict['Country'].append(item[2])
            self.data_dict['City'].append(item[3])
            self.data_dict['State'].append(item[4])
            self.data_dict['Postal Code'].append(int(item[5]))
            self.data_dict['Region'].append(item[6])
            self.data_dict['Category'].append(item[7])
            self.data_dict['Sub-Category'].append(item[8])
            self.data_dict['Sales'].append(float(item[9]))
            self.data_dict['Quantity'].append(int(item[10]))
            self.data_dict['Discount'].append(float(item[11]))
            self.data_dict['Profit'].append(float(item[12]))

    # ========== Calculations for Category Profit ==========
        """
        This Calculation iterates category and profit column and returns to the name of 
        category with the highest average profit with the profit amount

        Return:
            String with category name with the highest profit and average profit amount
            (example: Furniture $100.70)
         """
    # creates a list of profit assigned to their categories
    def group_profits_by_category(self):
        grouped = {}
        categories = self.data_dict['Category']
        profits = self.data_dict["Profit"]

        for i in range(len(categories)):
            category = categories[i]
            profit = profits[i]

            if category not in grouped:
                grouped[category] = []
            grouped[category].append(profit)

        return grouped
    
    # calculate average profit for each category
    def average_profit(self, profit_dict):
        dict = {}
        for category in profit_dict:
            profit = profit_dict[category]
            if profit:
                avg = sum(profit)/ len(profit)
            dict[category] = avg
        return dict
    
    # find the highest average profit and its category
    def max_average_profit(self, average_profit_dict):
        return ""
    
    # print category with highest profit
    def category_profit(self):
        return ""
    
    # ========== Calculations for State Ship Mode ==========
        """
        This Calculation iterates ship mode and state column and returns to the name of
        the most common ship mode in each state with the percentage of state's most common ship mode out of
        all ship mode

        Return:
            String with state, most commonly used ship mode name, and the percentage of
            the state's most common ship mode out of all ship mode (example: Alaska: First Class 55%)
        """
    # create a list of ship mode assigned to their state
    def group_shipmode_by_state(self):
        return ""
    
    # find most common ship mode in each state and the percentage of most common ship mode used
    def get_most_common_shipmode(self, state_modes_dict):
        return ""
    
    # format result output
    def format_result(self, state_mode_summary):
        return ""
    
    # input result for each state into format function
    def state_shipmode(self):
        return ""

class TestSuperstoreReader(unittest.TestCase):
    def setUp(self):
        self.superstore_reader = Superstore('SampleSuperstore.csv')
        self.superstore_reader.build_data_dict()

    def test_build_data_dict(self):
        # testing if the length of column matches across the rows
        self.assertEqual(len(self.superstore_reader.data_dict['Ship Mode']), len(self.superstore_reader.data_dict['Profit']))

        # testing if content in columns matches type (ex. int, str, float)
        self.assertTrue(all(isinstance(x, str) for x in self.superstore_reader.data_dict['Ship Mode']))
        self.assertTrue(all(isinstance(x, str) for x in self.superstore_reader.data_dict['Segment']))
        self.assertTrue(all(isinstance(x, str) for x in self.superstore_reader.data_dict['Country']))
        self.assertTrue(all(isinstance(x, str) for x in self.superstore_reader.data_dict['City']))
        self.assertTrue(all(isinstance(x, str) for x in self.superstore_reader.data_dict['State']))
        self.assertTrue(all(isinstance(x, int) for x in self.superstore_reader.data_dict['Postal Code']))
        self.assertTrue(all(isinstance(x, str) for x in self.superstore_reader.data_dict['Region']))
        self.assertTrue(all(isinstance(x, str) for x in self.superstore_reader.data_dict['Category']))
        self.assertTrue(all(isinstance(x, str) for x in self.superstore_reader.data_dict['Sub-Category']))
        self.assertTrue(all(isinstance(x, float) for x in self.superstore_reader.data_dict['Sales']))
        self.assertTrue(all(isinstance(x, int) for x in self.superstore_reader.data_dict['Quantity']))
        self.assertTrue(all(isinstance(x, float) for x in self.superstore_reader.data_dict['Discount']))
        self.assertTrue(all(isinstance(x, float) for x in self.superstore_reader.data_dict['Profit']))

    def test_group_profits_by_category(self):
        grouped = self.superstore_reader.group_profits_by_category()
        self.assertIsInstance(grouped, dict)
        self.assertTrue(all(isinstance(val, list) for val in grouped.values()))
        self.assertIn('Furniture', grouped)
        self.assertIn('Office Supplies', grouped)
    
    def test_average_profit(self):
        test_data = {
            'Furniture': [100.0, 200.0, 300.0], 
            'Technology': [500.0, 500.0]
        }
        result = self.superstore_reader.average_profit(test_data)
        self.assertEqual(result['Furniture'], 200.0)
        self.assertEqual(result['Technology'], 500.0)
    
    def test_max_average_profit(self):
        return ""
    
    def test_category_profit(self):
        return ""
    
    def test_group_shipmode_by_state(self):
        return ""
    
    def test_get_most_common_shipmode(self):
        return ""
    
    def test_format_result(self):
        return ""

    def test_state_shipmode(self):
        return ""

if __name__ == '__main__':
    unittest.main(verbosity=2)