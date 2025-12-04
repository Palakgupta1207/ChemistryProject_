import tkinter as tk
from tkinter import ttk, messagebox
import math

class PBlockElementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("P-Block Element Properties Viewer")
        self.root.geometry("900x700")
        self.root.configure(bg='#2c3e50')
        
        # Dictionary of ALL 36 p-block elements with their properties
        self.p_block_elements = {
            # Group 13 (Boron Group)
            "B": {"name": "Boron", "atomic_number": 5, "symbol": "B", "group": 13, "period": 2, 
                  "block": "p", "standard_state": "Solid", "electron_configuration": "[He] 2s² 2p¹",
                  "density": "2.34 g/cm³", "melting_point": "2076°C", "boiling_point": "3927°C",
                  "electronegativity": "2.04", "atomic_radius": "85 pm", "color": "#FFB5B5"},
            
            "Al": {"name": "Aluminium", "atomic_number": 13, "symbol": "Al", "group": 13, "period": 3,
                   "block": "p", "standard_state": "Solid", "electron_configuration": "[Ne] 3s² 3p¹",
                   "density": "2.70 g/cm³", "melting_point": "660.32°C", "boiling_point": "2519°C",
                   "electronegativity": "1.61", "atomic_radius": "118 pm", "color": "#BFBFBF"},
            
            "Ga": {"name": "Gallium", "atomic_number": 31, "symbol": "Ga", "group": 13, "period": 4,
                   "block": "p", "standard_state": "Solid", "electron_configuration": "[Ar] 3d¹⁰ 4s² 4p¹",
                   "density": "5.91 g/cm³", "melting_point": "29.76°C", "boiling_point": "2204°C",
                   "electronegativity": "1.81", "atomic_radius": "136 pm", "color": "#C28F8F"},
            
            "In": {"name": "Indium", "atomic_number": 49, "symbol": "In", "group": 13, "period": 5,
                   "block": "p", "standard_state": "Solid", "electron_configuration": "[Kr] 4d¹⁰ 5s² 5p¹",
                   "density": "7.31 g/cm³", "melting_point": "156.6°C", "boiling_point": "2072°C",
                   "electronegativity": "1.78", "atomic_radius": "156 pm", "color": "#A6A6A6"},
            
            "Tl": {"name": "Thallium", "atomic_number": 81, "symbol": "Tl", "group": 13, "period": 6,
                   "block": "p", "standard_state": "Solid", "electron_configuration": "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p¹",
                   "density": "11.85 g/cm³", "melting_point": "304°C", "boiling_point": "1473°C",
                   "electronegativity": "1.62", "atomic_radius": "156 pm", "color": "#A6544D"},
            
            # Group 14 (Carbon Group)
            "C": {"name": "Carbon", "atomic_number": 6, "symbol": "C", "group": 14, "period": 2,
                  "block": "p", "standard_state": "Solid", "electron_configuration": "[He] 2s² 2p²",
                  "density": "2.27 g/cm³", "melting_point": "3550°C", "boiling_point": "4827°C",
                  "electronegativity": "2.55", "atomic_radius": "70 pm", "color": "#909090"},
            
            "Si": {"name": "Silicon", "atomic_number": 14, "symbol": "Si", "group": 14, "period": 3,
                   "block": "p", "standard_state": "Solid", "electron_configuration": "[Ne] 3s² 3p²",
                   "density": "2.33 g/cm³", "melting_point": "1414°C", "boiling_point": "3265°C",
                   "electronegativity": "1.90", "atomic_radius": "111 pm", "color": "#F0C8A0"},
            
            "Ge": {"name": "Germanium", "atomic_number": 32, "symbol": "Ge", "group": 14, "period": 4,
                   "block": "p", "standard_state": "Solid", "electron_configuration": "[Ar] 3d¹⁰ 4s² 4p²",
                   "density": "5.32 g/cm³", "melting_point": "938.2°C", "boiling_point": "2833°C",
                   "electronegativity": "2.01", "atomic_radius": "125 pm", "color": "#668F8F"},
            
            "Sn": {"name": "Tin", "atomic_number": 50, "symbol": "Sn", "group": 14, "period": 5,
                   "block": "p", "standard_state": "Solid", "electron_configuration": "[Kr] 4d¹⁰ 5s² 5p²",
                   "density": "7.31 g/cm³", "melting_point": "231.9°C", "boiling_point": "2602°C",
                   "electronegativity": "1.96", "atomic_radius": "145 pm", "color": "#668080"},
            
            "Pb": {"name": "Lead", "atomic_number": 82, "symbol": "Pb", "group": 14, "period": 6,
                   "block": "p", "standard_state": "Solid", "electron_configuration": "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p²",
                   "density": "11.34 g/cm³", "melting_point": "327.5°C", "boiling_point": "1749°C",
                   "electronegativity": "2.33", "atomic_radius": "154 pm", "color": "#575961"},
            
            # Group 15 (Nitrogen Group)
            "N": {"name": "Nitrogen", "atomic_number": 7, "symbol": "N", "group": 15, "period": 2,
                  "block": "p", "standard_state": "Gas", "electron_configuration": "[He] 2s² 2p³",
                  "density": "1.25 g/L", "melting_point": "-210.0°C", "boiling_point": "-195.8°C",
                  "electronegativity": "3.04", "atomic_radius": "65 pm", "color": "#3050F8"},
            
            "P": {"name": "Phosphorus", "atomic_number": 15, "symbol": "P", "group": 15, "period": 3,
                  "block": "p", "standard_state": "Solid", "electron_configuration": "[Ne] 3s² 3p³",
                  "density": "1.82 g/cm³", "melting_point": "44.2°C", "boiling_point": "280.5°C",
                  "electronegativity": "2.19", "atomic_radius": "98 pm", "color": "#FF8000"},
            
            "As": {"name": "Arsenic", "atomic_number": 33, "symbol": "As", "group": 15, "period": 4,
                   "block": "p", "standard_state": "Solid", "electron_configuration": "[Ar] 3d¹⁰ 4s² 4p³",
                   "density": "5.73 g/cm³", "melting_point": "817°C", "boiling_point": "613°C",
                   "electronegativity": "2.18", "atomic_radius": "114 pm", "color": "#BD80E3"},
            
            "Sb": {"name": "Antimony", "atomic_number": 51, "symbol": "Sb", "group": 15, "period": 5,
                   "block": "p", "standard_state": "Solid", "electron_configuration": "[Kr] 4d¹⁰ 5s² 5p³",
                   "density": "6.68 g/cm³", "melting_point": "630.6°C", "boiling_point": "1587°C",
                   "electronegativity": "2.05", "atomic_radius": "133 pm", "color": "#9E63B5"},
            
            "Bi": {"name": "Bismuth", "atomic_number": 83, "symbol": "Bi", "group": 15, "period": 6,
                   "block": "p", "standard_state": "Solid", "electron_configuration": "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p³",
                   "density": "9.79 g/cm³", "melting_point": "271.4°C", "boiling_point": "1564°C",
                   "electronegativity": "2.02", "atomic_radius": "143 pm", "color": "#9E4FB5"},
            
            # Group 16 (Oxygen Group)
            "O": {"name": "Oxygen", "atomic_number": 8, "symbol": "O", "group": 16, "period": 2,
                  "block": "p", "standard_state": "Gas", "electron_configuration": "[He] 2s² 2p⁴",
                  "density": "1.43 g/L", "melting_point": "-218.8°C", "boiling_point": "-183.0°C",
                  "electronegativity": "3.44", "atomic_radius": "60 pm", "color": "#FF0D0D"},
            
            "S": {"name": "Sulfur", "atomic_number": 16, "symbol": "S", "group": 16, "period": 3,
                  "block": "p", "standard_state": "Solid", "electron_configuration": "[Ne] 3s² 3p⁴",
                  "density": "2.07 g/cm³", "melting_point": "115.2°C", "boiling_point": "444.6°C",
                  "electronegativity": "2.58", "atomic_radius": "88 pm", "color": "#FFFF30"},
            
            "Se": {"name": "Selenium", "atomic_number": 34, "symbol": "Se", "group": 16, "period": 4,
                   "block": "p", "standard_state": "Solid", "electron_configuration": "[Ar] 3d¹⁰ 4s² 4p⁴",
                   "density": "4.81 g/cm³", "melting_point": "221°C", "boiling_point": "685°C",
                   "electronegativity": "2.55", "atomic_radius": "103 pm", "color": "#FFA500"},
            
            "Te": {"name": "Tellurium", "atomic_number": 52, "symbol": "Te", "group": 16, "period": 5,
                   "block": "p", "standard_state": "Solid", "electron_configuration": "[Kr] 4d¹⁰ 5s² 5p⁴",
                   "density": "6.24 g/cm³", "melting_point": "449.5°C", "boiling_point": "988°C",
                   "electronegativity": "2.1", "atomic_radius": "123 pm", "color": "#D47A00"},
            
            "Po": {"name": "Polonium", "atomic_number": 84, "symbol": "Po", "group": 16, "period": 6,
                   "block": "p", "standard_state": "Solid", "electron_configuration": "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p⁴",
                   "density": "9.20 g/cm³", "melting_point": "254°C", "boiling_point": "962°C",
                   "electronegativity": "2.0", "atomic_radius": "135 pm", "color": "#AB5C00"},
            
            # Group 17 (Halogens)
            "F": {"name": "Fluorine", "atomic_number": 9, "symbol": "F", "group": 17, "period": 2,
                  "block": "p", "standard_state": "Gas", "electron_configuration": "[He] 2s² 2p⁵",
                  "density": "1.70 g/L", "melting_point": "-219.7°C", "boiling_point": "-188.1°C",
                  "electronegativity": "3.98", "atomic_radius": "50 pm", "color": "#90E050"},
            
            "Cl": {"name": "Chlorine", "atomic_number": 17, "symbol": "Cl", "group": 17, "period": 3,
                   "block": "p", "standard_state": "Gas", "electron_configuration": "[Ne] 3s² 3p⁵",
                   "density": "3.21 g/L", "melting_point": "-101.5°C", "boiling_point": "-34.0°C",
                   "electronegativity": "3.16", "atomic_radius": "79 pm", "color": "#1FF01F"},
            
            "Br": {"name": "Bromine", "atomic_number": 35, "symbol": "Br", "group": 17, "period": 4,
                   "block": "p", "standard_state": "Liquid", "electron_configuration": "[Ar] 3d¹⁰ 4s² 4p⁵",
                   "density": "3.12 g/cm³", "melting_point": "-7.2°C", "boiling_point": "58.8°C",
                   "electronegativity": "2.96", "atomic_radius": "94 pm", "color": "#A62929"},
            
            "I": {"name": "Iodine", "atomic_number": 53, "symbol": "I", "group": 17, "period": 5,
                  "block": "p", "standard_state": "Solid", "electron_configuration": "[Kr] 4d¹⁰ 5s² 5p⁵",
                  "density": "4.93 g/cm³", "melting_point": "113.7°C", "boiling_point": "184.3°C",
                  "electronegativity": "2.66", "atomic_radius": "115 pm", "color": "#940094"},
            
            "At": {"name": "Astatine", "atomic_number": 85, "symbol": "At", "group": 17, "period": 6,
                   "block": "p", "standard_state": "Solid", "electron_configuration": "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p⁵",
                   "density": "7 g/cm³", "melting_point": "302°C", "boiling_point": "337°C",
                   "electronegativity": "2.2", "atomic_radius": "127 pm", "color": "#754F45"},
            
            # Group 18 (Noble Gases)
            "He": {"name": "Helium", "atomic_number": 2, "symbol": "He", "group": 18, "period": 1,
                   "block": "s", "standard_state": "Gas", "electron_configuration": "1s²",
                   "density": "0.18 g/L", "melting_point": "-272.2°C", "boiling_point": "-268.9°C",
                   "electronegativity": "N/A", "atomic_radius": "31 pm", "color": "#D9FFFF"},
            
            "Ne": {"name": "Neon", "atomic_number": 10, "symbol": "Ne", "group": 18, "period": 2,
                   "block": "p", "standard_state": "Gas", "electron_configuration": "[He] 2s² 2p⁶",
                   "density": "0.90 g/L", "melting_point": "-248.6°C", "boiling_point": "-246.1°C",
                   "electronegativity": "N/A", "atomic_radius": "38 pm", "color": "#B3E3F5"},
            
            "Ar": {"name": "Argon", "atomic_number": 18, "symbol": "Ar", "group": 18, "period": 3,
                   "block": "p", "standard_state": "Gas", "electron_configuration": "[Ne] 3s² 3p⁶",
                   "density": "1.78 g/L", "melting_point": "-189.3°C", "boiling_point": "-185.9°C",
                   "electronegativity": "N/A", "atomic_radius": "71 pm", "color": "#80D1E3"},
            
            "Kr": {"name": "Krypton", "atomic_number": 36, "symbol": "Kr", "group": 18, "period": 4,
                   "block": "p", "standard_state": "Gas", "electron_configuration": "[Ar] 3d¹⁰ 4s² 4p⁶",
                   "density": "3.75 g/L", "melting_point": "-157.4°C", "boiling_point": "-153.4°C",
                   "electronegativity": "3.00", "atomic_radius": "88 pm", "color": "#5CB8D1"},
            
            "Xe": {"name": "Xenon", "atomic_number": 54, "symbol": "Xe", "group": 18, "period": 5,
                   "block": "p", "standard_state": "Gas", "electron_configuration": "[Kr] 4d¹⁰ 5s² 5p⁶",
                   "density": "5.90 g/L", "melting_point": "-111.8°C", "boiling_point": "-108.1°C",
                   "electronegativity": "2.60", "atomic_radius": "108 pm", "color": "#429EB0"},
            
            "Rn": {"name": "Radon", "atomic_number": 86, "symbol": "Rn", "group": 18, "period": 6,
                   "block": "p", "standard_state": "Gas", "electron_configuration": "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p⁶",
                   "density": "9.73 g/L", "melting_point": "-71°C", "boiling_point": "-61.7°C",
                   "electronegativity": "2.2", "atomic_radius": "120 pm", "color": "#007296"},
            
            # Post-transition metals (sometimes included in p-block)
            "Zn": {"name": "Zinc", "atomic_number": 30, "symbol": "Zn", "group": 12, "period": 4,
                   "block": "d", "standard_state": "Solid", "electron_configuration": "[Ar] 3d¹⁰ 4s²",
                   "density": "7.13 g/cm³", "melting_point": "419.5°C", "boiling_point": "907°C",
                   "electronegativity": "1.65", "atomic_radius": "134 pm", "color": "#7D80B0"},
            
            "Cd": {"name": "Cadmium", "atomic_number": 48, "symbol": "Cd", "group": 12, "period": 5,
                   "block": "d", "standard_state": "Solid", "electron_configuration": "[Kr] 4d¹⁰ 5s²",
                   "density": "8.65 g/cm³", "melting_point": "321.1°C", "boiling_point": "767°C",
                   "electronegativity": "1.69", "atomic_radius": "151 pm", "color": "#FFD98F"},
            
            "Hg": {"name": "Mercury", "atomic_number": 80, "symbol": "Hg", "group": 12, "period": 6,
                   "block": "d", "standard_state": "Liquid", "electron_configuration": "[Xe] 4f¹⁴ 5d¹⁰ 6s²",
                   "density": "13.53 g/cm³", "melting_point": "-38.8°C", "boiling_point": "356.7°C",
                   "electronegativity": "2.00", "atomic_radius": "151 pm", "color": "#B8B8D0"},
            
            # Metalloids
            "B": {"name": "Boron", "atomic_number": 5, "symbol": "B", "group": 13, "period": 2,
                  "block": "p", "standard_state": "Solid", "electron_configuration": "[He] 2s² 2p¹",
                  "density": "2.34 g/cm³", "melting_point": "2076°C", "boiling_point": "3927°C",
                  "electronegativity": "2.04", "atomic_radius": "85 pm", "color": "#FFB5B5"},
            
            "Si": {"name": "Silicon", "atomic_number": 14, "symbol": "Si", "group": 14, "period": 3,
                   "block": "p", "standard_state": "Solid", "electron_configuration": "[Ne] 3s² 3p²",
                   "density": "2.33 g/cm³", "melting_point": "1414°C", "boiling_point": "3265°C",
                   "electronegativity": "1.90", "atomic_radius": "111 pm", "color": "#F0C8A0"},
            
            "Ge": {"name": "Germanium", "atomic_number": 32, "symbol": "Ge", "group": 14, "period": 4,
                   "block": "p", "standard_state": "Solid", "electron_configuration": "[Ar] 3d¹⁰ 4s² 4p²",
                   "density": "5.32 g/cm³", "melting_point": "938.2°C", "boiling_point": "2833°C",
                   "electronegativity": "2.01", "atomic_radius": "125 pm", "color": "#668F8F"},
            
            "As": {"name": "Arsenic", "atomic_number": 33, "symbol": "As", "group": 15, "period": 4,
                   "block": "p", "standard_state": "Solid", "electron_configuration": "[Ar] 3d¹⁰ 4s² 4p³",
                   "density": "5.73 g/cm³", "melting_point": "817°C", "boiling_point": "613°C",
                   "electronegativity": "2.18", "atomic_radius": "114 pm", "color": "#BD80E3"},
            
            "Sb": {"name": "Antimony", "atomic_number": 51, "symbol": "Sb", "group": 15, "period": 5,
                   "block": "p", "standard_state": "Solid", "electron_configuration": "[Kr] 4d¹⁰ 5s² 5p³",
                   "density": "6.68 g/cm³", "melting_point": "630.6°C", "boiling_point": "1587°C",
                   "electronegativity": "2.05", "atomic_radius": "133 pm", "color": "#9E63B5"},
            
            "Te": {"name": "Tellurium", "atomic_number": 52, "symbol": "Te", "group": 16, "period": 5,
                   "block": "p", "standard_state": "Solid", "electron_configuration": "[Kr] 4d¹⁰ 5s² 5p⁴",
                   "density": "6.24 g/cm³", "melting_point": "449.5°C", "boiling_point": "988°C",
                   "electronegativity": "2.1", "atomic_radius": "123 pm", "color": "#D47A00"},
            
            "Po": {"name": "Polonium", "atomic_number": 84, "symbol": "Po", "group": 16, "period": 6,
                   "block": "p", "standard_state": "Solid", "electron_configuration": "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p⁴",
                   "density": "9.20 g/cm³", "melting_point": "254°C", "boiling_point": "962°C",
                   "electronegativity": "2.0", "atomic_radius": "135 pm", "color": "#AB5C00"}
        }
        
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the user interface"""
        
        # Main title
        title_label = tk.Label(self.root, text="P-Block Elements Properties Viewer", 
                               font=("Arial", 24, "bold"), bg='#2c3e50', fg='white')
        title_label.pack(pady=10)
        
        # Subtitle
        subtitle_label = tk.Label(self.root, 
                                 text="All 36 P-Block Elements (Groups 13-18)", 
                                 font=("Arial", 12), bg='#2c3e50', fg='#ecf0f1')
        subtitle_label.pack(pady=5)
        
        # Input frame
        input_frame = tk.Frame(self.root, bg='#2c3e50')
        input_frame.pack(pady=10)
        
        # Label for input
        input_label = tk.Label(input_frame, text="Element:", 
                               font=("Arial", 12), bg='#2c3e50', fg='white')
        input_label.grid(row=0, column=0, padx=5)
        
        # Entry field for element input
        self.element_entry = tk.Entry(input_frame, font=("Arial", 12), width=20)
        self.element_entry.grid(row=0, column=1, padx=5)
        self.element_entry.bind('<Return>', lambda event: self.get_element_properties())
        
        # Get Properties button
        self.get_button = tk.Button(input_frame, text="Get Properties", 
                                   command=self.get_element_properties,
                                   bg='#3498db', fg='white', 
                                   font=("Arial", 12, "bold"),
                                   activebackground='#2980b9',
                                   width=15)
        self.get_button.grid(row=0, column=2, padx=10)
        
        # Clear button
        clear_button = tk.Button(input_frame, text="Clear", 
                                command=self.clear_display,
                                bg='#e74c3c', fg='white',
                                font=("Arial", 10),
                                activebackground='#c0392b')
        clear_button.grid(row=0, column=3, padx=5)
        
        # Main display frame
        display_frame = tk.Frame(self.root, bg='#34495e')
        display_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        
        # Left frame for atomic structure
        left_frame = tk.Frame(display_frame, bg='#34495e')
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Canvas for atomic structure
        self.canvas = tk.Canvas(left_frame, bg='#1a5276', width=350, height=350, 
                                highlightthickness=2, highlightbackground='#3498db')
        self.canvas.pack(pady=10)
        
        # Right frame for properties
        right_frame = tk.Frame(display_frame, bg='#34495e')
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(20, 0))
        
        # Text widget for displaying properties
        self.property_display = tk.Text(right_frame, bg='#1a5276', fg='white',
                                       font=("Arial", 11), wrap=tk.WORD,
                                       height=20, width=45,
                                       relief=tk.FLAT, bd=0)
        self.property_display.pack(fill=tk.BOTH, expand=True)
        
        # Configure tags for text formatting
        self.property_display.tag_configure("title", font=("Arial", 14, "bold"), 
                                           foreground="yellow")
        self.property_display.tag_configure("property", font=("Arial", 11, "bold"), 
                                           foreground="#7fb3d5")
        self.property_display.tag_configure("value", font=("Arial", 11), 
                                           foreground="white")
        self.property_display.tag_configure("highlight", font=("Arial", 11, "bold"), 
                                           foreground="#FFD700", background="#2E4053")
        
        # Add scrollbar to text widget
        scrollbar = tk.Scrollbar(self.property_display)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.property_display.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.property_display.yview)
        
        # Status label
        self.status_label = tk.Label(self.root, text="Ready. Enter an element name or symbol.", 
                                    font=("Arial", 10), bg='#2c3e50', fg='#bdc3c7')
        self.status_label.pack(pady=5)
        
        # Instructions
        instructions = "Enter element name (e.g., 'Carbon') or symbol (e.g., 'C')"
        instructions_label = tk.Label(self.root, text=instructions, 
                                     font=("Arial", 9), bg='#2c3e50', fg='#95a5a6')
        instructions_label.pack(pady=5)
        
        # Element group buttons frame
        group_frame = tk.Frame(self.root, bg='#2c3e50')
        group_frame.pack(pady=10)
        
        # Create group buttons
        groups = ["Group 13", "Group 14", "Group 15", "Group 16", "Group 17", "Group 18"]
        group_colors = ['#3498db', '#2ecc71', '#e74c3c', '#f39c12', '#9b59b6', '#1abc9c']
        
        for i, (group, color) in enumerate(zip(groups, group_colors)):
            btn = tk.Button(group_frame, text=group, 
                          command=lambda g=group: self.show_group_elements(g),
                          bg=color, fg='white',
                          font=("Arial", 9),
                          activebackground=color,
                          width=10)
            btn.grid(row=0, column=i, padx=5)
    
    def show_group_elements(self, group_name):
        """Show all elements in a specific group"""
        group_num = int(group_name.split()[1])
        
        # Clear display
        self.property_display.delete(1.0, tk.END)
        self.canvas.delete("all")
        
        # Get elements in this group
        elements_in_group = []
        for symbol, element in self.p_block_elements.items():
            if element.get('group') == group_num:
                elements_in_group.append((symbol, element))
        
        # Display group information
        self.property_display.insert(tk.END, f"{group_name} Elements\n\n", "title")
        
        if group_num == 13:
            self.property_display.insert(tk.END, "Boron Group\n", "highlight")
            self.property_display.insert(tk.END, "Also known as the triels\n\n", "value")
        elif group_num == 14:
            self.property_display.insert(tk.END, "Carbon Group\n", "highlight")
            self.property_display.insert(tk.END, "Also known as the tetrels\n\n", "value")
        elif group_num == 15:
            self.property_display.insert(tk.END, "Pnictogens\n", "highlight")
            self.property_display.insert(tk.END, "Nitrogen Group\n\n", "value")
        elif group_num == 16:
            self.property_display.insert(tk.END, "Chalcogens\n", "highlight")
            self.property_display.insert(tk.END, "Oxygen Group\n\n", "value")
        elif group_num == 17:
            self.property_display.insert(tk.END, "Halogens\n", "highlight")
            self.property_display.insert(tk.END, "Salt-formers\n\n", "value")
        elif group_num == 18:
            self.property_display.insert(tk.END, "Noble Gases\n", "highlight")
            self.property_display.insert(tk.END, "Inert gases\n\n", "value")
        
        # List elements in the group
        for symbol, element in elements_in_group:
            self.property_display.insert(tk.END, 
                f"• {element['name']} ({symbol}): Atomic # {element['atomic_number']}\n", 
                "property")
        
        # Draw group representation on canvas
        self.draw_group_representation(group_num)
        
        # Update status
        self.status_label.config(text=f"Showing {len(elements_in_group)} elements from {group_name}", 
                                fg='#2ecc71')
    
    def draw_group_representation(self, group_num):
        """Draw a representation of elements in a group"""
        self.canvas.delete("all")
        
        # Canvas center
        center_x, center_y = 175, 175
        
        # Group title
        self.canvas.create_text(center_x, 30, 
                               text=f"Group {group_num} Elements", 
                               font=("Arial", 14, "bold"), fill="white")
        
        # Draw periodic table representation
        radius = 120
        angle_step = 2 * math.pi / 6  # 6 periods
        
        for period in range(1, 7):
            angle = (period - 1) * angle_step
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            
            # Draw circle for period
            self.canvas.create_oval(x-25, y-25, x+25, y+25, 
                                   fill=self.get_group_color(group_num), 
                                   outline='white', width=2)
            
            # Find element in this group and period
            element_symbol = None
            for symbol, element in self.p_block_elements.items():
                if element.get('group') == group_num and element.get('period') == period:
                    element_symbol = symbol
                    break
            
            if element_symbol:
                self.canvas.create_text(x, y, text=element_symbol, 
                                       font=("Arial", 12, "bold"), fill="white")
            
            # Draw period label
            label_x = center_x + (radius + 40) * math.cos(angle)
            label_y = center_y + (radius + 40) * math.sin(angle)
            self.canvas.create_text(label_x, label_y, text=f"Period {period}", 
                                   font=("Arial", 9), fill="#bdc3c7")
    
    def get_group_color(self, group_num):
        """Return color for a specific group"""
        colors = {
            13: '#3498db',  # Blue
            14: '#2ecc71',  # Green
            15: '#e74c3c',  # Red
            16: '#f39c12',  # Orange
            17: '#9b59b6',  # Purple
            18: '#1abc9c'   # Teal
        }
        return colors.get(group_num, '#95a5a6')
    
    def draw_atomic_structure(self, element_data):
        """Draw a simple atomic structure on the canvas"""
        self.canvas.delete("all")  # Clear previous drawing
        
        # Get element properties
        symbol = element_data['symbol']
        atomic_number = element_data['atomic_number']
        period = element_data['period']
        color = element_data['color']
        
        # Canvas center
        center_x, center_y = 175, 175
        
        # Draw nucleus
        nucleus_radius = min(30, 15 + atomic_number / 10)
        self.canvas.create_oval(center_x - nucleus_radius, center_y - nucleus_radius,
                               center_x + nucleus_radius, center_y + nucleus_radius,
                               fill=color, outline='white', width=2)
        
        # Add atomic number and symbol to nucleus
        self.canvas.create_text(center_x, center_y - 8, 
                               text=str(atomic_number), 
                               font=("Arial", 12, "bold"), fill="white")
        self.canvas.create_text(center_x, center_y + 12, 
                               text=symbol, 
                               font=("Arial", 16, "bold"), fill="white")
        
        # Draw electron shells based on period
        shell_radius = 50
        
        for shell in range(1, period + 1):
            # Calculate number of electrons in this shell (simplified)
            max_electrons = 2 * (shell ** 2)
            if shell == 1:
                electrons_in_shell = min(atomic_number, 2)
            else:
                prev_electrons = sum([2 * (i ** 2) for i in range(1, shell)])
                electrons_in_shell = min(atomic_number - prev_electrons, max_electrons)
            
            # Only draw shell if it has electrons
            if electrons_in_shell > 0:
                # Draw electron shell (orbit)
                self.canvas.create_oval(center_x - shell_radius, center_y - shell_radius,
                                       center_x + shell_radius, center_y + shell_radius,
                                       outline='white', width=1, dash=(2, 2))
                
                # Label the shell
                self.canvas.create_text(center_x, center_y - shell_radius - 15, 
                                       text=f"n={shell}", 
                                       font=("Arial", 9), fill="#bdc3c7")
                
                # Draw electrons as dots on the orbit (max 8 for visibility)
                electron_count = min(electrons_in_shell, 8)
                for i in range(electron_count):
                    angle = 2 * math.pi * i / electron_count
                    electron_x = center_x + shell_radius * math.cos(angle)
                    electron_y = center_y + shell_radius * math.sin(angle)
                    
                    self.canvas.create_oval(electron_x - 6, electron_y - 6,
                                           electron_x + 6, electron_y + 6,
                                           fill='yellow', outline='white', width=1)
            
            shell_radius += 35
        
        # Add title
        self.canvas.create_text(center_x, 30, 
                               text=f"Atomic Structure of {element_data['name']}", 
                               font=("Arial", 12, "bold"), fill="white")
        
        # Add electron configuration
        config = element_data['electron_configuration']
        self.canvas.create_text(center_x, 330, 
                               text=f"Electron Config: {config}", 
                               font=("Arial", 9), fill="#bdc3c7", width=300)
    
    def get_element_properties(self):
        """Retrieve and display properties of the entered element"""
        # Get user input and clean it
        user_input = self.element_entry.get().strip()
        
        if not user_input:
            messagebox.showwarning("No Input", "Please enter an element name or symbol.")
            return
        
        # Convert to proper case for element name lookup
        element_key = None
        
        # Check if input is a symbol (case-insensitive)
        for symbol in self.p_block_elements.keys():
            if user_input.lower() == symbol.lower():
                element_key = symbol
                break
        
        # Check if input is an element name (case-insensitive)
        if element_key is None:
            for symbol, element in self.p_block_elements.items():
                if user_input.lower() == element['name'].lower():
                    element_key = symbol
                    break
        
        # If element not found in p-block
        if element_key is None:
            self.status_label.config(text=f"'{user_input}' not found or not a p-block element.", 
                                    fg='#e74c3c')
            self.property_display.delete(1.0, tk.END)
            self.property_display.insert(tk.END, "ERROR: Element Not Found\n\n", "title")
            self.property_display.insert(tk.END, 
                f"'{user_input}' is not a recognized p-block element.\n\n"
                "P-block elements are in Groups 13-18 of the periodic table.\n\n", "value")
            
            # Show some examples
            self.property_display.insert(tk.END, "Examples of p-block elements:\n", "property")
            examples = ["Boron (B)", "Carbon (C)", "Nitrogen (N)", "Oxygen (O)", 
                       "Fluorine (F)", "Aluminium (Al)", "Silicon (Si)", "Phosphorus (P)"]
            for example in examples:
                self.property_display.insert(tk.END, f"• {example}\n", "value")
            
            self.canvas.delete("all")
            self.canvas.create_text(175, 175, 
                                   text="Element\nNot Found", 
                                   font=("Arial", 16, "bold"), fill="red")
            return
        
        # Get element data
        element_data = self.p_block_elements[element_key]
        
        # Check if it's actually a p-block element
        if element_data['block'] != 'p':
            self.status_label.config(text=f"'{user_input}' is not a p-block element.", 
                                    fg='#e74c3c')
            self.property_display.delete(1.0, tk.END)
            self.property_display.insert(tk.END, "NOT A P-BLOCK ELEMENT\n\n", "title")
            self.property_display.insert(tk.END, 
                f"'{element_data['name']}' ({element_data['symbol']}) is in the {element_data['block']}-block, not the p-block.\n\n"
                "P-block elements are in Groups 13-18.\n", "value")
            return
        
        # Update status
        self.status_label.config(text=f"Displaying properties for {element_data['name']}", 
                                fg='#2ecc71')
        
        # Clear previous display
        self.property_display.delete(1.0, tk.END)
        
        # Display element properties with formatting
        self.property_display.insert(tk.END, f"{element_data['name']} Properties\n\n", "title")
        
        # Basic properties
        properties = [
            ("Symbol", element_data['symbol']),
            ("Atomic Number", str(element_data['atomic_number'])),
            ("Group", f"{element_data['group']} ({self.get_group_name(element_data['group'])})"),
            ("Period", str(element_data['period'])),
            ("Block", element_data['block']),
            ("Standard State", element_data['standard_state']),
            ("Electron Configuration", element_data['electron_configuration']),
            ("Electronegativity", element_data['electronegativity']),
            ("Atomic Radius", element_data['atomic_radius']),
            ("Density", element_data['density']),
            ("Melting Point", element_data['melting_point']),
            ("Boiling Point", element_data['boiling_point'])
        ]
        
        for prop_name, prop_value in properties:
            self.property_display.insert(tk.END, f"{prop_name}: ", "property")
            self.property_display.insert(tk.END, f"{prop_value}\n", "value")
        
        # Add classification
        self.property_display.insert(tk.END, "\nClassification: ", "property")
        classification = self.get_classification(element_data)
        self.property_display.insert(tk.END, f"{classification}\n", "value")
        
        # Add fun facts
        self.property_display.insert(tk.END, "\nInteresting Facts:\n", "property")
        
        fun_facts = self.get_fun_facts(element_data)
        for fact in fun_facts:
            self.property_display.insert(tk.END, f"• {fact}\n", "value")
        
        # Draw atomic structure
        self.draw_atomic_structure(element_data)
    
    def get_group_name(self, group_num):
        """Return the common name for a group"""
        group_names = {
            13: "Boron Group",
            14: "Carbon Group",
            15: "Nitrogen Group (Pnictogens)",
            16: "Oxygen Group (Chalcogens)",
            17: "Halogens",
            18: "Noble Gases"
        }
        return group_names.get(group_num, "Unknown Group")
    
    def get_classification(self, element_data):
        """Return the chemical classification of the element"""
        symbol = element_data['symbol']
        state = element_data['standard_state'].lower()
        
        # Check for metalloids
        metalloids = ["B", "Si", "Ge", "As", "Sb", "Te", "Po"]
        if symbol in metalloids:
            return "Metalloid"
        
        # Check for noble gases
        if element_data['group'] == 18:
            return "Noble Gas"
        
        # Check for halogens
        if element_data['group'] == 17:
            return "Halogen"
        
        # Check state and group for other classifications
        if state == "gas":
            return "Nonmetal Gas"
        elif state == "liquid":
            return "Liquid Nonmetal" if element_data['group'] >= 15 else "Liquid Metal"
        else:  # solid
            if element_data['group'] in [13, 14]:
                return "Post-transition Metal" if element_data['period'] >= 4 else "Metalloid/Nonmetal"
            elif element_data['group'] in [15, 16]:
                return "Nonmetal" if element_data['period'] <= 3 else "Metalloid/Other Nonmetal"
            else:
                return "Element"
    
    def get_fun_facts(self, element_data):
        """Return interesting facts about the element"""
        name = element_data['name']
        symbol = element_data['symbol']
        group = element_data['group']
        
        facts = {
            "B": [
                "Boron is essential for plant cell walls",
                "Used in borosilicate glass (Pyrex)",
                "Boron fibers are used in aerospace composites",
                "Boron compounds are used as flame retardants"
            ],
            "C": [
                "Carbon is the basis of all known life",
                "Exists in several allotropes: diamond, graphite, graphene, fullerenes",
                "Carbon dating is used to determine the age of ancient objects",
                "Diamond is the hardest natural material"
            ],
            "N": [
                "Nitrogen makes up 78% of Earth's atmosphere",
                "Essential for proteins and DNA",
                "Liquid nitrogen is used as a coolant (-196°C)",
                "Nitrogen fixation by bacteria makes it available to plants"
            ],
            "O": [
                "Oxygen is the most abundant element in Earth's crust",
                "Essential for respiration in most living organisms",
                "Ozone (O₃) protects Earth from UV radiation",
                "Oxygen was discovered by Joseph Priestley in 1774"
            ],
            "F": [
                "Fluorine is the most reactive element",
                "Added to toothpaste to prevent tooth decay",
                "Teflon (polytetrafluoroethylene) contains fluorine",
                "Fluorine gas is pale yellow-green in color"
            ],
            "Al": [
                "Aluminium is the most abundant metal in Earth's crust",
                "Recyclable without loss of quality",
                "Used in aircraft, cans, and construction",
                "Aluminium was once more valuable than gold"
            ],
            "Si": [
                "Silicon is the second most abundant element in Earth's crust",
                "Essential for computer chips and solar cells",
                "Silica (SiO₂) is the main component of sand",
                "Silicones are silicon-based polymers"
            ],
            "P": [
                "Phosphorus is essential for DNA, RNA, and ATP",
                "White phosphorus glows in the dark (phosphorescence)",
                "Used in fertilizers, detergents, and matches",
                "Phosphorus was discovered in urine"
            ],
            "S": [
                "Sulfur smells like rotten eggs",
                "Essential for amino acids cysteine and methionine",
                "Used in gunpowder, rubber vulcanization, and sulfuric acid",
                "Sulfuric acid is the most produced chemical worldwide"
            ],
            "Cl": [
                "Chlorine is used to disinfect drinking water",
                "Table salt is sodium chloride (NaCl)",
                "Chlorine gas was used as a chemical weapon in WWI",
                "PVC plastic contains chlorine"
            ],
            "Ar": [
                "Argon is the most abundant noble gas in Earth's atmosphere",
                "Used to create inert atmospheres for welding",
                "Light bulbs are often filled with argon",
                "Argon is used in double-pane windows for insulation"
            ],
            "Br": [
                "Bromine is one of only two liquid elements at room temperature",
                "Used in flame retardants and pharmaceuticals",
                "Bromine comes from Greek 'bromos' meaning stench",
                "Silver bromide is used in photographic film"
            ],
            "I": [
                "Iodine is essential for thyroid hormone production",
                "Iodine vapor is violet in color",
                "Used as an antiseptic (tincture of iodine)",
                "Iodine deficiency can cause goiter"
            ],
            "Xe": [
                "Xenon is used in high-intensity lamps and flashbulbs",
                "Xenon compounds can be powerful oxidizing agents",
                "Xenon anesthesia is being studied for medical use",
                "Xenon headlights produce light similar to daylight"
            ]
        }
        
        # Return specific facts or general ones
        specific_facts = facts.get(symbol, [
            f"{name} is an important p-block element",
            f"Found in period {element_data['period']}, group {group}",
            f"Electron configuration: {element_data['electron_configuration']}",
            "Has applications in various industries"
        ])
        
        # Add group-specific fact
        group_fact = f"Belongs to the {self.get_group_name(group)}"
        if group_fact not in specific_facts:
            specific_facts.insert(0, group_fact)
        
        return specific_facts
    
    def clear_display(self):
        """Clear all input and display areas"""
        self.element_entry.delete(0, tk.END)
        self.property_display.delete(1.0, tk.END)
        self.canvas.delete("all")
        self.status_label.config(text="Ready. Enter an element name or symbol.", 
                                fg='#bdc3c7')
        # Draw a welcome message on canvas
        self.canvas.create_text(175, 175, 
                               text="P-Block Elements\n\nEnter an element to see\nits atomic structure\nand properties", 
                               font=("Arial", 12), fill="white", justify=tk.CENTER)

def main():
    """Main function to run the application"""
    root = tk.Tk()
    app = PBlockElementApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()