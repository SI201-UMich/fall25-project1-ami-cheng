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

class TestPollReader(unittest.TestCase):
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



if __name__ == '__main__':
    unittest.main(verbosity=2)