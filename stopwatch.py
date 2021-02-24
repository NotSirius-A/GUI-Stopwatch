import time
import tkinter as tk


############### APP ###################

class App:
    def __init__(self, master):
        self.master = master
        self.t_start_ns = 0
        #time between updates in milisec
        self.refresh_period_ms = 15

        ##### Main frame setup #####
        main_frame = tk.Frame(master, bg='grey')
        main_frame.pack(expand=True, fill=tk.BOTH, side=tk.TOP)

        ##### Stopwatch timer label setup #####
        timer_style = {'padx':10, 'pady':10, 'bg':'red', 'font':('Calibri', 40)}
        self.draw_timer(main_frame, timer_style)

        ##### Middle frame setup (this is where buttons go) #####
        middle_frame = tk.Frame(main_frame, height=100, bg='purple')
        middle_frame.pack(padx=30, side=tk.TOP, fill=tk.BOTH, expand=True)

        ##### Setting up buttons #####
        button_placement = {'padx':40, 'pady':35, 'side':tk.LEFT, 'fill':tk.BOTH, 'expand':True}
        button_size = {'padx':25, 'pady':10}
        self.draw_buttons(middle_frame, button_placement, button_size)

        ##### bottom frame setup #####
        bottom_frame = tk.Frame(main_frame, height=200, bg='lightgreen')
        bottom_frame.pack(padx=30, side=tk.TOP, fill=tk.BOTH, expand=True)

    def draw_timer(self, frame, timer_style):
        #timer_style = {'padx':pixels, 'pady':pixels, 'bg':'color', 'font':('font', size)}

        self.timer_value = tk.StringVar()
        # '00:00:00' is the default value
        self.timer_value.set('00:00:00.00')

        self.timer_label = tk.Label(frame, timer_style, textvariable=self.timer_value)
        self.timer_label.pack(pady=30, padx=70, fill=tk.BOTH, expand=True, side=tk.TOP)

    def draw_buttons(self, frame, button_placement, button_size):
        # button_placement = {'padx':pixels, 'pady':pixels, 'side':tk.LEFT, 'fill':tk.BOTH, 'expand':True}
        # button_size = {'padx':pixels, 'pady':pixels}


        self.StartStop_btn = tk.Button(frame, button_size, bg='green', text='Start', command=self.start_btn_func)
        self.StartStop_btn.pack(button_placement)

        self.reset_btn = tk.Button(frame, button_size, bg='yellow', text='Reset', command=self.reset_btn_func)
        self.reset_btn.pack(button_placement)

        self.round_btn = tk.Button(frame, button_size, bg='grey', text='Round', command=self.round_btn_func)
        self.round_btn.pack(button_placement)

    def start_btn_func(self):

        #transfrom into stop button
        self.StartStop_btn.config(bg='red', text='Stop', command=self.stop_btn_func)

        #start counting here
        self.t_start_ns = time.time_ns()

        #the func below will start a timer update job
        self.update_timer_value_job()


        # print('start')
        # print(self.master.winfo_height())
        # print(self.master.winfo_width())

    def update_timer_value_job(self):
        #Start to update every x milliseconds when func is called
        self.update_timer_job = self.master.after(self.refresh_period_ms, self.update_timer_value_job)

        x = self.time_since_ns(self.t_start_ns)
        self.timer_value.set(x/10e+8)


    def stop_btn_func(self):
        #stop updating
        self.master.after_cancel(self.update_timer_job)

        #transform inro start button
        self.StartStop_btn.config(bg='green', text='Start', command=self.start_btn_func)


    def reset_btn_func(self):
        self.timer_value.set("0")
        

    def round_btn_func(self):
        self.timer_value.set("1111s")
        print('round')


    def time_since_ns(self, time_start_ns=0):
        #this func return time in ns
        #ns means nanoseconds

        time_now = time.time_ns()
        rv = time_now - time_start_ns
        return rv


#######################################


# def StartStop_btn_func():
#     global job1
#     print('startstop')
#     print(app.master.winfo_height())
#     print(app.master.winfo_width())

#     x = time_since_ns(start_time_ns)
#     app.timer_value.set(x)

#     job1 = app.master.after(500, StartStop_btn_func)


# def reset_btn_func():
#     print('reset')
#     global job1
#     app.master.after_cancel(job1)


# def round_btn_func():
#     print('round')



if __name__ == '__main__':
    root = tk.Tk()

    root.title('Stopwatch')

    root.geometry("600x400")

    app = App(root)

    root.mainloop()