# To install Kafka - Run in terminal
wget https://archive.apache.org/dist/kafka/3.5.1/kafka_2.12-3.5.1.tgz
tar -xzf kafka_2.12-3.5.1.tgz
cd kafka_2.12-3.5.1

# Starting Zookeeper Service in the same terminal
bin/zookeeper-server-start.sh config/zookeeper.properties

# In a new terminal, starting Kafka Broker Service
cd kafka_2.12-3.5.1
bin/kafka-server-start.sh config/server.properties

# In a new terminal, installing kafka-python
cd kafka_2.12-3.5.1
pip3 install kafka-python

# Creating admin.py, producer.py, and consumer.py files

touch admin.py
# Open file and add code

touch producer.py
# Open file and add code

touch consumer.py
# Open file and add code

# Run admin.py and producer.py in same terminal
python3 admin.py
python3 producer.py

# In new terminal, run consumer.py
python3 consumer.py
