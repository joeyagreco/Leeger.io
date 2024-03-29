function addWeek() {
    startLoading();
    var leagueId = document.getElementById("league_id").value;
    var year = document.getElementById("year_number").value;
    window.location = "/add-week/"+leagueId+"/"+year;
}

function updateWeekDropdown(weekNumber) {
    startLoading();
    var leagueId = document.getElementById("league_id").value;
    var year = document.getElementById("year_number").value;
    window.location = "/add-update-weeks/"+leagueId+"/"+year+"/"+weekNumber;
}

function updateLeagueRedirect() {
    startLoading();
    var leagueId = document.getElementById("league_id").value;
    var year = document.getElementById("year_number").value;
    window.location = "/update-league/"+leagueId+"/"+year;
}

function deleteWeek() {
    var weekNumber = document.getElementById("week_number").value;
    var leagueId = document.getElementById("league_id").value;
    var yearNumber = document.getElementById("year_number").value;

    Swal.fire({
    title: 'Are you sure you want to delete week ' + weekNumber + '?',
    text: "This cannot be undone.",
    icon: 'warning',
    iconColor: '#914053',
    showCancelButton: true,
    confirmButtonColor: '#914053',
    cancelButtonColor: '#40916C',
    confirmButtonText: 'Yes, delete week ' + weekNumber + '.',
    heightAuto: false
    }).then((result) => {
        if (result.isConfirmed) {
            startLoading();
            window.location = "/delete-week/"+leagueId+"/"+yearNumber+"/"+weekNumber;
         }
    })
}

function setOriginalValues() {
    // this saves the original values of everything on the page to sessionStorage
    sessionStorage["numberOfTeams"] = document.getElementById("number_of_teams").value;
    for(i=1; i<=sessionStorage["numberOfTeams"]/2; i++) {
        sessionStorage["originalTeamAId_matchup_"+i] = document.getElementById("teamAId_matchup_"+i).value;
        sessionStorage["originalTeamAScore_matchup_"+i] = document.getElementById("teamAScore_matchup_"+i).value;
        sessionStorage["originalTeamBId_matchup_"+i] = document.getElementById("teamBId_matchup_"+i).value;
        sessionStorage["originalTeamBScore_matchup_"+i] = document.getElementById("teamBScore_matchup_"+i).value;
    }
}

function checkAndHandleIfChangeMade() {
    // this checks if a change was made and handles it accordingly
    for(i=1; i<=sessionStorage["numberOfTeams"]/2; i++) {
        if(sessionStorage["originalTeamAId_matchup_"+i] != document.getElementById("teamAId_matchup_"+i).value) {
            handleChangeMade();
            return;
        }
        if(sessionStorage["originalTeamAScore_matchup_"+i] != document.getElementById("teamAScore_matchup_"+i).value) {
            handleChangeMade();
            return;
        }
        if(sessionStorage["originalTeamBId_matchup_"+i] != document.getElementById("teamBId_matchup_"+i).value) {
            handleChangeMade();
            return;
        }
        if(sessionStorage["originalTeamBScore_matchup_"+i] != document.getElementById("teamBScore_matchup_"+i).value) {
            handleChangeMade();
            return;
        }
    }
    undoChangeMade();
}

function getChangeCount() {
    return parseInt(sessionStorage["changeCount"]);
}

function clearChanges() {
    // this sets/resets the change count to 0
    sessionStorage["changeCount"] = "0";
}

function disableDeleteWeek() {
    // this disables the delete week button if the week is 0
    if(document.getElementById("week_number").value == 1) {
        document.getElementById("deleteWeekButton").disabled = true;
        document.getElementById("deleteWeekButton").classList.add("disabled");
    }
}

function handleChangeMade() {
    // when this method is called, it increments the changeCount by 1
    // it also enables the save button
    // it also disables the add week button
    // it also disables the week select dropdown
    // it also disables the back to league button
    var saveButton = document.getElementById("saveChangesButton");
    saveButton.classList.remove("disabled");
    saveButton.disabled = false;
    var addWeekButton = document.getElementById("addWeekButton");
    addWeekButton.classList.add("disabled");
    addWeekButton.disabled = true;
    var weekSelectButton = document.getElementById("dropdownMenuButton");
    weekSelectButton.classList.add("disabled");
    weekSelectButton.disabled = true;
    var backToLeagueButtonElement = document.getElementById("updateLeagueButton");
    backToLeagueButtonElement.classList.add("disabled");
    backToLeagueButtonElement.disabled=true;
    var changeCount = getChangeCount();
    changeCount++;
    sessionStorage["changeCount"] = changeCount.toString();
}

function undoChangeMade() {
    // when this method is called, it sets the changeCount to 0
    // it also disables the save button
    // it also enables the add week button
    // it also enables the week select dropdown
    // it also enables the back to league button
    var saveButton = document.getElementById("saveChangesButton");
    saveButton.classList.add("disabled");
    saveButton.disabled = true;
    var addWeekButton = document.getElementById("addWeekButton");
    addWeekButton.classList.remove("disabled");
    addWeekButton.disabled = false;
    var weekSelectButton = document.getElementById("dropdownMenuButton");
    weekSelectButton.classList.remove("disabled");
    weekSelectButton.disabled = false;
    var backToLeagueButtonElement = document.getElementById("updateLeagueButton");
    backToLeagueButtonElement.classList.remove("disabled");
    backToLeagueButtonElement.disabled = false;
    clearChanges()
}

