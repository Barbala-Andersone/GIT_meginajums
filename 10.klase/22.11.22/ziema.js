function ziema(){
    //esošajā kanvā uzzīmēt 7 kvadrātus.
    var pamats=vieta;
    var aa=pamats.getContext("2d");
//ausis
    aa.beginPath();
    aa.fillStyle="black";
    aa.arc(300,0,60,0,2*Math.PI);
    aa.fill();
    aa.stroke();

    aa.beginPath();
    aa.fillStyle="black";
    aa.arc(0,0,60,0,2*Math.PI);
    aa.fill();
    aa.stroke();
//acis
    aa.beginPath();
    aa.fillStyle="black";
    aa.arc(90,75,15,0,2*Math.PI);
    aa.fill();
    aa.stroke();
    
    aa.beginPath();
    aa.fillStyle="black";
    aa.arc(210,75,15,0,2*Math.PI);
    aa.fill();
    aa.stroke();
    
    aa.beginPath();
    aa.fillStyle="white";
    aa.arc(215,70,7,0,2*Math.PI);
    aa.fill();
    aa.stroke();
    
    aa.beginPath();
    aa.fillStyle="white";
    aa.arc(95,70,7,0,2*Math.PI);
    aa.fill();
    aa.stroke();
//deguns
    aa.beginPath();
    aa.fillStyle="black";
    aa.moveTo(125,130);
    aa.lineTo(150,150);
    aa.lineTo(175,130);
    aa.fill();
    aa.stroke();

    aa.beginPath();
    aa.fillStyle="grey";
    aa.moveTo(140,132);
    aa.lineTo(150,138);
    aa.lineTo(160,132);
    aa.fill();
    aa.stroke();
//smaids
    aa.beginPath();
    aa.strokeStyle="black";
    aa.lineWidth=3;
    aa.arc(170,150,30,0,0.5*Math.PI);
    aa.stroke();
    
    aa.beginPath();
    aa.strokeStyle="black";
    aa.lineWidth=3;
    aa.arc(130,150,30,1*Math.PI,1.5,true);
    aa.stroke();
    
    aa.beginPath();
    aa.strokeStyle="black";
    aa.lineWidth=3;
    aa.moveTo(130,180);
    aa.lineTo(170,180);
    aa.stroke();

    aa.beginPath();
    aa.fillStyle="black";
    aa.arc(150,158,40,2.2*Math.PI,0.8*Math.PI);
    aa.fill();
    aa.stroke();

    aa.beginPath();
    aa.fillStyle="black";
    aa.rect(118,180,64,1);
    aa.fill();
    aa.stroke();
//mēle
    aa.beginPath();
    aa.fillStyle="pink";
    aa.strokeStyle="pink";
    aa.arc(150,205,16,0,2*Math.PI);
    aa.fill();
    aa.stroke();

    aa.beginPath();
    aa.fillStyle="pink";
    aa.rect(134,185,32,25);
    aa.fill();
    aa.stroke();

    aa.beginPath();
    aa.strokeStyle="salmon";
    aa.moveTo(134,185);
    aa.lineTo(166,185);
    aa.moveTo(150,185);
    aa.lineTo(150,210);
    aa.stroke();
//1.logs
    aa.beginPath();
    aa.fillStyle="white";
    aa.strokeStyle="white";
    aa.rect(40,250,220,30);
    aa.fill();
    aa.stroke();

    aa.beginPath();
    aa.fillStyle="white";
    aa.strokeStyle="white";
    aa.arc(40,265,15,0,2*Math.PI);
    aa.fill();
    aa.stroke();

    aa.beginPath();
    aa.fillStyle="white";
    aa.strokeStyle="white";
    aa.arc(260,265,15,0,2*Math.PI);
    aa.fill();
    aa.stroke();
//2.logs
    aa.beginPath();
    aa.fillStyle="white";
    aa.strokeStyle="white";
    aa.rect(40,295,220,30);
    aa.fill();
    aa.stroke();

    aa.beginPath();
    aa.fillStyle="white";
    aa.strokeStyle="white";
    aa.arc(40,310,15,0,2*Math.PI);
    aa.fill();
    aa.stroke();

    aa.beginPath();
    aa.fillStyle="white";
    aa.strokeStyle="white";
    aa.arc(260,310,15,0,2*Math.PI);
    aa.fill();
    aa.stroke();
//iekšējais logs
    aa.beginPath();
    aa.fillStyle="black";
    aa.strokeStyle="black";
    aa.arc(200,310,11,0,2*Math.PI);
    aa.fill();
    aa.stroke();

    aa.beginPath();
    aa.fillStyle="black";
    aa.strokeStyle="black";
    aa.arc(260,310,11,0,2*Math.PI);
    aa.fill();
    aa.stroke();

    aa.beginPath();
    aa.fillStyle="black";
    aa.strokeStyle="black";
    aa.rect(200,299,60,22);
    aa.fill();
    aa.stroke();
//3.logs
    aa.beginPath();
    aa.fillStyle="black";
    aa.strokeStyle="black";
    aa.rect(40,355,220,30);
    aa.fill();
    aa.stroke();

    aa.beginPath();
    aa.fillStyle="black";
    aa.strokeStyle="black";
    aa.arc(40,370,15,0,2*Math.PI);
    aa.fill();
    aa.stroke();

    aa.beginPath();
    aa.fillStyle="black";
    aa.strokeStyle="black";
    aa.arc(260,370,15,0,2*Math.PI);
    aa.fill();
    aa.stroke();








    /*for(var i=0; i<20;i=i+1){
        var x=Math.floor(Math.random()*300+1)
        var y=Math.floor(Math.random()*300+1)
        var r=Math.floor(Math.random()*300+1)//+1, lai nevarētu būt rādiuss 0
        aa.beginPath();
        aa.arc(x,y,r,0,2*Math.PI);
        aa.stroke();

    }*/
    /*
    Math.random(); ...... (0;1]
        (lai iegūtu labo pusi)
        ja nepieciešami veseli skaitļi (iegūst 0,3456789......*10=2.2345678)
        izmanto Math.floor()   noapaļo ar iztrūkumu (ja ir 5,4 -> 5, ja ir 5,6-> 5)
        ...........skaitļi no 0 līdz 9 (reizina ar 10)
        ...........skaitļi no 0 līdz 11 (reizina ar 12)

        (lai iegūtu kreiso pusi) (reizina ar ...+sākuma skaitli)
        skaitļi no 0 līdz 10 (reizina ar 10+1)
        */
  /* for (var i=20;i<300;i+40){
    aa.strokeRect(i,i,30,30);
     }
     */
    //document.write(Math.random())


    /*var sakums=2;
    var beigas=10;

    for (var i=sakums; i<=beigas; i++){

        document.write(i +" kvadrātā ir "+i*i+"<br>")
    }*/



    /*var sakums=1
    var beigas=10;
    for (var i =sakums; i<beigas; i++) {
        //iekavās nosacījumi (sākuma vērt.;(i<10, ja ir mazāks par 10, tad būs ierakstīts))
        document.write(i+ " ");
    }    

    document.write("<br>");

    document.write(" Izvadīju visus skaitļus no " + sakums + " līdz " +(beigas-1));*/
}