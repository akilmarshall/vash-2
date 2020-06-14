import tkinter as tk
from tkinter import ttk
import datetime

PROGRAM_NAME = 'VASH Report Helper'
DAYS = list(range(1, 31))
CURRENT_DAY = datetime.datetime.now().day
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
CURRENT_MONTH = MONTHS[datetime.datetime.now().month - 1]
YEAR = datetime.datetime.now().year
YEARS = list(range(2019, YEAR + 1))
INCIDENT_TYPES = ['physical assault', 'sexual assault', 'automobile accident', 'automobile theft', 'burglary', 'court case', 'death', 'disorderly conduct', 'evacuation',
                  'lodging scam', 'lost', 'lost items', 'medical emergency', 'property damage', 'robbery', 'terroristic threatening', 'theft', 'unauthorized entry into motor vehicle']
COD = ['Automobile Accident', 'Homicide', 'Suicide',
       'Natural Cause/Illness', 'Water Related', 'Other']
MMA = [
    'U.S. Pacific and Mountain (AK, CA, OR, WA, AZ, CO, ID, MT, NV, UT, WY)', 'U.S. East (other contiguous states)', 'Japan', 'Canada', 'Europe (United Kingdom, Germany, France, Italy and Switzerland)', 'New Zealand', 'China', 'Korea', 'Taiwan', 'Other Asia (Hong Kong, Singapore, Malaysia, etc.)', 'Latin America (Argentina, Brazil and Mexico)', 'All Other Countries/Territories']
REFERRED = ['Airline/Airport', 'Car Rental Agency', 'County Police', 'Cruise Line', 'Hospital', 'Hotel', 'Non-Hotel Accommodation',
            'Other Agency', 'Other VAP Provider', 'Visitor Bureau', 'Tour/Travel Agency', 'Walk In/Direct', 'Volcano National Park', 'Pier']
POLICE_STATIONS = ['Honoka"a', 'Laupahoehoe', 'Hilo',
                   'Pahoa', 'Na"alehu', 'Kona', 'Waimea', 'Kapa"au']


