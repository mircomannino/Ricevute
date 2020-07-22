import tkinter as tk
from ITEMS import *
from PRINT import *

# Global configuration
window = tk.Tk()
window.geometry("540x750")
window.title("LAVANDERIA VALDELSA - Ricevute")
window.resizable(True, False)
label_font = ("Times", 11, "bold")
label_main_font = ("Times", 20, "bold")
button_add_font = ("Times", 6, "bold")
button_main_font = ("Times", 20, "bold")

# Global variables
num_total = tk.DoubleVar()
num_total.set(0.0)
str_total = tk.StringVar()
str_total.set("Totale: "+ str(num_total.get()) + "€")

item_total_list = []
button_add_list = {}
button_sub_list = {}
label_list = {}
label_counter_list = {}
label_price_list = {}

################################################################################
############################ Functions #########################################
################################################################################
def add(item):
    # Update total price
    num_total.set(num_total.get() + item.price)
    str_total.set("Totale: " + str(num_total.get()) + "€")
    # Update total list of items
    item_total_list.append(item.name)
    # Update counter of the item
    old_counter = int(label_counter_list[item.name]['text'])
    new_counter = old_counter + 1
    label_counter_list[item.name]['text'] = str(new_counter)
    print((item_total_list))

def sub(item):
    if item.name in item_total_list:
        # Update total price
        num_total.set(num_total.get() - item.price)
        str_total.set("Totale: " + str(num_total.get()) + "€")
        # Update total list of items
        item_total_list.remove(item.name)
        # Update counter of the item
        old_counter = int(label_counter_list[item.name]['text'])
        new_counter = old_counter - 1
        label_counter_list[item.name]['text'] = str(new_counter)
        print((item_total_list))

def reset():
    # Update total price
    num_total.set(0.0)
    str_total.set("Totale: " + str(num_total.get()) + "€")
    # Update total list of items
    item_total_list.clear()
    print(item_total_list)
    # Azzerro i counter
    for item_name in label_counter_list:
        label_counter_list[item_name]['text'] = "0"
    # Deal with unknownn item
    for i in range(n_unknown):
        unknown_name_entry_list[i].config(state="normal")
        unknown_name_list[i].set("")
        unknown_price_list[i].set(0.0)
        unknown_quantity_list[i].set(0)
        unknown_confirm_button_list[i].config(state="normal")
        unknown_price_add_button_list[i].config(state="normal")
        unknown_price_sub_button_list[i].config(state="normal")
        unknown_quantity_add_button_list[i].config(state="normal")
        unknown_quantity_sub_button_list[i].config(state="normal")
    # Update tmp unknown item list
    unknown_tmp_item_dict.clear()
    print(unknown_tmp_item_dict )



################################################################################
############################ Objects ###########################################
################################################################################

############################### Known item list ################################
row_index = 0
print(len(item_dict))
for key in item_dict.keys():
    item = item_dict[key]

    price_label = ' (' + str(item.price) + "€)"

    label_list[item.name] = tk.Label(window, text=item.name, font=label_font)
    button_add_list[item.name] = tk.Button(text="+", font=button_add_font, command=lambda x=item : add(x))
    button_sub_list[item.name] = tk.Button(text="-", font=button_add_font, command=lambda x=item : sub(x))
    label_counter_list[item.name] = tk.Label(window, text="0", font=label_font)
    label_price_list[item.name] = tk.Label(window, text=price_label, font=label_font)

    label_list[item.name].grid(row=row_index, column=0, padx=5)
    button_add_list[item.name].grid(row=row_index, column=1, padx=5)
    label_counter_list[item.name].grid(row=row_index, column=2, padx=5)
    button_sub_list[item.name].grid(row=row_index, column=3, padx=5)
    label_price_list[item.name].grid(row=row_index, column=4)
    row_index += 1

############################### Unknown item list ##############################
# Functions unknown
def add_quantity(index):
    unknown_quantity_list[index].set(unknown_quantity_list[index].get() + 1)

def sub_quantity(index):
    if(unknown_quantity_list[index].get() > 0):
        unknown_quantity_list[index].set(unknown_quantity_list[index].get() - 1)

def add_price(index):
    unknown_price_list[index].set(unknown_price_list[index].get() + 0.5)

def sub_price(index):
    if(unknown_price_list[index].get() > 0):
        unknown_price_list[index].set(unknown_price_list[index].get() - 0.5)

