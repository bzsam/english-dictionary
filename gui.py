import tkinter as tk
import dictionary as dt


class GUI:
    def __init__(self, frame: tk.Tk):
        """GUI for the dictionary app. Takes only one input, the Tkinter frame."""
        self.frame = frame  # Tkinter frame

        # Frame configuration
        self.frame.title("Dictionary")
        self.frame.minsize(500, 500)
        self.frame.maxsize(500, 500)
        self.frame.configure(bg="#c6d0ff")

        # Label for asking input and it's configuration
        self.label = tk.Label(self.frame, text="Give your word(s) here:")
        self.label.configure(bg="#c6d0ff")
        self.label.config(font=('Helvatical bold', 15))
        self.label.pack(pady=(50, 0))

        # Entry box and it's configuration
        self.entry = tk.Entry(justify="center", bd=0, bg="#e3ffff")
        self.entry.focus()
        self.entry.pack(pady=(20, 0))

        # Ok button and it's configuration
        self.button = tk.Button(text="Ok", command=self._get_input, bg="#e3ffff", bd=0)
        self.button.config(font=('Helvatical bold', 14))
        self.frame.bind("<Return>", self._get_input)
        self.button.pack(pady=(20, 0))

        #  Label for the current word and it's configuration
        self.dict_label_word = tk.Label(self.frame, bd=0, bg="#c6d0ff", wraplength=350)
        self.dict_label_word.config(font=('Helvatical bold', 14))
        self.dict_label_word.pack(pady=(20, 0))

        # Label for the meaning of the current word and it's configuration
        self.dict_label_meaning = tk.Label(self.frame, bd=0, bg="#c6d0ff", wraplength=350)
        self.dict_label_meaning.config(font=('Helvatical bold', 8))
        self.dict_label_meaning.pack(pady=(0, 0))

        # Clear button and it's configuration
        self.clear = tk.Button(text="Clear", command=self._full_delete, bg="#e3ffff", bd=0)
        self.clear.config(font=('Helvatical bold', 14))
        self.clear.place(x=250, y=450, anchor="center")

        # Dictionary object
        self.dictionary = dt.Dictionary()

        self.num = 0  # Current word's number
        self.entry_input = ""  # Variable to store the input
        self.len_of_dict = 0  # Number of words
        self.next = None  # Next button
        self.previous = None  # Previous button

    def _get_input(self, inp=None):
        """Takes the input from the entry, gives it to the dictionary, and then prints it with another function"""
        if len(self.dictionary.words_list) > 0:
            self._part_delete()
        self.entry_input = self.entry.get()
        self.dictionary.input(self.entry_input)
        self._print_results()

    def _print_results(self):
        """Prints the current word, and its meaning"""
        self.dictionary.word_by_word(self.num)  # Finds the self.num-th word and its meaning
        self.len_of_dict = len(self.dictionary.words_list)  # The number of words
        self.dict_label_word.config(text=f"{self.dictionary.words_list[self.num].upper()}:\n"
                                         f"Type: {self.dictionary.keys}\n")  # Prints the current word and its types
        self.dict_label_meaning.config(text=f"Meaning:\n{self.dictionary.values}")  # Prints the meaning of the current
        # word
        if self.len_of_dict != 1:  # If there are more than one word, then calls the next and previous buttons
            self._next_previous()

    def _next_previous(self):
        """Creates the next and previous buttons"""
        self.next = tk.Button(text="Next", command=self._step_up, bg="#e3ffff", bd=0)
        self.next.config(font=('Helvatical bold', 14))
        self.next.place(x=450, y=450, anchor="center")

        self.previous = tk.Button(text="Previous", command=self._step_down, bg="#e3ffff", bd=0)
        self.previous.config(font=('Helvatical bold', 14))
        self.previous.place(x=60, y=450, anchor="center")

    def _full_delete(self):
        """If the clear button is pressed, this function resets every necessary variable"""
        self.entry.delete(0, "end")
        self._part_delete()

    def _part_delete(self):
        """If ok button or enter pressed more than once without clear this function resets the necessary variables"""
        self.dict_label_word.config(text="")
        self.dict_label_meaning.config(text="")
        self.dictionary.reset()
        self.num = 0
        if self.len_of_dict > 1:
            self.next.destroy()
            self.previous.destroy()

    def _step_up(self):
        """Next button pressed, calls for the next word if it exists"""
        if self.num < self.len_of_dict - 1:
            self.num += 1
        self._print_results()

    def _step_down(self):
        """Previous button pressed, calls for the previous word if it exists"""
        if self.num > 0:
            self.num -= 1
        self._print_results()
