// http://stackoverflow.com/questions/14160498/sort-element-by-numerical-value-of-data-attribute
function sort() {
  var value = $('#sort-blocs option:selected').val();

  if(value == "favourites"){
    $('#box > [data-fav="1"]').show();
    $('#box > [data-fav="0"]').hide();
  }
  else if (value == "video") {
    $('#box > [data-sort="video"]').show();
    $('#box > [data-sort="favourites"]').hide();
    $('#box > [data-sort="web"]').hide();
    $('#box > [data-sort="images"]').hide();
    $('#box > [data-sort="all"]').hide();
  }
  else if (value == "web") {
    $('#box > [data-sort="web"]').show();
    $('#box > [data-sort="favourites"]').hide();
    $('#box > [data-sort="video"]').hide();
    $('#box > [data-sort="images"]').hide();
    $('#box > [data-sort="all"]').hide();
  }
  else if (value == "images") {
    $('#box > [data-sort="images"]').show();
    $('#box > [data-sort="favourites"]').hide();
    $('#box > [data-sort="video"]').hide();
    $('#box > [data-sort="web"]').hide();
    $('#box > [data-sort="all"]').hide();
  }
  else if (value == "all") {
    $('#box > [data-showall="all"]').show();
  }
};
