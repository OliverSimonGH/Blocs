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
  $(".individual-bloc-checkbox").on('click', function() {
    var id = $(this).data('id');

    if($(this).data('move') == "none"){
      $(this).children('i').show();
      $(this).data('move', 'moved');
      $('#drag' + id).appendTo('#drag-links');
    }
    else if($(this).data('move') == "moved"){
      $(this).children('i').hide();
      $(this).data('move', 'none');
      $('#drag' + id).appendTo('#box');
      $('#new-block').insertAfter('#box');
    }
  });

  $('.individual-bloc-edit').one('click', function(){
    var id = $(this).data('id');
    $('#edit-popup-' + id).show();
    $('#cancel-' + id).on('click', function() {
      $('#edit-popup-' + id).hide();
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
        })
      );
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
        })
      );
    }
  });

  $("img").error(function(){
    $(this).attr('src', 'static/images/missing.png');
  });
});
