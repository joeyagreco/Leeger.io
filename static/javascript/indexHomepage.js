function redirectToLeagueHomepage() {
    startLoading();
    var leagueId = document.getElementById("league_id").value;
    window.location = "/league-homepage/"+leagueId;
}

function checkCharacterLimit() {
    // this function simply prevents the user from entering a league id that has more than 6 digits
    var leagueIdForm = document.getElementById("league_id");
    if(leagueIdForm.value.length > 6) {
        leagueIdForm.value = leagueIdForm.value.slice(0,6);
    }
}

function activateSubmitButton() {
    // this activates the submit button if the league name field isn't empty
    var leagueIdInputElement = document.getElementById("league_id");
    var loadLeagueButtonElement = document.getElementById("load_league_button");
    if(leagueIdInputElement.value.replaceAll(/\s/g,'').length == 6) {
        // valid league name given, enable submit button
        loadLeagueButtonElement.classList.remove("disabled");
    }
    else {
        // check if submit button is disabled, if not, disable it again
        if(!loadLeagueButtonElement.classList.contains("disabled")) {
            loadLeagueButtonElement.classList.add("disabled");
        }
    }
}