import PySimpleGUI as sg


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
    # the input data looks like a simple list when auto numbered
    print(f'{values["name"]} {values["address"]} {values["phone"]}')


def find_report():
    categories = ['Name', 'Incident Location', 'Place of Origin']
    layout = [
        [sg.Text('Find Report', justification='center')],
        [sg.Text('Category', size=(15, 1)), sg.Drop(
            values=categories, default_value=categories[0], readonly=True, auto_size_text=True)],
        [sg.Input(key='search term'), sg.Button(
            'Search', bind_return_key=True)],
        [sg.Cancel()],
    ]
    window = sg.Window('VASH Report Helper', layout)
    event, values = window.read()
    window.close()


def get_monthly_report():
    months = ['January', 'Feburary', 'March', 'April', 'May']
    layout = [
        [sg.Text('Get Monthly Report', justification='center')],
        # [sg.FolderBrowse(button_text='Download to')],
        [sg.Drop(months, default_value=months[-1], readonly=True)],
        [sg.Button(button_text='Download'), sg.Cancel()],
    ]
    window = sg.Window('VASH Report Helper', layout)
    event, values = window.read()
    window.close()


def get_yearly_report():
    # TODO populate this list with valid years in the database
    years = ['2020', '2019', '2018']
    layout = [
        [sg.Text('Find Report', justification='center')],
        [sg.Text('Year', size=(15, 1)), sg.Drop(
            values=years, default_value=years[0], readonly=True, auto_size_text=True)],
        [sg.Button(button_text='Download'), sg.Cancel()],
    ]
    window = sg.Window('VASH Report Helper', layout)
    event, values = window.read()
    window.close()


def advanced_options():
    pass


def home():
    sg.ChangeLookAndFeel('SystemDefault')
    events = {'New Report': new_report,
              'Find Report': find_report,
              'Download Monthly Report': get_monthly_report,
              'Download Yearly Report': get_yearly_report,
              'Advanced Options': advanced_options,
              }
    layout = [[sg.Button(button_text='New Report', size=(20, 1))],
              [sg.Button(button_text='Find Report', size=(20, 1))],
              [sg.Button(button_text='Download Monthly Report', size=(20, 1))],
              [sg.Button(button_text='Download Yearly Report', size=(20, 1))],
              [sg.Button(button_text='Advanced Options', size=(20, 1))],
              [sg.CloseButton('Exit', size=(20, 1))],

              ]
    window = sg.Window('VASH Report Helper',
                       default_element_size=(40, 1),
                       # font = ('Helvetica', 18, 'bold'),
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
