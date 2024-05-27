$(function() {
  $( "#button-submit" ).click(function() {
    $( "#button-submit" ).addClass( "onclic", 250, validate);
  });

  function validate() {
    setTimeout(function() {
      $( "#button-submit" ).removeClass( "onclic" );
      $( "#button-submit" ).addClass( "validate", 450, callback );
    }, 2250 );
  }
    function callback() {
      setTimeout(function() {
        $( "#button-submit" ).removeClass( "validate" );
      }, 1250 );
    }
  });