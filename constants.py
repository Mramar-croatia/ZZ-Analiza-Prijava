file_path = './DATA/Prijave 23.10..xlsx'
sheet_name = 'Form Responses 1'
column_dict = {'Timestamp':'VRIJEME', 'Ime i prezime': 'IME', 'Škola/fakultet': 'SKOLA', 'Razred':'RAZRED', 'Lokacija': 'LOKACIJA', 'Iz kojih područja primarno želiš davati instrukcije?': 'PREDMET', 'Lokacije koje ti odgovaraju (sve lokacije na koje možeš dolaziti)': 'TERMIN', 'Broj mobitela (za WhatsApp grupu)': 'BROJ'}
locations = ['Trešnjevka', 'Peščenica', 'Špansko']
school_tuples = [('MIOC', 'mioc', 'xv'), ('PŠVP', 'pšvp', 'ps', 'vla'), ('KGZ', 'kla', 'kgz'), ('GTB', 'gtb', 'tit'), ('GLV', 'glv', 'luc')]
subjects = ['matematika', 'jezici', 'prirodoslovni']
availabilities = ['utorak', 'četvrtak', 'nijedno']

reading_arguments = [file_path, sheet_name, column_dict, locations, school_tuples, subjects, availabilities]

font_ticks = {'family': 'DejaVu Sans', 'size': 14}
font_labels = {'family': 'DejaVu Sans', 'size': 22}
font_titles = {'family': 'DejaVu Sans', 'size': 24}

font_dict = {'tick': font_ticks, 'label': font_labels, 'title': font_titles}

colors = ['lightblue', 'lightgreen', 'salmon', '#FFCC80', 'purple']