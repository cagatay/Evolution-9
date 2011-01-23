#!/usr/bin/python2.6
import sys, traceback
import gtk
from brain.NN import neural_network
from util.storage import db

class evolution9_app(object):
    def __init__(self):
        self.store = db()

        self.builder = gtk.Builder()
        self.builder.add_from_file('res/gui.glade')

        self.window = self.builder.get_object('window')
        self.new_evolution_dialog = self.builder.get_object('new_evolution_dialog')
        self.new_neural_network_dialog = self.builder.get_object('new_neural_network_dialog')

        # hide dialogs instead of destroying them for reuse
        self.hide_dialog = gtk.Widget.hide_on_delete

        self.builder.connect_signals(self)

    def error_message(self, message):
        dialog = gtk.MessageDialog(None,
                                   gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
                                   gtk.MESSAGE_ERROR,
                                   gtk.BUTTONS_OK,
                                   message)
        dialog.run()
        dialog.destroy()

    def on_window_destroy(self, widget, data = None):
        gtk.main_quit()

    def main(self):
        self.window.show()
        gtk.main()

    def on_open_evolution_button_clicked(self, *args):
        self.error_message('There is no saved evolution. You must create one first')

    def on_new_neural_network_button_clicked(self, *args):
        self.new_neural_network_dialog.present()

    def on_new_neural_network_ok_button_clicked(self, *args):
        nn_name = self.builder.get_object('new_nn_name').get_text()
        ds_file_uri = self.builder.get_object('new_nn_dataset_file').get_filename()

        try:
            neural_network.new(nn_name, self.store, ds_file_uri)
        except Exception, err:
            self.error_message(str(err))
            traceback.print_exc(file=sys.stdout)
        else:
            self.new_neural_network_dialog.hide()

    def on_new_evolution_button_clicked(self, *args):
        self.new_evolution_dialog.present()
        
if __name__ == '__main__':
    app = evolution9_app()
    app.main()
