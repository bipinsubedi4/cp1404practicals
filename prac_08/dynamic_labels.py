from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    def build(self):
        self.names = ["Alice", "Bob", "Charlie", "Diana"]  # List of names
        self.root = Builder.load_file('dynamic_labels.kv')  # Load the KV file

        main_layout = self.root.ids.main  # Access the BoxLayout with id 'main'

        # Dynamically create Label widgets
        for name in self.names:
            temp_label = Label(text=name)
            main_layout.add_widget(temp_label)

        return self.root


if __name__ == '__main__':
    DynamicLabelsApp().run()
