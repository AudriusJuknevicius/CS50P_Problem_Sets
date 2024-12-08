import requests
import sqlite3
import pandas as pd
import logging


# Global variables for API
API_KEY = "a5cfb22b481f8b1a09cb64f796d1009e" # Limited to 100 independent requests per month, please register on their website to input your own API
BASE_URL = "http://api.weatherstack.com/current"


def main():
    """Main function to orchestrate the ETL process."""
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s') # Outputs logs in regards to the process

    cities = ["London", "Bristol", "Cardiff", "Birmingham", "Edinburgh"]

    # Step 1: Create the database (If it does not already exists)
    conn, cursor = create_database()

    # Step 2: Process each city in a loop to extract the data and load it into the database
    for city in cities:
        data = fetch_and_transform_data(city)
        if data:
            load_data_into_database(cursor, data)

    # Step 3: Commit changes(loads new data from API) and close the database
    conn.commit()
    conn.close()
    logging.info("All data has been processed and saved.")

    # Step 4: Export data to CSV
    try:
        export_to_csv()
    except Exception as e:
        logging.error(f"Failed to export data to CSV: {e}")


def create_database(database_name="weather_data.db"):
    """Create the SQLite database and weather table."""
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

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
    return conn, cursor


def fetch_and_transform_data(city):
    """Fetch weather data from the API and transform it."""
    querystring = {
        "access_key": API_KEY,
        "query": city,
        "units": "m"  # Metric units
    }

    response = requests.get(BASE_URL, params=querystring, timeout=10)

    if response.status_code != 200:
        logging.error(f"API call failed for {city}. HTTP Status: {response.status_code}")
        return None

    data = response.json()

    if "location" in data and "current" in data:
        city_name = data["location"]["name"]
        temperature = data["current"]["temperature"]
        feelslike = data["current"]["feelslike"]
        precipitation = data["current"]["precip"]
        humidity = data["current"]["humidity"]
        wind_speed = data["current"]["wind_speed"]
        wind_dir = data["current"]["wind_dir"]
        description = data["current"]["weather_descriptions"][0] if data["current"]["weather_descriptions"] else "No description available"
        uv_index = data["current"]["uv_index"]
        return city_name, temperature, feelslike, precipitation, humidity, wind_speed, wind_dir, description, uv_index
    else:
        logging.error(f"Failed to retrieve data for {city}. Error: {data.get('error', 'Unknown error')}")
        return None


def load_data_into_database(cursor, data):
    """Insert transformed data into the database."""
    city_name, temperature, feelslike, precipitation, humidity, wind_speed, wind_dir, description, uv_index = data

    try:
        cursor.execute('''
        INSERT INTO weather (city, temperature, feelslike, precipitation, humidity, wind_speed, wind_dir, description, uv_index)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (city_name, temperature, feelslike, precipitation, humidity, wind_speed, wind_dir, description, uv_index))
        logging.info(f"Data for {city_name} inserted into the database.")
    except sqlite3.Error as e:
        logging.error(f"Failed to insert data for {city_name}: {e}")


def export_to_csv(database_name="weather_data.db"):
    """Export data from the SQLite database to a CSV file using pandas."""
    conn = sqlite3.connect(database_name) # Use a dynamic database name

    # Use pandas to query the database and export to CSV
    df = pd.read_sql_query("SELECT * FROM weather", conn)
    df.to_csv("weather_data.csv", index=False, encoding="utf-8")  # Export to CSV without the index

    conn.close()
    logging.info("Data successfully exported to weather_data.csv")


if __name__ == "__main__":
    main()
