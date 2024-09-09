document.addEventListener('DOMContentLoaded', function () {
    fetch('/api/locations')
        .then(response => response.json())
        .then(data => {
            const pickupSelect = document.getElementById('pickup_location');
            const dropSelect = document.getElementById('drop_location');

            data.forEach(location => {
                let option = document.createElement('option');
                option.value = location;
                option.textContent = location;
                pickupSelect.appendChild(option.cloneNode(true));
                dropSelect.appendChild(option);
            });
        });

    fetch('/api/cabs')
        .then(response => response.json())
        .then(data => {
            const cabSelect = document.getElementById('cab_id');

            data.forEach(cab => {
                let option = document.createElement('option');
                option.value = cab.id;
                option.textContent = `${cab.cab_type} (From ${cab.location}) - $${cab.price_per_km}/km`;
                cabSelect.appendChild(option);
            });
        });
});
