from tkinter import *
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# -------------------- Data --------------------

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
y = np.array([7, 9, 10, 12, 14, 16, 17, 18, 19, 20])

# -------------------- Model --------------------

model = LinearRegression()
model.fit(x, y)
y_pred = model.predict(x)

# -------------------- Evaluation --------------------

mae = mean_absolute_error(y, y_pred)
mse = mean_squared_error(y, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y, y_pred)

# -------------------- GUI --------------------

window = Tk()
window.title('Student Score Predictor')
window.geometry("1000x850+500+100")
window.resizable(False, False)

# -------------------- Title --------------------
# Head label

label = Label(window, bg="#19291b")
label.place(width=1000, height=70)

text_head = Label(window, text="Student Score Predictor",
                  bg='#19291b', fg="white", font=('', 33, 'bold'))
text_head.place(x=245, y=5)

# -------------------- Input --------------------

input_label = Label(
    window,
    text=" : چند ساعت مطالعه کرده ای؟", font=("Arial", 22, 'bold'))

input_label.place(x=680, y=105, width=300, height=30)

entry = Entry(window, font=("Arial", 18, 'bold'), justify="center")

entry.place(x=560, y=105, width=100, height=40)

# -------------------- Result --------------------

result_label = Label(window, text=" : نمره احتمالی",
                     font=("Arial", 20, 'bold'))

result_label.place(x=130, y=104, width=150, height=35)
score_label = Label(window, text='', font=('', 22, 'bold'))
score_label.place(width=100, height=80, x=40, y=80)

# -------------------- Prediction --------------------


def predict_score():
    try:
        hours = float(entry.get())
        if hours < 0:
            result_label.config(
                text=".ساعات مطالعه نمیتوانند منفی باشند")
            return
        score = model.predict([[hours]])
        score_label.config(text=f"{score[0]: .2f}")
    except ValueError:

        result_label.config(
            text=".لطفا عدد معتبر وارد کنید")


predict_button = Button(
    window, text="پیش بینی نمره", command=predict_score,
    font=('', 18, 'bold'), bg='#19291b', fg='white', bd=2)

predict_button.place(x=310, y=102, width=170, height=40)

# -------------------- Graph Frame --------------------

graph_frame = Frame(window, bd=1, relief='solid')
graph_frame.place(x=60, y=300, width=600, height=500)

# -------------------- Graph --------------------

figure = Figure(figsize=(4.5, 3), dpi=100)

graph = figure.add_subplot(111)
canvas = FigureCanvasTkAgg(figure, master=graph_frame)
canvas.get_tk_widget().place(x=0, y=0, width=600, height=500)


def show_graph():
    graph.clear()
    graph.scatter(x, y, label="داده های واقعی")

    graph.plot(x, y_pred, label='رگرسیون خطی')
    graph.set_xlabel("ساعات مطالعه")
    graph.set_ylabel("نمره")
    graph.set_title("ساعات مطالعه vs نمره")
    graph.legend()
    graph.grid(True)
    figure.tight_layout()
    canvas.draw()


graph_button = Button(window, text="نمایش نمودار",
                      command=show_graph, font=('', 18, 'bold'),
                      bg='#19291b', fg='white', bd=2)

graph_button.place(x=410, y=205, width=180, height=50)

# -------------------- Evaluation --------------------

evaluation_label = Label(window, text=(
    f"{mae:.2f} : میانگین خطای مطلق مدل \n\n"
    f"{mse:.2f} : میانگین مربعات خطای مدل \n\n"
    f"{rmse:.2f} : ریشه میانگین مربعات خطا \n\n"
    f" {r2:.2f} : ضریب تعیین"
), font=("Arial", 18, 'bold'))

evaluation_label.place(x=690, y=325, width=300, height=265)

# -------------------- Run --------------------
window.mainloop()
