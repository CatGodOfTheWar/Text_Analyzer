from tkinter import *
from tkinter import filedialog as fd

data = ""

big_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
small_found = []
big_found = []


def find_words(data_):
    make_word = ""
    letters = []
    total_letters = 0
    count = 0
    for char in data_:
        if char != " " and char != "!" and char != "?" and char != "." and char != ",":
            if not char.isdigit():
                letters.append(char)
                total_letters += 1
                make_word += char.strip()
        else:

            if make_word.isalpha() or "'" in make_word:
                count += 1
            make_word = ""
    find_letters(letters, total_letters)
    words_nr_label.config(text=f"{count}")


def find_phrases(data_):
    count = 0
    for char in data_:
        if char == "." or char == "?" or char == "!":
            count += 1
    phrases_nr_label.config(text=f"{count}")


def find_cnp_phone_numbers(data_):
    make_nr = []
    cnp = []
    phone = []
    data_ = list(data_)
    for char in data_:
        if char != " " and char != "!" and char != "?" and char != "." and char != "," and not char.isalpha() and\
                char != "'" and char != "\n":
            make_nr.append(int(char))
        else:
            if len(make_nr) > 10:
                cnp.append(make_nr)
            if len(make_nr) > 2:
                if make_nr[0] == 0 and make_nr[1] == 7 and len(make_nr) == 10:
                    phone.append(make_nr)
            make_nr = []
    cnp_nr_label.config(text=f"{identical(cnp)}")
    phone_nr_label.config(text=f"{identical(phone)}")


def find_letters(letters, number_letters):
    global big_letters
    global small_letters
    global small_found
    global big_found
    count = 0
    big_let_found = []
    small_let_found = []
    for char in big_letters:
        for index in letters:
            if char == index:
                count += 1
        count = round((count / number_letters) * 100, 2)
        big_let_found.append(count)
        count = 0
    count = 0
    for char in small_letters:
        for index in letters:
            if char == index:
                count += 1
        count = round((count / number_letters) * 100, 2)
        small_let_found.append(count)
        count = 0
    big_found = big_let_found
    small_found = small_let_found


def identical(list_):
    count = 0
    i = 0
    j = 1
    length = len(list_)
    if length > 1:
        while i < length:
            while j < length:
                if list_[i] != list_[j]:
                    count += 1
                j += 1
            j = i + 1
            i += 1
        if count == 0:
            count = 1
    else:
        count = 1
    return count


def select_file():
    global data
    filetypes = (('text file', '.txt'), ('All files', '*.*'))

    content = fd.askopenfile(title='Open files', initialdir='/', filetypes=filetypes)
    data = content.read()


def create_letters():
    global big_found
    global small_found
    global big_letters
    global small_letters
    row, column = 0, 0 
    letters = zip(big_letters, small_letters)
    percent = zip(big_found, small_found)
    combine = zip(letters, percent)
    for i in combine:
        label_letter = Label(letters_frame, text=f"{i[0][0]}/{i[0][1]} : {i[1][0]}% / {i[1][1]}%", padx=10, pady=10,
                             font=("Times New Roman", 15), bg="#4B2142", fg="#8CC7A1")
        label_letter.grid(row=row, column=column)
        if column > 2:
            column = -1
            row += 1
        column += 1


def submit():
    main()


def main():
    global data
    find_words(data)
    find_phrases(data)
    find_cnp_phone_numbers(data)
    create_letters()


if __name__ == '__main__':
    window = Tk()
    window.geometry("1200x1000")
    window.title("Text Analyzer")
    window.resizable(False, False)
    window.config(bg="#816E94")

    frame_btn = Frame(window, bg="#4B2142", pady=15, padx=15)
    frame_btn.place(x=100, y=100)

    open_btn = Button(frame_btn, text="Choose the file!", command=select_file, font=('Ink Free', 30), borderwidth=0,
                      border=0, bg='#8CC7A1', fg='#4B2142', activebackground='#97EAD2', activeforeground='#4B2142')
    open_btn.pack()

    space_label = Label(frame_btn, borderwidth=0, border=0, bg="#4B2142")
    space_label.pack()

    submit_btn = Button(frame_btn, text="Apply!", command=submit, font=('Ink Free', 25), borderwidth=0, border=0,
                        bg='#8CC7A1', fg='#4B2142', activebackground='#97EAD2', activeforeground='#4B2142')
    submit_btn.pack()

    frame_output = Frame(window, bg="#4B2142", pady=15, padx=15)
    frame_output.place(x=700, y=100)

    words_label = Label(frame_output, text="Word Numbers:   ", font=('Times New Roman', 19), fg="#8CC7A1", bg="#4B2142")
    words_label.grid(row=0, column=0)

    phrases_label = Label(frame_output, text="Phrases Numbers:   ", font=('Times New Roman', 19), fg="#8CC7A1",
                          bg="#4B2142")
    phrases_label.grid(row=1, column=0)

    cnp_label = Label(frame_output, text="Unique CNP:   ", font=('Times New Roman', 19), fg="#8CC7A1", bg="#4B2142")
    cnp_label.grid(row=2, column=0)

    phone_label = Label(frame_output, text="Unique Phone Nr:   ", font=('Times New Roman', 19), fg="#8CC7A1",
                        bg="#4B2142")
    phone_label.grid(row=3, column=0)
    
    words_nr_label = Label(frame_output, text="None", font=('Times New Roman', 19), fg="#97EAD2", bg="#4B2142")
    words_nr_label.grid(row=0, column=1)

    phrases_nr_label = Label(frame_output, text="None", font=('Times New Roman', 19), fg="#97EAD2", bg="#4B2142")
    phrases_nr_label.grid(row=1, column=1)

    cnp_nr_label = Label(frame_output, text="None", font=('Times New Roman', 19), fg="#97EAD2", bg="#4B2142")
    cnp_nr_label.grid(row=2, column=1)

    phone_nr_label = Label(frame_output, text="None", font=('Times New Roman', 19), fg="#97EAD2", bg="#4B2142")
    phone_nr_label.grid(row=3, column=1)

    letters_frame = Frame(window, bg="#4B2142")
    letters_frame.place(x=60, y=400)


    
    window.mainloop()
