
# Cab Booking System

## Overview

The **Cab Booking System** is a web application built using Python's Flask framework and SQLite as the database. It allows users to book cabs by selecting a pickup and drop location, choosing a cab type, and providing their personal details. The system calculates the total cost of the trip based on the type of cab and the distance between the locations.

## Features

- **Cab Booking Form**: Users can select a pickup location, drop location, and cab type.
- **Dynamic Pricing**: The price per kilometer changes based on the selected cab type.
- **Distance Calculation**: Calculates the distance between pickup and drop locations.
- **Fare Estimation**: Provides a fare estimate based on the cab type and distance.
- **User Confirmation**: Shows a confirmation page with booking details after submitting the form.
- **Background Image**: Provides a visually appealing background for the booking form.

## Technologies Used

- **Backend**: Flask (Python), Fast API
- **Database**: SQLite
- **Frontend**: HTML, CSS, JavaScript
- **Template Engine**: Jinja2

## Prerequisites

- Python 3.x installed on your system.
- Basic knowledge of Flask, Python, and SQL.

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/Cab_booking_system.git
   cd Cab_booking_system
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up the database**:
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

6. **Run the application**:
   ```bash
   flask run
   ```
   The app will be available at `http://127.0.0.1:5000/`.

## Project Structure

- **app.py**: The main Flask application that handles routes and logic.
- **templates/**: Contains the HTML templates (Jinja2 format).
  - `booking_form.html`: The form for booking a cab.
  - `confirmation.html`: Displays booking details after confirmation.
- **static/**: Contains static files such as CSS, images, and JavaScript.
  - `style.css`: Styling for the booking form.
  - `cab-background1.jpg`: Background image for the booking form.
- **models.py**: Defines the database models for storing cab details and bookings.
- **database.db**: SQLite database file where booking and cab data is stored.

## How it Works

1. **User Interaction**: 
   - The user selects the pickup and drop locations from the dropdown menus.
   - They choose the cab type (e.g., Sedan, SUV, Bike, etc.).
   - They enter their name, email, and phone number.
   - After submitting, the total cost is calculated based on the distance between locations and the price per kilometer for the selected cab type.
   - The confirmation page shows a summary of the booking details.

## Future Enhancements

- Adding real-time distance calculation using a mapping API.
- Integration with payment gateways for secure online payments.
- Adding user authentication for storing previous bookings.

## License

This project is licensed under the MIT License.
