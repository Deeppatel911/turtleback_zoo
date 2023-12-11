import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from datetime import datetime
import backend.management_and_reporting_backend as mar

global selected_date, begin_date, end_date, selected_month_item
tdy = datetime.today().date()

def listbox_on_select_item(event, tree):
    pass


def on_dropdown_menu_selected_month(event):
    global selected_month_item
    selected_month_item = month_dropdown_menu.get()


def on_dropdown_menu_selected_year(event):
    global selected_year_item
    selected_year_item = year_dropdown_menu.get()


def day_revenue_by_source_assign_result(date,tree):
    result_day_revenue_by_source=mar.generate_day_revenue_by_source(date)
    
    for item in tree.get_children():
        tree.delete(item)

    for row in result_day_revenue_by_source:
        tree.insert("", "end", values=row)


def animal_stats_assign_result(tree):
    result_animal_stats=mar.generate_animal_stats()

    for item in tree.get_children():
        tree.delete(item)

    for row in result_animal_stats:
        tree.insert("", "end", values=row)


def compute_top_attractions_by_revenue_assign_result(begin_cal_date,end_cal_date,tree):
    begin_date_dt = datetime.strptime(begin_cal_date, "%m/%d/%y")
    formatted_begin_date_str = begin_date_dt.strftime("%Y-%m-%d")

    end_date_dt = datetime.strptime(end_cal_date, "%m/%d/%y")
    formatted_end_date_str = end_date_dt.strftime("%Y-%m-%d")

    result_compute_top_attractions_by_revenue=mar.compute_top_attractions_by_revenue(formatted_begin_date_str,formatted_end_date_str)
    for item in tree.get_children():
        tree.delete(item)

    for row in result_compute_top_attractions_by_revenue:
        tree.insert("", "end", values=row)


def compute_month_best_days_revenue_assign_result(month,tree):
    result_compute_month_best_days_revenue=mar.compute_month_best_days_revenue(month,globals()['selected_year_item'])

    for item in tree.get_children():
        tree.delete(item)

    for row in result_compute_month_best_days_revenue:
        tree.insert("", "end", values=row)


def compute_average_revenue_attraction_concession_totalAttendance_assign_result(begin_cal_date,end_cal_date,tree):
    begin_date_dt = datetime.strptime(begin_cal_date, "%m/%d/%y")
    formatted_begin_date_str = begin_date_dt.strftime("%Y-%m-%d")

    end_date_dt = datetime.strptime(end_cal_date, "%m/%d/%y")
    formatted_end_date_str = end_date_dt.strftime("%Y-%m-%d")

    result_compute_average_revenue_attraction_concession_totalAttendance=mar.compute_average_revenue_attraction_concession_totalAttendance(formatted_begin_date_str,formatted_end_date_str)
    
    for item in tree.get_children():
        tree.delete(item)

    for row in result_compute_average_revenue_attraction_concession_totalAttendance:
        tree.insert("", "end", values=row)


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

        columns = ("RID", "NAME", "TYPE", "BID", "SUBTOTAL")
        tree = ttk.Treeview(selected_tab, columns=columns, show="headings")

        for col in columns:
            tree.heading(col, text=col)

        button = ttk.Button(bottom_frame, text='Fetch', command=lambda:day_revenue_by_source_assign_result(cal.get_date(),tree))
        button.pack()

        
        #global result_day_revenue_by_source
        #result_day_revenue_by_source=None
        #for row in result_day_revenue_by_source:
        #    tree.insert("", "end", values=row)

        tree.bind("<<TreeviewSelect>>", lambda event: listbox_on_select_item(event, tree))

        tree.pack(side=tk.LEFT, fill='both', expand=True)

        sb = tk.Scrollbar(selected_tab)
        sb.pack(side=tk.RIGHT, fill='y')

        tree.config(yscrollcommand=sb.set)
    elif ae == "Animal_Stats":

        bottom_frame = tk.Frame(selected_tab)
        bottom_frame.pack(side=tk.BOTTOM, fill='x', expand='True')

        columns = ("RID", "NAME", "TYPE", "BID", "SUBTOTAL")
        tree = ttk.Treeview(selected_tab, columns=columns, show="headings")

        for col in columns:
            tree.heading(col, text=col)

        tree.bind("<<TreeviewSelect>>", lambda event: listbox_on_select_item(event, tree))

        tree.pack(side=tk.LEFT, fill='both', expand=True)

        sb = tk.Scrollbar(selected_tab)
        sb.pack(side=tk.RIGHT, fill='y')

        tree.config(yscrollcommand=sb.set)

        animal_stats_assign_result(tree)
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

        columns = ("Attraction Name", "Total Revenue")
        tree = ttk.Treeview(bottom_frame, columns=columns, show="headings")

        for col in columns:
            tree.heading(col, text=col)


        button = ttk.Button(bottom_frame, text='Fetch', command=lambda:compute_top_attractions_by_revenue_assign_result(begin_cal.get_date(),end_cal.get_date(),tree))
        button.pack()

        tree.bind("<<TreeviewSelect>>", lambda event: listbox_on_select_item(event, tree))

        tree.pack(side=tk.LEFT, fill='both', expand=True)

        sb = tk.Scrollbar(selected_tab)
        sb.pack(side=tk.RIGHT, fill='y')

        tree.config(yscrollcommand=sb.set)
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

        columns = ("Revenue Date", "Total Revenue")
        tree = ttk.Treeview(bottom_frame, columns=columns, show="headings")

        for col in columns:
            tree.heading(col, text=col)

        
        button = ttk.Button(bottom_frame, text='Fetch', command=lambda:compute_month_best_days_revenue_assign_result(month_list.index(selected_month.get())+1,tree))
        button.pack()

        tree.bind("<<TreeviewSelect>>", lambda event: listbox_on_select_item(event, tree))

        tree.pack(side=tk.LEFT, fill='both', expand=True)

        sb = tk.Scrollbar(selected_tab)
        sb.pack(side=tk.RIGHT, fill='y')

        tree.config(yscrollcommand=sb.set)
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
    
        columns = ("Item Name", "Average Revenue")
        tree = ttk.Treeview(bottom_frame, columns=columns, show="headings")

        for col in columns:
            tree.heading(col, text=col)

        button = ttk.Button(bottom_frame, text='Fetch', command=lambda:compute_average_revenue_attraction_concession_totalAttendance_assign_result(begin_cal.get_date(),end_cal.get_date(),tree))
        button.pack()

        tree.bind("<<TreeviewSelect>>", lambda event: listbox_on_select_item(event, tree))

        tree.pack(side=tk.LEFT, fill='both', expand=True)

        sb = tk.Scrollbar(selected_tab)
        sb.pack(side=tk.RIGHT, fill='y')

        tree.config(yscrollcommand=sb.set)

    
    #bottom_frame = tk.Frame(selected_tab)
    #bottom_frame.pack(side=tk.BOTTOM, fill='x', expand='True')

    
    #button = ttk.Button(bottom_frame, text='Fetch', command=command_function)
    #button.pack()

    #listbox = tk.Listbox(bottom_frame)
    #listbox.pack(side=tk.LEFT, fill='x', expand=True)

    #sb = tk.Scrollbar(bottom_frame)
    #sb.pack(side=tk.RIGHT, fill='y')

    #listbox.config(yscrollcommand=sb.set)


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

