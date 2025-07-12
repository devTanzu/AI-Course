import pygame
import chess
import random
import sys
from pygame.locals import *

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
BOARD_SIZE = 512
SQUARE_SIZE = BOARD_SIZE // 8
MARGIN = (WIDTH - BOARD_SIZE) // 2
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_SQUARE = (240, 217, 181)
DARK_SQUARE = (181, 136, 99)
HIGHLIGHT = (247, 247, 105, 150)
LEGAL_MOVE = (124, 252, 0, 150)
WHITE_PIECE = (255, 255, 255)
BLACK_PIECE = (0, 0, 0)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess: User vs Computer')
clock = pygame.time.Clock()

# Piece symbols for display if image is missing
PIECE_SYMBOLS = {
    'p': '♟', 'r': '♜', 'n': '♞', 'b': '♝', 'q': '♛', 'k': '♚'
}

# Load piece images
piece_images = {}
pieces = ['p', 'r', 'n', 'b', 'q', 'k']
colors = ['w', 'b']

def load_pieces():
    for color in colors:
        for piece in pieces:
            key = color + piece
            try:
                image = pygame.image.load(f'pieces/{key}.png')
                piece_images[key] = pygame.transform.smoothscale(image, (SQUARE_SIZE, SQUARE_SIZE))
            except:
                print(f"Missing image: {key}.png")
                piece_images[key] = None

load_pieces()

class ChessGame:
    def __init__(self):
        self.board = chess.Board()
        self.selected_square = None
        self.legal_moves = []
        self.computer_thinking = False
        self.message = ""
        self.font = pygame.font.SysFont('Arial', 18)
        self.piece_font = pygame.font.SysFont('Arial', int(SQUARE_SIZE * 0.8))

    def draw_board(self):
        # Draw squares
        for row in range(8):
            for col in range(8):
                color = LIGHT_SQUARE if (row + col) % 2 == 0 else DARK_SQUARE
                pygame.draw.rect(screen, color, (MARGIN + col * SQUARE_SIZE,
                                                 MARGIN + row * SQUARE_SIZE,
                                                 SQUARE_SIZE, SQUARE_SIZE))

        # Highlight selected and legal moves
        if self.selected_square is not None:
            row, col = 7 - self.selected_square // 8, self.selected_square % 8
            highlight_surface = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE), pygame.SRCALPHA)
            highlight_surface.fill(HIGHLIGHT)
            screen.blit(highlight_surface, (MARGIN + col * SQUARE_SIZE, MARGIN + row * SQUARE_SIZE))

        for move in self.legal_moves:
            to_square = move.to_square
            row, col = 7 - to_square // 8, to_square % 8
            highlight_surface = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE), pygame.SRCALPHA)
            highlight_surface.fill(LEGAL_MOVE)
            screen.blit(highlight_surface, (MARGIN + col * SQUARE_SIZE, MARGIN + row * SQUARE_SIZE))

        # Draw pieces
        for square in chess.SQUARES:
            piece = self.board.piece_at(square)
            if piece:
                row, col = 7 - square // 8, square % 8
                topleft = (MARGIN + col * SQUARE_SIZE, MARGIN + row * SQUARE_SIZE)
                piece_key = ('w' if piece.color == chess.WHITE else 'b') + piece.symbol().lower()
                image = piece_images.get(piece_key)

                if image:
                    screen.blit(image, topleft)
                else:
                    # Draw Unicode if image is missing
                    symbol = PIECE_SYMBOLS[piece.symbol().lower()]
                    color = WHITE_PIECE if piece.color == chess.WHITE else BLACK_PIECE
                    text = self.piece_font.render(symbol, True, color)
                    rect = text.get_rect(center=(topleft[0] + SQUARE_SIZE // 2,
                                                 topleft[1] + SQUARE_SIZE // 2))
                    screen.blit(text, rect)

        # Show messages
        if self.message:
            text = self.font.render(self.message, True, BLACK)
            screen.blit(text, (20, HEIGHT - 30))

        turn_text = "White's turn" if self.board.turn == chess.WHITE else "Black's turn"
        turn_color = BLACK if self.board.turn == chess.BLACK else WHITE
        text = self.font.render(turn_text, True, turn_color)
        screen.blit(text, (WIDTH - 150, 20))

        if self.computer_thinking:
            thinking_text = self.font.render("Computer thinking...", True, BLACK)
            screen.blit(thinking_text, (WIDTH - 180, HEIGHT - 30))

    def handle_click(self, pos):
        if self.computer_thinking or self.board.turn == chess.BLACK:
            return

        x, y = pos
        if MARGIN <= x < MARGIN + BOARD_SIZE and MARGIN <= y < MARGIN + BOARD_SIZE:
            col = (x - MARGIN) // SQUARE_SIZE
            row = 7 - (y - MARGIN) // SQUARE_SIZE
            square = row * 8 + col

            if self.selected_square is not None:
                move = chess.Move(self.selected_square, square)
                if (self.board.piece_at(self.selected_square).piece_type == chess.PAWN and
                        (square // 8 == 0 or square // 8 == 7)):
                    move = chess.Move(self.selected_square, square, promotion=chess.QUEEN)

                if move in self.legal_moves:
                    self.make_move(move)
                    self.selected_square = None
                    self.legal_moves = []
                    if not self.board.is_game_over() and self.board.turn == chess.BLACK:
                        self.computer_move()
                else:
                    piece = self.board.piece_at(square)
                    if piece and piece.color == self.board.turn:
                        self.selected_square = square
                        self.legal_moves = [m for m in self.board.legal_moves if m.from_square == square]
            else:
                piece = self.board.piece_at(square)
                if piece and piece.color == self.board.turn:
                    self.selected_square = square
                    self.legal_moves = [m for m in self.board.legal_moves if m.from_square == square]

    def make_move(self, move):
        self.board.push(move)
        self.update_status()

    def computer_move(self):
        self.computer_thinking = True
        pygame.time.delay(500)

        legal_moves = list(self.board.legal_moves)
        captures = [m for m in legal_moves if self.board.is_capture(m)]
        if captures:
            good = [m for m in captures if not self.board.is_into_check(m)]
            move = random.choice(good if good else captures)
        else:
            checks = [m for m in legal_moves if self.board.gives_check(m)]
            move = random.choice(checks if checks else legal_moves)

        self.make_move(move)
        self.computer_thinking = False

    def update_status(self):
        if self.board.is_checkmate():
            winner = "Black" if self.board.turn == chess.WHITE else "White"
            self.message = f"Checkmate! {winner} wins!"
        elif self.board.is_stalemate():
            self.message = "Stalemate!"
        elif self.board.is_insufficient_material():
            self.message = "Draw: insufficient material"
        elif self.board.is_seventyfive_moves():
            self.message = "Draw: 75-move rule"
        elif self.board.is_fivefold_repetition():
            self.message = "Draw: fivefold repetition"
        elif self.board.is_check():
            self.message = "Check!"
        else:
            self.message = ""

def main():
    game = ChessGame()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                game.handle_click(event.pos)
            elif event.type == KEYDOWN and event.key == K_r:
                game = ChessGame()

        screen.fill(WHITE)
        game.draw_board()
        pygame.display.flip()
        clock.tick(FPS)

        if game.board.is_game_over():
            pygame.time.delay(3000)
            running = False

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
