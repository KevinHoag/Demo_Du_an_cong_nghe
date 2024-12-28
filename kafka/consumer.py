from confluent_kafka import Consumer, KafkaException, KafkaError
import mysql.connector
import json

def consume_messages_and_write_to_mysql(bootstrap_servers, group_id, topic_name, mysql_config, table_name):
    consumer_config = {
        "bootstrap.servers": bootstrap_servers,
        "group.id": group_id,
        "auto.offset.reset": "earliest",
        "enable.auto.commit": True
    }

    consumer = Consumer(consumer_config)

    consumer.subscribe([topic_name])
    print(f"Subscribed to topic '{topic_name}'. Waiting for messages...")

    while True:
        connection = mysql.connector.connect(**mysql_config)
        cursor = connection.cursor()
        msg = consumer.poll(timeout=1.0)

        if msg is None:
            continue

        message = msg.value().decode('utf-8')

        try:
            record = json.loads(message)
            insert_into_mysql(cursor, connection, table_name, record)
            print("Message inserted into MySQL")
        except json.JSONDecodeError as e:
            if connection.is_connected():
                cursor.close()
                connection.close()
            print(f"Failed to decode message: {e}")

        if connection.is_connected():
            cursor.close()
            connection.close()


def insert_into_mysql(cursor, connection, table_name, record):
    insert_query = f"""
    INSERT INTO {table_name} (title, author, abstract, publication_date, keywords, research_field)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    values = (
        record.get("title"),
        record.get("author"),
        record.get("abstract"),
        record.get("publication_date"),
        record.get("keywords"),
        record.get("research_field"),
    )

    cursor.execute(insert_query, values)
    connection.commit()

if __name__ == "__main__":
    BOOTSTRAP_SERVERS = "localhost:9092"
    GROUP_ID = "example_group"
    TOPIC_NAME = "example_topic"

    MYSQL_CONFIG = {
        "host": "localhost",
        "port": "3316",
        "user": "root",
        "password": "password",
        "database": "test_database",
    }

    TABLE_NAME = "scientific_research"

    consume_messages_and_write_to_mysql(BOOTSTRAP_SERVERS, GROUP_ID, TOPIC_NAME, MYSQL_CONFIG, TABLE_NAME)
