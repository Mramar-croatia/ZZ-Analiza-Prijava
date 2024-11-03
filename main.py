import pandas as pd

from ORGANIZERS import organizer as org
import constants as const

import ANALYZERS.graphers as gra
import ANALYZERS.complex_graphers as cgra
import gender_loader as gl

df = org.process_xls(*const.reading_arguments)

gra.graph_razred(df, './RESULTS/')
gra.graph_skola(df, './RESULTS/')
gra.graph_lokacija(df, './RESULTS/')
gra.graph_termin(df, './RESULTS/')
gra.graph_predmet(df, './RESULTS/')
gra.graph_gender(gl.load_genders(), './RESULTS/')

cgra.graph_lokacije_pie(df, './RESULTS/')
cgra.graph_time_distribution_skole(df, './RESULTS/')
cgra.graph_time_distribution_general(df, './RESULTS/')