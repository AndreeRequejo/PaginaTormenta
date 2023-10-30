var hearts = document.querySelectorAll(".cora");

hearts.forEach(function(heart) {
  heart.addEventListener("click", function() {
    this.classList.toggle("clicked");
  });
});

var hearts1 = document.querySelectorAll(".cora1");

hearts1.forEach(function(heart) {
  heart.addEventListener("click", function() {
    this.classList.toggle("clicked");
  });
});

var hearts2 = document.querySelectorAll(".cora2");

hearts2.forEach(function(heart) {
  heart.addEventListener("click", function() {
    this.classList.toggle("clicked");
  });
});