const toggleMenuClicked = () => {
  const body = document.body;
  const openIcon = document.getElementById("open-icon");
  const closeIcon = document.getElementById("close-icon");

  body.classList.toggle("open");

  if (body.classList.contains("open")) {
    openIcon.style.display = "none";
    closeIcon.style.display = "flex";
  } else {
    openIcon.style.display = "flex";
    closeIcon.style.display = "none";
  }
};

