function uu(){
    var plosts;
    plosts=document.getElementById("vieta1").value;
   // console.log(plosts); pārbaudu vai piešķir vērtību*/
    if(document.getElementById('vieta2').checked){
        document.getElementById('vieta4').innerHTML=plosts+"- Tava atbilde ir pieņemta";
    }
    if(document.getElementById('vieta3').checked){
        document.getElementById('vieta4').innerHTML=plosts+"- Tava atbilde ir pieņemta.";
    }
}
function kk(){
    var plasts;
    plasts=document.getElementById.value
    if(dokument.getElementById("vieta5").checked){
        document.getElementById("vieta8").innerHTML="Tava atbilde ir sarkans.";
    }
    if(dokument.getElementById("vieta6").checked){
        document.getElementById("vieta8").innerHTML="Tava atbilde ir zils.";
    }
    if(dokument.getElementById("vieta7").checked){
        document.getElementById("vieta8").innerHTML="Tava atbilde ir dzeltens.";
    }
}