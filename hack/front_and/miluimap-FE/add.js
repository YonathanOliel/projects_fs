// add_soldier.js
const urlServer = "http://localhost:8000"

function setCookie(cname, cvalue, exdays) {
    const d = new Date();
    d.setTime(d.getTime() + (exdays*24*60*60*1000));
    let expires = "expires="+ d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}



function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    
    if (parts.length === 2) {
        return parts.pop().split(';').shift();
    }
}
const csrftoken = getCookie('csrftoken')

function submitSoldier() {
    // Get form values
    const firstName = document.getElementById('first_name').value;
    const lastName = document.getElementById('last_name').value;
    const mane_b = document.getElementById('name_b').value;
    const city = document.getElementById('city').value;
    const street = document.getElementById('street').value;
    const adreessNumber = document.getElementById('adreess_num').value;
    const type = document.getElementById('b_type').value;
    const googleMapsLink = document.getElementById('googleMapsLink').value;
    

    // Perform POST request to '/api/miluimnik/'
    fetch(`${urlServer}/api/miluimnik/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            firstName,
            lastName,
            mane_b,
            city,
            street,
            adreessNumber,
            type,
            // google_maps_link,
            // Add additional optional parameters with default values if needed
        }),
    })
    .then(response => response.json())
    .then(data => {
        // Handle successful response
        console.log('Soldier added successfully:', data);
        alert('Soldier added successfully!');
        // Redirect back to the main map page or perform any other desired action
    })
    .catch(error => {
        // Handle error
        console.error('Error adding soldier:', error);
        alert('Error adding soldier. Please try again.');
    });
}
