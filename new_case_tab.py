import tkinter as tk
from tkinter import ttk, messagebox, Listbox
from tkinter import scrolledtext
import tkcalendar
from constants import *
from database import database_functions, tables

from collections import namedtuple

Form_Data = namedtuple('Form_Data', ['first_name'])

'''
def New_Case(root):
    # define label objects
    first_name_label = tk.Label(root, text='First Name')
    # last_name_label = tk.Label(root, text='Last Name')
    # incident_date_label = tk.Label(root, text='Incident Date')
    # incident_type_label = tk.Label(root, text='Incident Type')
    # incident_location_label = tk.Label(root, text='Incident Location')
    # party_size_label = tk.Label(root, text='Party Size')
    # cause_of_death_label = tk.Label(
    #     root, text='Cause of Death (if applicable)')
    # referred_by_label = tk.Label(root, text='Referred by')
    # police_station_label = tk.Label(root, text='Police Station')
    # visitor_type_label = tk.Label(root, text='Visitor Type')
    # mma_label = tk.Label(root, text='MMA (Major Market Area)')
    # case_notes_label = tk.Label(root, text='Case Notes')

    # define entry objects
    # create a dictionary to store the associated StringVar objects
    string_var_dict = dict()
    string_var_dict['first name'] = tk.StringVar()
    string_var_dict['last name'] = tk.StringVar()
    string_var_dict['incident type'] = tk.StringVar()
    string_var_dict['incident location'] = tk.StringVar()
    string_var_dict['party size'] = tk.StringVar()
    string_var_dict['cause of death'] = tk.StringVar()
    string_var_dict['referred by'] = tk.StringVar()
    string_var_dict['police station'] = tk.StringVar()
    string_var_dict['visitor type'] = tk.StringVar()
    string_var_dict['mma'] = tk.StringVar()

    first_name_entry = tk.Entry(
        root, textvariable=string_var_dict['first name'])
    # last_name_entry = tk.Entry(
    #     root, textvariable=string_var_dict['last name'])
    # incident_date_entry = tkcalendar.DateEntry(master=root)
    # incident_type_combobox = ttk.Combobox(
    #     root, values=INCIDENT_TYPES, width=30, textvariable=string_var_dict['incident type'])
    # incident_location_entry = tk.Entry(
    #     root, textvariable=string_var_dict['incident location'])
    # party_size_entry = tk.Entry(
    #     root, textvariable=string_var_dict['party size'])
    # cause_of_death_combobox = ttk.Combobox(
    #     root, values=COD, textvariable=string_var_dict['cause of death'])
    # referred_by_combobox = ttk.Combobox(
    #     root, values=REFERRED, textvariable=string_var_dict['referred by'], width=25)
    # police_station_combobox = ttk.Combobox(
    #     root, values=POLICE_STATIONS, textvariable=string_var_dict['police station'])
    # visitor_type_combobox = ttk.Combobox(
    #     root, values=VISITOR_TYPE, textvariable=string_var_dict['visitor type'])
    # mma_combobox = ttk.Combobox(
    #     root, values=MMA, textvariable=string_var_dict['mma'], width=57)
    # case_notes_entry = scrolledtext.ScrolledText(
    #     root, width=60, height=10)

    def submit():
        # assemble a data dictionary
        data = dict()
        data['first name'] = string_var_dict['first name'].get()
        data['last name'] = string_var_dict['last name'].get()
        data['incident date'] = incident_date_entry.get()
        data['incident type'] = string_var_dict['incident type'].get()
        data['incident location'] = string_var_dict['incident location'].get()
        data['party size'] = string_var_dict['party size'].get()
        data['cause of death'] = string_var_dict['cause of death'].get()
        data['referred by'] = string_var_dict['referred by'].get()
        data['police station'] = string_var_dict['police station'].get()
        data['visitor type'] = string_var_dict['visitor type'].get()
        data['mma'] = string_var_dict['mma'].get()
        data['case notes'] = case_notes_entry.get(1.0, tk.END)
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
        case_notes_entry.grid(column=1, row=11, pady=10,
                              sticky='W', columnspan=2)

        submit.grid(column=1, row=12)
        clear.grid(column=2, row=12)
        '''


def clear_form_data(form_data):
    # form_data.first_name.set('')
    print(dir(form_data.first_name))
    print(type(form_data.first_name))


