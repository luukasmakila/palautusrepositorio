from player_reader import PlayerReader

class PlayerStats():

    def __init__(self, reader: PlayerReader):
        self.players = reader.players

    def top_scorers_by_nationality(self, nationality):

        top_scorers_by_nationality = []

        for player in self.players:
            if player.nationality == nationality:
                top_scorers_by_nationality.append(player)

        return top_scorers_by_nationality
