function nolasitSaturu(notikums){
    var datnesSaturs;
    datnesSaturs=notikums.target.result;
    izvade1.innerHTML=datnesSaturs;
}
function atvertDatni(){
    var d=datne.files[0];
    if (d){
        atvetLasisanai(d);
    }

}

function atvetLasisanai(d){
    var r=new FileReader();
    r.readAsText(d);
    r.onload=nolasitSaturu;
    r.onerror=kluduApstrade;
}

function kluduApstrade(notikums){
    if(notikums.target.error.name=="NotReadableError"){
        alert("Datnes nolasīšanas kļūda");
    }
}