

// document.getElementById('titulo').innerText = 'Hola Mundo'

// document.getElementById('titulo').style.color = 'red';




function cambiar_rojo() {
    document.getElementById('imagen').src = '../fotos/led_rojo.jpeg';
}

function cambiar_verde() {
    document.getElementById('imagen').src = '../fotos/led_verde.jpeg';
}


function sumar (num1,num2){
    var c = 0;
    c = num1 + num2;
    console.log(c);
    window.alert(c);
}


// Jquery

$(document).ready(function(){
    $("button").click(function(){
        $("p").hide();
    });
})