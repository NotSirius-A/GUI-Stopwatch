import time
import tkinter as tk


############### MAIN ###################

class App:
    def __init__(self, master):
        self.master = master

        main_frame = tk.Frame(master, bg='lightblue')
        main_frame.pack(expand=True, fill=tk.BOTH, side=tk.TOP)


        font=('Calibri', 40)
        timer_label = tk.Label(main_frame, width=7, height=1, padx=10, pady=10, text='dsfsdfsf', bg='red', font=font)
        timer_label.pack(pady=30, padx=70, fill=tk.BOTH, side=tk.TOP)

        middle_frame = tk.Frame(main_frame, height=100, bg='purple')
        middle_frame.pack(padx=20, side=tk.TOP, fill=tk.BOTH, expand=True)


        button_style = {'width':1, 'height':1, 'bg':'grey'}
        button_config = {'padx':60, 'pady':40, 'side':tk.LEFT, 'fill':tk.BOTH, 'expand':True}


        left_btn = tk.Button(middle_frame, button_style, text='fsdfs', command=lambda:print('ok'))
        left_btn.pack(button_config)

        mid_btn = tk.Button(middle_frame, button_style)
        mid_btn.pack(button_config)

        right_btn = tk.Button(middle_frame, button_style)
        right_btn.pack(button_config)


        bottom_frame = tk.Frame(main_frame, height=100, bg='lightgreen')
        bottom_frame.pack(padx=20, side=tk.TOP, fill=tk.BOTH, expand=True)






        # btn_frame = tk.Frame(master, width=500, height=100, bg='purple')
        # btn_frame.grid(column=1, row=4)

        # left_btn = tk.Button(btn_frame, text='sssdfs')
        # left_btn.pack(side=tk.LEFT)

        # right_btn = tk.Button(btn_frame, text='dfsf')
        # right_btn.pack(side=tk.RIGHT)



        root.mainloop()




    # canvas = tk.Frame(root, width=500, height=400, bg='lightblue')
    # canvas.grid(columnspan=3, rowspan=3)

    # label = tk.Label(root, text='4hh3242dsa3423')
    # label.grid(column=1, row=0)

    # btn_frame = tk.Frame(root)
    # btn_frame.grid(column=1, row=1)

    # ex_btn = tk.Button(btn_frame, text='sdfd', fg='red')
    # ex_btn.pack(side=tk.LEFT)

    # spacer = tk.Frame(btn_frame, width=20, height=1)
    # spacer.pack(side=tk.LEFT)

    # other_btn = tk.Button(btn_frame, text='gdfgd', fg='blue')
    # other_btn.pack(side=tk.RIGHT)












    # x = time.time_ns()
    # time.sleep(1)
    # print(time_since_ns(x))


############### DEF ####################


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