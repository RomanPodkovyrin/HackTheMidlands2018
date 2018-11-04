function onPositionReceived(position) {
    const longitude = position.coords.longitude
    const latitude = position.coords.latitude
    $.ajax({
        type: 'GET',
        url: '/recommend',
        data: {
            lon: longitude,
            lat: latitude
        },
        success: function(resp) {
            console.log(resp)
        },
        error: function() {
            console.log('Error: cannot GET');
        }
    });
}

function locatonNotReceived(positionError) {
    console.log(positionError);
}

$('document').ready(function() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(onPositionReceived, locatonNotReceived);
    }
});