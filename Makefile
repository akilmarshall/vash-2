: root.ui
	pyuic5 -x root.ui -o gui.py

gui: gui.py
	 python gui.py

exe: gui.py
	pyinstaller --name "VASH Report Helper" --windowed --onefile gui.py
