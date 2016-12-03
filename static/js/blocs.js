$(document).ready(function(){
  $('.individual-bloc-fav').each(function(){
    var id = $(this).data('fav');
    if ($(this).data('fav') == 1) {
      $(this).css('color', 'rgb(243, 249, 0)');
    }
    else if ($(this).data('fav') == 0) {
      $(this).css('color', 'rgb(0, 0, 0)');
    }
  });
});

$('.individual-bloc-edit').on('click', function(){
  var id = $(this).data('id');

  $('#edit-popup-' + id)[0].setAttribute('style', 'display: block;');
  $('#cancel-' + id).one('click', function() {
    console.log($("#edit-popup-" + id)[0]);
    $('#edit-popup-' + id)[0].setAttribute('style', 'display: none;');
  });
});

$('.individual-bloc-delete').on('click', function(){
  var id = $(this).data('id');
  $('#deleteBloc' + id).submit();
});

$('.individual-bloc-fav').on('click', function(){
  var blocId = $(this).data('id');

  if($(this).css('color') === 'rgb(0, 0, 0)'){
    $(this).css('color', '#f3f900');
    $('#form-' + blocId).submit(
      $.ajax({
        url: "/favBloc",
        data: $('#fav-form-' + blocId).serialize(),
        type: "POST",
        success: function (data) {
          $('#drag' + blocId).attr('data-fav', '1');
          console.log("success: " + data);
        }
      }));
  }
  else if($(this).css('color') === 'rgb(243, 249, 0)'){
    $(this).css('color', '#000000');
    $('#form-' + blocId).submit(
      $.ajax({
        url: "/unfavBloc",
        data: $('#unfav-form-' + blocId).serialize(),
        type: "POST",
        success: function (data) {
          $('#drag' + blocId).attr('data-fav', '0');
          console.log("success: " + data);
        }
      }));
  }
});

$("img").error(function(){
  $(this).attr('src', 'static/images/missing.png');
});
