var images = ['{% static '' %}assets/img/nature1.jpg','{% static '' %}assets/img/portrait2.jpg', '{% static '' %}assets/img/portrait3.jpg'];
var currentIndex = 0;
var element = document.getElementById('myElement');

function changeBackgroundImage() {
  currentIndex++;
  if (currentIndex >= images.length) {
    currentIndex = 0;
  }
  element.style.backgroundImage = 'url(' + images[currentIndex] + ')';
}

function startImageTransition() {
  element.style.backgroundImage = 'url(' + images[currentIndex] + ')';
  setInterval(changeBackgroundImage, 3000); // Change image every 3 seconds
}

startImageTransition();
