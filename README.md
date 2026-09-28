# SpendWise

SpendWise is a full-stack personal finance management application that helps users track expenses, monitor spending patterns, and gain useful insights into their financial habits through a secure and user-specific platform.

## Features

### Authentication

* User Registration and Login
* Secure Password Hashing
* JWT-based Authentication
* Protected API Routes
* User-specific Expense Access
* Password Visibility Toggle

### Expense Management

* Add Expenses
* View All Expenses
* Update Expenses
* Delete Expenses
* Expense Categories
* Multiple Payment Methods
* Expense Validation
* User-wise Expense Ownership

### Dashboard

* Daily Spending
* Weekly Spending
* Monthly Spending
* Recent Expenses
* Exact Expense Dates

### Spending Insights

* Highest Spending Category
* Category-wise Spending Percentage
* Daily Average Spending
* Monthly Spending Comparison
* Weekend vs Weekday Spending
* Small Expense Analysis
* No-Spend Days

---

## Technology Stack

### Backend

* Python
* Flask
* Flask Blueprints
* Flask-JWT-Extended
* Pydantic

### Database

* SQLite

### Frontend

* HTML5
* CSS3
* JavaScript
* Fetch API

---

## Database Design
### User Table
Stores:
* User ID
* Username
* Email
* Hashed Password
* Account Creation Date

### Expense Table
Stores:
* Expense ID
* User ID
* Amount
* Category
* Note
* Date
* Payment Method

Each expense is associated with the user who created it, ensuring users can only access and manage their own expenses.

---

## Installation

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Run Application

```bash
python app.py
```

### Step 3: Open Browser

```text
http://127.0.0.1:5000
```

---

## Security Features

* Password Hashing
* JWT-based Authentication
* Protected API Routes
* User-specific Expense Access
* Input Validation using Pydantic
* Unauthorized Request Handling

---

## Testing

* Authentication and JWT tested
* Expense CRUD tested
* Input validation tested
* User isolation tested
* Dashboard calculations tested
* Spending insights tested
* Frontend and API integration tested

---

## Future Enhancements

* Expense Data Export
* Advanced Spending Visualizations
* Budget Tracking
* Expense Search and Filtering
* More Detailed Financial Reports
* Production Deployment

```
```
