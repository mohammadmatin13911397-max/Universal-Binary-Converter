from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.clipboard import Clipboard


def to_binary(text):
    data = text.encode('utf-8')
    return ' '.join(format(b, '08b') for b in data)


def from_binary(binary):
    binary = ''.join(binary.split())

    if not binary:
        raise ValueError('Please enter binary code.')

    if any(bit not in '01' for bit in binary):
        raise ValueError('Only 0 and 1 are allowed.')

    if len(binary) % 8 != 0:
        raise ValueError('Invalid binary length.')

    data = bytes(
        int(binary[i:i+8], 2)
        for i in range(0, len(binary), 8)
    )

    return data.decode('utf-8')


class BinaryConverter(App):

    def build(self):
        layout = BoxLayout(
            orientation='vertical',
            padding=10,
            spacing=8
        )

        layout.add_widget(
            Label(
                text='UNIVERSAL BINARY CONVERTER',
                font_size=22,
                size_hint_y=None,
                height=45
            )
        )

        # TEXT TO BINARY

        layout.add_widget(
            Label(
                text='TEXT TO BINARY',
                size_hint_y=None,
                height=30
            )
        )

        self.text_input = TextInput(
            hint_text='Enter text in any language...',
            multiline=True,
            size_hint_y=0.22
        )

        layout.add_widget(self.text_input)

        btn = Button(
            text='CONVERT TO BINARY',
            size_hint_y=None,
            height=45
        )
        btn.bind(on_press=self.convert_text)
        layout.add_widget(btn)

        self.binary_output = TextInput(
            hint_text='Binary output...',
            readonly=True,
            multiline=True,
            size_hint_y=0.18
        )

        layout.add_widget(self.binary_output)

        btn = Button(
            text='COPY BINARY',
            size_hint_y=None,
            height=40
        )
        btn.bind(on_press=self.copy_binary)
        layout.add_widget(btn)

        # BINARY TO TEXT

        layout.add_widget(
            Label(
                text='BINARY TO TEXT',
                size_hint_y=None,
                height=30
            )
        )

        self.binary_input = TextInput(
            hint_text='Enter binary code...',
            multiline=True,
            size_hint_y=0.18
        )

        layout.add_widget(self.binary_input)

        btn = Button(
            text='CONVERT TO TEXT',
            size_hint_y=None,
            height=45
        )
        btn.bind(on_press=self.convert_binary)
        layout.add_widget(btn)

        self.text_output = TextInput(
            hint_text='Decoded text in any language...',
            readonly=True,
            multiline=True,
            size_hint_y=0.18
        )

        layout.add_widget(self.text_output)

        layout.add_widget(
            Label(
                text='If characters are not displayed, paste the text into another app.',
                size_hint_y=None,
                height=35,
                font_size=12
            )
        )

        btn = Button(
            text='COPY TEXT',
            size_hint_y=None,
            height=40
        )
        btn.bind(on_press=self.copy_text)
        layout.add_widget(btn)

        # CLEAR

        btn = Button(
            text='CLEAR ALL',
            size_hint_y=None,
            height=40
        )
        btn.bind(on_press=self.clear_all)
        layout.add_widget(btn)

        return layout

    def convert_text(self, instance):
        try:
            self.binary_output.text = to_binary(
                self.text_input.text
            )

        except Exception as e:
            self.binary_output.text = str(e)

    def convert_binary(self, instance):
        try:
            self.text_output.text = from_binary(
                self.binary_input.text
            )

        except Exception as e:
            self.text_output.text = (
                type(e).__name__ + ': ' + str(e)
            )

    def copy_binary(self, instance):
        Clipboard.copy(self.binary_output.text)

    def copy_text(self, instance):
        Clipboard.copy(self.text_output.text)

    def clear_all(self, instance):
        self.text_input.text = ''
        self.binary_output.text = ''
        self.binary_input.text = ''
        self.text_output.text = ''
        
        
BinaryConverter().run()
