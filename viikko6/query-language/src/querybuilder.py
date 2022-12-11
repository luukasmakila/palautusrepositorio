import matchers as commands


class QueryBuilder:
    def __init__(self, query = commands.All()):
        self.query = query
    
    def build(self):
        return self.query
    
    def oneOf(self, *matchers):
        return QueryBuilder(
            commands.Or(*matchers)
        )
    
    def playsIn(self, team):
        return QueryBuilder(
            commands.And(
                self.query, commands.PlaysIn(team=team)
            )
        )
    
    def hasAtLeast(self, value, attr):
        return QueryBuilder(
            commands.And(
                self.query, commands.HasAtLeast(value, attr)
            )
        )
    
    def hasFewerThan(self, value, attr):
        return QueryBuilder(
            commands.And(
                self.query, commands.HasFewerThan(value, attr)
            )
        )
