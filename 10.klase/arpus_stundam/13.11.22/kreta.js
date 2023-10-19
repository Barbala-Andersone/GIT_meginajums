//alert("vasara nāk"); 
function blue() {
    var mala=document.getElementById("vieta1").value;

    //if (document.getElementById("vieta1")) {
    //    document.getElementById("vieta2").innerHTML=mala+" - Jūsu atbilde ir saņemta.";
    //}
    if (document.getElementById("vieta11").checked) {
        document.getElementById("vieta2").innerHTML=mala+ " - Jūsu atbilde ir pieņemta.";
    }
    if (document.getElementById("vieta12").checked) {
        document.getElementById("vieta2").innerHTML=mala+ " - Jūsu atbilde ir pieņemta.";
    }
    if (document.getElementById("vieta13").checked) {
        document.getElementById("vieta2").innerHTML=mala+ " - Jūsu atbilde ir pieņemta.";
    }
}

function klue() {
    if (document.getElementById("vieta3").checked) {
        document.getElementById("vieta6").innerHTML="Jūsu atbilde ir zaļa.";
    }
    if (document.getElementById("vieta4").checked) {
        document.getElementById("vieta7").innerHTML="Jūsu atbilde ir zila.";
    }
    if (document.getElementById("vieta5").checked) {
        document.getElementById("vieta8").innerHTML="Jūsu atbilde ir dzeltena.";
    }
}