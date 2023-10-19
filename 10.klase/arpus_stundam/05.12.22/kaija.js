function p(){
    var vieta=v.getContext("2d");

    v.beginPath();
    v.strokeStyle="pink";
    v.strokeWidth=1;
    v.rect(100,100,50,50);
    v.stroke();

    v.beginPath();
    v.fillStyle="red";
    v.moveTo(100,100);
    v.lineTo(50,50);
    v.lineTo(150,150);
    v.fill();
    v.stroke();

    v.beginPath();
    v.arc(20,20,10,0,2*Math.PI);
    v.stroke();

    v.beginPath();
    v.arc(40,20,0,1*Math.PI);
    v.stroke();
}