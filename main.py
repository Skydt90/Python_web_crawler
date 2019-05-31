import threading
from queue import Queue
from spider import Spider
from domain import get_domain_name
from general import file_to_set

PROJECT_NAME = "elective_dummy"
HOMEPAGE = "https://clbokea.github.io/exam/"
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + "/queue.txt"
NUMBER_OF_THREADS = 1
thread_queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)

# Create worker threads (dies when main exits)
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        thread = threading.Thread(target=work)
        thread.daemon = True
        thread.start()

# Do the next job in queue
def work():
    while True:
        url = thread_queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        thread_queue.task_done()

# Each queued link is a new job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        thread_queue.put(link)
    thread_queue.join()
    crawl()

# Check if there are items in queue, if so, crawl
def crawl():
    queue_links = file_to_set(QUEUE_FILE)
    if len(queue_links) > 0:
        print(str(len(queue_links)) + " links in the queue")
        create_jobs()

create_workers()
crawl()