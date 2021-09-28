// -------------------------------------------------------------------- Hover color functions

// Change the colors of links
function hover(id){
    let hoverLink = document.getElementById(id);
    let socialIcon = hoverLink.children[0];
    let socialText = hoverLink.children[1];
    switch (id) {
        case "email":
            socialIcon.style.color = "#FEE101";
            socialText.style.color = "#FEE101";
            break;
        case "bandcamp":
            socialIcon.style.color = "#1DA0C3";
            socialText.style.color = "#1DA0C3";
            break;
        case "facebook":
            socialIcon.style.color = "#1298F6";
            socialText.style.color = "#1298F6";
            break;
        case "instagram":
            socialIcon.style.color = "#C9006B";
            socialText.style.color = "#C9006B";
            break;
        case "twitter":
            socialIcon.style.color = "#00A2F3";
            socialText.style.color = "#00A2F3";
            break;
        case "youtube":
            socialIcon.style.color = "#FF0000";
            socialText.style.color = "#FF0000";
            break;
        case "spotify":
            socialIcon.style.color = "#1ED760";
            socialText.style.color = "#1ED760";
            break;
        case "tiktok":
            socialIcon.style.color = "#00F7F2";
            socialText.style.color = "#00F7F2";
            break;
        case "soundcloud":
            socialIcon.style.color = "#FF5500";
            socialText.style.color = "#FF5500";
            break;
        default:
            socialIcon.style.color = "#FFF";
            socialText.style.color = "#FFF";
            break;
    }    
}

// Reset to normal after hover
function normal(id) {
    let hoverLink = document.getElementById(id);
    hoverLink.children[0].style.color = "#fff";
    hoverLink.children[1].style.color = "#fff";
}