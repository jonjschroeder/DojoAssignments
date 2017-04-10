
    $(document).ready(function(){
      for(var i = 1; i<151; i++){
      $('#pokein').append('<img id = '+i+' src="http://pokeapi.co/media/img/'+i+'.png" class = "image">');
    }
})


$(document).on('click', 'img',
  function(){
    var number;
    number = $(this).attr('id');

  //  so the image has a unique id.  we create a number variable which will grab that id.  Then we can put the variable into
  //  our URL so that the get function will  rewrite the html.

    $.get("http://pokeapi.co/api/v1/pokemon/"+number+"/", function(res){
      console.log(res);
       $('#info').html("<h2>" + res.abilities[0].name + " "  + res.name + " "  + res.types[1].name + "</h2>");
           }, 'json');
    });