class Case_check(tk.Tk):
    '''A widget to verify the information entered in the new case tab before committing to the database.'''

    # def __init__(self, case_info: dict, root):
    def __init__(self, form_data):
        # form_data is of the data type namedtuple Form_Data
        def OK():
            # def ok_box():

            # TODO input validation
            messagebox.showinfo('Success', 'Case Recorded')
            # database_functions.insert_case(case_info)
            # root.clear_case()
            clear_form_data(form_data)
            self.destroy()

        super().__init__()
        # self.case_info = case_info
        self.geometry('400x600')
        self.title('Preview Window')

        first_name_label = tk.Label(self, text='First Name:')
        first_name_label.grid(column=0, row=0, padx=10, pady=10, sticky='W')

        # first_name = tk.Label(self, text=form_data.first_name.get())
        # first_name.grid(column=1, row=0, padx=10, pady=10, sticky='W')

        # last_name_label = tk.Label(self, text='Last Name:')
        # last_name_label.grid(column=0, row=1, padx=10, pady=10, sticky='W')

        # last_name = tk.Label(self, text=case_info['last name'])
        # last_name.grid(column=1, row=1, padx=10, pady=10, sticky='W')

        # incident_date_label = tk.Label(self, text='Incident Date:')
        # incident_date_label.grid(column=0, row=2, padx=10, pady=10, sticky='W')

        # incident_date = tk.Label(self, text=case_info['incident date'])
        # incident_date.grid(column=1, row=2, padx=10, pady=10, sticky='W')

        # incident_type_label = tk.Label(self, text='Incident Type:')
        # incident_type_label.grid(column=0, row=3, padx=10, pady=10, sticky='W')

        # incident_type = tk.Label(self, text=case_info['incident type'])
        # incident_type.grid(column=1, row=3, padx=10, pady=10, sticky='W')

        # incident_location_label = tk.Label(self, text='Incident Location:')
        # incident_location_label.grid(
        #     column=0, row=4, padx=10, pady=10, sticky='W')

        # incident_location = tk.Label(self, text=case_info['incident location'])
        # incident_location.grid(column=1, row=4, padx=10, pady=10, sticky='W')

        # party_size_label = tk.Label(self, text='Party Size:')
        # party_size_label.grid(
        #     column=0, row=5, padx=10, pady=10, sticky='W')

        # party_size = tk.Label(self, text=case_info['party size'])
        # party_size.grid(column=1, row=5, padx=10, pady=10, sticky='W')

        # cod_label = tk.Label(self, text='Cause of Death:')
        # cod_label.grid(
        #     column=0, row=6, padx=10, pady=10, sticky='W')

        # cod = tk.Label(self, text=case_info['cause of death'])
        # cod.grid(column=1, row=6, padx=10, pady=10, sticky='W')

        # referred_label = tk.Label(self, text='Referred:')
        # referred_label.grid(
        #     column=0, row=7, padx=10, pady=10, sticky='W')

        # referred = tk.Label(self, text=case_info['referred by'])
        # referred.grid(column=1, row=7, padx=10, pady=10, sticky='W')

        # police_station_label = tk.Label(self, text='Police Station:')
        # police_station_label.grid(
        #     column=0, row=8, padx=10, pady=10, sticky='W')

        # police_station = tk.Label(self, text=case_info['police station'])
        # police_station.grid(column=1, row=8, padx=10, pady=10, sticky='W')

        # visitor_type_label = tk.Label(self, text='Visitor Type:')
        # visitor_type_label.grid(
        #     column=0, row=9, padx=10, pady=10, sticky='W')

        # visitor_type = tk.Label(self, text=case_info['visitor type'])
        # visitor_type.grid(column=1, row=9, padx=10, pady=10, sticky='W')

        # mma_label = tk.Label(self, text='MMA:')
        # mma_label.grid(
        #     column=0, row=10, padx=10, pady=10, sticky='W')

        # mma = tk.Label(self, text=case_info['mma'])
        # mma.grid(column=1, row=10, padx=10, pady=10, sticky='W')

        # notes_label = tk.Label(self, text='Notes:')
        # notes_label.grid(
        #     column=0, row=11, padx=10, pady=10, sticky='W')

        # notes = tk.Label(self, text=case_info['case notes'])
        # notes.grid(column=1, row=11, padx=10, pady=10, sticky='W')

        ok_button = tk.Button(self, text='OK', command=OK)
        ok_button.grid(column=1, row=12)

        cancel_button = tk.Button(self, text='Back', command=self.destroy)
        cancel_button.grid(column=2, row=12)


def New_case_tab(root):
    def submit(text_vars):
        verify_window = Case_check(text_vars)
        verify_window.mainloop()

    form_data = Form_Data(tk.StringVar)

    first_name_label = tk.Label(root, text='First Name')
    first_name_entry = tk.Entry(root, textvariable=form_data.first_name)

    first_name_label.grid(column=0, row=0, padx=20, pady=20)
    first_name_entry.grid(column=1, row=0, padx=20, pady=20)

    submit_button = tk.Button(
        root, text='Submit', command=lambda: submit(form_data))
    submit_button.grid(column=0, row=2)

    clear = tk.Button(root, text='Clear',
                      command=lambda: clear_form_data(form_data))
    clear.grid(column=1, row=2)


if __name__ == '__main__':
    root = tk.Tk()
    New_case_tab(root)
    root.mainloop()
