import time

from rediscluster import StrictRedisCluster
from rq import Queue
from my_module import count_words_at_url

# redis_hosts=[{'host': '127.0.0.1', 'port': '7000'}]
redis_hosts = [{'host': '127.0.0.1', 'port': '7000'},
               {'host': '127.0.0.1', 'port': '7001'},
               {'host': '127.0.0.1', 'port': '7002'},
               {'host': '127.0.0.1', 'port': '7003'},
               {'host': '127.0.0.1', 'port': '7004'},
               {'host': '127.0.0.1', 'port': '7005'}]

q = Queue(connection=StrictRedisCluster(startup_nodes=redis_hosts))

job = q.enqueue(count_words_at_url, 'http://nvie.com')

# print(job.result)

time.sleep(0.1)

print(job.result)

