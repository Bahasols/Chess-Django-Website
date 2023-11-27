# chess_app/models.py

from django.db import models

class ChessGame(models.Model):
    # Fields to represent the game state
    current_player = models.CharField(max_length=10)  # 'white' or 'black'
    checkmate = models.BooleanField(default=False)

    def __str__(self):
        return f"Chess Game {self.id}"

class ChessPiece(models.Model):
    game = models.ForeignKey(ChessGame, on_delete=models.CASCADE)
    row = models.IntegerField() # Also known as 'Rank'
    col = models.IntegerField() # Also known as 'File'
    color = models.CharField(max_length=10)  # 'white' or 'black'
    move_count = models.IntegerField()
    PIECE_TYPES = [
        ('king', 'King'),
        ('queen', 'Queen'),
        ('rook', 'Rook'),
        ('bishop', 'Bishop'),
        ('knight', 'Knight'),
        ('pawn', 'Pawn'),
    ]

    piece_type = models.CharField(max_length=10, choices=PIECE_TYPES)

    def __str__(self):
        return f"{self.color.capitalize()} {self.piece_type.capitalize()} at ({self.row}, {self.col})"
