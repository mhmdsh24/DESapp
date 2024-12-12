
from tkinter import END,messagebox,PhotoImage
import customtkinter
import desv2
from PIL import Image,ImageTk
import sqlite3




class DESApp:
    def __init__(self, root):
        self.root = root

        # Set appearance and theme
        customtkinter.set_appearance_mode("light")  # Use "light" or "dark" mode
        self.root.title("DES Teacher")
        self.root.geometry("1270x700")
        customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
        #customtkinter.set_default_color_theme("assets/violet.json")
        # Configure the grid layout for the main window
        self.root.grid_rowconfigure(0, weight=0)  # Adjust row weight for resizing
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=0)

        self.root.grid_columnconfigure(0, weight=1)  # Left column (history)
        self.root.grid_columnconfigure(1, weight=1,uniform='a')  # Center column (input and result)
        self.root.grid_columnconfigure(2, weight=1,uniform='a')
        self.root.grid_columnconfigure(3, weight=1,uniform='a')
        self.root.grid_columnconfigure(4, weight=1,uniform='a')
        # Initialize database
        self.setup_database()
        
        
        
        # Light/Dark Mode Switch
        self.theme_switch = customtkinter.CTkSwitch(
            self.root, text="",command=self.toggle_theme, font=("Leelawadee UI", 14)
        )
        self.theme_switch.grid(row=0, column=4, sticky="ne",padx=5)         
        current_mode = customtkinter.get_appearance_mode()
        if current_mode == "Dark":
            self.theme_switch.select()
            self.theme_switch.configure(text='Dark Mode')
        else:
            self.theme_switch.deselect()
            self.theme_switch.configure(text='Light Mode')        
        
        # Theme select
        self.dropdown = customtkinter.CTkOptionMenu(
            self.root, values=["violet", "rime", "coffee", "breeze", "orange", "midnight", "autumn", "metal", "cherry", "carrot"],
            command=self.set_theme)
        self.dropdown.set("Select a Theme")
        self.dropdown.grid(row=0, column=4, sticky="ne",padx=5,pady=(25,0))
        self.dropdown.grid_propagate(False)

        


        # Intro
        titlefont = customtkinter.CTkFont("Leelawadee UI", 30, weight="bold",)
        self.intro = customtkinter.CTkTextbox(self.root, wrap="word",
                    font=("Leelawadee UI", 15),fg_color="transparent",bg_color="transparent",height=165)
        self.intro.grid(row=0,columnspan=2,column=0,sticky="nsew",padx=10)
        self.intro.grid_propagate(False)
        self.intro.insert("end","Welcome to DES Teacher!","titlefont")
        self.intro.insert("end","\nDiscover the fascinating world of cryptography with our step-by-step guide to the Data Encryption Standard (DES).\nEnter a 64-bit message or any text and key, and we'll guide you step by step through the encryption and decryption process.\nLet's get started!")
        self.intro.tag_config("titlefont", cnf={"font": titlefont})
        self.intro.configure(state="disabled")

        
        # Input Frame
        self.input_tabview = customtkinter.CTkTabview(self.root)
        self.input_tabview.grid(row=0, column=2,columnspan=2, sticky='new', padx=5, pady=(10,5))
        
        
        self.input_frame = self.input_tabview.add("Normal Hex")
        self.input_frame.grid_rowconfigure(0, weight=0,uniform='a')
        self.input_frame.grid_rowconfigure(1, weight=0,uniform='a')
        self.input_frame.grid_rowconfigure(2, weight=0,uniform='a')
        self.input_frame.grid_columnconfigure(0, weight=1,uniform='a')
        self.input_frame.grid_columnconfigure(1, weight=0,uniform='a')
        self.input_frame.grid_columnconfigure(2, weight=1,uniform='a')
        # Message Input
        self.message_label = customtkinter.CTkLabel(
            self.input_frame, text="Message (Hexadecimal):", 
            font=("Leelawadee UI", 20, "bold"))
        self.message_label.grid(row=0, column=0, pady=0,sticky='e')  # Align to the right

        self.message_entry = customtkinter.CTkEntry(
            self.input_frame, justify='center', placeholder_text="0000000000000000", 
            font=("Leelawadee UI", 18), width=200,height=30)
        self.message_entry.grid(row=0, column=1, padx=5, pady=0)
        self.setup_hex_entry(self.message_entry)

        # Key Input
        self.key_label = customtkinter.CTkLabel(
            self.input_frame, text="Key (Hexadecimal):", 
            font=("Leelawadee UI", 20, "bold"))
        self.key_label.grid(row=1, column=0, pady=0,sticky='e')

        self.key_entry = customtkinter.CTkEntry(
            self.input_frame, justify='center', placeholder_text="0000000000000000", 
            font=("Leelawadee UI", 18), width=200,height=30)
        self.key_entry.grid(row=1, column=1, padx=5, pady=0)
        self.setup_hex_entry(self.key_entry)

        # Buttons next to inputs
        self.encrypt_button = customtkinter.CTkButton(
            self.input_frame, text="Encrypt", command=lambda: self.process(desv2.encrypt),
            font=("Leelawadee UI", 15,'bold'))
        self.encrypt_button.grid(row=0, column=2,sticky="w")

        self.decrypt_button = customtkinter.CTkButton(
            self.input_frame, text="Decrypt", command=lambda: self.process(desv2.decrypt),
            font=("Leelawadee UI", 15, "bold"))
        self.decrypt_button.grid(row=1, column=2,sticky="w")

        # Reset Button below
        self.reset_button = customtkinter.CTkButton(
            self.input_frame, text="Reset", command=self.reset,
            font=("Leelawadee UI", 15, "bold"))
        self.reset_button.grid(row=2, column=1, padx=5,pady=10)  # Centered below both inputs

        
        
        self.txtinput_frame = self.input_tabview.add("Normal Text")
        self.txtinput_frame.grid_rowconfigure(0, weight=0,uniform='a')
        self.txtinput_frame.grid_rowconfigure(1, weight=0,uniform='a')
        self.txtinput_frame.grid_rowconfigure(2, weight=0,uniform='a')
        self.txtinput_frame.grid_columnconfigure(0, weight=1,uniform='a')
        self.txtinput_frame.grid_columnconfigure(1, weight=0,uniform='a')
        self.txtinput_frame.grid_columnconfigure(2, weight=1,uniform='a')

        # Message Input
        self.message_labeltxt = customtkinter.CTkLabel(
            self.txtinput_frame, text="Message:", 
            font=("Leelawadee UI", 20, "bold"))
        self.message_labeltxt.grid(row=0, column=0, pady=0,sticky='e')  # Align to the right

        self.message_entrytxt = customtkinter.CTkEntry(
            self.txtinput_frame, justify='center', 
            font=("Leelawadee UI", 18), width=200,height=30)
        self.message_entrytxt.grid(row=0, column=1, padx=5, pady=0)
        # Key Input
        self.key_labeltxt = customtkinter.CTkLabel(
            self.txtinput_frame, text="Key (Hexadecimal):", 
            font=("Leelawadee UI", 20, "bold"))
        self.key_labeltxt.grid(row=1, column=0, pady=0,sticky='e')

        self.key_entrytxt = customtkinter.CTkEntry(
            self.txtinput_frame, justify='center', placeholder_text='0000000000000000',
            font=("Leelawadee UI", 18), width=200,height=30)
        self.key_entrytxt.grid(row=1, column=1, padx=5, pady=0)
        self.setup_hex_entry(self.key_entrytxt)

        # Buttons next to inputs
        self.encrypt_buttontxt = customtkinter.CTkButton(
            self.txtinput_frame, text="Encrypt", command=lambda: self.process(desv2.encrypt_sentence),
            font=("Leelawadee UI", 15,'bold'))
        self.encrypt_buttontxt.grid(row=0, column=2,sticky="w")

        self.decrypt_buttontxt = customtkinter.CTkButton(
            self.txtinput_frame, text="Decrypt", command=lambda: self.process(desv2.decrypt_sentence),
            font=("Leelawadee UI", 15, "bold"))
        self.decrypt_buttontxt.grid(row=1, column=2,sticky="w")

        # Reset Button below
        self.reset_buttontxt = customtkinter.CTkButton(
            self.txtinput_frame, text="Reset", command=self.reset,
            font=("Leelawadee UI", 15, "bold"))
        self.reset_buttontxt.grid(row=2, column=1, padx=5,pady=10)  # Centered below both inputs


        # History Frame on the left
        self.history_frame = customtkinter.CTkScrollableFrame(self.root, width=225,
            label_text="History",label_font=("Leelawadee UI", 22, "bold"))
        self.history_frame.grid(row=1, column=0,  sticky="nsew", padx=5, pady=5)
        self.history_frame.grid_rowconfigure(0, weight=1)
        self.history_frame.grid_columnconfigure(0, weight=1)
        self.clear_history_button = customtkinter.CTkButton(
            self.root, text="Clear History", command=self.clear_history,
            font=("Leelawadee UI", 14, "bold")
        )
        self.clear_history_button.grid(column=0,row=3,padx=5,pady=(0,5),sticky='nsew')
        # Refresh history
        self.load_history()





        # Final Result Frame
        self.final_result_frame = customtkinter.CTkFrame(self.root)
        self.final_result_frame.grid(row=1, column=1,rowspan=3,columnspan=4, 
                                     sticky="nsew", padx=5, pady=5)
        self.final_result_frame.grid_rowconfigure(0,weight=0)
        self.final_result_frame.grid_rowconfigure(1,weight=0)
        self.final_result_frame.grid_rowconfigure(2,weight=1)
        self.final_result_frame.grid_columnconfigure(0, weight=1)
        
        self.final_result_label = customtkinter.CTkLabel(
            self.final_result_frame, text="Final Result:", 
            font=("Leelawadee UI" ,26, "bold"))
        self.final_result_label.grid(row=0,column=0,pady=10,sticky='n')

        self.final_result_value = customtkinter.CTkLabel(
            self.final_result_frame, text=str(), 
            font=("Leelawadee UI", 22), wraplength=780, anchor="center")
        self.final_result_value.grid(row=1,column=0,pady=5,sticky='n')
        
        # Add a Copy to Clipboard Button
        copy_button = customtkinter.CTkButton(
            self.final_result_frame, text=str(), 
            image=customtkinter.CTkImage(Image.open("assets/copyw.png"),size=(25,25)),
            command=self.copy_to_clipboard, width=30, height=30)
        copy_button.grid(row=1,column=0,sticky='ne', padx=10, pady=10) 
        
        #show detials button
        self.details_button = customtkinter.CTkButton(
            self.final_result_frame, text="Show Details", command=self.details,
            font=("Leelawadee UI", 10, "bold"), width=50, height=25)
        self.details_button.grid(row=0,column=0,sticky='nw',pady=15,padx=15)
        
        self.final_result_frame.grid_propagate(False)

        # Load images once during initialization
        try:
            self.pc1table = ImageTk.PhotoImage(Image.open("assets/pc1table.jpg"))
            self.shifttable = ImageTk.PhotoImage(Image.open("assets/shifttable.jpg"))
            self.pc2table = ImageTk.PhotoImage(Image.open("assets/pc2table.jpg"))
            self.etable = ImageTk.PhotoImage(Image.open("assets/etable.jpg"))
            self.sboxes = ImageTk.PhotoImage(Image.open("assets/sboxes.jpg"))
            self.ptable = ImageTk.PhotoImage(Image.open("assets/ptable.jpg"))
            self.inviptable = ImageTk.PhotoImage(Image.open("assets/inviptable.jpg"))
            self.iptable = ImageTk.PhotoImage(Image.open("assets/iptable.jpg"))
        except FileNotFoundError as e:
            print(f"Error loading image: {e}")
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)


    def keymsgtabs(self,place):
        # Tabs for operation
        self.tab_view = customtkinter.CTkTabview(master=place)
        self.tab_view.grid_forget()
        # Add tabs
        self.key_rounds_tab = self.tab_view.add("Key Rounds")
        self.rounds_tab = self.tab_view.add("Message Rounds")
        

    def binary_format(self,input_string):
        return ' '.join(input_string[i:i+4] for i in range(0, len(input_string), 4))

    def setup_hex_entry(self, entry_widget, max_length=16):
      
        def on_validate_input(new_value):
            """Validate and enforce constraints on input."""
            if len(new_value) > max_length:
                show_error_message("Input too long!")
                return False  # Disallow input if exceeding max length
            return True

        def on_key_press(event):
            if event.keysym in ["BackSpace", "Delete"]:
                return  # Allow deleting
            key = event.char
            if key not in "0123456789abcdefABCDEF":  # Only allow hex characters
                show_error_message("Enter Valid HEX\n[0-9][A-F]")
                return "break"
            return True
        
        def convert_to_uppercase(event):  #Dynamically convert the Entry widget content to uppercase.
            widget = event.widget  # Get the widget that triggered the event
            current_text = widget.get()
            widget.delete(0, "end")  # Clear the Entry widget
            widget.insert(0, current_text.upper())
        
        def show_error_message(message):
            if entry_widget == self.message_entry:
                error_label = customtkinter.CTkLabel(self.input_frame, text=message, text_color="red",font=("Leelawadee UI",12))
                error_label.grid(row=0, column=2,padx=(0,50),pady=5,sticky='e')  # Show next to Message entry
            elif entry_widget == self.key_entry:
                error_label = customtkinter.CTkLabel(self.input_frame, text=message, text_color="red")
                error_label.grid(row=1, column=2,padx=(0,50),pady=5,sticky='e')  # Show next to Key entry
            elif entry_widget == self.key_entrytxt:
                error_label = customtkinter.CTkLabel(self.input_tabview.tab("Normal Text"), text=message, text_color="red")
                error_label.grid(row=1, column=2,padx=(0,40),pady=5,sticky='e')  # Show next to Key entry            
            # Clear the error after 3 seconds
            self.root.after(3000, lambda: error_label.grid_forget())

        # Bind events
        entry_widget.bind("<Key>", on_key_press)
        entry_widget.bind("<KeyRelease>", convert_to_uppercase)

        # Validate input to ensure length constraint
        validate_command = entry_widget.register(on_validate_input)
        entry_widget.configure(validate="key", validatecommand=(validate_command, "%P"))

    def reset(self):
        self.message_entry.delete(0, END)
        self.key_entry.delete(0, END)
        self.message_entrytxt.delete(0,END)
        self.key_entrytxt.delete(0,END)
        if self.details_button.cget('text') == 'Hide Details':
            if hasattr(self, 'blocks_tab_view') and self.blocks_tab_view.winfo_exists():
                self.blocks_tab_view.grid_forget()
            if hasattr(self, 'tab_view') and self.tab_view.winfo_exists():
                self.tab_view.grid_forget()
            self.details_button.configure(text='Show Details')
        self.final_result_value.configure(text=str())
        if hasattr(self, 'tab_view') and self.tab_view.winfo_exists():
            self.tab_view.destroy()
            print("reset tabview destroyed")
        if hasattr(self, 'blocks_tab_view') and self.blocks_tab_view.winfo_exists():
            self.blocks_tab_view.destroy()
            print("reset blocktabview destroyed")

 
    def process(self, operation):
        if self.details_button.cget('text') == 'Hide Details':
            if hasattr(self, 'blocks_tab_view') and self.blocks_tab_view.winfo_exists():
                self.blocks_tab_view.grid_forget()
            if hasattr(self, 'tab_view') and self.tab_view.winfo_exists():
                self.tab_view.grid_forget()
            self.details_button.configure(text='Show Details')
        self.final_result_value.configure(text=str())


        if hasattr(self, 'tab_view') and self.tab_view.winfo_exists():
            self.tab_view.destroy()
            print("tabview destroyed")        
        if hasattr(self, 'blocks_tab_view') and self.blocks_tab_view.winfo_exists():
            self.blocks_tab_view.destroy()
            print("block destroyed")

        
        if self.input_tabview.get()=="Normal Hex":
            self.keymsgtabs(self.final_result_frame) 
            # Get and validate inputs
            message = self.message_entry.get().ljust(16, '0')
            key = self.key_entry.get().ljust(16, '0')
            if key=="0000000000000000"and message=="0000000000000000":
                error_label = customtkinter.CTkLabel(self.input_frame, text="Key and message\ncannot be zero", text_color="red")
                error_label.grid(row=0, column=2,padx=(0,35),pady=5,sticky='e')  # Show next to Key entry
            # Clear the error after 3 seconds
                self.root.after(3000, lambda: error_label.grid_forget())
                return
            result, rounds = operation(message, key)
            rkb , key_rounds = desv2.key_gen(key)
            # Update result
            self.final_result_value.configure(text=str(result))
            # Populate rounds tab
            self.populate_rounds_tab(result ,rounds, rkb, key_rounds,operation)
            # Save operation to history
            operation_name = "Encrypt" if operation == desv2.encrypt else "Decrypt"
            self.save_to_history(message, key, result, operation_name)

        elif self.input_tabview.get()=="Normal Text":
            self.blocks_tab_view = customtkinter.CTkTabview(self.final_result_frame)
            self.blocks_tab_view.grid_forget()
            # Get and validate inputs
            sentence = self.message_entrytxt.get()
            if len(sentence)<16:
                sentence = self.message_entrytxt.get().ljust(16,"0")
            key = self.key_entrytxt.get().ljust(16,'0')
            if key=="0000000000000000"and sentence=="0000000000000000":
                error_label = customtkinter.CTkLabel(self.input_tabview.tab("Normal Text"), text="Key and message\ncannot be zero", text_color="red")
                error_label.grid(row=0, column=2,padx=(0,35),pady=5,sticky='e')  # Show next to Key entry
            # Clear the error after 3 seconds
                self.root.after(3000, lambda: error_label.grid_forget())
                return
            result1, blocks = operation(sentence, key)
            rkb , key_rounds = desv2.key_gen(key)
            # Update result
            self.final_result_value.configure(text=str(result1))
            fromdesv2 = desv2.encrypt if operation == desv2.encrypt_sentence else desv2.decrypt
            self.populate_sentence_rounds_tab(sentence, blocks, key, fromdesv2)
            operation_name = "Encrypt Sentence" if operation == desv2.encrypt_sentence else "Decrypt Sentence"
            self.save_to_history(sentence, key, result1, operation_name)
    
    def on_closing(self):
        """Handle the window close event."""
        self.conn.close()
        self.root.destroy()


    def populate_rounds_tab(self, cipher_text ,rounds, rkb, key_rounds, operation):
        self.kr_tab_view = customtkinter.CTkTabview(self.key_rounds_tab)
        self.kr_tab_view.pack(fill="both", expand=True)
        self.r_tab_view = customtkinter.CTkTabview(self.rounds_tab)
        self.r_tab_view.pack(fill="both", expand=True)
        
        # key rounds
        # round 0
        key_round_0 = self.kr_tab_view.add("Round 0")
        kr0_text_box = customtkinter.CTkTextbox(key_round_0, wrap="word",font=("Leelawadee UI", 15))
        kr0_text_box.pack(fill="both", expand=True)

        titlefont = customtkinter.CTkFont("Leelawadee UI", 25, weight="bold")
        headerfont = customtkinter.CTkFont("Leelawadee UI", 20, weight="bold")

        kr0_text_box.insert("end", "Round 0: Preprocessing", "titlefont")
        kr0_text_box.insert("end", "\nStep 1: Convert to Binary", "headerfont")
        kr0_text_box.insert("end", f"\nKey in binary (64-bit):\n{self.binary_format(key_rounds[0]['Key'])}")
        kr0_text_box.insert("end", "\n\nStep 2: Permute the Key according to PC-1 Table", "headerfont")
        kr0_text_box.insert("end", "\nShuffle bits according to PC-1:\n\n")
        kr0_text_box._textbox.image_create("end", image=self.pc1table)
        kr0_text_box.insert("end", f"\n\nKey after PC-1 (56-bit):\n{self.binary_format(key_rounds[0]['Key after PC1'])}")

        kr0_text_box.tag_config("titlefont", cnf={"font": titlefont})
        kr0_text_box.tag_config("headerfont", cnf={"font": headerfont})
        kr0_text_box.configure(state="disabled")

        # Rest of rounds

        for i in range(1, 17):
            key_rounds_tab = self.kr_tab_view.add(f"Round {i}")
            text_box = customtkinter.CTkTextbox(key_rounds_tab,wrap="word", font=("Leelawadee UI", 15))
            text_box.pack(fill="both", expand=True)

            text_box.insert("end", f"Round {i}", "titlefont")
            text_box.insert("end", "\nStep 1: Scheduled Left Circular Shift ", "headerfont")
            text_box.insert("end",f"\nSplit the key into two halves Ci (left) and Di (right), then left rotate each by 1 or 2 bits according to the table:\n\n")
            text_box._textbox.image_create("end", image=self.shifttable)
            text_box.insert("end",f"\n\nIn this round, left rotate by {desv2.shift_table[i-1]}:\nC{i} = {self.binary_format(key_rounds[i]['Left Half'])}\nD{i} = {self.binary_format(key_rounds[i]['Right Half'])}")
            text_box.insert("end", "\n\nStep 2: Concatenate Halves and Permute Through PC-2 Table", "headerfont")
            text_box.insert("end",f"\nAfter concatenation, the key becomes:\n{self.binary_format(key_rounds[i]['Left Half'] + key_rounds[i]['Right Half'])}\n\nPermute the concatenated key according to the PC-2 table:\n\n")
            text_box._textbox.image_create("end", image=self.pc2table)
            text_box.insert("end",f"\n\nRound {i} Key (48-bit): {self.binary_format(key_rounds[i]['Round Key (Binary)'])}\nRound {i} Key (Hex): {key_rounds[i]['Round Key (Hexadecimal)']}")

            text_box.tag_config("titlefont", cnf={"font": titlefont})
            text_box.tag_config("headerfont", cnf={"font": headerfont})
            text_box.configure(state="disabled")  # Make text read-only

        key_summary = self.kr_tab_view.add("Summary")
        key_sum_box = customtkinter.CTkTextbox(key_summary,wrap="word", font=("Leelawadee UI", 15))
        key_sum_box.pack(fill="both", expand=True)
        key_sum_box.insert("end", "Round Keys (48-bit)", "titlefont")
        for i in range(16):
            key_sum_box.insert("end", f"\nK{i+1} = {self.binary_format(rkb[i])}")
        key_sum_box.tag_config("titlefont", cnf={"font": titlefont})
        key_sum_box.configure(state="disabled")

        


        # text rounds
        # round 0
        msg_round_0 = self.r_tab_view.add("Round 0")
        msg0_text_box = customtkinter.CTkTextbox(msg_round_0, wrap="word",font=("Leelawadee UI", 15))
        msg0_text_box.pack(fill="both", expand=True)

        titlefont = customtkinter.CTkFont("Leelawadee UI", 25, weight="bold")
        headerfont = customtkinter.CTkFont("Leelawadee UI", 20, weight="bold")
        
        msg0_text_box.insert("end", "Round 0: Preprocessing", "titlefont")
        msg0_text_box.insert("end", "\nStep 1: Convert to Binary", "headerfont")
        msg0_text_box.insert("end", f"\nMessage in binary (64-bit):\n{self.binary_format(rounds[0]['Message'])}")
        msg0_text_box.insert("end", "\n\nStep 2: Permute the Message Through the IP Table", "headerfont")
        msg0_text_box.insert("end", "\nShuffle bits according to IP:\n\n")
        msg0_text_box._textbox.image_create("end", image=self.iptable)
        msg0_text_box.insert("end", f"\n\nMessage after IP (64-bit):\n{self.binary_format(rounds[0]['Message after IP'])}")
        msg0_text_box.insert("end", "\n\nStep 3: Split the Permuted Key into 2 Halves", "headerfont")
        msg0_text_box.insert("end", f"\nWe get (32-bit):\nL0: {self.binary_format(rounds[0]['Left'])}\nR0: {self.binary_format(rounds[0]['Right'])}")

        msg0_text_box.tag_config("titlefont", cnf = {"font": titlefont})
        msg0_text_box.tag_config("headerfont", cnf = {"font": headerfont})
        msg0_text_box.configure(state="disabled")
        
        # rest of rounds

        for i in range(1,17):
            rounds_tab = self.r_tab_view.add(f"Round {i}")
            text_box = customtkinter.CTkTextbox(rounds_tab, wrap="word",font=("Leelawadee UI", 15))
            text_box.pack(fill="both", expand=True)
            
            text_box.insert("end", f"Round {i}", "titlefont")
            text_box.insert("end", f"\nStep 1: Right Expansion", "headerfont")
            text_box.insert("end", f"\nExpand R{i-1} from 32 bits to 48 bits according to the Expansion Table:\n\n")
            text_box._textbox.image_create("end", image=self.etable)
            text_box.insert("end", f"\n\nExpanded Right Half E(R{i-1}) (48-bit):\n{self.binary_format(rounds[i]['Right Expanded'])}")
            text_box.insert("end", f"\n\nStep 2: XOR with Round Key", "headerfont")
            text_box.insert("end", f"\nExpanded R{i-1}:        {self.binary_format(rounds[i]['Right Expanded'])}\nRound {i} Key:     ⊕ {self.binary_format(rkb[i-1])}\n                              ________________________________________________________________________\nWe get:                 {self.binary_format(rounds[i]['XOR with Key'])}")
            text_box.insert("end", f"\n\nStep 3: S-Box Substitution", "headerfont")
            text_box.insert("end", f"\nIn S-Box Substitution, 8 S-Boxes map 6 bits to 4 bits:\nBits 1-6 goes to S-Box 1\nBits 7-12 goes to S-Box 2\nBits 13-18 goes to S-Box 3\n.\n.\n.\nBits 43-48 goes to S-Box 8\nThe 1st and 6th bits determine the row in the S-Box table, while the middle 4 bits determine the column.\n\n")
            text_box._textbox.image_create("end", image=self.sboxes)
            text_box.insert("end", f"\n\nWe get a 32-bit result: {self.binary_format(rounds[i]['S-box Substitution'])}")
            text_box.insert("end", f"\n\nStep 4: P-Permutation", "headerfont")
            text_box.insert("end", f"\nPermute the 32-bit result according to the P-Table:\n\n")
            text_box._textbox.image_create("end", image=self.ptable)
            text_box.insert("end", f"\n\nWe get (32-bit): {self.binary_format(rounds[i]['Permutation'])}")
            text_box.insert("end", f"\n\nStep 5: XOR with Left Half", "headerfont")
            text_box.insert("end", f"\nPermuted S-Box Result:        {self.binary_format(rounds[i]['Permutation'])}\n                                  L{i-1}:    ⊕ {self.binary_format(rounds[i]['Left'])}\n                                             _________________________________________________\nWe get:                                 {self.binary_format(rounds[i]['Result'])}")
            text_box.insert("end", f"\n\nStep 6: Swap the Halves", "headerfont")
            text_box.insert("end", f"\nL{i} = R{i-1}     and     R{i} = XOR Result\n\nL{i} = {self.binary_format(rounds[i-1]['Result'])}\nR{i} = {self.binary_format(rounds[i]['Result'])}")
            
            text_box.tag_config("titlefont", cnf={"font": titlefont})
            text_box.tag_config("headerfont", cnf={"font": headerfont})
            text_box.configure(state="disabled")  # Make text read-only
        
        final_textbox = self.r_tab_view.tab("Round 16").winfo_children()[0]
        final_textbox.configure(state="normal")
        final_textbox.insert("end", f"\n\nIn the final round, concatenate the halves backwards to get:", "headerfont")
        final_textbox.insert("end", f"\nR16 + L16 = {self.binary_format(rounds[16]['Right'] + rounds[16]['Left'])}\n\nThen re-shuffle R16 + L16 according to the Inverse IP table:\n\n")
        final_textbox._textbox.image_create("end", image=self.inviptable)
        final_textbox.insert("end", f"\n\nFinally, we have completed the DES {'Encryption' if operation==desv2.encrypt else 'Decryption'}!","headerfont")
        final_textbox.insert("end", f"\n{'Ciphertext' if operation==desv2.encrypt else 'Message'} (64-bit): {self.binary_format(desv2.hex2bin(cipher_text))}\n{'Ciphertext' if operation==desv2.encrypt else 'Message'} (Hex): {cipher_text}")
        final_textbox.tag_config("headerfont", cnf={"font": headerfont})
        final_textbox.configure(state="disabled")

    def details(self):
        if self.details_button.cget('text')=='Show Details':    
            if hasattr(self, 'blocks_tab_view') and self.blocks_tab_view.winfo_exists():
                self.blocks_tab_view.grid(row=2,column=0,sticky='nsew', padx=10, pady=10)
                self.details_button.configure(text='Hide Details')
            if hasattr(self, 'tab_view'):  
                self.tab_view.grid(row=2,column=0,sticky='nsew', padx=10, pady=10)
                self.details_button.configure(text='Hide Details')
        elif self.details_button.cget('text')=='Hide Details':
            if hasattr(self, 'blocks_tab_view') and self.blocks_tab_view.winfo_exists():
                self.blocks_tab_view.grid_forget()
                self.details_button.configure(text='Show Details')
            if hasattr(self, 'tab_view'):
                self.tab_view.grid_forget()
                self.details_button.configure(text='Show Details')

    def populate_sentence_rounds_tab(self ,sentence, blocks ,key ,operation):
        explanation_tab = self.blocks_tab_view.add("Block Explanation")
        explanation_textbox = customtkinter.CTkTextbox(explanation_tab, wrap="word", font=("Leelawadee UI", 15))
        explanation_textbox.pack(fill="both", expand=True)
        titlefont = customtkinter.CTkFont("Leelawadee UI", 25, weight="bold")
        headerfont = customtkinter.CTkFont("Leelawadee UI", 20, weight="bold")
        # Populate the explanation tab
        explanation_textbox.insert("end", "How the Blocks Were Derived\n", "titlefont")
        explanation_textbox.insert("end", f"Original Sentence:", "headerfont")
        explanation_textbox.insert("end", f"\n{sentence}\n\n")
        if operation == desv2.encrypt:
            explanation_textbox.insert("end", f"Step 1: Transform to Hex:", "headerfont")
            explanation_textbox.insert("end", f"\n{desv2.sentence_to_hex(sentence)}")
        else:
            explanation_textbox.insert("end", f"Message Already in Hex", "headerfont")
        explanation_textbox.insert("end", "\n\nStep 2: Split into 16 character Blocks:\n", "headerfont")
        for i, block in enumerate(blocks):
            explanation_textbox.insert("end", f"Block {i+1}: {block}\n")
        
        explanation_textbox.tag_config("titlefont", cnf={"font": titlefont})
        explanation_textbox.tag_config("headerfont", cnf={"font": headerfont})
        explanation_textbox.configure(state="disabled")
        for i in range(len(blocks)):
            block_tab = self.blocks_tab_view.add(f"Block {i+1}")
            tab_view = customtkinter.CTkTabview(block_tab)
            tab_view.pack(fill="both", expand=True) 
            # Add tabs
            self.key_rounds_tab = tab_view.add("Key Rounds")
            self.rounds_tab = tab_view.add("Message Rounds")
                      
            print(f"block{i+1} created")
            result, rounds = operation(blocks[i], key)
            rkb , key_rounds = desv2.key_gen(key)
            self.populate_rounds_tab(result ,rounds, rkb, key_rounds,operation)
        
    def copy_to_clipboard(self):
        # Get the text from the output field
        text_to_copy = self.final_result_value.cget("text").strip()
        
        if text_to_copy:
            # Copy to the clipboard
            self.root.clipboard_clear()
            self.root.clipboard_append(text_to_copy)
            self.root.update()  # Now the clipboard content is updated
        else:
            messagebox.showwarning("No Text", "There is no text to copy.")

    def setup_database(self):
        """Initialize the SQLite database and create the table if it doesn't exist."""
        self.conn = sqlite3.connect("des_history.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                message TEXT NOT NULL,
                key TEXT NOT NULL,
                result TEXT NOT NULL,
                operation TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.conn.commit()

    def save_to_history(self, message, key, result, operation):
        self.cursor.execute("""
            INSERT INTO history (message, key, result, operation)
            VALUES (?, ?, ?, ?)
        """, (message, key, result, operation))
        self.conn.commit()
        self.load_history()

    def button_history(self, message, key, operation):
        self.reset()
        if operation == "Encrypt Sentence" or operation == "Decrypt Sentence":
            self.input_tabview.set("Normal Text")
            self.message_entrytxt.insert(0, message)
            self.key_entrytxt.insert(0, key)
        elif operation == "Encrypt" or operation == "Decrypt":
            self.input_tabview.set("Normal Hex")
            self.message_entry.insert(0, message)
            self.key_entry.insert(0, key)

    def load_history(self):
        """Load the history from the database and display it in the listbox."""
        for widget in self.history_frame.winfo_children():
            widget.destroy()
        self.cursor.execute("SELECT * FROM history ORDER BY timestamp DESC")
        rows = self.cursor.fetchall()
        for row in rows:
            operation_button = customtkinter.CTkButton(self.history_frame,
                text=f"Operation: {row[4]}\nMessage: {row[1]}\nKey: {row[2]}\nResult: {row[3]}\nTimestamp: {row[5]}",
                command=lambda msg=row[1], key=row[2], operation=row[4]: self.button_history(msg, key, operation))
            operation_button.pack(fill="x", padx=5, pady=2.5)
           
    def clear_history(self):
        """Clear all records from the history table."""
        if messagebox.askyesno("Confirm", "Are you sure you want to clear all history?"):
            self.cursor.execute("DELETE FROM history")
            self.conn.commit()
            self.load_history()
        
    def toggle_theme(self):
        """Toggle between Light and Dark mode."""
        if self.theme_switch.get():
            customtkinter.set_appearance_mode("Dark")
            self.theme_switch.configure(text='Dark Mode')
        else:
            customtkinter.set_appearance_mode("Light")
            self.theme_switch.configure(text='Light Mode')

    def set_theme(self,choice):
        customtkinter.set_default_color_theme(f"assets/{choice}.json")
        self.root.destroy()  # Close the current window

        # Create a new window and reinitialize the app
        new_root = customtkinter.CTk()
        new_app = DESApp(new_root)
        new_root.after(0, lambda:new_root.state('zoomed'))
        new_root.mainloop() 




# Main application loop
if __name__ == "__main__":
    root = customtkinter.CTk()
    app = DESApp(root)
    root.after(0, lambda:root.state('zoomed'))
    root.mainloop()
