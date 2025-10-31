# Pharmacy Management System  
A Complete Python + MySQL Project for Pharmacy Automation

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![MySQL](https://img.shields.io/badge/Database-MySQL-orange?logo=mysql)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-yellow)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## Overview  

This Pharmacy Management System is a comprehensive Python-based project built with MySQL for data storage and Tkinter for graphical interfaces.  
It streamlines pharmacy operations by automating product management, billing, and customer purchases — all through a clean, interactive interface for both administrators and customers.

---

## Tech Stack  

| Component | Technology |
|------------|-------------|
| Frontend (GUI) | Tkinter |
| Backend (Logic) | Python |
| Database | MySQL |
| Utilities | tabulate, datetime, time |

---

## Features  

### Admin Panel
- Secure login (default: admin / 1234)
- Add, modify, and delete medicines  
- Manage inventory and update stock levels  
- View purchase history with filters  
- Change admin password  
- Display all products in tabulated form  

### Customer Panel
- Browse available medicines  
- Add items to cart  
- Remove items from cart  
- Generate and print digital bills  
- View purchase summary and total payable amount  

---

## Database Design  

Database Name: pysales_inventory

| Table | Description |
|--------|--------------|
| stock | Stores medicine details (product code, name, quantity, price) |
| purchase | Logs customer purchases with date, phone number, and total amount |
| login | Maintains admin credentials |
| cart | Temporary cart data during billing |
| bill | Stores billed product details (description, quantity, total, price) |

---

## System Flow  

```text
┌──────────────────────────────────────────────┐
│                Main Menu                     │
├──────────────────────────────────────────────┤
│ 1. Admin → Login → Manage Inventory, Reports │
│ 2. Customer → Add to Cart, View, Bill        │
│ 3. Exit                                      │
└──────────────────────────────────────────────┘
```

### Admin Flow
1. Login as admin  
2. Add / Update / Delete medicines  
3. Check purchase history  
4. Change password  
5. Logout  

### Customer Flow
1. View available medicines  
2. Add items to cart  
3. View / Edit cart  
4. Generate bill  
5. Exit  

---

## Installation & Setup  

### Prerequisites
Make sure you have installed:
- Python 3.x  
- MySQL Server  
- Required Python libraries:
  ```bash
  pip install mysql-connector-python tabulate
  ```

### Configure Database
Open your MySQL shell and run:
```sql
CREATE DATABASE pysales_inventory;
```

### Run the Application
```bash
python "pharmacy management system.py"
```

### Default Login
- Username: admin  
- Password: 1234  

---

## Example Screens & CLI Flow  

Startup:
```
________________________________
1. Admin
2. Customer
3. Exit
________________________________
```

Admin Menu:
```
1) Add New Item
2) Alter Stock
3) Delete Item
4) Display All Items
5) View Purchase History
6) Change Password
7) Logout
```

Customer Menu:
```
1. View Items
2. Add to Cart
3. View Cart
4. Delete Items from Cart
5. Print Bill
6. Exit Store
```

---

## Sample Bill Output  

```
____________________________________________________
                    BILL RECEIPT
----------------------------------------------------
Date of Billing: 31/10/2025
Customer Name: John Doe
Phone Number: 9876543210
----------------------------------------------------
DESCRIPTION         QUANTITY   UNIT PRICE(₹)   TOTAL(₹)
----------------------------------------------------
Paracetamol            2          20.00          40.00
Amoxicillin            1          60.00          60.00
----------------------------------------------------
TOTAL AMOUNT TO BE PAID: ₹ 100.00 /-
----------------------------------------------------
        THANK YOU FOR CHOOSING PHARMAHUB!
               GET WELL SOON!
```

---

## Code Structure  

```
pharmacy-management-system/
├── pharmacy management system.py     # Main application file
├── README.md                         # Project documentation
└── requirements.txt (optional)        # Dependencies list
```

---

## Future Enhancements  

- Add GUI interface for customer operations  
- Generate visual sales reports  
- Export bills as PDF or CSV  
- Deploy web version using Flask/Django  
- Integrate voice assistance for inventory search  

---


## License  

This project is released under the MIT License — you are free to use, modify, and distribute it with proper credit.
