import tkinter as tk
from tkinter import ttk
import backend.asset_management_backend as am


def listbox_on_select_item(event):
    pass


def clear_entity_tab_fields(tab):
    for widget in tab.winfo_children():
        widget.destroy()


def update_management_tab_content(ae):
    selected_tab = notebook.nametowidget(notebook.select())
    clear_entity_tab_fields(selected_tab)

    listbox = tk.Listbox(selected_tab)

    if ae == "Animals":
        # listbox.delete(0, 'end')
        #am.view_animals()

        a_id_label = ttk.Label(notebook.nametowidget(notebook.select()), text='A_ID')
        a_id_label.pack()
        a_id = tk.StringVar()
        a_id_entry = ttk.Entry(notebook.nametowidget(notebook.select()), textvariable=a_id)
        a_id_entry.pack()

        status_label = ttk.Label(notebook.nametowidget(notebook.select()), text='Status')
        status_label.pack()
        status = tk.StringVar()
        status_entry = ttk.Entry(notebook.nametowidget(notebook.select()), textvariable=status)
        status_entry.pack()

        birth_year_label = ttk.Label(notebook.nametowidget(notebook.select()), text='Birth_Year')
        birth_year_label.pack()
        birth_year = tk.StringVar()
        birth_year_entry = ttk.Entry(notebook.nametowidget(notebook.select()), textvariable=birth_year)
        birth_year_entry.pack()

        s_id_label = ttk.Label(notebook.nametowidget(notebook.select()), text='S_ID')
        s_id_label.pack()
        s_id = tk.StringVar()
        s_id_entry = ttk.Entry(notebook.nametowidget(notebook.select()), textvariable=s_id)
        s_id_entry.pack()

        b_id_label = ttk.Label(notebook.nametowidget(notebook.select()), text='B_ID')
        b_id_label.pack()
        b_id = tk.StringVar()
        b_id_entry = ttk.Entry(notebook.nametowidget(notebook.select()), textvariable=b_id)
        b_id_entry.pack()

        en_id_label = ttk.Label(notebook.nametowidget(notebook.select()), text='EN_ID')
        en_id_label.pack()
        en_id = tk.StringVar()
        en_id_entry = ttk.Entry(notebook.nametowidget(notebook.select()), textvariable=en_id)
        en_id_entry.pack()

        button = ttk.Button(selected_tab, text='Insert', command=lambda:am.insert_animal(a_id.get(),status.get(),birth_year.get(),s_id.get(),b_id.get(),en_id.get()))
        button.pack()
        button = ttk.Button(selected_tab, text='Update', command=lambda:am.update_animal(a_id.get(),status.get(),birth_year.get(),s_id.get(),b_id.get(),en_id.get()))
        button.pack()

        listbox.pack(side=tk.LEFT, fill='both', expand=True)

        sb = tk.Scrollbar(selected_tab)
        sb.pack(side=tk.RIGHT, fill='y')

        listbox.config(yscrollcommand=sb.set)
        listbox.bind('<<ListboxSelect>>',get_selected_row)
    elif ae == "Buildings":
        #am.view_buildings()

        b_id_label = ttk.Label(notebook.nametowidget(notebook.select()), text='B_ID')
        b_id_label.pack()
        b_id = tk.StringVar()
        b_id_entry = ttk.Entry(notebook.nametowidget(notebook.select()), textvariable=b_id)
        b_id_entry.pack()

        b_name_label = ttk.Label(notebook.nametowidget(notebook.select()), text='Name')
        b_name_label.pack()
        b_name = tk.StringVar()
        b_name_entry = ttk.Entry(notebook.nametowidget(notebook.select()), textvariable=b_name)
        b_name_entry.pack()

        building_type_label = ttk.Label(notebook.nametowidget(notebook.select()), text='Type')
        building_type_label.pack()
        building_type = tk.StringVar()
        building_type_entry = ttk.Entry(notebook.nametowidget(notebook.select()), textvariable=building_type)
        building_type_entry.pack()

        button = ttk.Button(selected_tab, text='Insert', command=lambda:am.insert_building(b_id,b_name,building_type))
        button.pack()
        button = ttk.Button(selected_tab, text='Update', command=lambda:am.update_building(b_id,b_name,building_type))
        button.pack()
    elif ae == "Attractions":
        #am.view_attractions()

        atr_id_label = ttk.Label(notebook.nametowidget(notebook.select()), text='ATR_ID')
        atr_id_label.pack()
        atr_id = tk.StringVar()
        atr_id_entry = ttk.Entry(notebook.nametowidget(notebook.select()), textvariable=atr_id)
        atr_id_entry.pack()

        attraction_name_label = ttk.Label(notebook.nametowidget(notebook.select()), text='Attraction_Name')
        attraction_name_label.pack()
        attraction_name = tk.StringVar()
        attraction_name_entry = ttk.Entry(notebook.nametowidget(notebook.select()), textvariable=attraction_name)
        attraction_name_entry.pack()

        bid_label = ttk.Label(notebook.nametowidget(notebook.select()), text='B_ID')
        bid_label.pack()
        bid = tk.StringVar()
        bid_entry = ttk.Entry(notebook.nametowidget(notebook.select()), textvariable=bid)
        bid_entry.pack()

        building_name_label = ttk.Label(notebook.nametowidget(notebook.select()), text='Building_Name')
        building_name_label.pack()
        building_name = tk.StringVar()
        building_name_entry = ttk.Entry(notebook.nametowidget(notebook.select()), textvariable=building_name)
        building_name_entry.pack()

        number_of_shows_per_day_label = ttk.Label(notebook.nametowidget(notebook.select()), text='Number_Of_Shows_Per_Day')
        number_of_shows_per_day_label.pack()
        number_of_shows_per_day = tk.StringVar()
        number_of_shows_per_day_entry = ttk.Entry(notebook.nametowidget(notebook.select()), textvariable=number_of_shows_per_day)
        number_of_shows_per_day_entry.pack()

        child_ticket_price_label = ttk.Label(notebook.nametowidget(notebook.select()), text='Child_Ticket_Price')
        child_ticket_price_label.pack()
        child_ticket_price = tk.StringVar()
        child_ticket_price_entry = ttk.Entry(notebook.nametowidget(notebook.select()), textvariable=child_ticket_price)
        child_ticket_price_entry.pack()

        adult_ticket_price_label = ttk.Label(notebook.nametowidget(notebook.select()), text='Adult_Ticket_Price')
        adult_ticket_price_label.pack()
        adult_ticket_price = tk.StringVar()
        adult_ticket_price_entry = ttk.Entry(notebook.nametowidget(notebook.select()), textvariable=adult_ticket_price)
        adult_ticket_price_entry.pack()

        senior_ticket_price_label = ttk.Label(notebook.nametowidget(notebook.select()), text='Senior_Ticket_Price')
        senior_ticket_price_label.pack()
        senior_ticket_price = tk.StringVar()
        senior_ticket_price_entry = ttk.Entry(notebook.nametowidget(notebook.select()), textvariable=senior_ticket_price)
        senior_ticket_price_entry.pack()

        aid_label = ttk.Label(notebook.nametowidget(notebook.select()), text='A_ID')
        aid_label.pack()
        aid = tk.StringVar()
        aid_entry = ttk.Entry(notebook.nametowidget(notebook.select()), textvariable=aid)
        aid_entry.pack()

        number_of_animals_label = ttk.Label(notebook.nametowidget(notebook.select()), text='Number_Of_Animals')
        number_of_animals_label.pack()
        number_of_animals = tk.StringVar()
        number_of_animals_entry = ttk.Entry(notebook.nametowidget(notebook.select()), textvariable=number_of_animals)
        number_of_animals_entry.pack()

        button = ttk.Button(selected_tab, text='Insert', command=lambda:am.insert_attraction(atr_id,attraction_name,b_id,building_name,number_of_shows_per_day,child_ticket_price,adult_ticket_price,senior_ticket_price,a_id,number_of_animals))
        button.pack()
        button = ttk.Button(selected_tab, text='Update', command=lambda:am.update_attraction(atr_id,attraction_name,b_id,building_name,number_of_shows_per_day,child_ticket_price,adult_ticket_price,senior_ticket_price,a_id,number_of_animals))
        button.pack()
    elif ae == "Employees":
        #am.view_employees()

        e_id_label = ttk.Label(notebook.nametowidget(notebook.select()), text='E_ID')
        e_id_label.pack()
        e_id = tk.StringVar()
        e_id_entry = ttk.Entry(notebook.nametowidget(notebook.select()), textvariable=e_id)
        e_id_entry.pack()

        fname_label = ttk.Label(notebook.nametowidget(notebook.select()), text='First_Name')
        fname_label.pack()
        fname = tk.StringVar()
        fname_entry = ttk.Entry(notebook.nametowidget(notebook.select()), textvariable=fname)
        fname_entry.pack()

        minit_label = ttk.Label(notebook.nametowidget(notebook.select()), text='Middle_Name_Initial')
        minit_label.pack()
        minit = tk.StringVar()
        minit_entry = ttk.Entry(notebook.nametowidget(notebook.select()), textvariable=minit)
        minit_entry.pack()

        lname_label = ttk.Label(notebook.nametowidget(notebook.select()), text='Last_Name')
        lname_label.pack()
        lname = tk.StringVar()
        lname_entry = ttk.Entry(notebook.nametowidget(notebook.select()), textvariable=lname)
        lname_entry.pack()

        street_label = ttk.Label(notebook.nametowidget(notebook.select()), text='Street')
        street_label.pack()
        street = tk.StringVar()
        street_entry = ttk.Entry(notebook.nametowidget(notebook.select()), textvariable=street)
        street_entry.pack()

        city_label = ttk.Label(notebook.nametowidget(notebook.select()), text='City')
        city_label.pack()
        city = tk.StringVar()
        city_entry = ttk.Entry(notebook.nametowidget(notebook.select()), textvariable=city)
        city_entry.pack()

        state_label = ttk.Label(notebook.nametowidget(notebook.select()), text='State')
        state_label.pack()
        state = tk.StringVar()
        state_entry = ttk.Entry(notebook.nametowidget(notebook.select()), textvariable=state)
        state_entry.pack()

        zip_label = ttk.Label(notebook.nametowidget(notebook.select()), text='Zip')
        zip_label.pack()
        zip_val = tk.StringVar()
        zip_entry = ttk.Entry(notebook.nametowidget(notebook.select()), textvariable=zip_val)
        zip_entry.pack()

        job_type_label = ttk.Label(notebook.nametowidget(notebook.select()), text='Job_Type')
        job_type_label.pack()
        job_type = tk.StringVar()
        job_type_entry = ttk.Entry(notebook.nametowidget(notebook.select()), textvariable=job_type)
        job_type_entry.pack()

        start_date_label = ttk.Label(notebook.nametowidget(notebook.select()), text='Start_Date')
        start_date_label.pack()
        start_date = tk.StringVar()
        start_date_entry = ttk.Entry(notebook.nametowidget(notebook.select()), textvariable=start_date)
        start_date_entry.pack()

        super_id_label = ttk.Label(notebook.nametowidget(notebook.select()), text='Super_ID')
        super_id_label.pack()
        super_id = tk.StringVar()
        super_id_entry = ttk.Entry(notebook.nametowidget(notebook.select()), textvariable=super_id)
        super_id_entry.pack()

        h_id_label = ttk.Label(notebook.nametowidget(notebook.select()), text='H_ID')
        h_id_label.pack()
        h_id = tk.StringVar()
        h_id_entry = ttk.Entry(notebook.nametowidget(notebook.select()), textvariable=h_id)
        h_id_entry.pack()

        r_id_label = ttk.Label(notebook.nametowidget(notebook.select()), text='R_ID')
        r_id_label.pack()
        r_id = tk.StringVar()
        r_id_entry = ttk.Entry(notebook.nametowidget(notebook.select()), textvariable=r_id)
        r_id_entry.pack()

        button = ttk.Button(selected_tab, text='Insert', command=lambda:am.insert_employee(e_id,fname,minit,lname,street,city,state,zip_val,job_type,start_date,super_id,h_id,r_id))
        button.pack()
        button = ttk.Button(selected_tab, text='Update', command=lambda:am.insert_employee(e_id,fname,minit,lname,street,city,state,zip_val,job_type,start_date,super_id,h_id,r_id))
        button.pack()
    elif ae == "Hourly_Rate":
        #am.view_hourly_rate()

        h_id_label = ttk.Label(notebook.nametowidget(notebook.select()), text='H_ID')
        h_id_label.pack()
        h_id = tk.StringVar()
        h_id_entry = ttk.Entry(notebook.nametowidget(notebook.select()), textvariable=h_id)
        h_id_entry.pack()

        rate_label = ttk.Label(notebook.nametowidget(notebook.select()), text='Rate')
        rate_label.pack()
        rate = tk.StringVar()
        rate_entry = ttk.Entry(notebook.nametowidget(notebook.select()), textvariable=rate)
        rate_entry.pack()

        button = ttk.Button(selected_tab, text='Insert', command=lambda:am.insert_hourly_rate(h_id,rate))
        button.pack()
        button = ttk.Button(selected_tab, text='Update', command=lambda:am.update_hourly_rate(h_id,rate))
        button.pack()


def switch_management_tab(event):
    selected_entity_tab = notebook.tab(notebook.select(), "text")
    update_management_tab_content(selected_entity_tab)


def assets_window_content(aw):
    aw.title('Asset Management')

    global notebook
    notebook = ttk.Notebook(aw)
    notebook.pack(fill='both', expand=True)

    asset_entities = ["Animals", "Buildings", "Attractions", "Employees", "Hourly_Rate"]
    for ae in asset_entities:
        tab = ttk.Frame(notebook)
        notebook.add(tab, text=ae)

    notebook.bind("<<NotebookTabChanged>>", switch_management_tab)

