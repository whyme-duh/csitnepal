function counterFunction(likes){
	alert("liked");
	var finalLikes = likes + 1;
	document.getElementById('like-btn').innerHtml = "1";

}



function display(showDisplay, offDisplay){
	document.getElementById(showDisplay).style.display = "block";
	document.getElementById(offDisplay).style.display = "none";
	
	
}
function offdisplay(showDisplay, offDisplay){
	document.getElementById(showDisplay).style.display = "block";
	document.getElementById(offDisplay).style.display = "none";
	
	
}