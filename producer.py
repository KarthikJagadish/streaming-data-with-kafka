from kafka import KafkaProducer
import json
producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'))
producer.send("bank_branch", {'atmid':1, 'transid':100})
producer.send("bank_branch", {'atmid':2, 'transid':101})

producer.flush()

producer.close()