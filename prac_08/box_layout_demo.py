from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Create class named BoxLayoutDemo."""
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Handles the Greet button click event."""
        name = self.root.ids.input_name.text
        if name.strip():
            self.root.ids.output_label.text = f"Hello {name}"
        else:
            self.root.ids.output_label.text = "Hello!"

    def handle_clear(self):
        """Handles the Clear button click event."""
        self.root.ids.input_name.text = ''
        self.root.ids.output_label.text = 'Enter your name'


BoxLayoutDemo().run()
