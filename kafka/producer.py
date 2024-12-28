import json
from confluent_kafka import Producer
import csv


def produce_messages(bootstrap_servers, topic_name, messages):
    producer_config = {
        "bootstrap.servers": bootstrap_servers, 
        "linger.ms": 5,                          
        "acks": "all"                            
    }

    producer = Producer(producer_config)

    for message in messages:
        json_message = json.dumps(message)

        producer.produce(
            topic_name,
            value=json_message.encode("utf-8"),
        )
        
        producer.flush()

    producer.flush()
    print("All messages delivered")

def read_csv_to_objects(filename):
    research_data = []
    
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            research_data.append({
                "title": row["title"],
                "author": row["author"],
                "abstract": row["abstract"],
                "publication_date": row["publication_date"],
                "keywords": row["keywords"],
                "research_field": row["research_field"]
            })
    
    return research_data


if __name__ == "__main__":
    BOOTSTRAP_SERVERS = "localhost:9092"
    TOPIC_NAME = "example_topic"
    MESSAGES = read_csv_to_objects("ai_research_data.csv")

    produce_messages(BOOTSTRAP_SERVERS, TOPIC_NAME, MESSAGES)
