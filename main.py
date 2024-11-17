import numpy as np
import random
import tkinter as tk
from tkinter import messagebox
import pickle


class TicTacToeAI:
    def __init__(self, q_table_file="q_table.pkl"):
        self.q_table = {}  # Qテーブル
        self.epsilon = 0.1  # ε-greedy法の探索率
        self.learning_rate = 0.5  # 学習率
        self.discount_factor = 0.9  # 割引率
        self.q_table_file = q_table_file  # Qテーブルを保存するファイル名

        # Qテーブルを読み込む
        self.load_q_table()

    def get_state(self, board):
        """ボードの状態を文字列で表現"""
        return "".join(["".join(row) for row in board])

    def choose_action(self, state, available_actions):
        """ε-greedy法で行動を選択"""
        if random.random() < self.epsilon:  # 探索
            return random.choice(available_actions)
        else:  # 利用
            return max(
                available_actions,
                key=lambda action: self.q_table.get((state, action), 0),
            )

    def update_q_table(self, state, action, reward, next_state, next_available_actions):
        """Qテーブルを更新"""
        next_max = max(
            [self.q_table.get((next_state, a), 0) for a in next_available_actions],
            default=0,
        )
        current_q = self.q_table.get((state, action), 0)
        self.q_table[(state, action)] = current_q + self.learning_rate * (
            reward + self.discount_factor * next_max - current_q
        )

    def save_q_table(self):
        """Qテーブルを保存する"""
        with open(self.q_table_file, "wb") as f:
            pickle.dump(self.q_table, f)

    def load_q_table(self):
        """Qテーブルを読み込む"""
        try:
            with open(self.q_table_file, "rb") as f:
                self.q_table = pickle.load(f)
        except FileNotFoundError:
            self.q_table = {}  # ファイルがない場合、新しいQテーブルを作成


class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("丸バツゲーム")
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"  # プレイヤー1は "X", AIは "O"
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.ai = TicTacToeAI()  # 強化学習AI
        self.create_board()

    def create_board(self):
        """ボードを作成"""
        for i in range(3):
            for j in range(3):
                button = tk.Button(
                    self.root,
                    text=" ",
                    font=("Arial", 24),
                    width=5,
                    height=2,
                    command=lambda row=i, col=j: self.make_move(row, col),
                )
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    def make_move(self, row, col):
        """プレイヤーのターン"""
        if self.board[row][col] != " ":
            messagebox.showwarning("無効な操作", "その場所はすでに埋まっています！")
            return

        self.board[row][col] = self.current_player
        self.buttons[row][col].config(text=self.current_player, state=tk.DISABLED)

        winner = self.check_winner()
        if winner:
            self.end_game(winner)
            return

        if self.is_full():
            self.end_game(None)
            return

        # AIのターン
        self.current_player = "O"
        self.ai_move()

    def ai_move(self):
        """AIのターン"""
        state = self.ai.get_state(self.board)
        available_actions = [
            (i, j) for i in range(3) for j in range(3) if self.board[i][j] == " "
        ]
        action = self.ai.choose_action(state, available_actions)

        # AIの行動を適用
        self.board[action[0]][action[1]] = "O"
        self.buttons[action[0]][action[1]].config(text="O", state=tk.DISABLED)

        winner = self.check_winner()
        if winner:
            self.end_game(winner)
            return

        if self.is_full():
            self.end_game(None)
            return

        # プレイヤーに交代
        self.current_player = "X"

    def check_winner(self):
        """勝者がいるかチェック"""
        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] != " ":
                return row[0]

        for col in range(3):
            if (
                self.board[0][col] == self.board[1][col] == self.board[2][col]
                and self.board[0][col] != " "
            ):
                return self.board[0][col]

        if (
            self.board[0][0] == self.board[1][1] == self.board[2][2]
            and self.board[0][0] != " "
        ):
            return self.board[0][0]
        if (
            self.board[0][2] == self.board[1][1] == self.board[2][0]
            and self.board[0][2] != " "
        ):
            return self.board[0][2]

        return None

    def is_full(self):
        """ボードが埋まっているかチェック"""
        for row in self.board:
            if " " in row:
                return False
        return True

    def end_game(self, winner):
        """ゲーム終了"""
        if winner:
            messagebox.showinfo("ゲーム終了", f"プレイヤー {winner} の勝ちです！")
        else:
            messagebox.showinfo("ゲーム終了", "引き分けです！")

        # 学習結果を保存
        self.ai.save_q_table()

        self.reset_board()

    def reset_board(self):
        """ゲームリセット"""
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=" ", state=tk.NORMAL)


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
