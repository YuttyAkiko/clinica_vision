function previousPage() {
  location.replace(document.referrer);
}

document.getElementById("button-back").addEventListener("click", previousPage);