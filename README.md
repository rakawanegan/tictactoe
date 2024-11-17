# 強化学習AIによる丸バツゲーム (Tic-Tac-Toe)

このプロジェクトは、Pythonで作成された強化学習AIを搭載した丸バツゲーム（Tic-Tac-Toe）です。プレイヤーは`X`を使用し、`O`を使用するAIと対戦します。AIは`Q-Learning`アルゴリズムを使用して学習し、対戦を繰り返すことで戦略を強化します。

## 特徴
- **強化学習**: AIは`Q-Learning`を使用してプレイ中に学習します。
- **学習結果の保存**: 学習結果（Qテーブル）は`q_table.pkl`ファイルに保存され、次回実行時に利用されます。
- **GUI対応**: `tkinter`を使用したシンプルなユーザーインターフェース。
- **継続学習**: ゲームをプレイするたびにAIが強化されます。

## 動作環境
- Python 3.8以降
- 必要ライブラリ: `tkinter`（標準ライブラリに含まれています）

## インストール
1. このリポジトリをクローンまたはZIPでダウンロードしてください:
   ```bash
   git clone https://github.com/your-repo/tic-tac-toe-ai.git
   cd tic-tac-toe-ai
   ```

2. Pythonがインストールされていることを確認してください。
   ```bash
   python --version
   ```

## 実行方法
1. プロジェクトディレクトリで以下を実行します:
   ```bash
   python main.py
   ```

2. GUIウィンドウが表示されます。プレイヤー（`X`）としてボタンをクリックし、AI（`O`）と対戦してください。

## ゲームのルール
1. プレイヤーとAIは交互に自分の記号（`X`または`O`）を空いているマスに置きます。
2. 縦、横、または斜めに同じ記号を3つ並べたプレイヤーが勝利します。
3. すべてのマスが埋まり、勝者がいない場合は引き分けです。

## ファイル構成
- `tic_tac_toe_ai.py`: ゲームのメインコード。
- `q_table.pkl`: 学習結果が保存されるファイル（初回実行時に生成）。

## AIの仕組み
- **Q-Learning**:
  - AIは各ゲームの状態と行動のペアを記録し、その価値（Q値）を更新します。
  - 勝利時: 報酬 +1
  - 引き分け時: 報酬 0
  - 敗北時: 報酬 -1
- **ε-Greedy法**:
  - AIはランダムな行動（探索）と最適な行動（利用）をバランスよく選択します。

## 注意点
- `q_table.pkl`が削除されると、AIの学習結果はリセットされます。
- ゲームを繰り返すことでAIの強さが向上します。

## 改善ポイント
- 学習アルゴリズムを`Deep Q-Learning`に拡張可能。
- 学習速度や探索率の調整によるさらなる強化。

## ライセンス
このプロジェクトはMITライセンスの下で提供されています。