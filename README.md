# expense-tracker-using-python-

## **Overview**
The Expense Tracker is a simple command-line application that allows users to track their expenses. Users can add expenses, view them, and generate summaries based on months or categories. The data is stored in a JSON file, making it easy to manage and retrieve.

## **Features**
- **Add Expense**: Record a new expense with details such as amount, category, and description.
- **View Expenses**: Display all recorded expenses in a readable format.
- **Monthly Summary**: Generate a summary of expenses grouped by month.
- **Category Summary**: Generate a summary of expenses grouped by category.
- **Data Persistence**: Automatically saves expenses to a JSON file for future access.

## **Requirements**
- Python 3.x
- No external libraries are required, as the code uses built-in libraries.

## **Installation**
1. Clone the repository or download the `expenc trackar main.py` file.
2. Ensure you have Python 3.x installed on your machine.
3. Run the script using the command:
   ```bash
   python expenc trackar main.py
   ```

## **Usage**
- Upon running the application, you will be presented with a menu of options:
  1. **Add Expense**: Input the amount, category, and description of the expense.
  2. **View Expenses**: List all recorded expenses.
  3. **Monthly Summary**: View total expenses for each month.
  4. **Category Summary**: View total expenses for each category.
  5. **Exit**: Close the application.

### **Example**
- To add an expense:
  - Choose option `1`, then enter the amount (e.g., `50`), category (e.g., `Food`), and description (e.g., `Lunch`).
- To view expenses:
  - Choose option `2` to see all recorded expenses.

## **Data Storage**
- Expenses are stored in a file named `expenses.json`. If the file does not exist or is empty, the application will create a new one.

## **Error Handling**
- The application includes basic error handling for invalid inputs, such as:
  - Non-numeric values for the amount.
  - Negative or zero amounts.

## **Contributing**
Contributions are welcome! If you have suggestions for improvements or new features, feel free to submit a pull request.

