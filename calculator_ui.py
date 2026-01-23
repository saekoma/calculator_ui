import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        a = float(entry_num1.get())
        b = float(entry_num2.get())
        op = operator.get()

        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            if b == 0:
                messagebox.showerror("오류", "0으로 나눌 수 없습니다")
                return
            result = a / b
        else:
            messagebox.showerror("오류", "연산자를 선택하세요")
            return

        label_result.config(text=f"결과: {result}")

    except ValueError:
        messagebox.showerror("오류", "숫자를 입력하세요")

# 창 생성
root = tk.Tk()
root.title("간단한 계산기")
root.geometry("300x250")

tk.Label(root, text="첫 번째 숫자").pack()
entry_num1 = tk.Entry(root)
entry_num1.pack()

tk.Label(root, text="두 번째 숫자").pack()
entry_num2 = tk.Entry(root)
entry_num2.pack()

operator = tk.StringVar(value="+")
tk.OptionMenu(root, operator, "+", "-", "*", "/").pack(pady=5)

tk.Button(root, text="계산하기", command=calculate).pack(pady=10)

label_result = tk.Label(root, text="결과:")
label_result.pack()

root.mainloop()
