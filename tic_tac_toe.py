class Game:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.turn = False
        self.board = Board()

        self.play()

    def play(self):
        while True:
            current_player = self.players[int(self.turn)]

            print(self.board.to_string())
            move = current_player.make_move(self.board)
            is_winning = self.board.place_mark(current_player.marker, move)
            if is_winning or self.board.is_draw():
                break
            self.turn = not self.turn

        if self.board.is_draw():
            print('No one wins:')
        else:
            print(f'Congratulations {current_player.name}, you win:')
        print(self.board.to_string())


class Board:
    def __init__(self, from_board=None):
        self.board = (from_board or list('012345678')).copy()

    def clone(self):
        return Board(self.board)

    def to_string(self):
        return '{}|{}|{}\n-----\n{}|{}|{}\n-----\n{}|{}|{}'.format(*self.board)

    def place_mark(self, marker, place):
        if self.board[place] not in '012345678' or place < 0 or place > 8:
            raise ValueError()
        self.board[place] = marker
        return self.is_winner(marker)

    def legal_move(self, i):
        return self.board[i] in '012345678'

    def is_winner(self, marker):
        winning_positions = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6)
        ]
        return any([sum([self.board[i] == marker for i in pos]) == 3 for pos in winning_positions])

    def is_draw(self):
        return all(str(i) not in self.board for i in range(9))


class Player:
    def __init__(self, name, marker, opponent_marker):
        self.name = name
        self.marker = marker
        self.opponent_marker = opponent_marker

    def make_move(self, board):
        move = int(input(f'This is the current board, {self.name} please make a move 0-8\n'))
        while True:
            if board.legal_move(move):
                return move
            else:
                move = int(input('Illegal move, please try again.\n'))

class Random(Player):
    def make_move(self, board):
        from random import choice
        options = [_ for _ in range(9) if board.legal_move(_)]
        return choice(options)


class Computer(Player):
    def score_move(self, board, i, turn=True):
        new_board = board.clone()
        try:
            new_board.place_mark(self.marker if turn else self.opponent_marker, i)
        except ValueError:
            return None

        if new_board.is_winner(self.marker):
            return 1
        elif new_board.is_winner(self.opponent_marker):
            return -1
        elif new_board.is_draw():
            return 0
        else:
            all_options = 0
            n_options = 0
            for i in range(9):
                if new_board.legal_move(i):
                    test = self.score_move(new_board, i, not turn)
                    all_options += test or 0
                    n_options += 1 if test is not None else 0
            return all_options / n_options

        
    def make_move(self, board):
        moves = []
        for i in range(9):
            if board.legal_move(i):
                moves.append((self.score_move(board, i), i))
        return sorted(moves)[-1][1]


Game(Computer('Bob', 'x', 'o'), Computer('Alice', 'o', 'x'))







