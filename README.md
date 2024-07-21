Tkinter-based billing application:

```markdown
# Restaurant Billing Application

A Tkinter-based GUI application for generating restaurant bills. This application allows users to input quantities for various items, calculates the total cost for each category, and generates a detailed bill.

## Features

- **Item Categories:** 
  - **Starters**: Samosa, Paneer Tikka, Chicken Tikka, Vegetable Pakora, Papdi Chaat, Tomato Soup, Masala Papad.
  - **Main Course**: Butter Chicken, Chicken Tikka Masala, Basmathi Rice, Paneer Masala, Palak Paneer, Dal Tadka, Chole Bhature.
  - **Snacks**: Noodles, Aloo Chaat, Pasta, Pav Bhaji, Bhel Puri, Paani Puri, Pakora.

- **Total Calculation:** Calculates and displays the total cost for each category and the overall bill.
- **Generate Bill:** Creates a detailed bill based on user input.
- **Clear Data:** Resets all input fields and totals.
- **Exit Application:** Closes the application.

## Requirements

- Python 3.12.0
- Tkinter (usually included with Python)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/manthan-wagh/restaurant-billing-app.git
   ```

2. Navigate to the project directory:
   ```bash
   cd restaurant-billing-app
   ```

3. Ensure you have Python installed and Tkinter is available.

## Usage

1. Run the application:
   ```bash
   python main.py
   ```

2. The GUI will open. Enter the quantities for each item in the respective entry fields.

3. Click the **Total** button to calculate the totals.

4. Click **Generate Bill** to view and print the bill.

5. Use **Clear** to reset all fields and totals.

6. Use **Exit** to close the application.

## Code Overview

- **`Bill_App` Class**: Main class for the application.
  - **`__init__`**: Initializes the GUI components and layout.
  - **`total`**: Calculates total costs for each category and updates totals.
  - **`bill_area`**: Generates and displays the bill.
  - **`clear`**: Resets all input fields and totals.
  - **`exit`**: Closes the application.

## Contributing

Feel free to fork the repository and submit pull requests. For any issues or feature requests, please open an issue.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact [waghmanthan13@gmail.com](mailto:waghmanthan13@gmail.com.com).