def confirm(index):
    if unknown_name_list[index].get() and unknown_quantity_list[index].get()>0 and unknown_price_list[index].get()>0 :
        # Create a new item
        new_item = Item(unknown_name_list[index].get(), unknown_price_list[index].get())
        unknown_tmp_item_dict[new_item.name] = new_item
        # Disable all the button
        unknown_confirm_button_list[index].config(state="disabled")
        unknown_price_add_button_list[index].config(state="disabled")
        unknown_price_sub_button_list[index].config(state="disabled")
        unknown_quantity_add_button_list[index].config(state="disabled")
        unknown_quantity_sub_button_list[index].config(state="disabled")
        unknown_name_entry_list[index].config(state="disabled")
        # Update total price
        num_total.set(num_total.get() + new_item.price * unknown_quantity_list[index].get())
        str_total.set("Totale: " + str(num_total.get()) + "€")
        # Update total list of items
        for i in range(unknown_quantity_list[index].get()):
            item_total_list.append(new_item.name)
        print(item_total_list)

# Unknown global variables
n_unknown = 2
start_row = 21
unknown_tmp_item_dict = {}  # Used to get the price of the new tmp item
unknown_name_list = []
unknown_quantity_list = []
unknown_price_list = []
for i in range(n_unknown):
    unknown_name_list.append(tk.StringVar())
    unknown_quantity_list.append(tk.IntVar())
    unknown_price_list.append(tk.DoubleVar())

# Create elements
unknown_name_entry_list = []
unknown_quantity_label_list = []
unknown_quantity_add_button_list = []
unknown_quantity_sub_button_list = []
unknown_price_label_list = []
unknown_price_add_button_list = []
unknown_price_sub_button_list = []
unknown_confirm_button_list = []
for i in range(n_unknown):
    # Entry
    name_altro = "Altro" + str(i+1)
    unknown_name_list[i].set(name_altro)
    new_entry = tk.Entry(window, width=15, textvariable=unknown_name_list[i], font=label_font)
    unknown_name_entry_list.append(new_entry)
    # Quantity
    new_label_quantity = tk.Label(window, textvariable=unknown_quantity_list[i], font=label_font)
    new_add_button_quantity = tk.Button(window, text="+", font=button_add_font, command=lambda x=i : add_quantity(x))
    new_sub_button_quantity = tk.Button(window, text="-", font=button_add_font, command=lambda x=i : sub_quantity(x))
    unknown_quantity_label_list.append(new_label_quantity)
    unknown_quantity_add_button_list.append(new_add_button_quantity)
    unknown_quantity_sub_button_list.append(new_sub_button_quantity)
    # Price
    new_label_price = tk.Label(window, textvariable=unknown_price_list[i], font=label_font)
    new_add_button_price = tk.Button(window, text="+", font=button_add_font, command=lambda x=i : add_price(x))
    new_sub_button_price = tk.Button(window, text="-", font=button_add_font, command=lambda x=i : sub_price(x))
    unknown_price_label_list.append(new_label_price)
    unknown_price_add_button_list.append(new_add_button_price)
    unknown_price_sub_button_list.append(new_sub_button_price)
    # Confirm
    new_confirm_button = tk.Button(window, text="OK", fg="green", command=lambda x=i : confirm(x))
    unknown_confirm_button_list.append(new_confirm_button)

    # Add to the GUI
    unknown_name_entry_list[i].grid(row=start_row+i, column=0, padx=5)
    unknown_quantity_add_button_list[i].grid(row=start_row+i, column=1, padx=5)
    unknown_quantity_label_list[i].grid(row=start_row+i, column=2, padx=5)
    unknown_quantity_sub_button_list[i].grid(row=start_row+i, column=3, padx=5)
    unknown_price_add_button_list[i].grid(row=start_row+i, column=4, padx=5)
    unknown_price_label_list[i].grid(row=start_row+i, column=5, padx=5)
    unknown_price_sub_button_list[i].grid(row=start_row+i, column=6, padx=5)
    unknown_confirm_button_list[i].grid(row=start_row+i, column=7, padx=5)
    start_row += 1
################################################################################


########################### Final buttons ######################################
start_row = 30
# Total Label
total_label = tk.Label(window, textvariable=str_total, font=label_main_font, justify="left")
total_label.grid(row=start_row, column=0, pady=20)


# Reset Button
reset_button = tk.Button(window, text="Riavvia", font=button_main_font, bg="orange", command=reset)
reset_button.grid(row=start_row+1, column=0)

# Print Button
print_button = tk.Button(
    window,
    text="Stampa",
    font=button_main_font,
    bg="green",
    command= lambda x = item_total_list, y = item_dict, z = unknown_tmp_item_dict, v = num_total : printAll(x, y, z, v))
print_button.grid(row=start_row+1, column=1, columnspan=3)
################################################################################


# Main
if __name__ == '__main__':
    window.mainloop()
