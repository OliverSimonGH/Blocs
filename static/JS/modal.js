// Get both popups that will be used.
var popupOne = document.getElementById('popup-1');
var popupTwo = document.getElementById('popup-2');

//Gets the link for the popups.
var linkFirstPopup = document.getElementsByClassName('new-block')[0];

//Buttons to close popups.
var cancelOne = document.getElementById("cancel1");
var cancelTwo = document.getElementById("cancel2");

//Profile Popup
var profile = document.getElementById('profile');

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

window.onclick = function(event) {
  if (event.target == popupOne) {
    popupOne.style.display = "none";
  };

  if (event.target == popupTwo) {
    popupTwo.style.display = "none";
  };

};

//Listens for click event for the first popup, open and close.
linkFirstPopup.addEventListener("click", display);
cancelOne.addEventListener("click", close);

profile.addEventListener("click", display1);
cancelTwo.addEventListener("click", close1);

//Listens for click event for the second popup, open and close.
// BtnSecondPopup.addEventListener("click", display1);
// CancelTwo.addEventListener("click", close1);
