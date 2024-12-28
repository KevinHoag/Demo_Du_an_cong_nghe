from confluent_kafka.admin import AdminClient, NewTopic

def create_kafka_topic(bootstrap_servers, topic_name, num_partitions=1, replication_factor=1):
    admin_client = AdminClient({"bootstrap.servers": bootstrap_servers})
    
    topic = NewTopic(
        topic=topic_name,
        num_partitions=num_partitions,
        replication_factor=replication_factor
    )
    if topic_name in admin_client.list_topics().topics:
        print(f"Topic {topic_name} already exists.")
        return 0
    future = admin_client.create_topics([topic])
    
    for topic, f in future.items():
        f.result()  
        print(f"Topic '{topic}' created successfully.")

if __name__ == "__main__":
    BOOTSTRAP_SERVERS = "localhost:9092"
    TOPIC_NAME = "example_topic"
    
    create_kafka_topic(BOOTSTRAP_SERVERS, TOPIC_NAME)
