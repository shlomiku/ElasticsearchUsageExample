import logging
import random

import redis
import json
import logstash
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("subscriber")
logger.addHandler(logstash.LogstashHandler('elk', 5044, version=1))


r = redis.StrictRedis(host='redis', port=6379, db=0)
p = r.pubsub()
p.subscribe('my-test-redis-channel')

while True:
    for m in p.listen():
        if isinstance(m['data'], str):
            try:

                print json.loads(m['data'])['quote']
                elements = json.loads(m['data'])['quote'].split(' ')
                rand_index = random.randint(0, len(elements))
                new_elements = elements[:rand_index]
                new_elements.append('kibana_markable')
                new_elements.extend(elements[rand_index:])
                logger.info('published: ' + " ".join(new_elements))
                # logger.info('python-logstash: test extra fields', extra=m['data'])
            except:
                pass # don't care