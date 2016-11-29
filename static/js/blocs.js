$("#edit-form").hide();
var pressed = false;

function editBloc() {

  if(pressed)
  {
    $("#edit-form").hide();
    pressed = false;
  }
  else {
    $("#edit-form").show();
    pressed = true;
  }
}
