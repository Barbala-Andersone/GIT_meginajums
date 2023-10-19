//alert("...Tu esi iegājis miega režīmā...");
function migla(){
    //sasaistīt html canvu ar JS
    var pamats=vieta6;
    var k=pamats.getContext("2d");

    //paņemšu krāsas vērtību
    var krasa=vieta1.value;
    // (lai paskatītos, vai darbojas) alert(krasa);
    //paņemšu līn. biezuma vērtību
    var linija=Number(vieta2.value);
    if (vieta3.checked) {
        //zīmēju kvadrātu
        k.beginPath();
        k.strokeStyle=krasa;
        k.lineWidth=linija;
        k.rect(100,100,150,150);
        k.stroke();
    }
    if (vieta4.checked) {
        //zīmēju taisnstūri
        k.beginPath();
        k.strokeStyle=krasa;
        k.lineWidth=linija;
        k.rect(150,150,150,30)
        k.stroke();
    }
    if (vieta5.checked) {
        //zīmēju apli
        k.beginPath();
        k.strokeStyle=krasa;
        k.lineWidth=linija;
        k.arc(70,70,60,0,2*Math.PI);
        k.stroke();
    }
    if (vieta7.checked) {
        //zīmēju aizpildītu trijstūri...........līniju
        k.beginPath();
        k.fillStyle=krasa; //pildījuma krāsa
        k.moveTo(70,50);
        k.lineTo(100,75);
        k.lineTo(100,25);
        k.fill()
        k.stroke();
    }
    if (vieta8.checked) {
        //zīmēju smaidiņu
        //galva
        k.beginPath();
        k.fillStyle="yellow";
        k.arc(200,200,70,0,2*Math.PI);
        k.fill()

        //smaids
        k.beginPath();
        k.strokeStyle="black";
        k.lineWidth=3;
        k.arc(200,200,50,0,Math.PI);

        //smaida līnija
        k.moveTo(160,190);
        k.lineTo(140,210);

        k.moveTo(240,190);
        k.lineTo(260,210);

        k.stroke();
    }
    if (vieta8.checked) {
        k.beginPath();
        k.fillStyle="black";
k.arc(230,170,5,0,2*Math.PI);
k.fill();
k.stroke();
        
    }
    if (vieta8.checked) {
        k.fillStyle="black";
k.beginPath();
k.arc(170,170,5,0,2*Math.PI);
k.fill();
k.stroke();
        
    }
}