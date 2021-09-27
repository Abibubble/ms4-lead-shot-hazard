// -------------------------------------------------------------------- Hover color functions

// Change the colors of links
function hover(id){
    let hoverLink = document.getElementById(id);
    switch (id) {
        case "email":
            hoverLink.style.color = "#FEE101";
            break;
        case "bandcamp":
            hoverLink.style.color = "#1da0c3";
            break;
        case "facebook":
            hoverLink.style.color = "#1298f6";
            break;
        case "instagram":
            hoverLink.style.color = "#c9006b";
            break;
        case "twitter":
            hoverLink.style.color = "#00a2f3";
            break;
        case "youtube":
            hoverLink.style.color = "#ff0000";
            break;
        case "spotify":
            hoverLink.style.color = "#1ed760";
            break;
        case "tiktok":
            hoverLink.style.color = "#00f7f2";
            break;
        case "soundcloud":
            hoverLink.style.color = "#ff5500";
            break;
        default:
            hoverLink.style.color = "#fff";
            break;
    }    
}

// Reset to normal after hover
function normal(id) {
	document.getElementById(id).style.color = "#fff";
}