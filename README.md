# Elasticsearch + Logstash + Kibana stack
** note: this is far from being a production ready. it's just a usage example ** 

I used my redis pubsub example(https://github.com/shlomikushchi/RedisPubsubOverDocker) to add the ELK stack

I'm using logstash to add LogHandler to the python logger:
logger.addHandler(logstash.LogstashHandler('elk', 5044, version=1))

so all logs written in python use the logstash pipeline to go in elasticsearch db

then I write logs as usual.

logs can be viewed and search using:

1. kibana: http://192.168.99.100:5601/app/kibana

2. sense: http://192.168.99.100:5601/app/sense

3. head plugin: http://192.168.99.100:9200/_plugin/head/

4. or by using code which is what I do in run_me.py
