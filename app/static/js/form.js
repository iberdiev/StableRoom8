function checked(arr){
    for(index in arr){
        if (arr[index].checked){
            return arr[index].value
        }
    }
}
function selected(element){
    for(index in element.options){
        if (element.options[index].selected){
            return element.options[index].text;
        }
    }
}

document.onreadystatechange = function(){
    let button = document.getElementById("submit");
    button.onclick = function(){
        let fullName = document.getElementById("fullName").value;
        let email = document.getElementById("email").value;
        let country = checked(document.getElementsByName("countryRadios"));
        let year = checked(document.getElementsByName("yearRadios"));
        let campus = checked(document.getElementsByName("campusRadios"));
        let gender = checked(document.getElementsByName("genderRadios"));
        let messyClean = document.getElementById("messyClean").value;
        let silenceLoud = document.getElementById("silenceLoud").value;
        let difficultEasy = document.getElementById("difficultEasy").value;
        let noDefinetely = document.getElementById("noDefinetely").value;
        let darknessLight = document.getElementById("darknessLight").value;
        let shyOutgoing = document.getElementById("shyOutgoing").value;
        let sleepEarlyLate = document.getElementById("sleepEarlyLate").value;
        let getUpEarlyLate = document.getElementById("getUpEarlyLate").value;
        let wantRoommate = checked(document.getElementsByName("wantRoommate"));
        let emailRoommate;
        if (wantRoommate == 1) {
            emailRoommate = document.getElementById("emailRoommate").value;
        } else {
            emailRoommate = "Nothing";
        }
        let whatsApp = document.getElementById("whatsApp").value;
        let tShirtSize = selected(document.getElementById("tShirtSize"));
        let hoodieSize = selected(document.getElementById("hoodieSize"));
        let healthIssues = document.getElementById("healthIssues").value;
        let comments = document.getElementById("comments").value;
        let emergency = document.getElementById("emergency").value;
        
    }
}