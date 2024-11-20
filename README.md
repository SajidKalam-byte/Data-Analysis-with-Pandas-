**Data Analysis with Pandas 📊🐼**

This project demonstrates basic and advanced data analysis tasks using the Pandas library in Python. The script loads a CSV file, performs various operations, and provides insights into the dataset.
🚀 Features

**The script covers the following tasks:**

* **Load and Explore a Dataset:**
    * Load a CSV file using Pandas.
    * Display:
        * First few rows of the dataset.
        * Shape of the dataset (rows and columns).
        * Column data types.
    *  Generate Descriptive Statistics:
        * Summary statistics for numerical columns.
    * Data Cleaning:
        * Check for missing values and duplicates.
    * Data Manipulation:
       * Count unique values in a column.
       * Group and aggregate data (e.g., average salary by age).
       * Sort data by a specific column (e.g., Salary).
       * Filter rows based on conditions (e.g., Salary > 50,000).
    * Export Processed Data:
        Save filtered results to a new CSV file.

**🛠️ Getting Started**

**Prerequisites**

Ensure you have the following installed:

    Python 3.x
    Pandas library
    Install Pandas using pip if it’s not already installed:

pip install pandas

Usage

    Clone or download this repository.

    Place your CSV file (e.g., sample.csv) in the same directory as the script.

    Update the file path in the script to point to your CSV file:

file_path = r'path_to_your_file/sample.csv'

Run the script:

    python data_analysis.py

**📂 Output**

The script provides:

    Insights:
    Column statistics, unique value counts, and missing value checks.
    Aggregated Views:
    Summarized and sorted data.
    Filtered Data:
    Rows meeting specific conditions exported as a new CSV file.

**🗂️ Example Dataset**

Here’s an example dataset used in the script (sample.csv):
Name	Age	Salary
David	28	48000
Emily	32	52000
Frank	27	46000
Grace	30	50000
Henry	35	55000
📊 Example Output
Descriptive Statistics:

Descriptive statistics:
             Age        Salary
count  65.000000     65.000000
mean   30.000000  50000.000000
std     3.162278   3481.553389
min    25.000000  45000.000000
...

Filtered Data:

Rows with Salary > 50,000 exported to high_salary.csv.

**🤝 Contributing**

Contributions are welcome! Feel free to fork this repository, make changes, and submit a pull request. Suggestions for improvements or additional features are highly appreciated.
📜 License

This project is licensed under the MIT License. See the LICENSE file for more details.

_⭐️ If you find this project helpful, give it a star! 😊_
