# Selenium/Python/Pytest Project Documentation

## Project Overview
This project is a Python program that does the following:

- Goes to Kenpom and gathers the latest Kenpom statistics for all D1 College Basketball teams - test_get_kenpom_data.py
- Goes to vegasinsider.com and scrapes the current day's matchup lines and totals - test_get_matchups_and_lines.py
- Runs the algorithm against the two sets of data and gives projected lines and totals and compares to the originals.

## Model Running Instructions

### Collect Kenpom Data
- Go to the tests folder
- Run the following:
   pytest test_get_kenpom_data.py -v -s 
- This creates the kenpom.csv file in the ModelData folder

### Collect Today's Lines and Totals

- Go to the tests folder
- Run the following:
   pytest test_get_matchups_and_lines.py -v -s 
- This creates the todays_matchups.csv file in the ModelData folder
- Clean this file by opening and removing any lines in the csv that do not have lines or manually add those lines (you will see matchups with N/A as the lines)

### Run the Model
- Go to the tests folder
- Run the following:
   pytest test_NCAAHoopsModelFromCSV.py -v -s 
- Model_Projections.csv is created in the ModelData folder.   The model will give who it thinks should be favored and the projected total.

### Run the Total Script to project Picks and Confidence
- Go to the tests folder
- Run the following:
   pytest test_total_model_picks.py -v -s 
- This creates the csv file Total_Model_Picks.csv that lists the games, lines, model projections and confidence in each pick (based on model versus actual lines.)



### Run the Line Script to project Picks and Confidence
- Go to the tests folder
- Run the following:
   pytest test_line_model_picks.py -v -s 
- This creates the csv file Line_Model_Picks.csv that lists the games, lines, model projections and confidence in each pick (based on model versus actual lines.)


### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/yourproject.git
    cd yourproject
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv virtual_env_name
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Install WebDriver**:
   - Download the appropriate WebDriver for your browser (e.g., ChromeDriver) and ensure it is in your system PATH or placed in the project directory.

## Usage Examples

### Running Tests

To run all tests, use:
```bash
pytest
```
To run tests in a particular file:
```bash
pytest test_logins.py
```
Run tests by module:
```bash
pytest test_logins.py::test_loginfromexcel
```
Another example specifying a test method in the command line:
```bash
pytest test_mod.py::TestClass::test_method
```
Run tests by marker expressions:
```bash
pytest -m smoke
```
Run tests by keyword expression
```bash
pytest -k "MyClass and not method"
```
Run tests with cutom option:
```bash
pytest --environment_name=chrome
```
Create JUnitXML Format Files
```bash
pytest --junitxml=path

```







