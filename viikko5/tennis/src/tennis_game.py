class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.scores = {self.player1_name: 0, self.player2_name: 0}

    def won_point(self, player_name):
        self.scores[player_name] += 1
    
    def is_score_equal(self):
        if self.scores[self.player1_name] == self.scores[self.player2_name]:
            return True
        return False

    def is_score_over_four(self):
        if self.scores[self.player1_name] >= 4 or self.scores[self.player2_name] >= 4:
            return True
        return False

    def handle_equal_score(self, score: dict):
        if self.scores[self.player1_name] == 0:
            score["score"] = "Love-All"
        elif self.scores[self.player1_name] == 1:
            score["score"] = "Fifteen-All"
        elif self.scores[self.player1_name] == 2:
            score["score"] = "Thirty-All"
        elif self.scores[self.player1_name] == 3:
            score["score"] = "Forty-All"
        else:
            score["score"] = "Deuce"

    def handle_score_over_four(self, score: dict):
        minus_result = self.scores[self.player1_name] - self.scores[self.player2_name]

        if minus_result == 1:
            score["score"] = "Advantage player1"
        elif minus_result == -1:
            score["score"] = "Advantage player2"
        elif minus_result >= 2:
            score["score"] = "Win for player1"
        else:
            score["score"] = "Win for player2"
    
    def handle_else(self, score: dict, temp_score: int):
         for i in range(1, 3):
            if i == 1:
                temp_score = self.scores[self.player1_name]
            else:
                score["score"] = score["score"] + "-"
                temp_score = self.scores[self.player2_name]

            if temp_score == 0:
                score["score"] = score["score"] + "Love"
            elif temp_score == 1:
                score["score"] = score["score"] + "Fifteen"
            elif temp_score == 2:
                score["score"] = score["score"] + "Thirty"
            elif temp_score == 3:
                score["score"] = score["score"] + "Forty"

    def get_score(self):
        score = {"score": ""}
        temp_score = 0

        if self.is_score_equal():
            self.handle_equal_score(score=score)
        elif self.is_score_over_four():
            self.handle_score_over_four(score=score)
        else:
            self.handle_else(score=score, temp_score=temp_score)

        return score["score"]
