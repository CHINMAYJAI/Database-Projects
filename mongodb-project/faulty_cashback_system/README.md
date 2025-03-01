
# Faulty Cashback System

A Tkinter-based GUI application that simulates a faulty cashback system integrated with MongoDB. The application processes payments, validates user input, and assigns rewards (coupon, better luck next time, or cashback) based on predefined probabilities.

## Features

- **Payment Processing**: 
  - Users input a payment amount (as an integer).
  - The app validates the payment amount (rejects 0 or non-integer inputs, displaying an error message below the input field).
- **Reward Mechanism**:
  - **Coupon** (80% chance)
  - **Better Luck Next Time** (15% chance)
  - **Cashback** (5% chance)
- **Database Integration**:
  - Payments are stored in the `FaultyCashbackSystem` collection.
  - Rewards are stored in the `Rewards` collection.
  - The payment record is updated with the corresponding reward details.
  
## Prerequisites

- Python 3.x
- MongoDB running on `mongoDB Link`
- Required Python packages:
  - Tkinter (usually bundled with Python)
  - Pillow
  - pymongo

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/CHINMAYJAI/Database-Projects.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd FaultyCashbackSystem
   ```

3. **Install dependencies:**

   ```bash
   pip install pillow pymongo
   ```

4. **Set up MongoDB:**

   Ensure MongoDB is installed and running. The application connects to the default MongoDB instance on port.

5. **Assets:**

   Place your logo image in the `assets` folder and name it `logoCJ.png`.

## Author
[CHINMAY JAIN](https://github.com/CHINMAYJAI/)
---