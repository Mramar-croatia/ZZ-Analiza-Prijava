import pandas as pd
import tkinter as tk
from tkinter import messagebox

class GenderSurveyApp:
    
    def __init__(self, master, names):
        
        self.master = master
        self.names = names
        self.index = 0
        
        self.label = tk.Label(master, text=f"{self.names[self.index].split()[0]}")
        self.label.pack(pady=20)
        
        self.button_male = tk.Button(master, text="M", command=self.record_male)
        self.button_male.pack(side=tk.LEFT, padx=20)
        
        self.button_female = tk.Button(master, text="Ž", command=self.record_female)
        self.button_female.pack(side=tk.RIGHT, padx=20)
        
        self.button_none = tk.Button(master, text="N", command=self.record_none)
        self.button_none.pack(side=tk.RIGHT, padx=60)
        
    def record_male(self):
        self.record_gender('M')
    
    def record_female(self):
        self.record_gender('Ž')
        
    def record_none(self):
        self.record_gender('N')
    
    def record_gender(self, gender):
        
        global name_dict
        
        name_dict['IME'].append(self.names[self.index])
        name_dict['SPOL'].append(gender)
        
        self.index += 1
        
        if self.index < len(self.names):
            self.label.config(text=f"{self.names[self.index].split()[0]}")
        else:
            messagebox.showinfo("Done", "All names have been classified.")
            self.master.quit()

def new_save_genders(file_path: str) -> pd.DataFrame:
    try:
        
        df = pd.read_excel(file_path)
        
        root = tk.Tk()
        root.title("Gender Classification Survey")
            
        imena = df['IME'].tolist()
            
        app = GenderSurveyApp(root, imena)

        name_dict = {'IME': [], 'SPOL': []}
            
        root.mainloop()
        
        name_df = pd.DataFrame(name_dict)

        name_df.to_csv('imena_spolovi.csv', index=False)
        
    except Exception as e:
        
        tk.messagebox.showerror('Error', f'Error while loading the file: {e}')
        return pd.DataFrame
    
def load_genders() -> pd.DataFrame:
    try:
        
        df = pd.read_csv('imena_spolovi.csv')
        
        return df
    
    except Exception as e:
        
        tk.messagebox.showerror('Error', f'Error while loading the file: {e}')
        
        return pd.DataFrame