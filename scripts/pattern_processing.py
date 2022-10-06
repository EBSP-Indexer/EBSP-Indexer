class background_processor():

    def __init__(self):
        self.file = os.path.join(self.working.dir, "Pattern.dat")
        self.s = kp.load(self.file, lazy=True)

    def remove_static(self):
        self.s.remove_static_background()

    def remove_dynamic(self):
        self.s.remove_dynamic_background()

    def averaging(self):
        window = kp.filters.Window("gaussian", std=1)
        self.s.average_neighbour_patterns(window)

    def save_to_file(self):
        self.s.save(os.path.joing(self.working_dir, "Pattern_ave.h5"))