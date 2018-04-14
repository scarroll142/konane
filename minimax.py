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

        if not moves:
            return []

        values = []
        for move in moves:
            values.append(self.minimax(self.nextBoard(board, self.side, move), 1))

        return moves[values.index(max(values))]

    def eval(self, board):
        return self.movesCount(board, self.opponent(self.side)) * -1
        #complete this – this will be your evaluation function. High values should be good for max.

    def movesCount(self, board, player):
        """
        Determines heuristic value of the number of possible moves for given player for current board
        """
        return len(self.generateMoves(board, player))

    def extendPath(self, board, side):
        moves = self.generateMoves(board, side)
        boards = []
        for move in moves:
            boards.append(self.nextBoard(board, side, move))

        return boards

    def minimax(self, board, depth):
        if depth >= self.limit:
            return self.eval(board)

        isMax = depth % 2 == 0

        if isMax:
            nextBoards = self.extendPath(board, self.side)
        else:
            nextBoards = self.extendPath(board, self.opponent(self.side))

        if not nextBoards:
            if isMax:
                return -float("inf")
            else:
                return float("inf")

        values = []
        for nextBoard in nextBoards:
            values.append(self.minimax(nextBoard, depth + 1))

        if isMax:
            return max(values)
        else:
            return min(values)
