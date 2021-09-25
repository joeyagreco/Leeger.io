function submitLeagueStat(year, leagueStat) {
    startLoading();
    var leagueId = document.getElementById("league_id").value;
    if(!year) {
        year = document.getElementById("select_year_button").value;
    }
    if(!leagueStat) {
        leagueStat = document.getElementById("stat_selection").value;
    }
    // check if the selected stat is an "ALWAYS ALL TIME" stat
    if(leagueStat == "Owner Comparison") {
        year = 0;
    }
    window.location = "/league-stats/"+leagueId+"/"+year+"?stat_selection="+leagueStat;
}

function lockYearDropdownToAllTime() {
    var yearDropdownElement = document.getElementById("select_year_button");
    yearDropdownElement.disabled = true;
    yearDropdownElement.classList.add("disabled");
}

function makeLeagueAveragesSquareCss() {
    // makes the height = width on all .averageBlock divs
    var allAverageBlocks = document.getElementsByClassName("averageBlock");
    var stylingInfo = allAverageBlocks[0].getBoundingClientRect();
    for(i=0; i<allAverageBlocks.length; i++) {
        allAverageBlocks[i].style.height = stylingInfo.width + "px";
        console.log(allAverageBlocks[i].style.height);
    }
}

function initializeTables() {
    $(document).ready( function () {
        $('#all_scores_table').DataTable(
            {
                "order": [[ 0, "desc" ]],
                "searching": false,
                "lengthMenu": [[10, 25, 50, -1], [10, 25, 50, "All"]]
            }
        );
    } );
    $(document).ready( function () {
        $('#margins_of_victory_table').DataTable(
            {
                "order": [[ 0, "desc" ]],
                "searching": false,
                "lengthMenu": [[10, 25, 50, -1], [10, 25, 50, "All"]]
            }
        );
    } );
    $(document).ready( function () {
        $('#streaks_table').DataTable(
            {
                "order": [[ 0, "desc" ]],
                "searching": false,
                "lengthMenu": [[10, 25, 50, -1], [10, 25, 50, "All"]]
            }
        );
    } );
        $(document).ready( function () {
        $('#owner_comparison_table').DataTable(
            {
                "order": [[ 4, "desc" ]],
                "searching": false,
                "lengthMenu": [[10, 25, 50, -1], [10, 25, 50, "All"]]
            }
        );
    } );
}
