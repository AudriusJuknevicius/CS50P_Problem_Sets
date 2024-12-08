CS50P_Final_Project/

    # WEATHERFLOW

#### Video Demo: [https://youtu.be/X0OuZ0YfXEc]

#### Description:
**WeatherFlow** is a Python-based ETL (Extract, Transform, Load) project that collects live weather data from the WeatherStack API, processes it into a structured format, and stores it in an SQLite database. The project also includes a feature to export the processed data into a CSV file, making it suitable for further analysis or sharing.

The purpose of this project is to demonstrate the integration of Python programming, API interaction, data transformation, and database management. It reflects foundational data engineering principles and showcases problem-solving skills in handling real-world data workflows.

---

## Project Features
1. **API Integration**:
   - Fetches live weather data from the WeatherStack API for multiple cities.
   - Handles missing or erroneous data gracefully with appropriate fallbacks.

2. **Data Transformation**:
   - Extracts relevant weather parameters such as temperature, humidity, wind speed, and more.
   - Cleans and structures the data for consistency and accuracy.

3. **Database Management**:
   - Stores the transformed data in an SQLite database with a robust schema.
   - Ensures data integrity and reusability for other applications.

4. **CSV Export**:
   - Allows users to export the stored data into a CSV file for further analysis.

5. **Testing**:
   - Comprehensive tests using pytest to validate database creation, data transformation, and CSV export functionality.

---

## File Breakdown
1. **`project.py`**:
   - Contains the main functionality of the ETL process, split into four custom functions:
     1. `create_database`: Creates the SQLite database and defines the schema.
     2. `fetch_and_transform_data`: Fetches weather data from the API and transforms it.
     3. `load_data_into_database`: Inserts transformed data into the database.
     4. `export_to_csv`: Exports the database contents to a CSV file.

2. **`test_project.py`**:
   - Includes pytest-based tests to ensure the robustness of each function:
     - Tests for database creation.
     - Verification of the weather table schema.
     - Validation of data fetching, transformation, and CSV export functionality.

3. **`weather_data.db`**:
   - SQLite database file created by the project to store processed weather data.

4. **`README.md`**:
   - Provides an overview of the project, its features, and its functionality.

---

## How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/AudriusJuknevicius/CS50P_Final_Project

2. Install the required packages:
pip install requests
pip install pandas
pip install pytest

3. Run the main project file:
python project.py

4. To execute tests:
pytest test_project.py

## Design Choices

1. **SQLite**:
    - Chosen for its simplicity and ease of use in small-scale projects.
    - Ensures the project remains portable and functional for all users.

2. **WeatherStack API**:
    - Provides detailed and reliable weather data.
    - The free-tier usage aligns well with the scope of this project.

3. **Pandas**:
    - Used for its powerful data manipulation capabilities, especially for CSV export.

4. **Error Handling**:
    - Integrated to manage API errors, missing data, and invalid inputs.


## Challenges and Learnings

- Debugging API requests and handling edge cases in data fetching taught valuable problem-solving skills.

- Managing database connections and ensuring clean resource handling was an essential learning experience.

- Writing tests improved the reliability and maintainability of the project, showcasing the importance of test-driven development.

## Conclusion

Weatherflow is a complete ETL pipeline that demonstrates Python programming, API integration, and database management skills. It showcases the potential for scalable and reusable data workflows, reflecting the foundational principles of data engineering.

Thank you for reviewing my project!
