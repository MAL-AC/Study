import Text_fiels
import Text_fiels as tf
import View
import Model


def start():
    while True:
        choice = View.main_menu()
        match choice:
            case 1:
                Model.open_file()
                View.print_message(tf.open_successful)
            case 2:
                Model.save_file()
                View.print_message(Text_fiels.save_successаul)
            case 3:
                pb = Model.phone_book
                View.show_contact(pb, tf.no_phone_book)
            case 4:
                new_contact = View.input_contact(tf.new_contact)
                Model.add_contact(new_contact)
                View.print_message(tf.add_successful)
            case 5:
                contact = View.find_contact()
                pb = Model.phone_book
                View.print_message(View.sh_cont(Model.find_contact(contact, pb)))
            case 6:
                pb = Model.phone_book
                View.show_contact(pb, '')
                choice = View.input_choice(len(pb), tf.change_choice) - 1
                change_contact = View.input_contact(tf.change_contact)
                res = Model.change(choice, change_contact)
                View.print_message(tf.changed(res['name']))
            case 7:
                pb = Model.get_pb()
                name = Model.del_contact(View.input_index(tf.index_del_contact, pb, tf.load_error))
                View.print_message(tf.del_contact(name))
            case 8:
                View.print_message(View.close())
                break

