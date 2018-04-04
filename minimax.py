class MinimaxPlayer(Konane, Player):
    """
    Plays best move determined by minimax algorithm.
    """
    def __init__(self, size, depthLimit):
        Konane.__init__(self, size)
        self.limit = depthLimit
    def initialize(self, side):
        #complete this
    def getMove(self, board):
        #complete this
    def eval(self, board):
        #complete this – this will be your evaluation function. High values should be good for max.
