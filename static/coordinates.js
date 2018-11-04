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

    var chart = new CanvasJS.Chart("chartContainer", {
        animationEnabled: true,
        theme: "light2",
        title:{
          text: "Temperature throughout the day"
        },
        axisY:{
          includeZero: false
        },
        data: [{        
          type: "line",       
          dataPoints: [
            { y: 14 },
            { y: 14},
            { y: 15, indexLabel: "highest",markerColor: "red", markerType: "triangle" },
            { y: 13 },
            { y: 14 },
            { y: 13 },
            { y: 13 },
            { y: 12 },
            { y: 7 , indexLabel: "lowest",markerColor: "DarkSlateGrey", markerType: "cross" },
            { y: 10 },
            { y: 9 },
            { y: 8 }
          ]
        }]
      });
      chart.render();

      document.getElementById('recommendations').append("It's COLD outside, wear something light. Wear ONE layer. Also, It's going to rain today, bring an umbrella and waterproof boots");

      $('#chartContainer').fadeTo(1000, 1);
      $('#recommendations').fadeTo(1000, 1);


}

function locatonNotReceived(positionError) {
    console.log(positionError);
}

$('document').ready(function() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(onPositionReceived, locatonNotReceived);
    }
});