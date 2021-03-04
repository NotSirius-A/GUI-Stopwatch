import time
import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk


############## NOTES ##################

#ns in var/func name means that its expressed in nanoseconds
#there's a bug round_btn_func, when timer exceeds 99h

############### APP ###################


class App:
    def __init__(self, master):
        self.master = master
        self.t_start_ns = 0
        self.timer_value_ns = 0
        self.last_time_value_ns = 0
        self.round_labels = [0]
        self.last_round_time_ns = 0

        #refresh period = time between updates in milisec
        self.refresh_period_ms = 15



        ##### Main frame setup #####
        main_frame = tk.Frame(master, bg='#222222')
        main_frame.pack(expand=True, fill=tk.BOTH, side=tk.TOP)

        ##### Stopwatch timer label setup #####
        timer_style = {'padx':15, 'pady':15, 'bg':'#1A1A1A', 'fg':'#E8E8E8', 'font':('Segoe UI', 65)}
        self.draw_timer(main_frame, timer_style)

        ##### Middle frame setup (this is where buttons go) #####
        middle_frame = tk.Frame(main_frame, height=60, bg='#222222')
        middle_frame.pack(padx=30, side=tk.TOP, fill=tk.BOTH, expand=False)

        ##### Setting up buttons #####
        button_placement = {'padx':30, 'pady':25, 'side':tk.LEFT, 'fill':tk.BOTH, 'expand':True}
        button_style = {'padx':25, 'pady':10, 'font':('Gadugi', 16, 'bold')}
        self.draw_buttons(middle_frame, button_placement, button_style)

        ##### Bottom frame setup #####
        bottom_frame = tk.Frame(main_frame, height=200, bg='#222222')
        bottom_frame.pack(padx=30, side=tk.TOP, fill=tk.BOTH, expand=True)

        #### Round textbox setup ####
        round_textframe_style = {'bg':'#222222'}
        self.draw_round_textframe(bottom_frame, round_textframe_style)

        #### Logo setup ####
        logo_path = 'logo.png'
        logo_style = {'bg':'#222222', 'fg':'#E8E8E8'}
        sign_font = ('Dubai', 17)
        self.draw_logo(bottom_frame, logo_style, logo_path, sign_font)





    def draw_timer(self, frame, timer_style):
        #timer_style = {'padx':pixels, 'pady':pixels, 'bg':'color', 'font':('font', size)}

        self.timer_value = tk.StringVar()
        # '00:00:00' is the default value
        self.timer_value.set('00:00:00.00')

        self.timer_label = tk.Label(frame, timer_style, textvariable=self.timer_value)
        self.timer_label.pack(pady=30, padx=70, fill=tk.BOTH, expand=False, side=tk.TOP)


    def draw_buttons(self, frame, button_placement, button_style):
        # button_placement = {'padx':pixels, 'pady':pixels, 'side':tk.LEFT, 'fill':tk.BOTH, 'expand':True}
        # button_size = {'padx':pixels, 'pady':pixels, 'font':('font', size)}


        self.StartStop_btn = tk.Button(frame, button_style, bg='#00a87a', text='Start', command=self.start_btn_func)
        self.StartStop_btn.pack(button_placement)

        self.round_btn = tk.Button(frame, button_style, bg='#0077af', text='Round', command=self.round_btn_func, state='disabled')
        self.round_btn.pack(button_placement)

        self.reset_btn = tk.Button(frame, button_style, bg='#ff6700', text='Reset', command=self.reset_btn_func)
        self.reset_btn.pack(button_placement)


    def start_btn_func(self):

        #transfrom into stop button
        self.StartStop_btn.config(bg='#F00030', text='Stop', command=self.stop_btn_func)

        #lock the reset button
        self.reset_btn.config(state='disabled')

        #unlock the round button
        self.round_btn.config(state='normal')

        #start counting here
        self.t_start_ns = time.time_ns()

        #the func below will start a timer update job
        self.update_timer_value_job()


    def update_timer_value_job(self):
        #Start to update every x milliseconds when func is called
        self.update_timer_job = self.master.after(self.refresh_period_ms, self.update_timer_value_job)

        self.timer_value_ns = self.time_since_ns(self.t_start_ns)

        self.timer_value_ns = self.timer_value_ns + self.last_time_value_ns

        value = self.format_ns_to_human(self.timer_value_ns)

        a = str(value['hours'])
        b = str(value['minutes'])
        c = str(value['seconds'])
        d = str(value['centyseconds'])

        #formatting values to look nicer
        a, b, c, d = ('00'+a)[-2:], ('00'+b)[-2:], ('00'+c)[-2:], ('00'+d)[-2:]

        self.timer_value.set(f"{a}:{b}:{c}.{d}")


    def stop_btn_func(self):
        #stop updating
        self.master.after_cancel(self.update_timer_job)

        #unlock the reset button
        self.reset_btn.config(state='normal')

        #lock the round button
        self.round_btn.config(state='disabled')

        #transform into start button
        self.StartStop_btn.config(bg='#00a87a', text='Start', command=self.start_btn_func)

        #save the last value 
        self.last_time_value_ns = self.timer_value_ns

        #!!! always makes an extra round appear when stop button is pressed
        self.round_btn_func()


    def reset_btn_func(self):
        self.timer_value.set("00:00:00.00")
        self.timer_value_ns = 0
        self.last_time_value_ns = 0
        self.last_round_time_ns = 0

        for i in self.round_labels:
            if i != 0:
                i.destroy()

        self.round_labels = [0]
                  

    def round_btn_func(self):
        round_time = tk.StringVar()
        x = self.timer_value_ns - self.last_round_time_ns
        self.last_round_time_ns = self.timer_value_ns

        x = self.format_ns_to_human(x)

        a = str(x['hours'])
        b = str(x['minutes'])
        c = str(x['seconds'])
        d = str(x['centyseconds'])

        #formatting values to look nicer
        #BUG it will not show correctly when hours reach 99+, but i dont think its worth fixing
        a, b, c, d = ('00'+a)[-2:], ('00'+b)[-2:], ('00'+c)[-2:], ('00'+d)[-2:]

        #theres always a 0 at the start, so no need for +1
        round_num = len(self.round_labels)

        round_time.set(f"| Round {round_num}    --->    {a}:{b}:{c}.{d}")


        #insert a label into the round_textframe Frame at the bottom of the list
        y = tk.Label(self.round_frame, bg='#1A1A1A', fg='#E8E8E8', width=25, anchor='w', font=('Segoe UI', 15, 'bold'), textvariable=round_time)
        y.pack(pady=(0,4), padx=(3,0), side=tk.TOP, fill=tk.X, expand=True)

        self.round_labels.append(y)


    def draw_round_textframe(self, frame, round_textframe_style):
        #round_textframe_style = {'bg':'color'}


        style = ttk.Style()
        style.configure("BW.TLabel", background=round_textframe_style['bg'])

        container = ttk.Frame(frame, style='BW.TLabel')
        canvas = tk.Canvas(container, round_textframe_style)

        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)

        self.round_frame = ttk.Frame(canvas, style='BW.TLabel')
        self.round_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=self.round_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        container.pack(padx=(40, 10), pady=30, side=tk.LEFT, fill=tk.BOTH, expand=True)
        canvas.pack(pady=(0,0), side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


    def time_since_ns(self, time_start_ns=0):

        time_now = time.time_ns()
        rv = time_now - time_start_ns
        return rv


    def format_ns_to_human(self, time_in_ns):
        human_time = {}

        time_in_s = time_in_ns/1e+9

        human_time['hours'] = int(time_in_s/3600)
        time_in_s = time_in_s - human_time['hours']*3600

        human_time['minutes'] = int(time_in_s/60)
        time_in_s = time_in_s - human_time['minutes']*60

        human_time['seconds'] = int((time_in_s))
        time_in_s = time_in_s - human_time['seconds']

        human_time['centyseconds'] = int(time_in_s*100)

        return human_time


    def draw_logo(self, frame, img_style, image_path, text_font):
        #logo_path = 'logo.png'
        #logo_style = {'bg':'color', 'fg':'color'}
        #sign_font = ('font', size)



        logo_frame = tk.Frame(frame, bg=img_style['bg'])
        logo_frame.pack(pady=10, padx=(20, 0), side=tk.TOP, fill=tk.BOTH, expand=True)

        sign_down = tk.Label(logo_frame, img_style, font=text_font, text='NotSirius-A')
        sign_down.pack(side=tk.BOTTOM, pady=(0, 15))

        sign_up = tk.Label(logo_frame, img_style, font=text_font, text='Made by:')
        sign_up.pack(side=tk.BOTTOM)


        image = Image.open(image_path)
        image = image.resize((80, 80), Image.ANTIALIAS)

        logo = ImageTk.PhotoImage(image)

        logo_label = tk.Label(logo_frame, img_style, width=150, image=logo)
        logo_label.image = logo

        logo_label.pack(side=tk.BOTTOM, pady=10)



#######################################



if __name__ == '__main__':
    root = tk.Tk()

    root.title('Stopwatch')

    root.geometry("700x650")

    app = App(root)

    root.mainloop()