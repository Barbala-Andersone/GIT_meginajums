function kola(){
    var izvele1=document.getElementById("aka1")
    var izvele2=document.getElementById("aka2")
    if (izvele1.checked==true){
        document.getElementById("vieta1").innerHTML="Esi izvēlējies zaļu krāsu."
    }
    if (izvele2.checked==true){
        document.getElementById("vieta2").innerHTML="Esi izvēlējies baltu krāsu."
    }
    if (izvele1.checked==false & izvele2.checked==false){
        document.getElementById("vieta1").innerHTML="Neesi neko izvēlējies."
    }


}