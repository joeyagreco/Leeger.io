class Constants:
    """
    This class is used to hold constants.
    The variables declared within this class are NOT meant to be modified.
    """

    # used for League Model Navigator
    WIN = "Win"
    LOSS = "Loss"
    TIE = "Tie"

    # used for Graphs
    PPG_BY_WEEK = "PPG by Week"
    SCORING_SHARE = "Scoring Share"
    AWAL_PER_GAME_OVER_SCORING_SHARE = "AWAL Per Game/Scoring Share"
    FREQUENCY_OF_SCORES = "Frequency of Scores"
    POINTS_FOR_OVER_POINTS_AGAINST = "Points For/Points Against"
    AWAL_BY_WEEK = "AWAL by Week"
    STRENGTH_OF_SCHEDULE_OVER_SCORING_SHARE_AGAINST = "Strength of Schedule/Scoring Share Against"
    GRAPH_OPTIONS = [SCORING_SHARE,
                     FREQUENCY_OF_SCORES,
                     AWAL_PER_GAME_OVER_SCORING_SHARE,
                     POINTS_FOR_OVER_POINTS_AGAINST,
                     STRENGTH_OF_SCHEDULE_OVER_SCORING_SHARE_AGAINST,
                     PPG_BY_WEEK,
                     AWAL_BY_WEEK]

    # used for Stats Explained
    # and dropdowns
    # and stat table headers
    # team stats
    WINS_STAT_TITLE = "Wins"
    LOSSES_STAT_TITLE = "Losses"
    TIES_STAT_TITLE = "Ties"
    WIN_PERCENTAGE_STAT_TITLE = "Win Percentage"
    WAL_STAT_TITLE = "WAL"
    AWAL_STAT_TITLE = "AWAL"
    AWAL_PER_GAME_STAT_TITLE = "AWAL Per Game"
    SMART_WINS_STAT_TITLE = "Smart Wins"
    PPG_STAT_TITLE = "PPG"
    SCORING_SHARE_STAT_TITLE = "Scoring Share"
    SCORING_SHARE_AGAINST_STAT_TITLE = "Scoring Share Against"
    PPG_AGAINST_STAT_TITLE = "PPG Against"
    STRENGTH_OF_SCHEDULE_STAT_TITLE = "Strength of Schedule"
    PLUS_MINUS_STAT_TITLE = "Plus/Minus"
    MAX_SCORE_STAT_TITLE = "Max Score"
    MIN_SCORE_STAT_TITLE = "Min Score"
    STDEV_STAT_TITLE = "Scoring STDEV"
    TEAM_SCORE_STAT_TITLE = "Team Score"
    TEAM_SUCCESS_STAT_TITLE = "Team Success"
    TEAM_LUCK_STAT_TITLE = "Team Luck"
    TEAM_STATS_STAT_TITLES = [WINS_STAT_TITLE, LOSSES_STAT_TITLE, TIES_STAT_TITLE, WIN_PERCENTAGE_STAT_TITLE,
                              WAL_STAT_TITLE, AWAL_STAT_TITLE, AWAL_PER_GAME_STAT_TITLE, SMART_WINS_STAT_TITLE,
                              PPG_STAT_TITLE,
                              SCORING_SHARE_STAT_TITLE, SCORING_SHARE_AGAINST_STAT_TITLE, PPG_AGAINST_STAT_TITLE,
                              STRENGTH_OF_SCHEDULE_STAT_TITLE, PLUS_MINUS_STAT_TITLE, MAX_SCORE_STAT_TITLE,
                              MIN_SCORE_STAT_TITLE, STDEV_STAT_TITLE, TEAM_SCORE_STAT_TITLE, TEAM_SUCCESS_STAT_TITLE,
                              TEAM_LUCK_STAT_TITLE]

    # league averages titles
    AVERAGE_SCORE_STAT_TITLE = "Average Team Score"
    AVERAGE_SCORE_IN_WINS_STAT_TITLE = "Average Team Score in Wins"
    AVERAGE_SCORE_IN_LOSSES_STAT_TITLE = "Average Team Score in Losses"

    # league stats
    OWNER_COMPARISON_STAT_TITLE = "Owner Comparison"
    ALL_SCORES_STAT_TITLE = "All Scores"
    MARGINS_OF_VICTORY_STAT_TITLE = "Margins of Victory"
    WINNING_STREAKS_STAT_TITLE = "Winning Streaks"
    LOSING_STREAKS_STAT_TITLE = "Losing Streaks"
    LEAGUE_AVERAGES_STAT_TITLE = "League Averages"
    LEAGUE_STATS_STAT_TITLES = sorted(
        [OWNER_COMPARISON_STAT_TITLE, ALL_SCORES_STAT_TITLE, MARGINS_OF_VICTORY_STAT_TITLE,
         WINNING_STREAKS_STAT_TITLE, LOSING_STREAKS_STAT_TITLE, LEAGUE_AVERAGES_STAT_TITLE])

    # excluded stats (stats that don't need explanation)
    EXCLUDED_STAT_TITLES = [ALL_SCORES_STAT_TITLE, LOSSES_STAT_TITLE, TIES_STAT_TITLE, WINS_STAT_TITLE,
                            OWNER_COMPARISON_STAT_TITLE, WINNING_STREAKS_STAT_TITLE, LOSING_STREAKS_STAT_TITLE,
                            LEAGUE_AVERAGES_STAT_TITLE, AWAL_PER_GAME_STAT_TITLE]

    # all stat titles without the excluded stats list
    ALL_STAT_TITLES = list(set(TEAM_STATS_STAT_TITLES + LEAGUE_STATS_STAT_TITLES) - set(EXCLUDED_STAT_TITLES))
