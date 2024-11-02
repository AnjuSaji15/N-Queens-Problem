import tkinter as tk
from tkinter import messagebox

# Function to create an empty chessboard
def create_board(N):
    return [['.' for _ in range(N)] for _ in range(N)]

# Function to check if a queen can be placed safely
def is_safe(board, row, col, N):
    for i in range(row):
        if board[i][col] == 'Q' or \
           (col - (row - i) >= 0 and board[i][col - (row - i)] == 'Q') or \
           (col + (row - i) < N and board[i][col + (row - i)] == 'Q'):
            return False
    return True

# Function to solve the N-Queens problem using backtracking
def solve_n_queens_util(board, row, N, solutions):
    if row == N:
        solutions.append([row.copy() for row in board])
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 'Q'
            solve_n_queens_util(board, row + 1, N, solutions)
            board[row][col] = '.'

# Function to solve the N-Queens problem and return all solutions
def solve_n_queens(N):
    board = create_board(N)
    solutions = []
    solve_n_queens_util(board, 0, N, solutions)
    return solutions

# Function to display a solution on the chessboard in the UI
def display_solution(board, N):
    for row in range(N):
        for col in range(N):
            color = "white" if (row + col) % 2 == 0 else "black"  # Alternating white and black squares
            labels[row][col].config(text=board[row][col], bg=color, fg="black" if color == "white" else "white")

# Function to handle the "Solve" button click and show the first solution
def on_solve():
    global current_solution, solutions

    try:
        N = int(entry.get())
        if N < 4:
            messagebox.showerror("Error", "N must be 4 or greater.")
            return
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")
        return

    solutions = solve_n_queens(N)
    if not solutions:
        result_label.config(text="No solution found.", font=("Arial", 12), fg="red")
    else:
        result_label.config(text=f"Found {len(solutions)} solutions. Showing solution 1.", font=("Arial", 12), fg="green")
        create_grid(N)
        current_solution = 0
        display_solution(solutions[current_solution], N)
        next_button.pack(pady=10)  # Show the "Next Solution" button after solving

# Function to show the next solution when clicking "Next"
def on_next_solution():
    global current_solution, solutions

    if solutions and current_solution < len(solutions) - 1:
        current_solution += 1
        result_label.config(text=f"Showing solution {current_solution + 1} of {len(solutions)}", font=("Arial", 12), fg="green")
        display_solution(solutions[current_solution], len(solutions[current_solution]))

# Function to dynamically create the chessboard grid based on the input size N
def create_grid(N):
    global labels
    for widget in frame.winfo_children():
        widget.destroy()

    labels = [[tk.Label(frame, width=3, height=1, font=('Arial', 18), borderwidth=1, relief="solid") for _ in range(N)] for _ in range(N)]

    for row in range(N):
        for col in range(N):
            labels[row][col].grid(row=row, column=col, padx=2, pady=2)

# Function to start the N-Queens Solver from the initial screen
def start_solver():
    start_button.pack_forget()
    label.pack(pady=5)
    entry.pack(pady=5)
    solve_button.pack(pady=10)
    result_label.pack(pady=10)
    frame.pack(pady=10)

# Set up the Tkinter window with a professional interface
root = tk.Tk()
root.title("N-Queens Problem Solver")

# Set the window size and background color
root.geometry("500x600")
root.configure(bg="#f0f0f0")

# Create and display a start button
start_button = tk.Button(root, text="Start N-Queens Problem", command=start_solver, font=('Arial', 18, 'bold'), bg="#4CAF50", fg="white", padx=10, pady=5)
start_button.pack(pady=50)

# Label for entering the number of queens
label = tk.Label(root, text="Enter the number of queens:", font=('Arial', 14), bg="#f0f0f0")
label.pack_forget()

# Input field and label for the number of queens
entry = tk.Entry(root, font=('Arial', 14))
entry.pack_forget()

# Solve button with professional styling
solve_button = tk.Button(root, text="Solve", command=on_solve, font=('Arial', 14, 'bold'), bg="#4CAF50", fg="white", padx=10, pady=5)
solve_button.pack_forget()

# Button for showing the next solution
next_button = tk.Button(root, text="Next Solution", command=on_next_solution, font=('Arial', 14, 'bold'), bg="#2196F3", fg="white", padx=10, pady=5)
next_button.pack_forget()

# Label to show results and messages
result_label = tk.Label(root, text="", font=('Arial', 12), bg="#f0f0f0")
result_label.pack_forget()

# Frame to hold the chessboard
frame = tk.Frame(root, bg="#f0f0f0")
frame.pack_forget()

# Variables to track solutions and the current solution index
solutions = []
current_solution = 0

# Start the Tkinter event loop
root.mainloop()
