from app import db, Cab, Location

# Insert cabs
cab1 = Cab(cab_type="Sedan", location="Downtown", price_per_km=10)
cab2 = Cab(cab_type="SUV", location="Airport", price_per_km=15)
cab3 = Cab(cab_type="Hatchback", location="Suburb", price_per_km=8)

# Insert locations
loc1 = Location(name="Downtown", distance_from_center=5)
loc2 = Location(name="Airport", distance_from_center=20)
loc3 = Location(name="Suburb", distance_from_center=10)

# Add and commit to the database
db.session.add_all([cab1, cab2, cab3, loc1, loc2, loc3])
db.session.commit()

print("Data inserted successfully!")
