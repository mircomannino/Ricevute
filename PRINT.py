# Function to print the result
from escpos.printer import Usb
printer = Usb(0x0483,0x5743,0)
printer.codepage = 'CP858'


def printAll(total_item, real_item_list, tmp_item_list, total_tk):
    # print(printer.paper_status())
    printer.set(align='center', height=2)
    printer.text("LAVANDERIA VALDELSA\n")
    printer.text("Via Roma 22/24\n")
    printer.text("53034 - Colle di Val d'Elsa(SI)\n")
    printer.text("0577 920703\n\n")
    printer.set(width=2)
    printer.text("________________________\n")
    printer.set(align='left', width=1, height=1) # Reset setting
    # Header
    printer.set(width=2)
    printer.text('{:17} {:1}'.format('Descrizione', 'Prezzo') + '\n\n')
    # Corpus
    for item in total_item:
        line = ""
        if item in real_item_list:
            # line = real_item_list[item].name + ":\t" + str(real_item_list[item].price) + " \n\n"
            price_str = str('{:1.2f}'.format(real_item_list[item].price))
            line = '{:17} {:}'.format(real_item_list[item].name, price_str) + '\n'
        if item in tmp_item_list:
            # line = tmp_item_list[item].name + ":\t" + str(tmp_item_list[item].price) + " \n\n"
            price_str = str('{:1.2f}'.format(tmp_item_list[item].price))
            unknown_name = "Altro"
            line = '{:17} {:}'.format(unknown_name, price_str) + '\n'
        printer.text(line)
    printer.text("________________________\n")
    # Totale
    printer.text("\nTOTALE: " + '{:1.2f}'.format(total_tk.get())  + '\u00C7 \n')
    # Numerino
    printer.text("________________________\n")
    printer.text("\nNUMERO:\n")
    # Saluti cordiali
    printer.text("________________________\n")
    printer.text('\nGrazie e arrivederci!')
    # Fine
    printer.cut()
