import tkinter as tk
from tkinter import ttk
import random

class LottoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("행님을 위한 로또 번호 추천기")
        self.root.geometry("500x600")
        self.root.configure(bg="#f5f5f5")

        # 역대 최다 빈도수 데이터 (예시 통계 데이터 반영)
        # 실제 최신 데이터는 API 연동이 필요하나, 여기서는 누적 통계상 상위 번호들에 가중치를 둠
        self.frequent_numbers = [
            1, 10, 12, 13, 14, 17, 18, 21, 24, 26, 27, 33, 34, 39, 40, 43, 45
        ]
        self.all_numbers = list(range(1, 46))

        self.setup_ui()

    def setup_ui(self):
        # 헤더 설정
        header = tk.Label(
            self.root, text="Lotto Lucky Numbers", 
            font=("Helvetica", 20, "bold"), bg="#f5f5f5", fg="#333"
        )
        header.pack(pady=20)

        # 결과 표시 프레임
        self.result_frame = tk.Frame(self.root, bg="#f5f5f5")
        self.result_frame.pack(expand=True, fill="both", padx=20)

        # 추천 버튼
        self.btn_generate = tk.Button(
            self.root, text="번호 추천받기", command=self.generate_bundles,
            font=("NanumGothic", 14, "bold"), bg="#4CAF50", fg="white",
            padx=20, pady=10, relief="flat", cursor="hand2"
        )
        self.btn_generate.pack(pady=30)

    def get_ball_color(self, num):
        if 1 <= num <= 10: return "#fbc400" # 노랑
        if 11 <= num <= 20: return "#69c8f2" # 파랑
        if 21 <= num <= 30: return "#ff7272" # 빨강
        if 31 <= num <= 40: return "#aaa"    # 회색
        return "#b0d840"                     # 초록

    def generate_lotto_numbers(self):
        # 빈도수 높은 번호에서 3개, 나머지에서 3개 혼합하여 전략적 추출
        high_pick = random.sample(self.frequent_numbers, 3)
        remains = [n for n in self.all_numbers if n not in high_pick]
        low_pick = random.sample(remains, 3)
        
        combination = sorted(high_pick + low_pick)
        return combination

    def generate_bundles(self):
        # 기존 결과 삭제
        for widget in self.result_frame.winfo_children():
            widget.destroy()

        for i in range(5):
            numbers = self.generate_lotto_numbers()
            row_frame = tk.Frame(self.result_frame, bg="#f5f5f5", pady=10)
            row_frame.pack()

            label_idx = tk.Label(row_frame, text=f"제 {i+1} 조합 : ", font=("NanumGothic", 10), bg="#f5f5f5")
            label_idx.pack(side="left", padx=5)

            for num in numbers:
                color = self.get_ball_color(num)
                ball = tk.Label(
                    row_frame, text=num, font=("Helvetica", 12, "bold"),
                    width=4, height=2, fg="white", bg=color
                )
                ball.pack(side="left", padx=3)

if __name__ == "__main__":
    root = tk.Tk()
    app = LottoApp(root)
    root.mainloop()