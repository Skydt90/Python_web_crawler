import unittest
from spider import *

class TestSpider(unittest.TestCase):

    #name is a string, no umbers are allowed in the string and name should not be empty
    #CPR format xxxxxx-xxxx where xx is numbers and is a valid CPR number

    def test_create_spider():
        
        project_name = 'some_project_name'
        home_page = 'some_home_page'

        self.assertRaises(project_name, )
        Spider(main.project_name, main.home_page, main.domain_name)

        if project_name

    def test_if_stud_name_is_a_string(self):
        
        student = Student()
        self.assertRaises(TypeError, Student, 12)

    def test_type_create_student():
        print('sefsef')

    def test_numbers_in_create_student():
        self.assertRaises(ValueError, Student, 'Claus12', 112321-1234)