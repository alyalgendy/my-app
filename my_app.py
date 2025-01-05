from customtkinter import *


# Create the main app
app = CTk()
app.title("Chemical Calculations")
app.geometry('700x700')

# Function to reset the screen to the initial state
def reset_screen(theme_switch=None):
    # Clear the app
    for widget in app.winfo_children():
        widget.destroy()

    # Add theme switch
    theme_switch = CTkSwitch(
        master=app, 
        text="Light Mode", 
        command=lambda: toggle_theme(theme_switch), 
        onvalue="dark", 
        offvalue="light"
    )
    theme_switch.place(relx=0.9, rely=0.1, anchor="center")

    # Title CTkLabel
    lbl = CTkLabel(
        master=app, 
        text="Let's Solve Chemistry", 
        font=("Times New Roman", 50)
    )
    lbl.place(relx=0.5, rely=0.3, anchor="center")

    # Begin CTkButton
    btn = CTkButton(
        master=app, 
        text="Begin", 
        font=("Arial", 16), 
        corner_radius=32,
        command=begin
    )
    btn.place(relx=0.5, rely=0.5, anchor="center")


# Set the theme to green
set_appearance_mode("green")

# Function to toggle theme
def toggle_theme(theme_switch):
    if appearance_mode == "light":
        set_appearance_mode("dark")
        theme_switch.configure(text="Dark Mode")
    else:
        set_appearance_mode("light")
        theme_switch.configure(text="Light Mode")

# Set the initial theme to light
appearance_mode = "light"
set_appearance_mode(appearance_mode)
# Function to toggle theme
def toggle_theme(theme_switch):
    global appearance_mode
    if appearance_mode == "light":
        set_appearance_mode("dark")
        theme_switch.configure(text="Dark Mode")
        appearance_mode = "dark"
    else:
        set_appearance_mode("light")
        theme_switch.configure(text="Light Mode")
        appearance_mode = "light"

# Function to handle the "begin" CTkButton
def begin():
    # Clear the app for the new screen
    for widget in app.winfo_children():
        widget.destroy()

    # CTkLabel
    lbl = CTkLabel(
        app, 
        text="Choose what you want to calculate!", 
        font=("Andalus", 30)
    )
    lbl.place(relx=0.5, rely=0.1, anchor="center")

    # Limiting Reactant CTkButton
    btn_lim_reac = CTkButton(
        app, 
        text="Limiting Reactant", 
        font=("Arial", 16), 
        command=limreac
    )
    btn_lim_reac.place(relx=0.5, rely=0.3, anchor="center")

    # Number of Moles CTkButton
    btn_num_mole = CTkButton(
        app, 
        text="Number of moles", 
        font=("Arial", 16), 
        command=MoleNo
    )
    btn_num_mole.place(relx=0.5, rely=0.4, anchor="center")

    # Solution Concentration CTkButton
    btn_Sol_con = CTkButton(
        app,
        text="Solution Concentration",
        font=("Arial", 16), 
        command=Solcon
    )
    btn_Sol_con.place(relx=0.5, rely=0.5, anchor="center")

    # Back CTkButton
    btn_back = CTkButton(
        app, 
        text="Back", 
        font=("Arial", 16), 
        command=reset_screen
    )
    btn_back.place(relx=0.5, rely=0.6, anchor="center")

# Function to handle limiting reactant calculation
def limreac():
    # Clear the app for new inputs
    for widget in app.winfo_children():
        widget.destroy()

    # Calculate Function
    def calculate():
        try:
            # Get input values
            a_coefficient = int(entry_a_coeff.get())
            mass_a = float(entry_mass_a.get())
            momass_a = float(entry_momass_a.get())
            b_coefficient = int(entry_b_coeff.get())
            mass_b = float(entry_mass_b.get())
            momass_b = float(entry_momass_b.get())

            # Perform calculations
            x_a = mass_a / momass_a / a_coefficient
            x_b = mass_b / momass_b / b_coefficient

            if x_a > x_b:
                rem_mass = (x_a - x_b) * a_coefficient * momass_a
                result_lbl.configure(
                    text=f"B is the limiting reactant. Remaining mass of A: {rem_mass:.2f}"
                )
            elif x_b > x_a:
                rem_mass = (x_b - x_a) * b_coefficient * momass_b
                result_lbl.configure(
                    text=f"A is the limiting reactant. Remaining mass of B: {rem_mass:.2f}"
                )
            else:
                result_lbl.configure(text="There is no limiting reactant.")
        except ValueError:
            result_lbl.configure(text="Invalid input. Please enter numeric values.")

    # Input Fields and CTkLabels
    inputs = [
        ("Coefficient of Reactant A:", 0.1),
        ("Mass of Reactant A:", 0.2),
        ("Molar Mass of Reactant A:", 0.3),
        ("Coefficient of Reactant B:", 0.4),
        ("Mass of Reactant B:", 0.5),
        ("Molar Mass of Reactant B:", 0.6),
    ]

    entries = []
    for text, rely in inputs:
        CTkLabel(app, text=text, font=("Arial", 14)).place(relx=0.3, rely=rely, anchor="e")
        entry = CTkEntry(app, font=("Arial", 14))
        entry.place(relx=0.5, rely=rely, anchor="center")
        entries.append(entry)

    entry_a_coeff, entry_mass_a, entry_momass_a, entry_b_coeff, entry_mass_b, entry_momass_b = entries

    # Calculate CTkButton
    calculate_btn = CTkButton(
        app, 
        text="Calculate", 
        font=("Arial", 16), 
        command=calculate
    )
    calculate_btn.place(relx=0.5, rely=0.7, anchor="center")

    # CTkLabel to display results
    result_lbl = CTkLabel(app, text="", font=("Arial", 14))
    result_lbl.place(relx=0.5, rely=0.8, anchor="center")

    # Back CTkButton
    back_btn = CTkButton(
        app, 
        text="Back", 
        font=("Arial", 16), 
        command=begin
    )
    back_btn.place(relx=0.5, rely=0.9, anchor="center")

