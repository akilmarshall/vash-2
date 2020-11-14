import tabs.root
from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox, Listbox
from tkinter import scrolledtext
import tkcalendar
from database import database_functions


class Root(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('VASH Report Helper')

        # define the intial size of the window
        self.geometry('700x700')

        # create the notebook object to contain the frames
        self.tab_root = ttk.Notebook(self)

        # define each frame
        self.tab_home = ttk.Frame(self.tab_root)
        self.tab_new_case = ttk.Frame(self.tab_root)
        self.tab_search = ttk.Frame(self.tab_root)

        # setup each tab
        self.__setup_home_tab__()
        self.__setup_new_case_tab__()
        self.__setup_search_tab__()

        # add each frame to the notebook object
        self.tab_root.add(self.tab_home, text='Home')
        self.tab_root.add(self.tab_new_case, text='New Case')
        self.tab_root.add(self.tab_search, text='Search')

        # display the root object
        self.tab_root.pack(expand=1, fill='both')

    def __setup_home_tab__(self):
        welcome_text = ttk.Label(
            self.tab_home, text='Welcome to the VASH Report Helper')
        welcome_text.grid(column=0, row=0, padx=20, pady=20)

    def clear_case(self):
        for key in self.string_var_dict.keys():
            self.string_var_dict[key].set('')
        self.case_notes_entry.delete(1.0, tk.END)

    def __setup_new_case_tab__(self):
        # define label objects
        first_name_label = tk.Label(
            self.tab_new_case, text='First Name')
        last_name_label = tk.Label(self.tab_new_case, text='Last Name')
        incident_date_label = tk.Label(self.tab_new_case, text='Incident Date')
        incident_type_label = tk.Label(self.tab_new_case, text='Incident Type')
        incident_location_label = tk.Label(
            self.tab_new_case, text='Incident Location')
        party_size_label = tk.Label(self.tab_new_case, text='Party Size')
        cause_of_death_label = tk.Label(
            self.tab_new_case, text='Cause of Death (if applicable)')
        referred_by_label = tk.Label(self.tab_new_case, text='Referred by')
        police_station_label = tk.Label(
            self.tab_new_case, text='Police Station')
        visitor_type_label = tk.Label(self.tab_new_case, text='Visitor Type')
        mma_label = tk.Label(self.tab_new_case, text='MMA (Major Market Area)')
        case_notes_label = tk.Label(self.tab_new_case, text='Case Notes')

        # define entry objects
        # create a dictionary to store the associated StringVar objects
        self.string_var_dict = dict()
        self.string_var_dict['first name'] = tk.StringVar()
        self.string_var_dict['last name'] = tk.StringVar()
        self.string_var_dict['incident type'] = tk.StringVar()
        self.string_var_dict['incident location'] = tk.StringVar()
        self.string_var_dict['party size'] = tk.StringVar()
        self.string_var_dict['cause of death'] = tk.StringVar()
        self.string_var_dict['referred by'] = tk.StringVar()
        self.string_var_dict['police station'] = tk.StringVar()
        self.string_var_dict['visitor type'] = tk.StringVar()
        self.string_var_dict['mma'] = tk.StringVar()

        first_name_entry = tk.Entry(
            self.tab_new_case, textvariable=self.string_var_dict['first name'])
        last_name_entry = tk.Entry(
            self.tab_new_case, textvariable=self.string_var_dict['last name'])
        self.incident_date_entry = tkcalendar.DateEntry(self.tab_new_case)
        incident_type_combobox = ttk.Combobox(
            self.tab_new_case, values=INCIDENT_TYPES, width=30, textvariable=self.string_var_dict['incident type'])
        incident_location_entry = tk.Entry(
            self.tab_new_case, textvariable=self.string_var_dict['incident location'])
        party_size_entry = tk.Entry(
            self.tab_new_case, textvariable=self.string_var_dict['party size'])
        cause_of_death_combobox = ttk.Combobox(
            self.tab_new_case, values=COD, textvariable=self.string_var_dict['cause of death'])
        referred_by_combobox = ttk.Combobox(
            self.tab_new_case, values=REFERRED, textvariable=self.string_var_dict['referred by'], width=25)
        police_station_combobox = ttk.Combobox(
            self.tab_new_case, values=POLICE_STATIONS, textvariable=self.string_var_dict['police station'])
        visitor_type_combobox = ttk.Combobox(
            self.tab_new_case, values=VISITOR_TYPE, textvariable=self.string_var_dict['visitor type'])
        mma_combobox = ttk.Combobox(
            self.tab_new_case, values=MMA, textvariable=self.string_var_dict['mma'], width=57)
        self.case_notes_entry = scrolledtext.ScrolledText(
            self.tab_new_case, width=60, height=10)

        def submit():
            # assemble a data dictionary
            data = dict()
            data['first name'] = self.string_var_dict['first name'].get()
            data['last name'] = self.string_var_dict['last name'].get()
            data['incident date'] = self.incident_date_entry.get()
            data['incident type'] = self.string_var_dict['incident type'].get()
            data['incident location'] = self.string_var_dict['incident location'].get()
            data['party size'] = self.string_var_dict['party size'].get()
            data['cause of death'] = self.string_var_dict['cause of death'].get()
            data['referred by'] = self.string_var_dict['referred by'].get()
            data['police station'] = self.string_var_dict['police station'].get()
            data['visitor type'] = self.string_var_dict['visitor type'].get()
            data['mma'] = self.string_var_dict['mma'].get()
            data['case notes'] = self.case_notes_entry.get(1.0, tk.END)
            last_check = Case_check(data, self)
            last_check.mainloop()

        submit = tk.Button(self.tab_new_case, text='Submit', command=submit)
        clear = tk.Button(self.tab_new_case, text='Clear',
                          command=self.clear_case)

        # setup each label, entry pair
        first_name_label.grid(column=0, row=0, padx=20, pady=10, sticky='W')
        first_name_entry.grid(column=1, row=0, sticky='W')

        last_name_label.grid(column=0, row=1, padx=20, pady=10, sticky='W')
        last_name_entry.grid(column=1, row=1, sticky='W')

        incident_date_label.grid(column=0, row=2, padx=20, pady=10, sticky='W')
        self.incident_date_entry.grid(column=1, row=2, sticky='W')

        incident_type_label.grid(column=0, row=3, padx=20, pady=10, sticky='W')
        incident_type_combobox.grid(column=1, row=3, sticky='W')

        incident_location_label.grid(
            column=0, row=4, padx=20, pady=10, sticky='W')
        incident_location_entry.grid(column=1, row=4, sticky='W')

        party_size_label.grid(column=0, row=5, padx=20, pady=10, sticky='W')
        party_size_entry.grid(column=1, row=5, sticky='W')

        cause_of_death_label.grid(
            column=0, row=6, padx=20, pady=10, sticky='W')
        cause_of_death_combobox.grid(column=1, row=6, sticky='W')

        referred_by_label.grid(column=0, row=7, padx=20, pady=10, sticky='W')
        referred_by_combobox.grid(column=1, row=7, sticky='W')

        police_station_label.grid(
            column=0, row=8, padx=20, pady=10, sticky='W')
        police_station_combobox.grid(column=1, row=8, sticky='W')

        visitor_type_label.grid(column=0, row=9, padx=20, pady=10, sticky='W')
        visitor_type_combobox.grid(column=1, row=9, sticky='W')

        mma_label.grid(column=0, row=10, padx=20, pady=10, sticky='W')
        mma_combobox.grid(column=1, row=10, sticky='W')

        case_notes_label.grid(column=0, row=11, padx=20, pady=10, sticky='W')
        self.case_notes_entry.grid(column=1, row=11, pady=10,
                                   sticky='W', columnspan=2)

        submit.grid(column=1, row=12)
        clear.grid(column=2, row=12)

    def __setup_search_tab__(self):
        def search():
            '''
            query the database, display the results in a Listbox
            '''
            def view(case: Cases):
                print(case)
                pass

            search_results = database_functions.search_case(
                self.category.get(), self.search_term.get())
            # create the listbox
            lb = Listbox(self.tab_search)
            for result, i in zip(search_results, range(1, len(search_results) + 1)):
                lb.insert(i, result)
            lb.grid(column=2, row=3)
            view_button = tk.Button(self.tab_search, text='View', command=view)
            view_button.grid(column=2, row=4)

        self.category = tk.StringVar()
        self.search_term = tk.StringVar()

        category_label = tk.Label(self.tab_search, text='Category')
        category_label.grid(column=0, row=0, padx=20, pady=10, sticky='W')

        category_combobox = ttk.Combobox(
            self.tab_search, values=SEARCH_CATEGORIES, width=25, textvariable=self.category)
        category_combobox.grid(column=1, row=0, sticky='W')

        search_term_label = tk.Label(self.tab_search, text='Search Term')
        search_term_label.grid(column=0, row=1, padx=20, sticky='W')

        search_term_entry = tk.Entry(
            self.tab_search, textvariable=self.search_term)
        search_term_entry.grid(column=1, row=1, sticky='W')

        search_button = tk.Button(
            self.tab_search, text='Search', command=search)
        search_button.grid(column=1, row=2, pady=10)
