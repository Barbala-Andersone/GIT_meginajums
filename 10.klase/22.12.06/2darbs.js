function lo() {
    var kim=min;
    var z=kim.getContext("2d");
    var x=100;
    var y=100;
    z.fillStype="pink";
    z.fillRect(x,y,30,30);
    addEventListener("keydown", j);
   
    function j(kals){
        var kods=e.keyCode;
//pa kreisi
        if(kods==37){
            z.clearRect(0,0,min.width,min.height);
            x=x-10;
            z.fillRect(x,y,30,30);
        }
//pa labi
        if(kods==39){
            z.clearRect(0,0,min.width,min.height);
            x=x+10;
            z.fillRect(x,y,30,30);
        }
//uz augšu
        if(kods==38){
            z.clearRect(0,0,min.width,min.height);
            y=y-10;
            z.fillRect(x,y,30,30);
        }
//uz leju
        if(kods==40){
            z.clearRect(0,0,min.width,min.height);
            y=y+10;
            z.fillRect(x,y,30,30); 
        }
        //b ar kuru aizver logu
        if(kods==66){
            window.close();
        }
    }
}