### Authors:     Sam Carroll and Tommy Russoniello
### Professor:   Dr. Schwartz
### Class:       CSCI 450 Spring 2018
### Assignment:  Minimax Konane
### Date:        April 17, 2018

from konane import *

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
        """
        Given the current board, should return a valid move.
        """
        moves = self.generateMoves(board, self.side)

        if not moves:
            return []

        values = []
        alpha = -float("inf")
        for move in moves:
            values.append(self.minimax(self.nextBoard(board, self.side, move), 1, alpha, float("inf")))

            if max(values) > alpha:
                alpha = max(values)

        return moves[values.index(max(values))]

    def eval(self, board):
        """
        Determines heuristic value of given board.
        """
        return (self.movablePieces(board, self.side) - (3 * self.movablePieces(board, self.opponent(self.side)))) + (self.movesCount(board, self.side) - (4 * self.movesCount(board, self.opponent(self.side))))
        #return 2 * (self.movesCount(board, self.side) - self.movesCount(board, self.opponent(self.side))) + (self.countSymbol(board, self.side) - self.countSymbol(board, self.opponent(self.side)))

    def movesCount(self, board, player):
        """
        Determines heuristic value of the number of possible moves for given player for current board.
        """
        return len(self.generateMoves(board, player))

    def movablePieces(self, board, player):
        """
        Determines the heuristic value of the number of movable pieces for given player for current board.
        """
        moves = self.generateMoves(board, player)
        counter = 0
        pieces = []
        for move in moves:
            if [moves[counter][0], moves[counter][1]] not in pieces:
                pieces.append([moves[counter][0], moves[counter][1]])
            counter += 1
        return len(pieces)

    def extendPath(self, board, side):
        """
        Returns resulting boards for all possible legal moves from given board for given player.
        """
        moves = self.generateMoves(board, side)
        boards = []
        for move in moves:
            boards.append(self.nextBoard(board, side, move))

        return boards

    def minimax(self, board, depth, alpha, beta):
        """
        Uses Minimax algorithm to give best possible board heuristic value up to end of game/given search depth assuming optimal opponent.
        """
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
        newAlpha = alpha
        newBeta = beta
        for nextBoard in nextBoards:
            if values:
                if isMax:
                    if max(values) >= beta:
                        break
                    if max(values) > alpha:
                        newAlpha = max(values)
                else:
                    if min(values) <= alpha:
                        break
                    if min(values) < beta:
                        newBeta = min(values)

            values.append(self.minimax(nextBoard, depth + 1, newAlpha, newBeta))

        if isMax:
            return max(values)
        else:
            return min(values)

class MinimaxPlayer2(Konane, Player):
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
        self.name = "Beep Boop Bop 2.0"

    def getMove(self, board):
        """
        Given the current board, should return a valid move.
        """
        moves = self.generateMoves(board, self.side)

        if not moves:
            return []

        values = []
        alpha = -float("inf")
        for move in moves:
            values.append(self.minimax(self.nextBoard(board, self.side, move), 1, alpha, float("inf")))

            if max(values) > alpha:
                alpha = max(values)

        return moves[values.index(max(values))]

    def eval(self, board):
        """
        Determines heuristic value of given board.
        """
        return self.movablePieces(board, self.side) - (3 * self.movablePieces(board, self.opponent(self.side)))
        #return (self.movablePieces(board, self.side)) - (self.movablePieces(board, self.opponent(self.side)))

    def movesCount(self, board, player):
        """
        Determines heuristic value of the number of possible moves for given player for current board.
        """
        return len(self.generateMoves(board, player))

    def movablePieces(self, board, player):
        """
        Determines the heuristic value of the number of movable pieces for given player for current board.
        """
        moves = self.generateMoves(board, player)
        counter = 0
        pieces = []
        for move in moves:
            if [moves[counter][0], moves[counter][1]] not in pieces:
                pieces.append([moves[counter][0], moves[counter][1]])
            counter += 1
        return len(pieces)

    def extendPath(self, board, side):
        """
        Returns resulting boards for all possible legal moves from given board for given player.
        """
        moves = self.generateMoves(board, side)
        boards = []
        for move in moves:
            boards.append(self.nextBoard(board, side, move))

        return boards

    def minimax(self, board, depth, alpha, beta):
        """
        Uses Minimax algorithm to give best possible board heuristic value up to end of game/given search depth assuming optimal opponent.
        """
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
        newAlpha = alpha
        newBeta = beta
        for nextBoard in nextBoards:
            if values:
                if isMax:
                    if max(values) >= beta:
                        break
                    if max(values) > alpha:
                        newAlpha = max(values)
                else:
                    if min(values) <= alpha:
                        break
                    if min(values) < beta:
                        newBeta = min(values)

            values.append(self.minimax(nextBoard, depth + 1, newAlpha, newBeta))

        if isMax:
            return max(values)
        else:
            return min(values)
