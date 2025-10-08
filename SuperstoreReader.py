# Amelia Cheng
# amicheng
# 2504 8424
# I worked on this project independently, with assistance of ChatGPT to correct my function definitions and errors in creating dictionaries

import os
import unittest
import csv

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

    # ========== Write functions into CSV file ==========
    def results_to_csv(self, results, filename="output.csv"):
        output_path = os.path.join(self.base_path, filename)

        with open(output_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            writer.writerow(["Result"])
            
            for line in results:
                writer.writerow([line])

        print(f"Results written to {output_path}")

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
                avg = round(sum(profit)/ len(profit),4)
            dict[category] = avg
        return dict
    
    # find the highest average profit and its category
    def max_average_profit(self, average_profit_dict):
        max_category = None
        max_profit = 0
        for category, profit in average_profit_dict.items():
            if profit > max_profit:
                max_profit = profit
                max_category = category
        return f"{max_category} ${max_profit:.4f}"
    
    # print category with highest profit
    def category_profit(self):
        grouped = self.group_profits_by_category()
        average_profit = self.average_profit(grouped)
        return self.max_average_profit(average_profit)
    
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
        grouped = {}
        states = self.data_dict['State']
        ship_mode = self.data_dict['Ship Mode']

        for i in range(len(states)):
            state = states[i]
            ship_modes = ship_mode[i]

            if state not in grouped:
                grouped[state] = []
            grouped[state].append(ship_modes)

        return grouped

    
    # find most common ship mode in each state and the percentage of most common ship mode used
    def get_most_common_shipmode(self, state_modes_dict):
        result = {}
        for state, modes in state_modes_dict.items():
            if not modes:
                result[state] = {"Ship Mode": None, "Percentage": 0}
                continue

            mode_count = {}
            total = len(modes)

            for mode in modes:
                if mode not in mode_count:
                    mode_count[mode] = 0
                mode_count[mode] += 1

            common_mode = max(mode_count.items(), key= lambda x: x[1])
            mode_name = common_mode[0]
            count = common_mode[1]

            percentage = int((count/total) * 100)
            result[state] = {"Ship Mode": mode_name, "Percentage": percentage}
        return result

    # format result output
    def format_result(self, state_mode_summary):
        list = []
        for state, info in state_mode_summary.items():
            if isinstance (info, dict):
                mode = info["Ship Mode"]
                percentage = info["Percentage"]
                list.append(f"{state}: {mode} {percentage}%")
        return list
    
    # input result for each state into format function
    def state_shipmode(self):
        grouped = self.group_shipmode_by_state()
        result = self.get_most_common_shipmode(grouped)
        return self.format_result(result)

# ========== Test cases for Superstore class ==========
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
            'Furniture': [100.00, 200.00, 300.00], 
            'Technology': [500.0000, 500.0000],
            'Office Supplies': [937.3279, 671.5801, 937.6748],
            'Hygiene': [-2.1853, 580.10 , -908.7594, 0.9457]
        }
        result = self.superstore_reader.average_profit(test_data)
        
        # general cases
        self.assertEqual(result['Furniture'], 200.0000)
        self.assertEqual(result['Technology'], 500.0000)

        # edge cases: negative profit, varied decimal
        self.assertEqual(result['Office Supplies'], 848.8609)
        self.assertEqual(result['Hygiene'], -82.4748)

    def test_max_average_profit(self):
        average_profit_dict = {
            'Furniture': 200.0000,
            'Office Supplies': 848.8609,
            'Technology': 500.0000,
            'Hygiene': -82.4748,
        }
        result = self.superstore_reader.max_average_profit(average_profit_dict)
        self.assertEqual(result, 'Office Supplies $848.8609')
        self.assertFalse(result == 'Hygiene -82.4748')

    def test_category_profit(self):
        result = self.superstore_reader.category_profit()
        self.assertIsInstance(result, str)

    def test_group_shipmode_by_state(self):
        grouped = self.superstore_reader.group_shipmode_by_state()
        self.assertIsInstance(grouped, dict)
        self.assertTrue(all(isinstance(val, list) for val in grouped.values()))
        self.assertIn('Texas', grouped)
        self.assertIn('Washington', grouped)
    
    def test_get_most_common_shipmode(self):
        state_mode_dict = {
            'Alaska': ['First Class', 'First Class', 'First Class', 'Same Day', 'Same Day', 'Second Class'],
            'Washington': ['Same Day', 'Same Day', 'Same Day', 'Same Day', 'First Class', 'Second Class'],
            'Texas': ['First Class', 'Second Class', 'Same Day', 'Standard Class'],
            'Michigan': ['First Class', 'Second Class'],
            'Ohio': []
        }
        result = self.superstore_reader.get_most_common_shipmode(state_mode_dict)
        self.assertIsInstance(result, dict)

        # testing format 
        self.assertIn('Alaska', result)
        self.assertTrue('Ship Mode' in result['Alaska'])
        self.assertTrue('Percentage' in result['Alaska'])

        # general cases for calculation
        self.assertEqual(result['Alaska']['Ship Mode'], 'First Class')
        self.assertEqual(result['Alaska']['Percentage'], 50)
        self.assertEqual(result['Washington']['Ship Mode'], 'Same Day')
        self.assertEqual(result['Washington']['Percentage'], 66)

        # edge cases for calculation: tie in ship modes, no ship mode found
        self.assertEqual(result['Texas']['Ship Mode'], 'First Class')
        self.assertEqual(result['Texas']['Percentage'], 25)
        self.assertEqual(result['Ohio']['Ship Mode'], None)
        self.assertEqual(result['Ohio']['Percentage'], 0)

    def test_format_result(self):
        dict = {
            'Alaska': {'Ship Mode': 'First Class', 'Percentage': 50},
            'Washington': {'Ship Mode': 'Same Day', 'Percentage': 66},
            'Texas': {'Ship Mode': 'First Class', 'Percentage': 25},
            'Ohio': {'Ship Mode': None, 'Percentage': 0}
        }
        result = self.superstore_reader.format_result(dict)
        self.assertEqual(result, [
            'Alaska: First Class 50%',
            'Washington: Same Day 66%',
            'Texas: First Class 25%',
            'Ohio: None 0%'])

    def test_state_shipmode(self):
        input_dict = {
            'Alaska': ['First Class', 'First Class', 'First Class', 'Same Day', 'Same Day', 'Second Class'],
            'Washington': ['Same Day', 'Same Day', 'Same Day', 'Same Day', 'First Class', 'Second Class'],
            'Texas': ['First Class', 'Second Class', 'Same Day', 'Standard Class'],
            'Ohio': []
        }

        output_list = [
            'Alaska: First Class 50%',
            'Washington: Same Day 66%',
            'Texas: First Class 25%',
            'Ohio: None 0%']
        
        self.superstore_reader.group_shipmode_by_state = lambda: input_dict
        result = self.superstore_reader.state_shipmode()

        self.assertIsInstance(result, list)
        self.assertEqual(result, output_list)
        self.assertTrue(all(isinstance(line, str) for line in output_list))

if __name__ == '__main__':
    reader = Superstore('SampleSuperstore.csv')
    reader.build_data_dict

    results = reader.category_profit()
    reader.results_to_csv(results, filename= "category_profit.csv")
    unittest.main(verbosity=2)