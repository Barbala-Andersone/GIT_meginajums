function po(){
    var kam=document.getElementById("vieta");
    var kas=kam.getContext("2d");

    var aka=-20;
    function ka(){
        kas.clearRect(0,0,200,200);//notīra canvu
        kas.fillStyle="pink";
        kas.fillRect(aka,20,20,20);
        aka=aka+1;
        if(aka>200){
            aka=-20;
        }
    }

    setInterval(ka, 20);

}
    /*
   setInterval(ka, 30)
}*/
/*
Metode setInterval
(metode, kas noteiktā laika intervālā liek izdarīt noteiktu darbību)
*/
//setInterval ('alert("Sveiki")', 5000);

/*function darbiba() {
    alert("Sveiki");
}

setInterval(darbiba, 5000);
*/
//izveidot canvu, kurā pārvietojas kvadrāts, j
//a canva beidzas, sāk atkal no sākuma.