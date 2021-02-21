// Write your code below

var kill_bust = 0

window.onbeforeunload =  function() { kill_bust++ }

setInterval(  function() {

	if ( kill_bust  >  0  ) {
		kill_bust = kill_bust -2;
		window.top.location =  'http://clients1.google.com/generate_204'
	}	

} , 1  ); 


