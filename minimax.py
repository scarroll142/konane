class MinimaxPlayer(Konane, Player):
    """
    Plays best move determined by minimax algorithm.
    """
    def __init__(self, size, depthLimit):
        Konane.__init__(self, size)
        self.limit = depthLimit

    def initialize(self, side):
        """
        Prompts a roboto player for a move.
        """
        self.side = side
        self.name = "Beep Boop Bop"

    def getMove(self, board):
        moves = self.generateMoves(board, self.side)
        n = len(moves)
        if n == 0:
            return []
        else:
            evalValues = []
            for move in moves:
                evalValues.append(self.eval(self.nextBoard(board, self.side, move)))
            return moves[evalValues.index(max(evalValues))]

    def eval(self, board):
        return self.movesCount(board, self.opponent(self.side)) * -1
        #complete this – this will be your evaluation function. High values should be good for max.

    def movesCount(self, board, player):
        """
        Determines heuristic value of the number of possible moves for given player for current board
        """
        return len(self.generateMoves(board, player))