function makeActiveTeam(newTeamElement, newTeam, matchupId) {
    // this makes the given team active
    var activeClassName = "activeOdd";
    var teamAorB = "teamA";
    if(newTeamElement.classList.contains("evenTeam")) {
        activeClassName = "activeEven";
        teamAorB = "teamB"
    }
    var activeElement = document.getElementsByClassName(activeClassName)[0];
    // make the selected element have the active class and take it from the old active element
    newTeamElement.classList.add("active");
    newTeamElement.classList.add(activeClassName);
    activeElement.classList.remove("active");
    activeElement.classList.remove(activeClassName);
    // now update the display button
    var displayButtonElement = document.getElementsByClassName(teamAorB+"MatchupButton"+matchupId)[0];
    displayButtonElement.innerHTML = newTeam["teamName"];
    displayButtonElement.value = newTeam["teamId"];
    // remove teamId styling class
    for(var i=displayButtonElement.classList.length-1; i>=0; i--) {
        var className = displayButtonElement.classList[i];
        if(className.startsWith("backgroundTeamId")) {
            displayButtonElement.classList.remove(className);
        }
    }
    displayButtonElement.classList.add("backgroundTeamId"+newTeam["teamId"]);
    // update the score input
    var scoreElement = document.getElementById(teamAorB+"Score_matchup_"+matchupId);
    // remove teamId styling class
    for(var i=scoreElement.classList.length-1; i>=0; i--) {
        var className = scoreElement.classList[i];
        if(className.startsWith("backgroundTeamId")) {
            scoreElement.classList.remove(className);
        }
    }
    scoreElement.classList.add("backgroundTeamId"+newTeam["teamId"]);
    // change id of score element
    scoreElement.id = teamAorB+"Score_matchup_"+matchupId;
    // handle change
    checkAndHandleIfChangeMade();
}

function postWeek() {
    startLoading();
    // this posts all needed info for the week
    var leagueId = document.getElementById("league_id").value;
    var weekNumber = document.getElementById("week_number").value;
    var yearNumber = document.getElementById("year_number").value;
    var numberOfTeams = document.getElementById("number_of_teams").value;

    data = {"league_id": leagueId,
            "week_number": weekNumber,
            "year_number": yearNumber};
    // add all the teams and scores
    for(i=1; i<=numberOfTeams/2; i++) {
        // add team
        data["teamAId_matchup_"+i] = document.getElementById("teamAId_matchup_"+i).value;
        data["teamBId_matchup_"+i] = document.getElementById("teamBId_matchup_"+i).value;
        // add scores
        data["teamAScore_matchup_"+i] = document.getElementById("teamAScore_matchup_"+i).value;
        data["teamBScore_matchup_"+i] = document.getElementById("teamBScore_matchup_"+i).value;
    }
    // validate data here
    var error = getErrorInData(data);
    if (error) {
        window.location = "/add-update-weeks/"+leagueId+"/"+yearNumber+"?error_message="+error;
        return;
    }
    // send POST request
    var fetchPromise = fetch("/update-week", {method: "POST",
                                                headers: {"Content-Type": "application/json"},
                                                body: JSON.stringify(data)});
    fetchPromise.then(response => {
        window.location.href = response.url;
    });
}

function getErrorInData(data) {
    // this validates the dict about to be posted
    var numberOfTeams = document.getElementById("number_of_teams").value;
    // check teams first
    var allTeamIds = [];
    var allTeamScores = [];
    for(i=1; i<=numberOfTeams/2; i++) {
        allTeamIds.push(data["teamAId_matchup_"+i]);
        allTeamIds.push(data["teamBId_matchup_"+i]);
        allTeamScores.push(data["teamAScore_matchup_"+i]);
        allTeamScores.push(data["teamBScore_matchup_"+i]);
    }
    var allTeamIdsSet = [...new Set(allTeamIds)]
    if(allTeamIds.length != allTeamIdsSet.length) {
        return "All teams must play once per week.";
    }
    for(i=0; i<allTeamScores.length; i++) {
        if(allTeamScores[i] == "") {
            return "All teams need a score.";
        }
    }
    return "";
}

function getMaxTeamNameLength(teams) {
    var maxLength = 0;
    for(i=0; i<teams.length; i++) {
        var newLength = teams[i]["teamName"].length;
        if(newLength > maxLength) {
            maxLength = newLength;
        }
    }
    return maxLength;
}

function setTeamDropdownWidths(teams) {
    // get all team dropdown button elements
    var width = getMaxTeamNameLength(teams);
    // add room for dropdown arrow
    width += 6;
    teamDropdownButtons = document.getElementsByClassName("teamDropdownButton");
    for(i=0; i<teamDropdownButtons.length; i++) {
        teamDropdownButtons[i].setAttribute('style', 'width:'+width+'ch');
    }
}