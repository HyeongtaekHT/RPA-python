# tkinter 모듈 임포트
import tkinter as tk

# random 모듈 임포트
import random

# 창 객체 생성
window = tk.Tk()

# 창 제목 설정
window.title("Random Numbers")

# 창 크기 설정
window.geometry("300x200")

# 레이블 객체 생성
label = tk.Label(window, text="1~99 사이에서 6개의 숫자를 랜덤으로 보여줍니다.")

# 레이블 배치
label.pack()

# 결과 텍스트 객체 생성
result = tk.Text(window)

# 결과 텍스트 배치
result.pack()

# 버튼 클릭 이벤트 함수 정의
def show_numbers():
    # 1~99 사이의 숫자 리스트 생성
    numbers = list(range(1,100))

    # 리스트에서 6개의 숫자를 랜덤으로 선택
    random_numbers = random.sample(numbers, 6)

    # 결과 텍스트 초기화
    result.delete(1.0, "end")

    # 결과 텍스트에 선택된 숫자 삽입
    result.insert(1.0, str(random_numbers))

# 버튼 객체 생성 및 클릭 이벤트 연결
button = tk.Button(window, text="Show Numbers", command=show_numbers)

# 버튼 배치
button.pack()

# 창 실행
window.mainloop()