# Function to handle Number Of Moles calculation
def MoleNo():
    # Clear the app for new inputs
    for widget in app.winfo_children():
        widget.destroy()

    # Calculate Function
    def calculate():
        try:
            # Get input values
            mass = float(entry_mass_a.get())
            momass = float(entry_momass_a.get())

            # Perform calculations
            NoMoles = mass / momass
            result_lbl.configure(text=f"The number of moles is: {NoMoles:.2f}")

        except ValueError:
            result_lbl.configure(text="Invalid input. Please enter numeric values.")

    # Input Fields and CTkLabels
    inputs = [
        ("Mass:", 0.3),
        ("Molar Mass:", 0.4),
    ]

    entries = []
    for text, rely in inputs:
        CTkLabel(app, text=text, font=("Arial", 14)).place(relx=0.3, rely=rely, anchor="e")
        entry = CTkEntry(app, font=("Arial", 14))
        entry.place(relx=0.5, rely=rely, anchor="center")
        entries.append(entry)

    entry_mass_a, entry_momass_a = entries

    # Calculate CTkButton
    calculate_btn = CTkButton(
        app, 
        text="Calculate", 
        font=("Arial", 16), 
        command=calculate
    )
    calculate_btn.place(relx=0.5, rely=0.6, anchor="center")

    # CTkLabel to display results
    result_lbl = CTkLabel(app, text="", font=("Arial", 14))
    result_lbl.place(relx=0.5, rely=0.7, anchor="center")

    # Back CTkButton
    back_btn = CTkButton(
        app, 
        text="Back", 
        font=("Arial", 16), 
        command=begin
    )
    back_btn.place(relx=0.5, rely=0.8, anchor="center")

def Solcon():
    for widget in app.winfo_children():
        widget.destroy()
    
    # CTkLabel
    lbl = CTkLabel(
        app, 
        text="Choose a way!", 
        font=("Andalus", 30)
    )
    lbl.place(relx=0.5, rely=0.1, anchor="center")

    #Molarity CTkButton
    btn_molarity=CTkButton(
        app,
        text="Molarity",
        font=("Arial", 16),
        command=Molarity
    )
    btn_molarity.place(relx=0.5, rely=0.3, anchor="center")

    #Molality CTkButton
    btn_molality=CTkButton(
        app,
        text="Molality",
        font=("Arial", 16),
        command=Molality
    )
    btn_molality.place(relx=0.5, rely=0.4, anchor="center")

    #Normality CTkButton
    btn_norrmality=CTkButton(
        app,
        text="Normality",
        font=("Arial", 16),
        command=Normality
    )
    btn_norrmality.place(relx=0.5, rely=0.5, anchor="center")

    # Back CTkButton
    back_btn = CTkButton(
        app, 
        text="Back", 
        font=("Arial", 16), 
        command=begin
    )
    back_btn.place(relx=0.5, rely=0.6, anchor="center")

# Function to handle Molarity calculation
def Molarity():
    # Clear the app for new inputs
    for widget in app.winfo_children():
        widget.destroy()

    # Calculate Function
    def calculate():
        try:
            # Get input values
            Molsolute = float(entry_molsolute.get())
            volume = float(entry_volume.get())

            # Perform calculations
            Molarity = Molsolute / volume
            result_lbl.configure(text=f"The Molarity is: {Molarity:.2f}")

        except ValueError:
            result_lbl.configure(text="Invalid input. Please enter numeric values.")

    # Input Fields and CTkLabels
    inputs = [
        ("Moles of Solute:", 0.3),
        ("Volume in litre:", 0.4),
    ]

    entries = []
    for text, rely in inputs:
        CTkLabel(app, text=text, font=("Arial", 14)).place(relx=0.3, rely=rely, anchor="e")
        entry = CTkEntry(app, font=("Arial", 14))
        entry.place(relx=0.5, rely=rely, anchor="center")
        entries.append(entry)

    entry_molsolute, entry_volume = entries

    # Calculate CTkButton
    calculate_btn = CTkButton(
        app, 
        text="Calculate", 
        font=("Arial", 16), 
        command=calculate
    )
    calculate_btn.place(relx=0.5, rely=0.6, anchor="center")

    # CTkLabel to display results
    result_lbl = CTkLabel(app, text="", font=("Arial", 14))
    result_lbl.place(relx=0.5, rely=0.7, anchor="center")

    # Back CTkButton
    back_btn = CTkButton(
        app, 
        text="Back", 
        font=("Arial", 16), 
        command=Solcon
    )
    back_btn.place(relx=0.5, rely=0.8, anchor="center")

