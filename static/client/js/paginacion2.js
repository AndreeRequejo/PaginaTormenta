
var currentIndex = 1; 

  function avanzar() {
    if (currentIndex < 2) {
      currentIndex++;
      cambiarContenido(currentIndex);
    }
  }

  function retroceder() {
    if (currentIndex > 1) {
      currentIndex--;
      cambiarContenido(currentIndex);
    }
  }

  function cambiarContenido(numero) {
    if ((numero === "uno")) {
      document.getElementById("contenido1").style.display = "block";
      document.getElementById("contenido2").style.display = "block";
      document.getElementById("contenido3").style.display = "block";
      document.getElementById("contenido4").style.display = "block";
      document.getElementById("contenido9").style.display = "block";
      document.getElementById("contenido10").style.display = "block";
      document.getElementById("contenido11").style.display = "block";
      document.getElementById("contenido12").style.display = "block";
      document.getElementById("contenido5").style.display = "none";
      document.getElementById("contenido6").style.display = "none";
      document.getElementById("contenido7").style.display = "none";
      document.getElementById("contenido8").style.display = "none";
      document.getElementById("contenido13").style.display = "none";
      document.getElementById("contenido14").style.display = "none";
      document.getElementById("contenido15").style.display = "none";
      document.getElementById("contenido16").style.display = "none";
    }else if ((numero === "dos")) {
      document.getElementById("contenido5").style.display = "block";
      document.getElementById("contenido6").style.display = "block";
      document.getElementById("contenido7").style.display = "block";
      document.getElementById("contenido8").style.display = "block";
      document.getElementById("contenido13").style.display = "block";
      document.getElementById("contenido14").style.display = "block";
      document.getElementById("contenido15").style.display = "block";
      document.getElementById("contenido16").style.display = "block";
      document.getElementById("contenido1").style.display = "none";
      document.getElementById("contenido2").style.display = "none";
      document.getElementById("contenido3").style.display = "none";
      document.getElementById("contenido4").style.display = "none";
      document.getElementById("contenido9").style.display = "none";
      document.getElementById("contenido10").style.display = "none";
      document.getElementById("contenido11").style.display = "none";
      document.getElementById("contenido12").style.display = "none";
    }
    if ((numero === 1)) {
      document.getElementById("contenido1").style.display = "block";
      document.getElementById("contenido2").style.display = "block";
      document.getElementById("contenido3").style.display = "block";
      document.getElementById("contenido4").style.display = "block";
      document.getElementById("contenido9").style.display = "block";
      document.getElementById("contenido10").style.display = "block";
      document.getElementById("contenido11").style.display = "block";
      document.getElementById("contenido12").style.display = "block";
      document.getElementById("contenido5").style.display = "none";
      document.getElementById("contenido6").style.display = "none";
      document.getElementById("contenido7").style.display = "none";
      document.getElementById("contenido8").style.display = "none";
      document.getElementById("contenido13").style.display = "none";
      document.getElementById("contenido14").style.display = "none";
      document.getElementById("contenido15").style.display = "none";
      document.getElementById("contenido16").style.display = "none";
    }else if ((numero === 2)) {
      document.getElementById("contenido5").style.display = "block";
      document.getElementById("contenido6").style.display = "block";
      document.getElementById("contenido7").style.display = "block";
      document.getElementById("contenido8").style.display = "block";
      document.getElementById("contenido13").style.display = "block";
      document.getElementById("contenido14").style.display = "block";
      document.getElementById("contenido15").style.display = "block";
      document.getElementById("contenido16").style.display = "block";
      document.getElementById("contenido1").style.display = "none";
      document.getElementById("contenido2").style.display = "none";
      document.getElementById("contenido3").style.display = "none";
      document.getElementById("contenido4").style.display = "none";
      document.getElementById("contenido9").style.display = "none";
      document.getElementById("contenido10").style.display = "none";
      document.getElementById("contenido11").style.display = "none";
      document.getElementById("contenido12").style.display = "none";
    }
  
  }



