var imgAtual = "daniel.jpg"
var aux = "";
var img2 = "img2.png"
var a = 3

function loopimg(){
    if (a<2){
    document.getElementById("img").src = imgAtual
    aux = imgAtual
    imgAtual = img2
    img2 = aux
    }
    else{
        
        document.getElementById("btn").innerText += 'a'
    }
}
