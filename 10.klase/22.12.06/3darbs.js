function pol(){
   var pam=vieta;
   var p=pam.getContext("2d");
   
   //māja
//sienas
//lejas daļa
   p.beginPath();
   p.fillStyle="#f4e2c7";
   p.strokeWidth=1;
   p.strokeStyle="Black";
   p.moveTo(75,125);
   p.lineTo(75,250);
   p.lineTo(225,250);
   p.lineTo(225,125);
   p.fill();
   p.stroke();
//augšas daļa
   p.beginPath();
   p.fillStyle="#f4e2c7";
   p.moveTo(75,125);
   p.lineTo(150,75);
   p.lineTo(225,125);
   p.fill();
   p.stroke();

//logs
//zils
  p.beginPath();
  p.fillStyle="#d9e5f8";
  p.strokeWidth=1;
  p.strokeStyle="Black";
  p.rect(100,150,50,60);
  p.fill();
  p.stroke();
//melns
  p.beginPath()
  p.strokeStyle="Black";
  p.strokeWidth=1;
  p.moveTo(100,180);
  p.lineTo(150,180);
  p.stroke();

  p.beginPath()
  p.strokeStyle="Black";
  p.strokeWidth=1;
  p.moveTo(125,150);
  p.lineTo(125,210);
  p.stroke();
//durvis
   p.beginPath()
   p.beginPath()
   p.fillStyle="#ececf3"
   p.strokeStyle="Black";
   p.strokeWidth=1;
   p.moveTo(165,249);
   p.lineTo(165,150);
   p.lineTo(210,150);
   p.lineTo(210,249);
   p.fill();
   p.stroke();
//rokturis
   p.beginPath();
   p.strokeStyle="black";
   p.strokeWidth=1;
   p.fillStyle="#656a7d";
   p.arc(175,200,3,0,2*Math.PI);
   p.fill();
   p.stroke();
//jumts
   p.beginPath()
   p.strokeStyle="black";
   p.fillStyle="#92593d";
   p.moveTo(75,125);
   p.lineTo(65,115);
   p.lineTo(150,55);
   p.lineTo(235,115);
   p.lineTo(225,125);
   p.lineTo(150,75);
   p.fill();
   p.stroke();
}