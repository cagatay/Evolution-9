#!/usr/bin/python2.6
import sys, traceback
import gtk
from brain.NN import neural_network
from evolution.manager import evolution
from util.storage import db

class evolution9_app(object):
    def __init__(self):
        self.store = db()

        self.builder = gtk.Builder()
        self.builder.add_from_file('res/gui.glade')

        self.window = self.builder.get_object('window')
        self.new_evolution_dialog = self.builder.get_object('new_evolution_dialog')
        self.new_neural_network_dialog = self.builder.get_object('new_neural_network_dialog')
        self.open_evolution_dialog = self.builder.get_object('open_evolution_dialog')
        

        self.nn_list = gtk.ListStore(str)
        self.nn_combo = self.builder.get_object('nn_combo')
        self.nn_combo.set_model(self.nn_list)
        cell = gtk.CellRendererText()
        self.nn_combo.pack_start(cell, True)
        self.nn_combo.add_attribute(cell,'text', 0)

        self.update_nn_list()

        self.evolution_list = gtk.ListStore(str)
        self.evolution_combo = self.builder.get_object('evolution_combo')
        self.evolution_combo.set_model(self.evolution_list)
        cell = gtk.CellRendererText()
        self.evolution_combo.pack_start(cell, True)
        self.evolution_combo.add_attribute(cell, 'text', 0)

        self.update_evolution_list()

        self.genome_list = gtk.ListStore(int, str)
        self.genome_view = self.builder.get_object('genome_view')
        self.genome_view.set_model(self.genome_list)
        cell = gtk.CellRendererText()
        column = gtk.TreeViewColumn('Genome', cell, text=1)
        self.genome_view.append_column(column)

        self.controls = {
            'initialize': self.builder.get_object('initialize_button'),
            'evaluate': self.builder.get_object('evaluate_button'),
            'select' : self.builder.get_object('apply_selection_button'),
            'graphs' : self.builder.get_object('generation_info_tab'),
            'play' : self.builder.get_object('play_button')
        }

        self.console = gtk.TextBuffer()
        self.builder.get_object('console').set_buffer(self.console)
        
        # hide dialogs instead of destroying them for reuse
        self.hide_dialog = gtk.Widget.hide_on_delete

        self.builder.connect_signals(self)

    def log_console(self, text):
        self.console.insert_at_cursor(text + '\n')
        self.builder.get_object('console').scroll_to_mark(self.console.get_insert(), 0)


    def start_evolution(self):
        if self.evolution9.initialized:
            self.controls['initialize'].set_label('Reproduce')
        self.update_state()
        self.update_genome_list()

        self.log_console('%s is started'%self.evolution9.name)

        #self.builder.get_object('generation_info_tab').set_sensitive(True)
    def update_state(self):
        for k, v in self.controls.iteritems():
            v.set_sensitive(False)
        
        if self.evolution9:
            if not self.evolution9.initialized or self.evolution9.state == 'reproduce':
                self.controls['initialize'].set_sensitive(True)
            elif self.evolution9.state == 'evaluation':
                self.controls['evaluate'].set_sensitive(True)
            elif self.evolution9.state == 'select':
                self.controls['select'].set_sensitive(True)
                self.controls['graphs'].set_sensitive(True)

            self.builder.get_object('step_50_button').set_sensitive(True)

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

    def show_individual_info(self, treeview, path, view_column, *args):
        index = path[0]
        individual = self.evolution9.current_generation[index]
        
        self.builder.get_object('name_label').set_text(individual.name)
        self.builder.get_object('parent1_label').set_text(individual.parent_1)
        self.builder.get_object('parent2_label').set_text(individual.parent_2)
        self.builder.get_object('grade_label').set_text(str(individual.grade))
        self.builder.get_object('selected_label').set_text(str(individual.selected))

        self.controls['play'].set_sensitive(True)

    def main(self):
        self.window.show()
        gtk.main()

    def update_evolution_list(self):
        self.evolution_list.clear()
        evolutions = evolution.get_list(self.store)
        
        if evolutions:
            for e in evolutions:
                self.evolution_combo.append_text(e)

        return

    def update_nn_list(self):
        self.nn_list.clear()
        networks = neural_network.get_list(self.store)

        if networks:
            for n in networks:
                self.nn_combo.append_text(n)

        return

    def update_genome_list(self):
        self.genome_list.clear()
        l = self.evolution9.current_generation

        if l:
            for x in range(len(l)):
                self.genome_list.append((x, l[x].genome))
        return

    def on_new_evolution_ok_button_clicked(self, *args):
        name = self.builder.get_object('new_evolution_name').get_text()
        population_size = self.builder.get_object('new_evolution_pop_size').get_text()
        evaluator = self.builder.get_object('nn_combo').get_active_text()

        try:
            self.evolution9 = evolution(name, evaluator, int(population_size), self.store)
        except Exception, err:
            self.error_message(str(err))
            traceback.print_exc(file=sys.stdout)
        else:
            self.new_evolution_dialog.hide()
            self.start_evolution()

    def on_open_evolution_button_clicked(self, *args):
        self.open_evolution_dialog.present()
        return

    def on_apply_selection_button_clicked(self, *args):
        self.evolution9.apply_selection(self.log_console)
        self.update_genome_list()
        self.update_state()

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
            self.log_console('created neural network : %s' % nn_name)
            self.update_nn_list()
            self.new_neural_network_dialog.hide()

    def on_new_evolution_button_clicked(self, *args):
        self.new_evolution_dialog.present()
        return

    def on_open_evolution_ok_button_clicked(self, *args):
        name = self.builder.get_object('evolution_combo').get_active_text()

        try:
            self.evolution9 = evolution.get_saved(name, self.store)
        except Exception, err:
            self.error_message(str(err))
            traceback.print_exc(file=sys.stdout)
        else:
            self.start_evolution()
            self.open_evolution_dialog.hide()

    def on_evaluate_button_clicked(self, *args):
        self.evolution9.evaluate(self.log_console)
        self.update_genome_list()
        self.update_state()
        return

    def on_initialize_button_clicked(self, *args):
        self.evolution9.initialize(self.log_console)
        self.controls['initialize'].set_label('Reproduce')
        self.update_state()
        self.update_genome_list()
        
if __name__ == '__main__':
    app = evolution9_app()
    app.main()
