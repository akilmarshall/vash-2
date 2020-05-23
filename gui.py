import PySimpleGUI as sg


def home():
    def new_report():
        layout = [
            [sg.Text('New Report', justification='center')],
            [sg.Text('Name', size=(15, 1)), sg.Input(key='name')],
            [sg.Text('Address', size=(15, 1)), sg.Input(key='address')],
            [sg.Text('Phone', size=(15, 1)), sg.Input(key='phone')],
            [sg.Submit(), sg.Cancel()]
        ]

        window = sg.Window('VASH Report Helper', layout)
        event, values = window.read()
        window.close()
        # print(f'{values["name"]} {values["address"]} {values["phone"]}')

    def find_report():
        categories = ['Name', 'Incident Location', 'Place of Origin']
        layout = [
            [sg.Text('Find Report', justification='center')],
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
            [sg.Text('Get Monthly Report', justification='center')],
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
            [sg.Text('Get Annual Report', justification='center')],
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
        pass

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
