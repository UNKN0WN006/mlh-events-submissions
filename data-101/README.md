# Data Cleaning Process

The `clean_data.ipynb` notebook performs the following steps to clean the messy data:

1. **Read the Raw Data:**  
	The notebook reads the contents of `messy_data.csv` line by line.

2. **Extract Fields Using Regular Expressions:**  
	For each line, it uses regular expressions to extract the `Name`, `Address`, `Age`, and `Gender` fields.

3. **Organize Data into Lists:**  
	The extracted values are stored in separate lists for each column.

4. **Create a Clean DataFrame:**  
	These lists are combined into a pandas DataFrame with columns: `Name`, `Address`, `Age`, and `Gender`.

5. **Save Cleaned Data:**  
	The cleaned DataFrame is saved as `cleaned_data.csv`.

    ## Use of GitHub Copilot

    GitHub Copilot was used to assist in writing the data cleaning code, suggesting regular expressions for field extraction, and providing code snippets for reading, processing, and saving the data efficiently. Copilot also helped with documentation and improving code readability throughout the notebook.