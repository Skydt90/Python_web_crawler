import unittest

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

        queue = []       ## in spider class it is a set
        crawled = []     ## in spider class it is a set
        queue.append(link_one)
        crawled.append(link_two)

        ### method from spider class 
        for url in links:
            if url in queue:
                continue
            if url in crawled:
                continue
            if domain_name not in url:
                continue
            queue.append(url)
        ### method from spider class 

        is_dublicate_link_one = False
        is_dublicate_link_two = False
        counter_link_one = 0
        counter_link_two = 0

        for link in queue:
            if link == link_one:
                counter_link_one += 1
            if link == link_two:
                counter_link_two += 1

        if counter_link_one > 1:
            is_dublicate_link_one = True
        if counter_link_two > 1:
            is_dublicate_link_two = True
        
        self.assertFalse(is_dublicate_link_one, 'Error: queued link added to queue. \nThis url: ' + link_one)
        self.assertFalse(is_dublicate_link_two, 'Error: crawled link added to queue. \nThis url: ' + link_two)
        self.assertNotIn(link_not_in_domain, queue, 'Error added a url to queue who is not in the domain. \nDomain: ' + domain_name + '\nUrl added: ' + link_not_in_domain)



if __name__ == '__main__':
    unittest.main()