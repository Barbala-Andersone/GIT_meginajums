function poga(){
    var pam=vieta;
    var p=pam.getContext("2d");

    //koks
//stumbrs
    p.beginPath();
    p.fillStyle="#814000";
    p.strokeStyle="#814000";
    p.moveTo(60,230);
    p.lineTo(65,115);
    p.lineTo(100,115);
    p.lineTo(110,230);
    p.fill();
    p.stroke();

//koka lapas
    p.beginPath();
    p.fillStyle="#037e00";
    p.strokeStyle="#037e00";
    p.moveTo(115,125);
    p.lineTo(50,120)
    p.lineTo(20,100);
    p.lineTo(35,50);
    p.lineTo(50,40);
    p.lineTo(100,35);
    p.lineTo(130,45);
    p.lineTo(150,105);
    p.fill();
    p.stroke();

    //māja
//sienas
   p.beginPath()
   p.fillStyle="gray";
   p.strokeStyle="gray";
   p.moveTo(200,110);
   p.lineTo(190,230);
   p.lineTo(330,230);
   p.lineTo(315,110);
   p.fill();
   p.stroke();

//logs
   p.beginPath()
   p.fillStyle="#01fefd";
   p.strokeStyle="#01fefd";
   p.moveTo(210,130);
   p.lineTo(207,170);
   p.lineTo(255,170);
   p.lineTo(253,130);
   p.fill();
   p.stroke();

//durvis
   p.beginPath()
   p.fillStyle="#834002";
   p.strokeStyle="#834002";
   p.moveTo(283,230);
   p.lineTo(278,170);
   p.lineTo(308,170);
   p.lineTo(313,230);
   p.fill();
   p.stroke();

//jumts
    p.beginPath();
    p.fillStyle="#ff8000";
    p.strokeStyle="#ff8000";
    p.moveTo(165,110);
    p.lineTo(260,40);
    p.lineTo(355,110);
    p.fill();
    p.stroke();
}