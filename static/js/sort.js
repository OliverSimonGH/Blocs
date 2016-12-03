// http://stackoverflow.com/questions/14160498/sort-element-by-numerical-value-of-data-attribute
function sort() {
  var value = $('#sort-blocs option:selected').val();

  if(value == "favourites"){
    $('#drop > [data-fav="1"]').show();
    $('#drop > [data-fav="0"]').hide();
  }
  else if (value == "video") {
    $('#drop > [data-sort="video"]').show();
    $('#drop > [data-sort="favourites"]').hide();
    $('#drop > [data-sort="web"]').hide();
    $('#drop > [data-sort="images"]').hide();
    $('#drop > [data-sort="all"]').hide();
  }
  else if (value == "web") {
    $('#drop > [data-sort="web"]').show();
    $('#drop > [data-sort="favourites"]').hide();
    $('#drop > [data-sort="video"]').hide();
    $('#drop > [data-sort="images"]').hide();
    $('#drop > [data-sort="all"]').hide();
  }
  else if (value == "images") {
    $('#drop > [data-sort="images"]').show();
    $('#drop > [data-sort="favourites"]').hide();
    $('#drop > [data-sort="video"]').hide();
    $('#drop > [data-sort="web"]').hide();
    $('#drop > [data-sort="all"]').hide();
  }
  else if (value == "all") {
    $('#drop > [data-showall="all"]').show();
  }
};
