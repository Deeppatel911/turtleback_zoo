import tkinter as tk
from tkinter import ttk
import frontend.asset_management_frontend as am
import frontend.daily_zoo_activity_frontend as dza
import frontend.management_and_reporting_frontend as mar


def open_management():
    assets_window = tk.Toplevel(main_window)
    am.assets_window_content(assets_window)


def open_daily_zoo_activity():
    activity_window = tk.Toplevel(main_window)
    dza.daily_zoo_window_content(activity_window)


def open_management_and_reporting():
    management_and_reporting_window = tk.Toplevel(main_window)
    mar.management_and_reporting_content(management_and_reporting_window)


main_window = tk.Tk()
main_window.title('Turtleback Zoo')

heading = ttk.Label(main_window, text='Turtleback Zoo', font=('Arial', 16, 'bold'))
heading.pack(pady=10)

asset_management_button = ttk.Button(main_window, text='Asset Management', command=open_management)
asset_management_button.pack()
daily_zoo_activity_button = ttk.Button(main_window, text='Daily Zoo Activity', command=open_daily_zoo_activity)
daily_zoo_activity_button.pack()
management_and_reporting = ttk.Button(main_window, text='Management And Reporting',
                                      command=open_management_and_reporting)
management_and_reporting.pack()

main_window.mainloop()