# Function to handle Number Of Moles calculation
def Molality():
    # Clear the app for new inputs
    for widget in app.winfo_children():
        widget.destroy()

    # Calculate Function
    def calculate():
        try:
            # Get input values
            molsolute = float(entry_molsolute.get())
            massolvant = float(entry_massolvant.get())

            # Perform calculations
            Molality = molsolute / massolvant
            result_lbl.configure(text=f"The Molality is: {Molality:.2f}")

        except ValueError:
            result_lbl.configure(text="Invalid input. Please enter numeric values.")

    # Input Fields and CTkLabels
    inputs = [
        ("Moles of solute:", 0.3),
        ("Mass of solvent in Kg:", 0.4),
    ]

    entries = []
    for text, rely in inputs:
        CTkLabel(app, text=text, font=("Arial", 14)).place(relx=0.3, rely=rely, anchor="e")
        entry = CTkEntry(app, font=("Arial", 14))
        entry.place(relx=0.5, rely=rely, anchor="center")
        entries.append(entry)

    entry_molsolute, entry_massolvant = entries

    # Calculate CTkButton
    calculate_btn = CTkButton(
        app, 
        text="Calculate", 
        font=("Arial", 16), 
        command=calculate
    )
    calculate_btn.place(relx=0.5, rely=0.6, anchor="center")

    # CTkLabel to display results
    result_lbl = CTkLabel(app, text="", font=("Arial", 14))
    result_lbl.place(relx=0.5, rely=0.7, anchor="center")

    # Back CTkButton
    back_btn = CTkButton(
        app, 
        text="Back", 
        font=("Arial", 16), 
        command=Solcon
    )
    back_btn.place(relx=0.5, rely=0.8, anchor="center")

# Function to handle Number Of Moles calculation
def Normality():
    # Clear the app for new inputs
    for widget in app.winfo_children():
        widget.destroy()

    # Calculate Function
    def calculate():
        try:
            # Get input values
            Molsolute = float(entry_molsolute.get())
            Eqsolute = float(entry_Eqsolute.get())
            volume = float(entry_volume.get())

            # Perform calculations
            Normality = Molsolute * Eqsolute / volume
            result_lbl.configure(text=f"The Normality is: {Normality:.2f}")

        except ValueError:
            result_lbl.configure(text="Invalid input. Please enter numeric values.")

    # Input Fields and CTkLabels
    inputs = [
        ("Moles of Solute:", 0.3),
        ("Number Of equivalents (Moles of electrons):", 0.4),
        ("Volume in litre:", 0.5),
    ]

    entries = []
    for text, rely in inputs:
        CTkLabel(app, text=text, font=("Arial", 14)).place(relx=0.3, rely=rely, anchor="e")
        entry = CTkEntry(app, font=("Arial", 14))
        entry.place(relx=0.5, rely=rely, anchor="center")
        entries.append(entry)

    entry_molsolute, entry_Eqsolute, entry_volume = entries

    # Calculate CTkButton
    calculate_btn = CTkButton(
        app, 
        text="Calculate", 
        font=("Arial", 16), 
        command=calculate
    )
    calculate_btn.place(relx=0.5, rely=0.6, anchor="center")

    # CTkLabel to display results
    result_lbl = CTkLabel(app, text="", font=("Arial", 14))
    result_lbl.place(relx=0.5, rely=0.7, anchor="center")

    # Back CTkButton
    back_btn = CTkButton(
        app, 
        text="Back", 
        font=("Arial", 16), 
        command=Solcon
    )
    back_btn.place(relx=0.5, rely=0.8, anchor="center")


# Add theme switch
theme_switch = CTkSwitch(
    master=app, 
    text="Light Mode", 
    command=lambda: toggle_theme(theme_switch), 
    onvalue="dark", 
    offvalue="light"
)
theme_switch.place(relx=0.9, rely=0.1, anchor="center")

# Title CTkLabel
lbl = CTkLabel(
    master=app, 
    text="Let's Solve Chemistry", 
    font=("Times New Roman", 50)
)
lbl.place(relx=0.5, rely=0.3, anchor="center")

# Begin CTkButton
btn = CTkButton(
    master=app, 
    text="Begin", 
    font=("Arial", 16), 
    corner_radius=32,
    command=begin
)
btn.place(relx=0.5, rely=0.5, anchor="center")

# Run the main loop
app.mainloop()
