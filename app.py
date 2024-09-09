from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='/static')

# Route for the booking form
@app.route('/')
def booking_form():
    return render_template('booking_form.html')

@app.route('/test-image')
def test_image():
    return '<img src="/static/images/cab-background1.jpg" alt="Test Image">'


# Route for confirming the booking
@app.route('/confirm-booking', methods=['POST'])
def confirm_booking():
    # Get form data
    name = request.form['name']
    email = request.form['email']
    pickup_location = request.form['pickup_location']
    drop_location = request.form['drop_location']
    cab_type = request.form['cab_type']
    distance = calculate_distance(pickup_location, drop_location)  # You need to implement this

    # Price per km for each cab type
    cab_prices = {
        'Sedan': 1.00,
        'SUV': 1.50,
        'Bike': 0.50,
        'Mini': 0.80,
        'Luxury': 2.50,
        'Outstation': 1.20
    }

    # Calculate the total cost
    price_per_km = cab_prices[cab_type]
    total_cost = price_per_km * distance

    # Render the confirmation page with booking details
    return render_template('confirmation.html',
                           name=name,
                           email=email,
                           pickup=pickup_location,
                           drop=drop_location,
                           cab=cab_type,
                           distance=distance,
                           total_cost=total_cost)

# Optional route for testing
@app.route('/test')
def test_template():
    return render_template('test.html')


def calculate_distance(pickup, drop):
    # Example: You can implement actual distance calculation here
    return 10  # Assuming the distance is 10 km for demonstration purposes


if __name__ == '__main__':
    app.run(debug=True)
