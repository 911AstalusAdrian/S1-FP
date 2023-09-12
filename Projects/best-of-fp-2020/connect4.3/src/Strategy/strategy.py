from copy import *
from random import shuffle


class Strategy:
    def __init__(self):
        self.BOARD_WIDTH = 7
        self.BOARD_HEIGHT = 6
        self.AI_PLAYER = 'O'
        self.HUMAN_PLAYER = 'X'

    def MiniMaxAlphaBeta(self, board, depth, player):
        """
        A minimax algorithm[5] is a recursive algorithm for choosing the next move in an n-player game,
        usually a two-player game.A value is associated with each position or state of the game. This value is computed
        by means of a position evaluation function and it indicates how good it would be for a player to reach that
        position. The player then makes the move that maximizes the minimum value of the position resulting from the
        opponent's possible following moves. If it is A's turn to move, A gives a value to each of their legal moves.
        :param board:
        :param depth:
        :param player:
        :return:
        """
        # get array of possible moves
        validMoves = self.getValidMoves(board)
        shuffle(validMoves)
        bestMove = validMoves[0]
        bestScore = float("-inf")

        # initial alpha & beta values for alpha-beta pruning
        alpha = float("-inf")
        beta = float("inf")

        if player == self.AI_PLAYER:
            opponent = self.HUMAN_PLAYER
        else:
            opponent = self.AI_PLAYER

        # go through all of those boards
        for move in validMoves:
            # create new board from move
            tempBoard = self.makeMove(board, move, player)[0]
            # call min on that new board
            boardScore = self.minimizeBeta(tempBoard, depth - 1, alpha, beta, player, opponent)
            if boardScore > bestScore:
                bestScore = boardScore
                bestMove = move
        return bestMove

    def minimizeBeta(self, board, depth, a, b, player, opponent):
        """
        The algorithm continues evaluating the maximum and minimum values of the child nodes alternately until it
        reaches the root node, where it chooses the move with the largest value (represented in the figure with a
        blue arrow). This is the move that the player should make in order to minimize the maximum possible loss.
        :param board:
        :param depth:
        :param a:
        :param b:
        :param player:
        :param opponent:
        :return:
        """
        validMoves = []
        for col in range(7):
            # if column col is a legal move...
            if self.isValidMove(col, board):
                # make the move in column col for curr_player
                temp = self.makeMove(board, col, player)[2]
                validMoves.append(temp)

        # check to see if game over
        if depth == 0 or len(validMoves) == 0 or self.gameIsOver(board):
            return self.utilityValue(board, player)

        validMoves = self.getValidMoves(board)
        beta = b

        # if end of tree evaluate scores
        for move in validMoves:
            boardScore = float("inf")
            # else continue down tree as long as ab conditions met
            if a < beta:
                tempBoard = self.makeMove(board, move, opponent)[0]
                boardScore = self.maximizeAlpha(tempBoard, depth - 1, a, beta, player, opponent)

            if boardScore < beta:
                beta = boardScore
        return beta

    def maximizeAlpha(self, board, depth, a, b, player, opponent):
        """
        The algorithm continues evaluating the maximum and minimum values of the child nodes alternately until it
        reaches the root node, where it chooses the move with the largest value (represented in the figure with a
        blue arrow). This is the move that the player should make in order to minimize the maximum possible loss.
        :param board:
        :param depth:
        :param a:
        :param b:
        :param player:
        :param opponent:
        :return:
        """
        validMoves = []
        for col in range(7):
            # if column col is a legal move...
            if self.isValidMove(col, board):
                # make the move in column col for curr_player
                temp = self.makeMove(board, col, player)[2]
                validMoves.append(temp)
        # check to see if game over
        if depth == 0 or len(validMoves) == 0 or self.gameIsOver(board):
            return self.utilityValue(board, player)

        alpha = a
        # if end of tree, evaluate scores
        for move in validMoves:
            boardScore = float("-inf")
            if alpha < b:
                tempBoard = self.makeMove(board, move, player)[0]
                boardScore = self.minimizeBeta(tempBoard, depth - 1, alpha, b, player, opponent)

            if boardScore > alpha:
                alpha = boardScore
        return alpha

    def isColumnValid(self, Board, Col):
        """
        check if column still has place
        :param Board:
        :param Col:
        :return:
        """
        if Board[0][Col] == ' ':
            return True
        return False

    # check the search range for rows and columns
    def isRangeValid(self, row, col):
        """
        check the search range for rows and columns
        :param row:
        :param col:
        :return:
        """
        if row >= 0 and col >= 0 and row < self.BOARD_HEIGHT and col < self.BOARD_WIDTH:
            return True
        return False

    # return all valid moves (empty columns) from the board
    def getValidMoves(self, Board):
        """
        return all valid moves (empty columns) from the board
        :param Board:
        :return:
        """
        Columns = []
        for Col in range(self.BOARD_WIDTH):
            if self.isColumnValid(Board, Col):
                Columns.append(Col)
        return Columns

    # places the current move's player ['x'|'o'] in the referenced column in the board
    def makeMove(self, board, col, player):
        """
        places the current move's player ['x'|'o'] in the referenced column in the board
        :param board:
        :param col:
        :param player:
        :return:
        """
        # deepcopy is used to take a copy of current board and not affecting the original one
        tempBoard = deepcopy(board)
        for row in range(5, -1, -1):
            if tempBoard[row][col] == ' ':
                tempBoard[row][col] = player
                return tempBoard, row, col

    # check if the played move is in empty column or not
    def isValidMove(self, col, board):
        """
        Check if the played move is in empty column or not
        :param col:
        :param board:
        :return:
        """
        for row in range(self.BOARD_HEIGHT):
            if board[row][col] == ' ':
                return True
        return False

    # check if the board is filled with players' moves
    def isBoardFilled(self, board):
        """
        check if the board is filled with players' moves
        :param board:
        :return:
        """
        # Check the first row and Selected column if it filled or not
        for row in range(self.BOARD_HEIGHT):
            for col in range(self.BOARD_WIDTH):
                if board[row][col] == ' ': return False
        return True

    # find four or more of ('x'|'o') in arrow in any direction
    def findFours(self, board):
        """
        find four or more of ('x'|'o') in arrow in any direction
        :param board:
        :return:
        """
        # find four or more of ('x'|'o') in arrow in vertical direction
        def verticalCheck(row, col):
            """
            find four or more of ('x'|'o') in arrow in vertical direction
            :param row:
            :param col:
            :return:
            """
            fourInARow = False
            count = 0
            for rowIndex in range(row, self.BOARD_HEIGHT):
                if board[rowIndex][col] == board[row][col]:
                    count += 1
                else:
                    break

            if count >= 4:
                fourInARow = True

            return fourInARow, count

        # find four or more of ('x'|'o') in arrow in horizontal direction
        def horizontalCheck(row, col):
            """
            find four or more of ('x'|'o') in arrow in horizontal direction
            :param row:
            :param col:
            :return:
            """
            fourInARow = False
            count = 0
            for colIndex in range(col, self.BOARD_WIDTH):
                if board[row][colIndex] == board[row][col]:
                    count += 1
                else:
                    break

            if count >= 4:
                fourInARow = True

            return fourInARow, count

        # find four or more of ('x'|'o') in arrow in positive diagonal direction
        def posDiagonalCheck(row, col):
            """
            find four or more of ('x'|'o') in arrow in positive diagonal direction /
            :param row:
            :param col:
            :return:
            """
            # check for diagonals with positive slope
            slope = None
            count = 0
            colIndex = col
            for rowIndex in range(row, self.BOARD_HEIGHT):
                if colIndex > self.BOARD_HEIGHT:
                    break
                elif board[rowIndex][colIndex] == board[row][col]:
                    count += 1
                else:
                    break
                colIndex += 1  # increment column when row is incremented

            if count >= 4:
                slope = 'positive'

            return slope, count

        # find four or more of ('x'|'o') in arrow in negative diagonal direction \
        def negDiagonalCheck(row, col):
            """
            find four or more of ('x'|'o') in arrow in negative diagonal direction \
            :param row:
            :param col:
            :return:
            """
            # check for diagonals with positive slope
            slope = None
            count = 0
            colIndex = col
            for rowIndex in range(row, -1, -1):
                if colIndex > 6:
                    break
                elif board[rowIndex][colIndex] == board[row][col]:
                    count += 1
                else:
                    break
                colIndex += 1  # increment column when row is decremented

            if count >= 4:
                slope = 'negative'

            return slope, count

        # find four or more of ('x'|'o') in arrow in any diagonal direction
        def diagonalCheck(row, col):
            """
            find four or more of ('x'|'o') in arrow in any diagonal direction
            :param row:
            :param col:
            :return:
            """
            positiveSlop, positiveCount = posDiagonalCheck(row, col)
            negativeSlop, negativeCount = negDiagonalCheck(row, col)

            if positiveSlop == 'positive' and negativeSlop == 'negative':
                fourInARow = True
                slope = 'both'
            elif positiveSlop == None and negativeSlop == 'negative':
                fourInARow = True
                slope = 'negative'
            elif positiveSlop == 'positive' and negativeSlop == None:
                fourInARow = True
                slope = 'positive'
            else:
                fourInARow = False
                slope = None

            return fourInARow, slope, positiveCount, negativeCount

        # make the winning moves in uppercase
        def capitalizeFourInARow(row, col, dir):
            """
            make the winning moves in uppercase
            :param row:
            :param col:
            :param dir:
            :return:
            """
            if dir == 'vertical':
                for rowIndex in range(verticalCount):
                    board[row + rowIndex][col] = board[row + rowIndex][col].upper()


            elif dir == 'horizontal':
                for colIndex in range(horizontalCount):
                    board[row][col + colIndex] = board[row][col + colIndex].upper()

            elif dir == 'diagonal':
                if slope == 'positive' or slope == 'both':
                    for diagIndex in range(positiveCount):
                        board[row + diagIndex][col + diagIndex] = board[row + diagIndex][col + diagIndex].upper()

                elif slope == 'negative' or slope == 'both':
                    for diagIndex in range(negativeCount):
                        board[row - diagIndex][col + diagIndex] = board[row - diagIndex][col + diagIndex].upper()

        # initialize the variables
        FourInRowFlag = False
        slope = None
        verticalCount = 0
        horizontalCount = 0
        positiveCount = 0
        negativeCount = 0
        for rowIndex in range(self.BOARD_HEIGHT):
            for colIndex in range(self.BOARD_WIDTH):
                if board[rowIndex][colIndex] != ' ':
                    # check for a vertical match starts at (rowIndex, colIndex)
                    fourInARow, verticalCount = verticalCheck(rowIndex, colIndex)
                    if fourInARow:
                        capitalizeFourInARow(rowIndex, colIndex, 'vertical')
                        FourInRowFlag = True

                    fourInARow, horizontalCount = horizontalCheck(rowIndex, colIndex)
                    # check for horizontal match starts at (rowIndex, colIndex)
                    if fourInARow:
                        capitalizeFourInARow(rowIndex, colIndex, 'horizontal')
                        FourInRowFlag = True

                    # check for diagonal match starts at (rowIndex, colIndex)
                    # also, get the slope of the four if there is one
                    fourInARow, slope, positiveCount, negativeCount = diagonalCheck(rowIndex, colIndex)
                    if fourInARow:
                        capitalizeFourInARow(rowIndex, colIndex, 'diagonal')
                        FourInRowFlag = True

        return FourInRowFlag

    # gets number of the empty valid locations in the board
    def getEmptyLocations(self, board):
        """
        Gets number of the empty valid locations in the board
        :param board:
        :return:
        """
        emptyLocations = 0
        for row in range(self.BOARD_HEIGHT):
            for col in range(self.BOARD_WIDTH):
                if board[row][col] == ' ':
                    emptyLocations += 1
        return emptyLocations

    def countSequence(self, board, player, length):
        """ Given the board state , the current player and the length of Sequence you want to count
            Return the count of Sequences that have the given length
        """

        def verticalSeq(row, col):
            """Return 1 if it found a vertical sequence with the required length
            """
            count = 0
            for rowIndex in range(row, self.BOARD_HEIGHT):
                if board[rowIndex][col] == board[row][col]:
                    count += 1
                else:
                    break
            if count >= length:
                return 1
            else:
                return 0

        def horizontalSeq(row, col):
            """Return 1 if it found a horizontal sequence with the required length
            """
            count = 0
            for colIndex in range(col, self.BOARD_WIDTH):
                if board[row][colIndex] == board[row][col]:
                    count += 1
                else:
                    break
            if count >= length:
                return 1
            else:
                return 0

        def negDiagonalSeq(row, col):
            """Return 1 if it found a negative diagonal sequence with the required length
            """
            count = 0
            colIndex = col
            for rowIndex in range(row, -1, -1):
                if colIndex > self.BOARD_HEIGHT:
                    break
                elif board[rowIndex][colIndex] == board[row][col]:
                    count += 1
                else:
                    break
                colIndex += 1  # increment column when row is incremented
            if count >= length:
                return 1
            else:
                return 0

        def posDiagonalSeq(row, col):
            """Return 1 if it found a positive diagonal sequence with the required length
            """
            count = 0
            colIndex = col
            for rowIndex in range(row, self.BOARD_HEIGHT):
                if colIndex > self.BOARD_HEIGHT:
                    break
                elif board[rowIndex][colIndex] == board[row][col]:
                    count += 1
                else:
                    break
                colIndex += 1  # increment column when row incremented
            if count >= length:
                return 1
            else:
                return 0

        totalCount = 0
        # for each piece in the board...
        for row in range(self.BOARD_HEIGHT):
            for col in range(self.BOARD_WIDTH):
                # ...that is of the player we're looking for...
                if board[row][col] == player:
                    # check if a vertical streak starts at (row, col)
                    totalCount += verticalSeq(row, col)
                    # check if a horizontal four-in-a-row starts at (row, col)
                    totalCount += horizontalSeq(row, col)
                    # check if a diagonal (both +ve and -ve slopes) four-in-a-row starts at (row, col)
                    totalCount += (posDiagonalSeq(row, col) + negDiagonalSeq(row, col))
        # return the sum of sequences of length 'length'
        return totalCount

    def utilityValue(self, board, player):
        """ A utility function to evaluate the state of the board and report it to the calling function,
            utility value is defined as the  score of the player who calls the function - score of opponent player,
            The score of any player is the sum of each sequence found for this player scaled by large factor for
            sequences with higher lengths.
        """
        if player == self.HUMAN_PLAYER:
            opponent = self.AI_PLAYER
        else:
            opponent = self.HUMAN_PLAYER

        playerfours = self.countSequence(board, player, 4)
        playerthrees = self.countSequence(board, player, 3)
        playertwos = self.countSequence(board, player, 2)
        playerScore = playerfours * 99999 + playerthrees * 999 + playertwos * 99

        opponentfours = self.countSequence(board, opponent, 4)
        opponentthrees = self.countSequence(board, opponent, 3)
        opponenttwos = self.countSequence(board, opponent, 2)
        opponentScore = opponentfours * 99999 + opponentthrees * 999 + opponenttwos * 99

        if opponentfours > 0:
            # This means that the current player lost the game
            # So return the biggest negative value => -infinity
            return float('-inf')
        else:
            # Return the playerScore minus the opponentScore
            return playerScore - opponentScore

    def gameIsOver(self, board):
        """Check if there is a winner in the current state of the board
        """
        if self.countSequence(board, self.HUMAN_PLAYER, 4) >= 1:
            return True
        elif self.countSequence(board, self.AI_PLAYER, 4) >= 1:
            return True
        else:
            return False
