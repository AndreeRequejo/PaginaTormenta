function seleccionado() {
  var card1 = document.getElementById("card1");
  var card2 = document.getElementById("card2");
  var flexRadioDefault1 = document.getElementById("envioGratis");
  var flexRadioDefault2 = document.getElementById("recojoTienda");

  if (flexRadioDefault1.checked) {
    card1.style.backgroundColor = "#717FE0";
    card2.style.backgroundColor = "";
    card1.style.color = "white";
    card2.style.color = "";
    document.getElementById("contenido1").style.display = "block";
    document.getElementById("contenido2").style.display = "none";
  } else if (flexRadioDefault2.checked) {
    card2.style.backgroundColor = "#717FE0";
    card1.style.backgroundColor = "";
    card2.style.color = "white";
    card1.style.color = "";
    document.getElementById("contenido2").style.display = "block";
    document.getElementById("contenido1").style.display = "none";
  }
}