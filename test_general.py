import unittest
from general import *

class TestSum(unittest.TestCase):

    def test_create_project_directory(self):
        directory = 'elective_dummy'
        create_project_directory(directory) # testing this method
        is_created = False
        if os.path.exists(directory):
            is_created = True
        self.assertTrue(is_created)

    def test_create_data_files(self):
        project_name = 'elective_dummy'
        base_url = 'https://clbokea.github.io/exam/'
        queue = project_name + "/queue.txt"
        crawled = project_name + "/crawled.txt"
        contents = project_name + "/contents.md"

        is_created_queue = False
        is_created_crawled = False
        is_created_contents = False

        create_data_files(project_name, base_url) # testing this method

        if os.path.exists(queue):
            is_created_queue = True
        if os.path.exists(crawled):
            is_created_crawled = True
        if os.path.exists(contents):
            is_created_contents = True
        self.assertTrue(is_created_queue, 'did not create file: ' + queue)
        self.assertTrue(is_created_crawled, 'did not create file: ' + crawled)
        self.assertTrue(is_created_contents, 'did not create file: ' + contents)

    def test_write_file(self):
        project_name = 'elective_dummy'
        contents = project_name + "/contents.md"
        path = contents
        data = 'this is some test data'
        write_file(path, data) # testing this method
        f = open(path, "r")
        resultData = f.read()
        self.assertEqual(resultData, data, 'did not write correctly to file, expected: ' + data + ' got: ' + data)
    
    '''
    def test_add_to_file(self):
        project_name = 'elective_dummy'
        contents = project_name + "/contents.md"
        path = contents
        pre_data = 'this is already in the file'
        data = 'add this to existing file'
        with open(path, "w") as file:
                file.write(pre_data)

        add_to_file(path, data) # testing this method
        f = open(path, "r")
        resultData = f.read()
        self.assertEqual(pre_data + data, resultData, ('did not add correctly to file, predata: ' + pre_data + ' data to add: ' + data + ' got: ' + resultData))
    '''
    def test_add_md_formatting(self):
        contents = []

        header1Tag = 'h1im a header tag'
        header1TagResult = '\n# im a header tag\n'
        
        header2Tag = 'h2im a header2 tag'
        header2Tag_result = '\n## im a header2 tag'

        ptag = 'pim a p tag'
        ptag_result = 'im a p tag  '

        litag = 'liim a li tag'
        litag_result = '* im a li tag'

        atag = 'aim a a tag'
        atag_result = ''
        contents.append(header1Tag)
        contents.append(header2Tag)
        contents.append(ptag)
        contents.append(litag)
        contents.append(atag)

        formatted_list = add_md_formatting(contents)

        self.assertEqual(formatted_list[0], header1TagResult, 'did not format correctly, expected: ' + header1TagResult + 'got: ' + contents[0])
        self.assertEqual(formatted_list[1], header2Tag_result, 'did not format correctly, expected: ' + header2Tag_result + 'got: ' + contents[1])
        self.assertEqual(formatted_list[2], ptag_result, 'did not format correctly, expected: ' + ptag_result + 'got: ' + contents[2])
        self.assertEqual(formatted_list[3], litag_result, 'did not format correctly, expected: ' + litag_result + 'got: ' + contents[3])
        self.assertEqual(formatted_list[4], atag_result, 'did not format correctly, expected: ' + atag_result + 'got: ' + contents[4])


if __name__ == '__main__':
    unittest.main()