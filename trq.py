import time

from rediscluster import StrictRedisCluster
from rq import Queue
from my_module import count_words_at_url

q = Queue(connection=StrictRedisCluster(
    startup_nodes=[{'host': '127.0.0.1', 'port': '7000'}]))

job = q.enqueue(count_words_at_url, 'http://nvie.com')

# print(job.result)

time.sleep(2)

print(job.result)

