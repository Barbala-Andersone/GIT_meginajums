function po(){
    addEventListener("keydown", bam)

    function bam(kurs){
        if (kurs.keyCode==82) {
            document.body.style.background="red";
        }
        if (kurs.keyCode==71) {
            document.body.style.background="green";
        }
        if (kurs.keyCode==66) {
            document.body.style.background="blue";
        }
        if (kurs.keyCode==86) {
            document.body.style.background="violet";
        }
        if (kurs.keyCode==80) {
            document.body.style.background="pink";
        }
        if (kurs.keyCode==84) {
            document.body.style.background="teal";
        }
        if (kurs.keyCode==87) {
            document.body.style.background="white";
        }
        if (kurs.keyCode==89) {
            document.body.style.background="yellow";
        }    
    }
}