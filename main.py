from Board import Board

def parse_square(square_str):
    """
    Converts input like 'e2' to (row, col) coordinates
    """
    col_map = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
    if len(square_str) != 2:
        return None
    col = col_map.get(square_str[0].lower())
    row = 8 - int(square_str[1])
    if col is None or not (0 <= row <= 7):
        return None
    return (row, col)

def main():
    board = Board()
    turn = "white"

    while True:
        board.print_board()
        print(f"{turn}'s turn")

        move_str = input("Enter your move (e.g. e2 e4) or 'quit': ").strip()
        if move_str.lower() == "quit":
            print("Game ended by user.")
            break

        try:
            from_sq, to_sq = move_str.split()
        except ValueError:
            print("Invalid input. Enter moves like 'e2 e4'.")
            continue

        src = parse_square(from_sq)
        dst = parse_square(to_sq)

        if src is None or dst is None:
            print("Invalid square notation.")
            continue

        piece = board.get_piece(src[0], src[1])
        if piece is None:
            print("No piece at source square.")
            continue

        if piece.color != turn:
            print(f"That's not your piece. It's {turn}'s turn.")
            continue

        target = board.get_piece(dst[0], dst[1])
        if target is None:
            piece.move(dst[0], dst[1], board)
        else:
            if target.color == turn:
                print("You cannot capture your own piece.")
                continue
            piece.eat(dst[0], dst[1], board)

        # Check if a king has been captured
        white_king = board.get_king_position("white")
        black_king = board.get_king_position("black")
        if white_king is None:
            print("Black wins! White king captured.")
            break
        if black_king is None:
            print("White wins! Black king captured.")
            break

        # Remove the piece from its old position
        board.game_board[src[0]][src[1]] = None

        # Switch turns
        turn = "black" if turn == "white" else "white"

if __name__ == "__main__":
    main()
