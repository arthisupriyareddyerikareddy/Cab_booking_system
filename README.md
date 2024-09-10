
# Cab Booking System

## Overview

This project is a web-based Cab Booking System developed using Flask, SQLAlchemy, and SQLite. The system allows users to book a cab by selecting pickup and drop locations, along with the type of cab, and receive a fare estimation. It includes a user-friendly interface with dynamic price calculation based on the cab type.

## Features

- **Booking Form:** Users can enter pickup location, drop location, cab type, name, email, and contact number.
- **Price Estimation:** Price per kilometer varies depending on the selected cab type.
- **Dynamic Interface:** The system uses a background image and a modern layout to provide a great user experience.
- **Confirmation Page:** After booking, users get a confirmation of their ride with details like distance, cab type, and total fare.

## Technologies Used

- **Flask:** Python web framework for building the backend of the application.
- **Jinja2:** Templating engine used with Flask for rendering HTML pages.
- **SQLite:** Lightweight database system used for storing cab booking data.
- **SQLAlchemy:** ORM for database interactions in Flask.
- **HTML/CSS:** For the frontend design.
- **JavaScript:** For dynamic price calculation based on the cab type.

## Project Structure

```
Cab_booking_system/
│
├── static/
│   ├── css/
│   │   └── style.css          # Stylesheet for the web interface
│   └── images/
│       └── cab-background1.jpg # Background image for the booking form
│
├── templates/
│   ├── booking_form.html       # Main booking form page
│   └── confirmation.html       # Booking confirmation page
│
├── app.py                      # Main Flask application
├── models.py                   # SQLAlchemy models for database
├── README.md                   # Project documentation (this file)
├── requirements.txt            # List of dependencies for the project
└── config.py                   # Configuration settings for the app

```

## Setup Instructions

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/Cab_booking_system.git
   cd Cab_booking_system
   ```

2. **Create a Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate    # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**

   Install the required dependencies by running:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database:**

   Run the following command to set up the SQLite database and create the necessary tables:

   ```bash
   python app.py
   ```

5. **Run the Application:**

   Start the Flask development server:

   ```bash
   flask run
   ```

   Open your browser and go to `http://127.0.0.1:5000/` to access the booking system.

## Usage Instructions

1. Enter the pickup and drop locations from the dropdown menu.
2. Select the type of cab you want to book.
3. Enter your name, email, and contact number.
4. Click the **Book Now** button to confirm the booking.
5. On the confirmation page, review the booking details and fare calculation.

## Pricing Model

- **Sedan:** $10 per km
- **SUV:** $15 per km
- **Bike:** $5 per km
- **Mini:** $8 per km
- **Luxury:** $20 per km
- **Outstation:** $12 per km

## Known Issues

- Background image might not load properly in some environments. Ensure the correct path is set in the `style.css` file.

## Future Enhancements

- Add user authentication for registered users.
- Implement Google Maps API to calculate the exact distance between pickup and drop locations.
- Add more detailed pricing and surge pricing during peak hours.
