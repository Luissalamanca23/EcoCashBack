function iniciarmap(){
    var coord = {lat: -41.2619749501792, lng: -73.00187412681538}; //Llanquihue
    var coord2 = {lat: -41.31700019317179, lng: -72.98731783329482}; //Puerto Varas
    var coord3 = {lat: -41.459500917181245, lng: -72.93891320076274}; //Puerto Montt
    var map = new google.maps.Map(document.getElementById('map'),{
        zoom: 9,
        center: coord2
    });

    //Marcadores
    var marker1 = new google.maps.Marker({
        position: coord,
        map: map
    });

    var marker2 = new google.maps.Marker({
        position: coord2,
        map: map
    });

    var marker3 = new google.maps.Marker({
        position: coord3,
        map: map
    });

    //Información de los marcadores
    var info1 = new google.maps.InfoWindow({
        content: '<h1 style="font-size: 16px;">Punto Limpio en Llanquihue</h1>'   // Nueva información
    });

    var info2 = new google.maps.InfoWindow({
        content: '<h1 style="font-size: 16px;">Punto Limpio en Puerto Varas</h1>' // Nueva información
    });

    var info3 = new google.maps.InfoWindow({
        content: '<h1 style="font-size: 16px;">Punto Limpio en Puerto Montt</h1>' // Nueva información
    });

    //Eventos de los marcadores (click)
    marker1.addListener('click', function(){
        info1.open(map, marker1);
    });

    marker2.addListener('click', function(){
        info2.open(map, marker2);
    });

    marker3.addListener('click', function(){
        info2.open(map, marker3);
    });    
}