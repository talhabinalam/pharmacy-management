# Pharmacy Management System

This project is an Online Pharmacy Management System built with Django Backend and HTML,CSS for Frontend. It provides an interface for administrators to manage medicines in an inventory, including adding, editing, and deleting entries. Regular users can view and search for medicines in the inventory. This project demonstrates CRUD operations, authentication, and role-based access control in Django.

## Features
### User Authentication
* __Admin Login__: Only users with superuser/admin privileges can add, edit, or delete medicines.
* __User__: Regular users can log in and view the medicine inventory, but they cannot modify it.

### Medicine Management (Admin Only)

* **Add Medicine**: Admins can add new medicines to the inventory, specifying details such as name, generic name, manufacturer, description, price, and batch number.
* **Edit Medicine**: Admins can update information for existing medicines.
* **Delete Medicine**: Admins can delete medicines from the inventory.

### Medicine Viewing (Accessible by All)

* **View Medicines**: Both admins and regular users can view the list of medicines available in the inventory.
* **Paginated Display**: Medicines are displayed with pagination, showing a set number of items per page.

### Medicine Search

* **Search Medicines**: Users can search for medicines by their name or generic name using a search bar.

# Installation

### Prerequisites

* **Python 3.8+**: Make sure Python is installed on your machine. You can download it from [python.org](https://www.python.org).


## Setup Instructions

#### 1. Clone the Repository:

```bash
git clone https://github.com/talhabinalam/pharmacy-management.git
```
__Change Directory:__
```bash
cd pharmacy-management
```

#### 2. Set Up a Virtual Environment:
```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```
#### 3. Install Dependencies:
```bash  
pip install -r requirements.txt
```
#### 4. Apply Migrations Set up the database:
```bash  
python manage.py makemigrations
python manage.py migrate
```
#### 5. Create an admin user to access the management features:
```bash  
python manage.py createsuperuser
```
#### Note: Use (__admin__) as username and password for the existing database.

#### 6. Run the Development Server Start the Django development server.
```bash  
python manage.py runserver
```

### Access application: http://127.0.0.1:8000/


# Project Structure

* **views.py**: Contains class-based views for handling HTTP requests for various features (login, logout, add, edit, delete medicines).
* **models.py**: Defines the Medicine model with fields such as name, generic name, manufacturer, description, price, and batch number.
* **templates/**: Contains HTML templates for each view (e.g., login page, index page, add/edit form).
* **urls.py**: Defines URL routes for the app.

# Usage

## Admin Access

Admins can:
* **Add New Medicines**: Go to the "Add Medicine" page and enter all required details.
* **Edit Existing Medicines**: Click on an existing medicine entry to edit its details.
* **Delete Medicines**: Remove entries from the inventory.

## User Access

Regular users can:
* **View Medicines**: Access the paginated list of medicines available in the inventory.
* **Search Medicines**: Use the search bar to look for medicines by name or generic name.

# Requirements

The `requirements.txt` file includes all necessary Python packages. Major dependencies include:

* **Django**: For building the web application.

## Overview:
![image](https://github.com/user-attachments/assets/51b667cb-c9b4-4072-8770-fa5f213676a9)
