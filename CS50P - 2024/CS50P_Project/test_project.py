from project import create_database, fetch_and_transform_data, export_to_csv
import sqlite3
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def test_create_database():
    create_database("weather_data_test.db")

    assert os.path.exists("weather_data_test.db"), "Database file does not exist."

    # Open and manually close the connection
    conn = sqlite3.connect("weather_data_test.db")
    conn.close()  # Explicitly close the lingering connection

    logging.info("test_create_database passed!")


def test_weather_table_exists():
    create_database("weather_data_test.db")
    conn = sqlite3.connect("weather_data_test.db") # Connection
    cursor = conn.cursor() # Cursor/SQlite3 interface object
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='weather';")
    table_exists = cursor.fetchone() # Using fetch to retrieve the first row of result as a tuple
    conn.close()
    assert table_exists, "Weather table does not exist in the database."


def test_fetch_and_transform_data():
    test_city = "London"
    data = fetch_and_transform_data(test_city)

    # Check if the function returns any result
    assert data is not None, "No data returned for a valid city."

    # Basic checks on the returned data
    assert isinstance(data[0], str), "City name should be a string."
    assert isinstance(data[1], (int, float)), "Temperature should be a number."

    logging.info("test_fetch_and_transform_data passed!")


def test_export_to_csv():
    # Create a test database
    conn = sqlite3.connect("weather_data_test.db")
    cursor = conn.cursor()

    # Create table and mock insert data
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS weather (
        id INTEGER PRIMARY KEY,
        city TEXT NOT NULL,
        temperature REAL NOT NULL,
        feelslike REAL NOT NULL,
        precipitation REAL NOT NULL,
        humidity INTEGER NOT NULL,
        wind_speed REAL NOT NULL,
        wind_dir TEXT NOT NULL,
        description TEXT NOT NULL,
        uv_index INTEGER NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    );
    ''')
    cursor.execute('''
    INSERT INTO weather (city, temperature, feelslike, precipitation, humidity, wind_speed, wind_dir, description, uv_index)
    VALUES ('TestCity', 20.0, 18.0, 0.5, 60, 5.0, 'N', 'Clear skies', 3);
    ''')

    conn.commit()
    conn.close()

    # Call export function
    try:
        export_to_csv("weather_data_test.db")
        assert os.path.exists("weather_data.csv"), "CSV file was not created."
    finally:
        if os.path.exists("weather_data.csv"):
            os.remove("weather_data.csv")

    logging.info("test_export_to_csv passed!")
    