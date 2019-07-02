class ChessBoard:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        #set up white
        self.board[0][0] = Rook(0, 0, "W")

        self.board[7][0] = Rook(7, 0, "W")

        #set up black
        self.board[0][7] = Rook(0, 0, "B")

        self.board[7][7] = Rook(7, 0, "B")

    def __repr__(self):
        master_l = []
        for i in range(8):
            l = []
            for j in range(8):
                l.append(self.board[j][i])
            master_l.append(l)
        res = ""
        for l in master_l[::-1]:
            res += str(l) + "\n"
        return res

    def move(self, source_coordinates, target_coordinates):
        source = self.board[source_coordinates[0]][source_coordinates[1]]
        target = self.board[target_coordinates[0]][target_coordinates[1]]
        if target is not None:
            if target.colour == source.colour:
                raise IllegalMoveException("Cannot move {0} to {1}, there's an ally ({2}) in it.".format(source, target_coordinates, target))
        source.move(target_coordinates)
        self.board[target_coordinates[0]][target_coordinates[1]] = source
        self.board[source_coordinates[0]][source_coordinates[1]] = None

    def start_game(self):
        raise NotImplementedError("start game in chess board not implemented yet")


class ChessPiece:
    def __init__(self, x_position, y_position, colour):
        self.position = (x_position, y_position)
        if colour != "B" and colour != "W":
            raise ValueError("got colour " + colour + ", needs either B (black) or W (white)")
        self.colour = colour

    def __repr__(self):
        if self.colour == "B":
            return "Black"
        return "White"

    def move(self, target):
        if self.position == target:
            raise IllegalMoveException("Cannot move someone to the same location it's already in")
        if target[0] < 0 or target[0] > 7 or target[1] < 0 or target[1] > 7:
            raise IllegalMoveException("Target coordinates " + target + " are out of the board's range")
        self.position = (target[0], target[1])


class Rook(ChessPiece):
    def __init__(self, x_position, y_position, colour):
        super(Rook, self).__init__(x_position, y_position, colour)

    def __repr__(self):
        return super(Rook, self).__repr__() + " Rook"

    def move(self, target):
        if target[0] == self.position[0] or target[1] == self.position[1]:
            super(Rook, self).move(target)
        else:
            raise IllegalMoveException("A rook must move must move in a straight line, tried to move from {0} to {1}".format(self.position, target))


class IllegalMoveException(Exception):
    def __init__(self, s):
        super(IllegalMoveException, self).__init__(s)


def main():
    cb = ChessBoard()
    print(cb)

if __name__ == '__main__':
    main()