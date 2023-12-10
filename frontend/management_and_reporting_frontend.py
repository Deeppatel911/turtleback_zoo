import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from datetime import datetime
import backend.management_and_reporting_backend as mar

global selected_date, begin_date, end_date, selected_month_item
tdy = datetime.today().date()


def on_dropdown_menu_selected_month(event):
    global selected_month_item
    selected_month_item = month_dropdown_menu.get()


def on_dropdown_menu_selected_year(event):
    global selected_year_item
    selected_year_item = year_dropdown_menu.get()


def clear_entity_tab_fields(tab):
    for widget in tab.winfo_children():
        widget.destroy()


def update_management_and_reporting_tab_content(ae):
    selected_tab = notebook.nametowidget(notebook.select())
    clear_entity_tab_fields(selected_tab)

    if ae == "Day_Revenue_By_Source":
        cal = Calendar(selected_tab, selectmode = 'day',
               year = tdy.year, month = tdy.month,
               day = tdy.day)
        cal.pack()
        
        bottom_frame = tk.Frame(selected_tab)
        bottom_frame.pack(side=tk.BOTTOM, fill='x', expand='True')

        button = ttk.Button(bottom_frame, text='Fetch', command=lambda:mar.generate_day_revenue_by_source(cal.get_date()))
        button.pack()
    elif ae == "Animal_Stats":
        #mar.generate_animal_stats()

        bottom_frame = tk.Frame(selected_tab)
        bottom_frame.pack(side=tk.BOTTOM, fill='x', expand='True')
    elif ae == "Top_Attractions_By_Revenue":
        upper_frame = tk.Frame(selected_tab)
        upper_frame.pack(side=tk.TOP,fill='both',expand=True)

        left_frame = tk.Frame(upper_frame)
        left_frame.pack(side=tk.LEFT,fill='x', expand=True)

        begin_date_label = tk.Label(left_frame, text="Begin Date:")
        begin_date_label.pack()

        begin_cal = Calendar(left_frame, selectmode='day', year=tdy.year, month=tdy.month, day=tdy.day)
        begin_cal.pack()

        right_frame = tk.Frame(upper_frame)
        right_frame.pack(side=tk.RIGHT, fill='x', expand=True)

        end_date_label = tk.Label(right_frame, text="End Date:")
        end_date_label.pack()

        end_cal = Calendar(right_frame, selectmode='day', year=tdy.year, month=tdy.month, day=tdy.day)
        end_cal.pack()

        bottom_frame = tk.Frame(selected_tab)
        bottom_frame.pack(side=tk.BOTTOM, fill='x', expand='True')

        button = ttk.Button(bottom_frame, text='Fetch', command=lambda:mar.compute_top_attractions_by_revenue(begin_cal.get_date(),end_cal.get_date()))
        button.pack()
    elif ae == "Month_Best_Days_Revenue":
        selected_month=tk.StringVar(value='Select_Month')
        month_list=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

        global month_dropdown_menu
        month_label = ttk.Label(notebook.nametowidget(notebook.select()), text='Month')
        month_label.pack()
        month_dropdown_menu = ttk.Combobox(selected_tab, state='readonly', textvariable=selected_month, values=month_list)
        month_dropdown_menu.pack()
        month_dropdown_menu.bind("<<ComboboxSelected>>",on_dropdown_menu_selected_month)


        global year_dropdown_menu
        selected_year=tk.StringVar(value='Select_Year')
        year_list=[i for i in range(tdy.year,1970,-1)]
        month_label = ttk.Label(notebook.nametowidget(notebook.select()), text='Year')
        month_label.pack()
        year_dropdown_menu = ttk.Combobox(selected_tab, state='readonly', textvariable=selected_year, values=year_list)
        year_dropdown_menu.pack()
        year_dropdown_menu.bind("<<ComboboxSelected>>",on_dropdown_menu_selected_year)

        bottom_frame = tk.Frame(selected_tab)
        bottom_frame.pack(side=tk.BOTTOM, fill='x', expand='True')

        
        button = ttk.Button(bottom_frame, text='Fetch', command=lambda:mar.compute_month_best_days_revenue(globals()['selected_month_item'],globals()['selected_year_item']))
        button.pack()
    elif ae == "Average_Revenue_Attraction_Concession_TotalAttendance":
        upper_frame = tk.Frame(selected_tab)
        upper_frame.pack(side=tk.TOP,fill='both',expand=True)

        left_frame = tk.Frame(upper_frame)
        left_frame.pack(side=tk.LEFT,fill='x', expand=True)

        begin_date_label = tk.Label(left_frame, text="Begin Date:")
        begin_date_label.pack()

        begin_cal = Calendar(left_frame, selectmode='day', year=tdy.year, month=tdy.month, day=tdy.day)
        begin_cal.pack()

        right_frame = tk.Frame(upper_frame)
        right_frame.pack(side=tk.RIGHT, fill='x', expand=True)

        end_date_label = tk.Label(right_frame, text="End Date:")
        end_date_label.pack()

        end_cal = Calendar(right_frame, selectmode='day', year=tdy.year, month=tdy.month, day=tdy.day)
        end_cal.pack()

        bottom_frame = tk.Frame(selected_tab)
        bottom_frame.pack(side=tk.BOTTOM, fill='x', expand='True')
    
        button = ttk.Button(bottom_frame, text='Fetch', command=lambda:mar.compute_average_revenue_attraction_concession_totalAttendance(begin_cal.get_date(),end_cal.get_date()))
        button.pack()

    
    #bottom_frame = tk.Frame(selected_tab)
    #bottom_frame.pack(side=tk.BOTTOM, fill='x', expand='True')

    
    #button = ttk.Button(bottom_frame, text='Fetch', command=command_function)
    #button.pack()

    listbox = tk.Listbox(bottom_frame)
    listbox.pack(side=tk.LEFT, fill='x', expand=True)

    sb = tk.Scrollbar(bottom_frame)
    sb.pack(side=tk.RIGHT, fill='y')

    listbox.config(yscrollcommand=sb.set)


def switch_management_and_reporting_tab(event):
    selected_entity_tab = notebook.tab(notebook.select(), "text")
    update_management_and_reporting_tab_content(selected_entity_tab)


def management_and_reporting_content(aw):
    aw.title('Management and Reporting')

    global notebook
    notebook = ttk.Notebook(aw)
    notebook.pack(fill='both', expand=True)

    asset_entities = ["Day_Revenue_By_Source", "Animal_Stats", "Top_Attractions_By_Revenue", "Month_Best_Days_Revenue",
                      "Average_Revenue_Attraction_Concession_TotalAttendance"]
    for ae in asset_entities:
        tab = ttk.Frame(notebook)
        notebook.add(tab, text=ae)

    notebook.bind("<<NotebookTabChanged>>", switch_management_and_reporting_tab)

