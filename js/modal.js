// Get both popups that will be used.
var popupOne = document.getElementsByClassName('popup')[0];
var popupTwo = document.getElementsByClassName('popup')[1];

//Gets the link for the popups.
var linkFirstPopup = document.getElementsByClassName('new-block')[0];

//Buttons to close popups.
var cancelOne = document.getElementById("cancel");
var CancelTwo = document.getElementById("cancel1");

//Button to open the second popup.
var BtnSecondPopup = document.getElementById('link-btn');

//First two function are to display and cose first popup.
function display() {
  popupOne.style.display = "block";
};

function close() {
  popupOne.style.display = "none";
};

//Next two function are to display and cose second popup.
function display1() {
  popupTwo.style.display = "block";
};

function close1() {
  popupTwo.style.display = "none";
};

//Listens for click event for the first popup, open and close.
linkFirstPopup.addEventListener("click", display);
cancelOne.addEventListener("click", close);

//Listens for click event for the second popup, open and close.
BtnSecondPopup.addEventListener("click", display1);
CancelTwo.addEventListener("click", close1);
