import time
import tkinter as tk


############### APP ###################

class App:
    def __init__(self, master):
        self.master = master

        main_frame = tk.Frame(master, bg='grey')
        main_frame.pack(expand=True, fill=tk.BOTH, side=tk.TOP)



        self.timer_value = tk.StringVar()
        self.timer_value.set(0)

        font=('Calibri', 40)
        timer_label = tk.Label(main_frame, width=7, height=1, padx=10, pady=10, textvariable=self.timer_value, bg='red', font=font)
        timer_label.pack(pady=30, padx=70, fill=tk.BOTH, expand=True, side=tk.TOP)




        middle_frame = tk.Frame(main_frame, height=100, bg='purple')
        middle_frame.pack(padx=30, side=tk.TOP, fill=tk.BOTH, expand=True)


        button_placement = {'padx':40, 'pady':35, 'side':tk.LEFT, 'fill':tk.BOTH, 'expand':True}

        start_or_stop='Start'

        StartStop_btn = tk.Button(middle_frame, padx=25, pady=10, bg='green', text=start_or_stop, command=StartStop_btn_func)
        StartStop_btn.pack(button_placement)

        reset_btn = tk.Button(middle_frame, padx=25, pady=10, bg='yellow', text='Reset', command=reset_btn_func)
        reset_btn.pack(button_placement)

        round_btn = tk.Button(middle_frame, padx=25, pady=10, bg='grey', text='Round', command=round_btn_func)
        round_btn.pack(button_placement)


        bottom_frame = tk.Frame(main_frame, height=200, bg='lightgreen')
        bottom_frame.pack(padx=30, side=tk.TOP, fill=tk.BOTH, expand=True)





    # x = time.time_ns()
    # time.sleep(1)
    # print(time_since_ns(x))


############### DEF ####################

def StartStop_btn_func():
    print('startstop')
    print(app.master.winfo_height())
    print(app.master.winfo_width())

    app.timer_value.set(10)

def reset_btn_func():
    print('reset')


def round_btn_func():
    print('round')


def time_since_ns(time_start_ns=0):
    #this func return time in ns
    #ns means nanoseconds

    time_now = time.time_ns()
    rv = time_now - time_start_ns
    return rv


if __name__ == '__main__':
    root = tk.Tk()

    root.title('Stopwatch')

    root.geometry("600x400")

    app = App(root)

    root.mainloop()