class Root(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('VASH Report Helper')
        # form.geometry('800x800')
        self.geometry('800x800')

        self.tab_parent = ttk.Notebook(self)

        self.tab1 = ttk.Frame(self.tab_parent)
        self.tab2 = ttk.Frame(self.tab_parent)

        self.tab_parent.add(self.tab1, text='Home')
        self.tab_parent.add(self.tab2, text='New Case')

        self.tab_parent.pack(expand=1, fill='both')
        # self.label = tk.Label(
        #     self, text='VASH Report Helper Home', padx=5, pady=5)

        # self.label.pack()


# root = tk.Tk()
# root.title('VASH Report Helper')


# def myClick():
#     myLabel = tk.Label(root, text="Look! I clicked a Button!!")
#     myLabel.pack()


# myButton = tk.Button(root, text="Click Me!", command=myClick)
# myButton.pack()


# root.mainloop()

if __name__ == '__main__':
    root = Root()
    root.mainloop()

# form = tk.Tk()
# form.title('VASH Report Helper')
# form.geometry('800x800')

# tab_parent = ttk.Notebook(form)

# tab1 = ttk.Frame(tab_parent)
# tab2 = ttk.Frame(tab_parent)

# tab_parent.add(tab1, text='Home')
# tab_parent.add(tab2, text='New Case')

# tab_parent.pack(expand=1, fill='both')

# form.mainloop()


"""
def home():
    def new_report():
        layout = [
            [sg.Text('New Report')],
            [sg.Text('First Name', size=(15, 1)), sg.Input(key='first_name')],
            [sg.Text('Last Name', size=(15, 1)), sg.Input(key='last_name')],
            [sg.Text('Incident Date')],
            [sg.Text('Year'), sg.Drop(values=YEARS, readonly=True, auto_size_text=True, default_value=YEARS[-1], key='year'), sg.Text('Month'),
             sg.Drop(values=MONTHS, readonly=True, auto_size_text=True, default_value=CURRENT_MONTH, key='month'), sg.Text('Day'), sg.Drop(values=DAYS, readonly=True, auto_size_text=True, default_value=CURRENT_DAY, key='day')],
            [sg.Text('Incident Type'), sg.Drop(
                values=INCIDENT_TYPES, readonly=True, key='incident type', auto_size_text=True)],
            [sg.Text('Party Size', size=(15, 1)), sg.Drop(
                values=list(range(1, 11)), key='party size', auto_size_text=True)],
            [sg.Text('Cause of Death', size=(15, 1)),
             sg.Drop(values=COD, key='mma', readonly=True, auto_size_text=True)],
            [sg.Text('Incident Location'), sg.Input(key='incident location')],
            [sg.Text('Referred By'), sg.Drop(
                values=REFERRED, key='referred by', readonly=True)],
            [sg.Text('Police Station'), sg.Drop(
                values=POLICE_STATIONS, key='police station', readonly=True)],
            [sg.Text('Visitor Type'), sg.Drop(
                values=['land', 'cruise'], key='visitor type', readonly=True, auto_size_text=True)],
            [sg.Text('Place of Origin', size=(15, 1)), sg.Drop(
                values=MMA, readonly=True, auto_size_text=True)],
            [sg.Text('Notes', size=(15, 1)), sg.InputText(
                size=(100, 4), key='notes')],
            [sg.Submit(), sg.Cancel()]
        ]

        window = sg.Window('VASH Report Helper', layout)
        event, values = window.read()
        window.close()

    def find_report():
        categories = ['Name', 'Incident Location', 'Place of Origin']
        layout = [
            [sg.Text('Find Report')],
            [sg.Text('Category', size=(15, 1)), sg.Drop(
                values=categories, default_value=categories[0], readonly=True, auto_size_text=True)],
            [sg.Input(key='search term')],
            [sg.Button('Search', bind_return_key=True), sg.Cancel()],
        ]
        window = sg.Window('VASH Report Helper', layout)
        event, values = window.read()
        window.close()

    def get_monthly_report():
        months = ['January', 'February', 'March', 'April', 'May']
        layout = [
            [sg.Text('Get Monthly Report')],
            # [sg.FolderBrowse(button_text='Download to')],
            [sg.Drop(months, default_value=months[-1], readonly=True)],
            [sg.Button(button_text='Download'), sg.Cancel()],
        ]
        window = sg.Window('VASH Report Helper', layout)
        event, values = window.read()
        window.close()

    def get_annual_report():
        # TODO populate this list with valid years in the database
        years = ['2020', '2019', '2018']
        layout = [
            [sg.Text('Get Annual Report')],
            [sg.Text('Year', size=(15, 1)), sg.Drop(
                values=years, default_value=years[0], readonly=True, auto_size_text=True)],
            [sg.Button(button_text='Download'), sg.Cancel()],
        ]
        window = sg.Window('VASH Report Helper', layout)
        event, values = window.read()
        window.close()

    def advanced_options():
        def any_month():
            pass

        def month_range():
            pass

        def database_merge():
            pass

        def import_file():
            def import_excel():
                pass

            def import_database():
                pass

        events = {'Download any Month': any_month,
                  'Download by Range': month_range,
                  'Merge Database': database_merge,
                  'Import': import_file,
                  }
        layout = [[sg.Button(button_text='Download any Month', size=(20, 1))],
                  [sg.Button(
                      button_text='Download by Range', size=(20, 1))],
                  [sg.Button(button_text='Merge Database', size=(20, 1))],
                  [sg.Button(button_text='Import', size=(20, 1))],
                  [sg.CloseButton('Exit', size=(20, 1))],
                  ]
        window = sg.Window('VASH Report Helper : Advanced Options',
                           default_element_size=(40, 1),
                           grab_anywhere=False
                           ).layout(layout)
        while True:
            event, values = window.Read()
            if event in events:
                events[event]()
            else:
                break
        window.Close()

    def settings():
        name = 'Jill Doe'
        email = 'jdoe@vash.hawaii'
        download_location = '~/Desktop'

        layout = [
            [sg.Text('Settings')],
            [sg.Text('Name', size=(15, 1)),
             sg.Input(key='name', default_text=name)],
            [sg.Text('Email', size=(15, 1)),
             sg.Input(key='email', default_text=email)],
            [sg.FileBrowse(button_text='Download Location',
                           initial_folder=download_location)],
            [sg.OK(), sg.Cancel()]
        ]

        window = sg.Window('VASH Report Helper', layout)
        event, values = window.read()
        window.close()

    sg.ChangeLookAndFeel('SystemDefault')
    events = {'New Report': new_report,
              'Find Report': find_report,
              'Download Monthly Report': get_monthly_report,
              'Download Annual Report': get_annual_report,
              'Advanced Options': advanced_options,
              'Settings': settings,
              }
    layout = [[sg.Button(button_text='New Report', size=(20, 1))],
              [sg.Button(button_text='Find Report', size=(20, 1))],
              [sg.Button(button_text='Download Monthly Report', size=(20, 1))],
              [sg.Button(button_text='Download Annual Report', size=(20, 1))],
              [sg.Button(button_text='Advanced Options', size=(20, 1))],
              [sg.Button(button_text='Settings', size=(20, 1))],
              [sg.CloseButton('Exit', size=(20, 1))],

              ]
    window = sg.Window('VASH Report Helper',
                       default_element_size=(40, 1),
                       grab_anywhere=False
                       ).layout(layout)
    while True:
        event, values = window.Read()
        if event in events:
            events[event]()
        else:
            break
    window.Close()


def main():
    home()


if __name__ == '__main__':
    main()
"""
