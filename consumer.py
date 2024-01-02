from kafka import KafkaConsumer

# Creating a KafkaConsumer subscribing to the topic bank_branch
consumer = KafkaConsumer('bank_branch',
                        group_id=None,
                         bootstrap_servers=['localhost:9092'],
                         auto_offset_reset = 'earliest')

print("Hello")
print(consumer)

# Once the consumer is created, it will receive all available messages from the topic bank_branch. 
# Then we can iterate and print them with the following code snippet
for msg in consumer:
    print(msg.value.decode("utf-8"))
