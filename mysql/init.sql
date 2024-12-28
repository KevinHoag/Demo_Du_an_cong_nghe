USE test_database;

CREATE TABLE scientific_research (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(255),
    abstract TEXT,
    publication_date DATE,
    keywords VARCHAR(255),
    research_field VARCHAR(100)
);
