import tkinter as tk
from tkinter import ttk, messagebox

class TemperatureConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Temperature Converter")
        self.root.geometry("500x600")
        self.root.resizable(True, True)
        
        # Set theme colors
        self.bg_color = "#f0f8ff"
        self.button_color = "#4CAF50"
        self.text_color = "#333333"
        
        self.root.configure(bg=self.bg_color)
        self.setup_ui()
    
    def celsius_to_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32

    def celsius_to_kelvin(self, celsius):
        return celsius + 273.15

    def fahrenheit_to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5/9

    def fahrenheit_to_kelvin(self, fahrenheit):
        celsius = self.fahrenheit_to_celsius(fahrenheit)
        return self.celsius_to_kelvin(celsius)

    def kelvin_to_celsius(self, kelvin):
        return kelvin - 273.15

    def kelvin_to_fahrenheit(self, kelvin):
        celsius = self.kelvin_to_celsius(kelvin)
        return self.celsius_to_fahrenheit(celsius)
    
    def setup_ui(self):
        # Header
        header_frame = tk.Frame(self.root, bg=self.bg_color)
        header_frame.pack(pady=20)
        
        title_label = tk.Label(
            header_frame, 
            text="Temperature Converter", 
            font=("Arial", 20, "bold"),
            bg=self.bg_color,
            fg=self.text_color
        )
        title_label.pack()
        
        subtitle_label = tk.Label(
            header_frame,
            text="Convert between Celsius, Fahrenheit, and Kelvin",
            font=("Arial", 10),
            bg=self.bg_color,
            fg=self.text_color
        )
        subtitle_label.pack(pady=5)
        
        # Input Section
        input_frame = tk.Frame(self.root, bg=self.bg_color)
        input_frame.pack(pady=20, padx=40, fill="x")
        
        # Temperature input
        tk.Label(
            input_frame, 
            text="Temperature:", 
            font=("Arial", 12),
            bg=self.bg_color,
            fg=self.text_color
        ).grid(row=0, column=0, sticky="w", pady=5)
        
        self.temp_var = tk.StringVar()
        self.temp_entry = tk.Entry(
            input_frame, 
            textvariable=self.temp_var,
            font=("Arial", 12),
            width=15
        )
        self.temp_entry.grid(row=0, column=1, padx=10, pady=5)
        
        # From scale selection
        tk.Label(
            input_frame, 
            text="From Scale:", 
            font=("Arial", 12),
            bg=self.bg_color,
            fg=self.text_color
        ).grid(row=1, column=0, sticky="w", pady=5)
        
        self.from_scale = tk.StringVar(value="Celsius")
        scale_options = ["Celsius", "Fahrenheit", "Kelvin"]
        from_combobox = ttk.Combobox(
            input_frame, 
            textvariable=self.from_scale,
            values=scale_options,
            state="readonly",
            width=12
        )
        from_combobox.grid(row=1, column=1, padx=10, pady=5)
        
        # Conversion type selection
        tk.Label(
            input_frame, 
            text="Conversion Type:", 
            font=("Arial", 12),
            bg=self.bg_color,
            fg=self.text_color
        ).grid(row=2, column=0, sticky="w", pady=5)
        
        self.conversion_type = tk.StringVar(value="Single")
        type_options = ["Single", "All Scales"]
        type_combobox = ttk.Combobox(
            input_frame, 
            textvariable=self.conversion_type,
            values=type_options,
            state="readonly",
            width=12
        )
        type_combobox.grid(row=2, column=1, padx=10, pady=5)
        
        # To scale selection (only for single conversion)
        self.to_scale_label = tk.Label(
            input_frame, 
            text="To Scale:", 
            font=("Arial", 12),
            bg=self.bg_color,
            fg=self.text_color
        )
        self.to_scale_label.grid(row=3, column=0, sticky="w", pady=5)
        
        self.to_scale = tk.StringVar(value="Fahrenheit")
        self.to_combobox = ttk.Combobox(
            input_frame, 
            textvariable=self.to_scale,
            values=scale_options,
            state="readonly",
            width=12
        )
        self.to_combobox.grid(row=3, column=1, padx=10, pady=5)
        
        # Bind events
        type_combobox.bind('<<ComboboxSelected>>', self.toggle_to_scale)
        
        # Convert button
        button_frame = tk.Frame(self.root, bg=self.bg_color)
        button_frame.pack(pady=20)
        
        convert_btn = tk.Button(
            button_frame,
            text="Convert Temperature",
            command=self.convert_temperature,
            bg=self.button_color,
            fg="white",
            font=("Arial", 12, "bold"),
            padx=20,
            pady=10,
            cursor="hand2"
        )
        convert_btn.pack()
        
        # Results Section
        results_frame = tk.Frame(self.root, bg=self.bg_color)
        results_frame.pack(pady=20, padx=40, fill="both", expand=True)
        
        tk.Label(
            results_frame, 
            text="Results:", 
            font=("Arial", 14, "bold"),
            bg=self.bg_color,
            fg=self.text_color
        ).pack(anchor="w")
        
        self.results_text = tk.Text(
            results_frame,
            height=8,
            width=50,
            font=("Arial", 11),
            bg="white",
            fg=self.text_color,
            relief="solid",
            bd=1
        )
        self.results_text.pack(fill="both", expand=True, pady=10)
        
        # Clear button
        clear_btn = tk.Button(
            results_frame,
            text="Clear Results",
            command=self.clear_results,
            bg="#ff6b6b",
            fg="white",
            font=("Arial", 10),
            padx=15,
            pady=5
        )
        clear_btn.pack(anchor="e")
        
        # Set focus to entry field
        self.temp_entry.focus()
    
    def toggle_to_scale(self, event=None):
        if self.conversion_type.get() == "All Scales":
            self.to_scale_label.grid_remove()
            self.to_combobox.grid_remove()
        else:
            self.to_scale_label.grid()
            self.to_combobox.grid()
    
    def validate_input(self):
        try:
            temperature = float(self.temp_var.get())
            return temperature
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number for temperature.")
            return None
    
    def convert_temperature(self):
        temperature = self.validate_input()
        if temperature is None:
            return
        
        from_scale = self.from_scale.get()
        conversion_type = self.conversion_type.get()
        
        self.results_text.delete(1.0, tk.END)
        
        if conversion_type == "All Scales":
            self.convert_to_all_scales(temperature, from_scale)
        else:
            to_scale = self.to_scale.get()
            self.convert_single(temperature, from_scale, to_scale)
    
    def convert_single(self, temperature, from_scale, to_scale):
        if from_scale == to_scale:
            result = temperature
        else:
            if from_scale == "Celsius":
                if to_scale == "Fahrenheit":
                    result = self.celsius_to_fahrenheit(temperature)
                else:  # Kelvin
                    result = self.celsius_to_kelvin(temperature)
            elif from_scale == "Fahrenheit":
                if to_scale == "Celsius":
                    result = self.fahrenheit_to_celsius(temperature)
                else:  # Kelvin
                    result = self.fahrenheit_to_kelvin(temperature)
            else:  # Kelvin
                if to_scale == "Celsius":
                    result = self.kelvin_to_celsius(temperature)
                else:  # Fahrenheit
                    result = self.kelvin_to_fahrenheit(temperature)
        
        # Display result
        result_text = f"{temperature:.2f}° {from_scale[0]} = {result:.2f}° {to_scale[0]}\n\n"
        result_text += f"Detailed Conversion:\n"
        result_text += f"Input: {temperature:.6f} {from_scale}\n"
        result_text += f"Output: {result:.6f} {to_scale}"
        
        self.results_text.insert(tk.END, result_text)
    
    def convert_to_all_scales(self, temperature, from_scale):
        if from_scale == "Celsius":
            c = temperature
            f = self.celsius_to_fahrenheit(c)
            k = self.celsius_to_kelvin(c)
        elif from_scale == "Fahrenheit":
            f = temperature
            c = self.fahrenheit_to_celsius(f)
            k = self.celsius_to_kelvin(c)
        else:  # Kelvin
            k = temperature
            c = self.kelvin_to_celsius(k)
            f = self.celsius_to_fahrenheit(c)
        
        # Display results
        result_text = f"Complete Temperature Conversion:\n\n"
        result_text += f"Input: {temperature:.2f}° {from_scale[0]}\n\n"
        result_text += f"{'Scale':<12} {'Temperature':<15}\n"
        result_text += "-" * 30 + "\n"
        result_text += f"{'Celsius':<12} {c:.6f}° C\n"
        result_text += f"{'Fahrenheit':<12} {f:.6f}° F\n"
        result_text += f"{'Kelvin':<12} {k:.6f} K\n\n"
        result_text += f"Conversion Formulas:\n"
        
        if from_scale == "Celsius":
            result_text += f"Fahrenheit = (Celsius × 9/5) + 32\n"
            result_text += f"Kelvin = Celsius + 273.15"
        elif from_scale == "Fahrenheit":
            result_text += f"Celsius = (Fahrenheit - 32) × 5/9\n"
            result_text += f"Kelvin = Celsius + 273.15"
        else:  # Kelvin
            result_text += f"Celsius = Kelvin - 273.15\n"
            result_text += f"Fahrenheit = (Celsius × 9/5) + 32"
        
        self.results_text.insert(tk.END, result_text)
    
    def clear_results(self):
        self.results_text.delete(1.0, tk.END)
        self.temp_var.set("")
        self.temp_entry.focus()

def main():
    try:
        root = tk.Tk()
        app = TemperatureConverterApp(root)
        root.mainloop()
    except Exception as e:
        print(f"Error starting application: {e}")

if __name__ == "__main__":
    main()