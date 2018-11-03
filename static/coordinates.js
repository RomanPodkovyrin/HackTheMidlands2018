function onPositionReceived(position) {
    console.log(position.coords.latitude);
    console.log(position.coords.longitude);

    console.log(position);
}

function locatonNotReceived(positionError) {
    console.log(positionError);
}

if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(onPositionReceived, locatonNotReceived);
}