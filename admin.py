from kafka.admin import KafkaAdminClient,NewTopic

# Creating KafkaAdminClient Object
admin_client = KafkaAdminClient(bootstrap_servers="localhost:9092", client_id='test')
# bootstrap_servers="localhost:9092" argument: specifies the host/IP and port that the consumer should contact to bootstrap initial cluster metadata
# client_id specifies an id of current admin client

# the most common usage of admin_client is managing topics such as creating and deleting topics.
# initial empty topic list
topic_list = []

# Creating new topic
new_topic = NewTopic(name="bank_branch", num_partitions= 2, replication_factor=1)
topic_list.append(new_topic)
admin_client.create_topics(new_topics=topic_list)

# Once new topics are created, we can easily check its configuration details using describe_configs() method
configs = admin_client.describe_configs(
    config_resources=[ConfigResource(ConfigResourceType.TOPIC, "bank_branch")])
# This is same as running "kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic bank_branch" in terminal
