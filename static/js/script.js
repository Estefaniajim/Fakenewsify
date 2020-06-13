function myFunction() {
  var element = document.body;
  element.classList.toggle("dark-mode");

  (document.getElementsByClassName("form-control")[0]).classList.toggle("dark-mode-input");

}