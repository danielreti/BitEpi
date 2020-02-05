import Tkinter as tk
import tkMessageBox
import pandas as pd


class FormGUI:

    def __init__(self, controller):
        self.controller = controller
        print("Inside GUI")

    # Load file upon clicking submit on the GUI
    def load_files(self, input_file, annotation_file):
        valid = self.controller.validate_input_files(input_file, annotation_file)

        if valid:
            print('The input file, {}, has been successfully validated.'
                  .format(input_file))
            tkMessageBox.showinfo('Success', 'Files have been successfully loaded')
        else:
            print('Error found in input file format.')
            tkMessageBox.showinfo('Error', 'Please input valid files')

    # Method to create the form
    def form(self):
        root = tk.Tk()

        canvas = tk.Canvas(root, height=640, width=640)
        canvas.pack()

        main_title = tk.Label(root, text='Hi, please fill out the specifics you would like to see!')
        main_title.place(relx=0.1, rely=0.05, relheight=0.05, relwidth=0.75)

        file_frame = tk.Frame(root, bg='#a9a9a9', bd=5)
        file_frame.place(relx=0.5, rely=0.1, relwidth=0.95, relheight=0.2, anchor='n')

        input_file_title = tk.Label(file_frame, text='Prefix file path: ')
        input_file_title.place(relx=0.02, rely=0.1, relheight=0.2, relwidth=0.25)

        input_file_entry = tk.Entry(file_frame)
        input_file_entry.place(relx=0.3, rely=0.1, relwidth=0.675, relheight=0.2)

        annot_file_title = tk.Label(file_frame, text='Annotation file path: ')
        annot_file_title.place(relx=0.02, rely=0.4, relheight=0.2, relwidth=0.25)

        annot_file_entry = tk.Entry(file_frame)
        annot_file_entry.place(relx=0.3, rely=0.4, relwidth=0.675, relheight=0.2)

        load_button = tk.Button(file_frame, bg='#808080', text="Load files",
                                command=lambda: self.load_files(input_file_entry.get(), annot_file_entry.get()))
        load_button.place(relx=0.725, rely=0.7, relheight=0.2, relwidth=0.25)

        view_frame = tk.Frame(root, bg='#808080', bd=5)
        view_frame.place(relx=0.258, rely=0.31, relwidth=0.468, relheight=0.575, anchor='n')

        view_frame_title = tk.Label(view_frame, bg='#808080', text='Specify how you would like to put styles!')
        view_frame_title.place(relx=0.04, rely=0.05, relheight=0.1, relwidth=0.95)

        node_colour_title = tk.Label(view_frame, bg='#696969', justify='left', text='Node colour by: ')
        node_colour_title.place(relx=0.04, rely=0.2, relheight=0.1, relwidth=0.45)

        node_color_list = ['None', 'Order', 'Type']
        node_colour_variable = tk.StringVar(view_frame)
        node_colour_variable.set(node_color_list[0])
        node_colour_options = tk.OptionMenu(view_frame, node_colour_variable, *node_color_list)
        node_colour_options.place(relx=0.525, rely=0.2, relheight=0.1, relwidth=0.45)

        node_size_title = tk.Label(view_frame, bg='#696969', text='Node size by: ')
        node_size_title.place(relx=0.04, rely=0.35, relheight=0.1, relwidth=0.45)

        node_size_list = ['None', 'Order', 'Alpha', 'Beta']
        node_size_variable = tk.StringVar(view_frame)
        node_size_variable.set(node_size_list[0])
        node_size_options = tk.OptionMenu(view_frame, node_size_variable, *node_size_list)
        node_size_options.place(relx=0.525, rely=0.35, relheight=0.1, relwidth=0.45)

        node_shape_title = tk.Label(view_frame, bg='#696969', text='Node shape by: ')
        node_shape_title.place(relx=0.04, rely=0.5, relheight=0.1, relwidth=0.45)

        node_shape_list = ['None', 'Alpha', 'Beta']
        node_shape_variable = tk.StringVar(view_frame)
        node_shape_variable.set(node_shape_list[0])
        node_shape_options = tk.OptionMenu(view_frame, node_shape_variable, *node_shape_list)
        node_shape_options.place(relx=0.525, rely=0.5, relheight=0.1, relwidth=0.45)

        edge_colour_title = tk.Label(view_frame, bg='#696969', text='Edge colour by: ')
        edge_colour_title.place(relx=0.04, rely=0.65, relheight=0.1, relwidth=0.45)

        edge_colour_list = ['None', 'Order']
        edge_colour_variable = tk.StringVar(view_frame)
        edge_colour_variable.set(edge_colour_list[0])
        edge_colour_options = tk.OptionMenu(view_frame, edge_colour_variable, *edge_colour_list)
        edge_colour_options.place(relx=0.525, rely=0.65, relheight=0.1, relwidth=0.45)

        edge_thickness_title = tk.Label(view_frame, bg='#696969', text='Edge thickness by: ')
        edge_thickness_title.place(relx=0.04, rely=0.8, relheight=0.1, relwidth=0.45)

        edge_thickness_list = ['None', 'Alpha', 'Beta']
        edge_thickness_variable = tk.StringVar(view_frame)
        edge_thickness_variable.set(edge_thickness_list[0])
        edge_thickness_options = tk.OptionMenu(view_frame, edge_thickness_variable, *edge_thickness_list)
        edge_thickness_options.place(relx=0.525, rely=0.8, relheight=0.1, relwidth=0.45)

        filter_frame = tk.Frame(root, bg='#696969', bd=5)
        filter_frame.place(relx=0.74, rely=0.31, relwidth=0.468, relheight=0.575, anchor='n')

        filter_frame_title = tk.Label(filter_frame, bg='#696969', text='Specify how you would like to filter!')
        filter_frame_title.place(relx=0.04, rely=0.05, relheight=0.1, relwidth=0.95)

        filter_entry = tk.Entry(filter_frame, font=24)
        filter_entry.place(relx=0.05, rely=0.2, relwidth=0.925, relheight=0.3)

        hide_button = tk.Button(filter_frame, bg='#808080', text="Hide", command=lambda: self.hide(hide_button))
        hide_button.place(relx=0.04, rely=0.55, relheight=0.1, relwidth=0.45)

        show_button = tk.Button(filter_frame, bg='#808080', text="Show", command=lambda: self.show())
        show_button.place(relx=0.525, rely=0.55, relheight=0.1, relwidth=0.45)

        hl_button = tk.Button(filter_frame, bg='#808080', text="Highlight", command=lambda: self.highlight())
        hl_button.place(relx=0.04, rely=0.7, relheight=0.1, relwidth=0.45)

        gray_button = tk.Button(filter_frame, bg='#808080', text="Gray out", command=lambda: self.grayout())
        gray_button.place(relx=0.525, rely=0.7, relheight=0.1, relwidth=0.45)

        reset_button = tk.Button(filter_frame, bg='#808080', text="Reset", command=lambda: self.reset())
        reset_button.place(relx=0.04, rely=0.85, relheight=0.1, relwidth=0.45)

        help_button = tk.Button(filter_frame, bg='#808080', text="Help", command=lambda: self.help())
        help_button.place(relx=0.525, rely=0.85, relheight=0.1, relwidth=0.45)

        submit_button = tk.Button(root, text="Submit", command=lambda root=root: self.quit(root))
        submit_button.place(relx=0.3, rely=0.9, relheight=0.075, relwidth=0.35)

        root.mainloop()

        data = {node_colour_variable.get(), node_size_variable.get(), node_shape_variable.get(),
                edge_colour_variable.get()
            , edge_thickness_variable.get(), filter_entry.get()}

        form_details_df = pd.DataFrame(data, columns=['node_colour', 'node_size', 'node_shape'
            , 'edge_colour', 'edge_thickness', 'query'])

        return form_details_df

    def hide(self, hide_button):
        if hide_button.config('text')[-1] == 'Hide':
            hide_button.config(text='Disable hide')
        elif hide_button.config('text')[-1] == 'Disable hide':
            hide_button.config(text='Hide')

    def show(self):
        pass

    def highlight(self):
        pass

    def grayout(self):
        pass

    def reset(self):
        pass

    def help(self):
        tkMessageBox.showinfo('Info', 'This is how the query should be done: \nAaaaaaseemmennnyaaaa hfkewrhgethg4ui5!!')
        pass

    def quit(self, root):
        root.quit()