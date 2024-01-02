from kafka import KafkaProducer
import json

# Once a topic is created (here bank_branch)
# For kafka-python, we use KafkaProducer class to produce messages
producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Since Kafka produces and consumes messages in raw bytes, we need to encode our JSON messages and serialize them into bytes.
# For the value_serializer argument, we define a lambda function to take a Python dict/list object and serialize it into bytes.

# With the KafkaProducer created, we can use it to produce two ATM transaction messages in JSON format as follows:
producer.send("bank_branch", {'atmid':1, 'transid':100})
producer.send("bank_branch", {'atmid':2, 'transid':101})

# The first argument specifies the topic bank_branch to be sent, and 
# The second argument represents the message value in a Python dict format and will be serialized into bytes

# The above producing message operation is equivalent to using kafka-console-producer.sh --topic in Kafka CLI client:
# kafka-console-producer.sh --bootstrap-server localhost:9092 --topic bank_branch

producer.flush()

producer.close()
