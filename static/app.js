function take_snapshot() {
    Webcam.snap( function(data_uri) {
      document.getElementById('my_result').innerHTML = '<img src="'+data_uri+'"/>';
      console.log(data_uri)
    } );
  }
