function u(){
    var pam=vieta;
    var v=pam.getContext("2d");

//māja

//sienas
    v.beginPath();
    v.fillStyle="gray";
    v.strokeStyle="gray",
    v.moveTo(145,275);
    v.lineTo(155,160);
    v.lineTo(250,160);
    v.lineTo(260,275);
    v.fill();
    v.stroke();
//logs
    v.beginPath();
    v.strokeStyle="#01fefd";
    v.fillStyle="#01fefd";
    v.rect(160,185,35,30);
    v.fill();
    v.stroke();
//durvis
    v.beginPath();
    v.fillStyle="#834002";
    v.strokeStyle="#834002";
    v.moveTo(225,275);
    v.lineTo(220,220);
    v.lineTo(245,220);
    v.lineTo(250,275);
    v.fill();
    v.stroke();
//jumts
    v.beginPath();
    v.fillStyle="#ff8000";
    v.strokeStyle="#ff8000";
    v.moveTo(130,165);
    v.lineTo(205,110);
    v.lineTo(280,165);
    v.fill();
    v.stroke();

//koks

//stubrs
    v.beginPath();
    v.fillStyle="#834002";
    v.strokeStyle="#834002";
    v.moveTo(50,280);
    v.lineTo(52,180);
    v.lineTo(80,180);
    v.lineTo(88,280);
    v.fill();
    v.stroke();
//lapas
    v.beginPath();
    v.fillStyle="#037e00";
    v.strokeStyle="#037e00";
    v.moveTo(100,190);
    v.lineTo(35,185);
    v.lineTo(10,155);
    v.lineTo(25,105);
    v.lineTo(45,95);
    v.lineTo(80,92);
    v.lineTo(115,115);
    v.lineTo(125,165);
    v.fill();
    v.stroke();
}