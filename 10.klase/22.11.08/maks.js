function zimet(){
    //tiekn izveidots "savienojums" uz canvu
    var pamatne=document.getElementById("vieta1");
    var zim=pamatne.getContext("2d");
    //uzzīmēšu sarkanu kvadrātu
    zim.beginPath();
    zim.lineWidth=16;
    zim.strokeStyle="red";//līnijas krāsa
    zim.rect(50,50,150,150)
    zim.stroke()
}
function zimet1(){
    var pamatne1=document.getElementById("vieta2");
    var zim1=pamatne1.getContext("2d");

    zim1.beginPath();
    zim1.lineWidth=16;
    zim1.strokeStyle="black";
    zim1.fillStyle="blue";
    zim1.rect(50,50,150,150);
    zim1.fill();

    zim1.stroke();
}
function zimet2(){
    var pamatne2=document.getElementById("vieta3");
    var zim2=pamatne2.getContext("2d");
    zim2.beginPath();
    zim2.arc(120,100,10,0,2*Math.PI)
    zim2.lineWidth=2;
    zim2.strokeStyle="white";
    zim2.fillStyle="white";
    zim2.fill();
    zim2.arc(120,100,30,0,2*Math.PI);
    zim2.fill();
    zim2.stroke();
}
function zimet3(){
    var pamatne3=document.getElementById("vieta3")
    var zim3=pamatne3.getContext("2d");
    zim3.beginPath()
    zim3.arc(120,150,40,0,2*Math.PI);
    zim3.lineWidth=2;
    zim3.strokeStyle="white";
    zim3.fillStyle="white";
    zim3.fill();
    zim3.arc(120,150,20,0,2*Math.PI);
    zim3.fill();
    zim3.stroke();
}
function zimet4(){
    var pamatne3=document.getElementById("vieta3")
    var zim3=pamatne3.getContext("2d");
    zim3.beginPath()
    zim3.arc(120,200,50,0,2*Math.PI);
    zim3.lineWidth=2;
    zim3.strokeStyle="white";
    zim3.fillStyle="white";
    zim3.fill();
    zim3.arc(120,200,30,0,2*Math.PI);
    zim3.fill();
    zim3.stroke();
}
function zimet5(){
    var pamatne1=document.getElementById("vieta3");
    var zim1=pamatne1.getContext("2d");

    zim1.beginPath();
    zim1.lineWidth=6;
    zim1.strokeStyle="black";
    zim1.fillStyle="black";
    zim1.rect(100,20,40,60);
    zim1.fill();

    zim1.stroke();
}
function zimet6(){
    var pamatne1=document.getElementById("vieta3");
    var zim1=pamatne1.getContext("2d");

    zim1.beginPath();
    zim1.lineWidth=16;
    zim1.strokeStyle="black";
    zim1.fillStyle="blue";
    zim1.rect(80,70,80,10);
    zim1.fill();

    zim1.stroke();
}
function zimet7(){
    var pamatne1=document.getElementById("vieta3");
    var zim1=pamatne1.getContext("2d");

    zim1.beginPath();
    zim1.lineWidth=6;
    zim1.strokeStyle="black";
    zim1.fillStyle="black";
    zim1.rect(105,100,5,5);
    zim1.fill();
    zim1.stroke();
}
function zimet8(){
    var pamatne1=document.getElementById("vieta3");
    var zim1=pamatne1.getContext("2d");

    zim1.beginPath();
    zim1.lineWidth=6;
    zim1.strokeStyle="black";
    zim1.fillStyle="black";
    zim1.rect(120,100,5,5);
    zim1.fill();
    zim1.stroke();
}
function zimet9(){
    var pamatne3=document.getElementById("vieta3")
    var zim3=pamatne3.getContext("2d");
    zim3.beginPath()
    zim3.arc(120,120,5,0,2*Math.PI);
    zim3.lineWidth=2;
    zim3.strokeStyle="black";
    zim3.fillStyle="orange";
    zim3.fill();
    zim3.arc(120,120,5,0,2*Math.PI);
    zim3.fill();
    zim3.stroke();
}