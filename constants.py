file_path = './DATA/Prijave 3.11..xlsx'
sheet_name = 'Form Responses 1'
column_dict = {'Timestamp':'VRIJEME', 'Ime i prezime': 'IME', 'Škola/fakultet': 'SKOLA', 'Razred':'RAZRED', 'Lokacije koje ti odgovaraju (sve lokacije na koje možeš dolaziti)': 'LOKACIJA', 'Iz kojih područja primarno želiš davati instrukcije?': 'PREDMET', 'Koji termin ti odgovara?': 'TERMIN', 'Broj mobitela (za WhatsApp grupu)': 'BROJ'}
locations = ['Trešnjevka', 'Peščenica', 'Špansko']
school_tuples = [('MIOC', 'mioc', 'xv'), ('PŠVP', 'pšvp', 'ps', 'vla'), ('KGZ', 'kla', 'kgz'), ('GTB', 'gtb', 'tit'), ('GLV', 'glv', 'luc'), ('III.', 'iii', 'III', '3. gim')]
subjects = ['matematika', 'jezici', 'prirodoslovni']
availabilities = ['utorak', 'četvrtak', 'nijedno']

reading_arguments = [file_path, sheet_name, column_dict, locations, school_tuples, subjects, availabilities]

font_ticks = {'family': 'DejaVu Sans', 'size': 14}
font_labels = {'family': 'DejaVu Sans', 'size': 22}
font_titles = {'family': 'DejaVu Sans', 'size': 24}

font_dict = {'tick': font_ticks, 'label': font_labels, 'title': font_titles}

colors = ['lightblue', 'lightgreen', 'salmon', '#FFCC80', 'purple']