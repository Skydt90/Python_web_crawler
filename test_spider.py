import unittest
from spider import *

class Test_Spider(unittest.TestCase):

    def test_add_links_to_queue_test(self):
        
        domain_name = 'clbokea.github.io/exam'
        links = []
        link_one = 'https://clbokea.github.io/exam/assignment_1.html'
        link_two = 'https://clbokea.github.io/exam/assignment_2.html'
        link_three = 'https://clbokea.github.io/exam/assignment_3.html'
        link_not_in_domain = 'www.facebook.com'

        links.append(link_one)
        links.append(link_two)
        links.append(link_three)
        links.append(link_not_in_domain)

        Spider.domain_name = 'clbokea.github.io/exam'
        Spider.crawled.add(link_one)
        Spider.add_links_to_queue(links) # testing this method
        
        self.assertNotIn(link_one, Spider.queue, 'Error: crawled link added to queue. \nThis url: ' + link_one)
        self.assertNotIn(link_not_in_domain, Spider.queue, 'Error added a url to queue who is not in the domain. \nDomain: ' + domain_name + '\nUrl added: ' + link_not_in_domain)



if __name__ == '__main__':
    unittest.main()