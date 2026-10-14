class Referee:
    def check_everything_and_print_and_judge(self, board, p_char):
        
        for r in range(3):
            for c in range(7):
                if board[r][c] == p_char and board[r+1][c] == p_char and board[r+2][c] == p_char and board[r+3][c] == p_char:
                    return True
                    
        for r in range(6):
            for c in range(4):
                if board[r][c] == p_char and board[r][c+1] == p_char and board[r][c+2] == p_char and board[r][c+3] == p_char:
                    return True
                    
        for r in range(3):
            for c in range(4):
                if board[r][c] == p_char and board[r+1][c+1] == p_char and board[r+2][c+2] == p_char and board[r+3][c+3] == p_char:
                    return True
                    
        for r in range(3, 6):
            for c in range(4):
                if board[r][c] == p_char and board[r-1][c+1] == p_char and board[r-2][c+2] == p_char and board[r-3][c+3] == p_char:
                    return True
                    
        return False

def logic_gate_proc():
    global T
    ref = Referee()
    pm = PlayerManager('X', 'O')
    
    while T < 42:
        char = pm.p1 if T % 2 == 0 else pm.p2
        
        for row in B:
            print("|" + "|".join(row) + "|")
        try:
            choice = int(input(f"Player {char} move: "))
            
            if choice < 0 or choice > 6:
                print("invalid column.")
                continue
                
            placed = False
            for r in range(5, -1, -1):
                if B[r][choice] == ' ':
                    B[r][choice] = char
                    placed = True
                    break
                    
            if not placed:
                print("Column full.")
                continue
            if ref.check_everything_and_print_and_judge(B, char):
                print(f"{char} wins.")
                break
            T += 1
        except ValueError:
            print("please enter a number.")

logic_