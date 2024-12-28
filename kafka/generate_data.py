import csv
import random
from faker import Faker
from datetime import datetime

fake = Faker()

keywords_pool = [
    "deep learning", "neural networks", "machine learning", "computer vision", "NLP", 
    "reinforcement learning", "GANs", "transformers", "AI ethics", "autonomous systems"
]
research_fields = [
    "Artificial Intelligence", "Computer Vision", "Natural Language Processing", 
    "Reinforcement Learning", "AI Ethics"
]

authors = [
    "Alice Johnson", "Bob Smith", "Charles Lee", "David Martinez", "Emma Brown", 
    "Fiona Clark", "George Wilson", "Hannah Davis", "Ian Taylor", "Jack White"
]

def generate_random_research(authors):
    start_date = datetime(2010, 1, 1)
    end_date = datetime(2024, 12, 31)
    
    return {
        "title": fake.sentence(nb_words=5),
        "author": random.choice(authors),
        "abstract": fake.sentence(nb_words=15),
        "publication_date": fake.date_between(start_date=start_date, end_date=end_date).strftime("%Y-%m-%d"),
        "keywords": ", ".join(random.sample(keywords_pool, k=random.randint(5, 10))),
        "research_field": random.choice(research_fields)
    }

def save_to_csv(filename, data):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    research_data = [generate_random_research(authors) for _ in range(1000)]

    csv_filename = "ai_research_data.csv"
    save_to_csv(csv_filename, research_data)

    print(f"Generated data saved to {csv_filename}")
