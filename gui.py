from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox, Listbox
from tkinter import scrolledtext
import tkcalendar
from database import database_functions

PROGRAM_NAME = 'VASH Report Helper'
DAYS = list(range(1, 31))
CURRENT_DAY = datetime.now().day
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
CURRENT_MONTH = MONTHS[datetime.now().month - 1]
YEAR = datetime.now().year
YEARS = list(range(2019, YEAR + 1))
INCIDENT_TYPES = ['Physical Assault', 'Sexual Assault', 'Automobile Accident', 'Automobile Theft', 'Burglary', 'Court Case', 'Death', 'Disorderly Conduct', 'Evacuation',
                  'Lodging Scam', 'Lost', 'Lost Items', 'Medical Emergency', 'property Damage', 'Robbery', 'Terroristic Threatening', 'Theft', 'Unauthorized Entry into Motor Vehicle']
COD = ['Automobile Accident', 'Homicide', 'Suicide',
       'Natural Cause/Illness', 'Water Related', 'Other']
MMA = [
    'U.S. Pacific and Mountain (AK, CA, OR, WA, AZ, CO, ID, MT, NV, UT, WY)', 'U.S. East (other contiguous states)', 'Japan', 'Canada', 'Europe (United Kingdom, Germany, France, Italy and Switzerland)', 'New Zealand', 'China', 'Korea', 'Taiwan', 'Other Asia (Hong Kong, Singapore, Malaysia, etc.)', 'Latin America (Argentina, Brazil and Mexico)', 'All Other Countries/Territories']
REFERRED = ['Airline/Airport', 'Car Rental Agency', 'County Police', 'Cruise Line', 'Hospital', 'Hotel', 'Non-Hotel Accommodation',
            'Other Agency', 'Other VAP Provider', 'Visitor Bureau', 'Tour/Travel Agency', 'Walk In/Direct', 'Volcano National Park', 'Pier']
POLICE_STATIONS = ["Honoka'a", 'Laupahoehoe', 'Hilo',
                   'Pahoa', "Na'alehu", 'Kona', 'Waimea', "Kapa'au"]
VISITOR_TYPE = ['Land', 'Cruise']
SEARCH_CATEGORIES = ['first name', 'last name', 'incident type', 'incident location',
                     'party size', 'cause of death', 'referred by', 'police station', 'visitor type', 'mma', 'notes']


class Case_check(tk.Tk):
    def __init__(self, case_info: dict, root):
        def OK():
            # def ok_box():

            # TODO input validation
            messagebox.showinfo('Success', 'Case Recorded')
            database_functions.insert_case(case_info)
            root.clear_case()
            self.destroy()

        super().__init__()
        self.case_info = case_info
        self.geometry('600x800')
        self.title('Preview Window')

        first_name_label = tk.Label(self, text='First Name:')
        first_name_label.grid(column=0, row=0, padx=10, pady=10, sticky='W')

        first_name = tk.Label(self, text=case_info['first name'])
        first_name.grid(column=1, row=0, padx=10, pady=10, sticky='W')

        last_name_label = tk.Label(self, text='Last Name:')
        last_name_label.grid(column=0, row=1, padx=10, pady=10, sticky='W')

        last_name = tk.Label(self, text=case_info['last name'])
        last_name.grid(column=1, row=1, padx=10, pady=10, sticky='W')

        incident_date_label = tk.Label(self, text='Incident Date:')
        incident_date_label.grid(column=0, row=2, padx=10, pady=10, sticky='W')

        incident_date = tk.Label(self, text=case_info['incident date'])
        incident_date.grid(column=1, row=2, padx=10, pady=10, sticky='W')

        incident_type_label = tk.Label(self, text='Incident Type:')
        incident_type_label.grid(column=0, row=3, padx=10, pady=10, sticky='W')

        incident_type = tk.Label(self, text=case_info['incident type'])
        incident_type.grid(column=1, row=3, padx=10, pady=10, sticky='W')

        incident_location_label = tk.Label(self, text='Incident Location:')
        incident_location_label.grid(
            column=0, row=4, padx=10, pady=10, sticky='W')

        incident_location = tk.Label(self, text=case_info['incident location'])
        incident_location.grid(column=1, row=4, padx=10, pady=10, sticky='W')

        party_size_label = tk.Label(self, text='Party Size:')
        party_size_label.grid(
            column=0, row=5, padx=10, pady=10, sticky='W')

        party_size = tk.Label(self, text=case_info['party size'])
        party_size.grid(column=1, row=5, padx=10, pady=10, sticky='W')

        cod_label = tk.Label(self, text='Cause of Death:')
        cod_label.grid(
            column=0, row=6, padx=10, pady=10, sticky='W')

        cod = tk.Label(self, text=case_info['cause of death'])
        cod.grid(column=1, row=6, padx=10, pady=10, sticky='W')

        referred_label = tk.Label(self, text='Referred:')
        referred_label.grid(
            column=0, row=7, padx=10, pady=10, sticky='W')

        referred = tk.Label(self, text=case_info['referred by'])
        referred.grid(column=1, row=7, padx=10, pady=10, sticky='W')

        police_station_label = tk.Label(self, text='Police Station:')
        police_station_label.grid(
            column=0, row=8, padx=10, pady=10, sticky='W')

        police_station = tk.Label(self, text=case_info['police station'])
        police_station.grid(column=1, row=8, padx=10, pady=10, sticky='W')

        visitor_type_label = tk.Label(self, text='Visitor Type:')
        visitor_type_label.grid(
            column=0, row=9, padx=10, pady=10, sticky='W')

        visitor_type = tk.Label(self, text=case_info['visitor type'])
        visitor_type.grid(column=1, row=9, padx=10, pady=10, sticky='W')

        mma_label = tk.Label(self, text='MMA:')
        mma_label.grid(
            column=0, row=10, padx=10, pady=10, sticky='W')

        mma = tk.Label(self, text=case_info['mma'])
        mma.grid(column=1, row=10, padx=10, pady=10, sticky='W')

        notes_label = tk.Label(self, text='Notes:')
        notes_label.grid(
            column=0, row=11, padx=10, pady=10, sticky='W')

        notes = tk.Label(self, text=case_info['case notes'])
        notes.grid(column=1, row=11, padx=10, pady=10, sticky='W')

        ok_button = tk.Button(self, text='OK', command=OK)
        ok_button.grid(column=1, row=12)

        cancel_button = tk.Button(self, text='Back', command=self.destroy)
        cancel_button.grid(column=2, row=12)


class Root(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('VASH Report Helper')

        # define the intial size of the window
        self.geometry('800x800')

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
            self.tab_new_case, width=70, height=10)

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
            pass

        category = tk.StringVar()
        search_term = tk.StringVar()

        category_label = tk.Label(self.tab_search, text='Category')
        category_label.grid(column=0, row=0, padx=20, pady=10, sticky='W')

        category_combobox = ttk.Combobox(
            self.tab_search, values=SEARCH_CATEGORIES, width=25, textvariable=category)
        category_combobox.grid(column=1, row=0, sticky='W')

        search_term_label = tk.Label(self.tab_search, text='Search Term')
        search_term_label.grid(column=0, row=1, padx=20, sticky='W')

        search_term_entry = tk.Entry(self.tab_search, textvariable=search_term)
        search_term_entry.grid(column=1, row=1, sticky='W')

        search_button = tk.Button(
            self.tab_search, text='Search', command=search)
        search_button.grid(column=1, row=2, pady=10)


if __name__ == '__main__':
    root = Root()
    root.mainloop()
