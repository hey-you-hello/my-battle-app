from BCSFE_Python import __main__


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.clipboard import Clipboard
from BCSFE_Python.server_handler import get_b

class TransferApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        # Label and input for transferCode
        self.add_widget(Label(text='Enter Transfer Code:'))
        self.transfer_input = TextInput(hint_text='Transfer Code', multiline=False)
        self.add_widget(self.transfer_input)

        # Label and input for PIN
        self.add_widget(Label(text='Enter PIN:'))
        self.pin_input = TextInput(hint_text='PIN', multiline=False, password=True)
        self.add_widget(self.pin_input)

        # Submit button
        self.submit_button = Button(text='Submit')
        self.submit_button.bind(on_press=self.process_inputs)
        self.add_widget(self.submit_button)

        # Copy transferCode button
        self.copy_transfer_button = Button(text='Copy Transfer Code')
        self.copy_transfer_button.bind(on_press=self.copy_transfer_code)
        self.add_widget(self.copy_transfer_button)

        # Copy PIN button
        self.copy_pin_button = Button(text='Copy PIN')
        self.copy_pin_button.bind(on_press=self.copy_pin)
        self.add_widget(self.copy_pin_button)

        # Output label
        self.result_label = Label(text='')
        self.add_widget(self.result_label)

    def process_inputs(self, instance):
        transfer_code = self.transfer_input.text
        pin = self.pin_input.text

        if not transfer_code or not pin:
            self.result_label.text = 'Please enter both Transfer Code and PIN.'
        else:
            # Call a placeholder function to handle the logic
            result = self.handle_inputs(transfer_code, pin)
            self.result_label.text = f'Processed Transfer Code: {result["transferCode"]}\nProcessed PIN: {result["pin"]}'
            self.processed_result = result

    def handle_inputs(self, transfer_code, pin):
        # Mock logic for processing inputs (you can replace this with your actual logic)
        try:
            __main__.normal_start_up(transfer_code, pin, '14.0.0')
        except IndexError:
            processed_transfer_code = get_b()['transferCode']
            pin = get_b()['pin']
        processed_transfer_code = processed_transfer_code 
        processed_pin = f'{pin}'
        return {"transferCode": processed_transfer_code, "pin": processed_pin}

    def copy_transfer_code(self, instance):
        if hasattr(self, 'processed_result') and self.processed_result.get('transferCode'):
            Clipboard.copy(self.processed_result['transferCode'])
            self.result_label.text = 'Transfer Code copied to clipboard!'

    def copy_pin(self, instance):
        if hasattr(self, 'processed_result') and self.processed_result.get('pin'):
            Clipboard.copy(self.processed_result['pin'])
            self.result_label.text = 'PIN copied to clipboard!'

class MyApp(App):
    def build(self):
        return TransferApp()

if __name__ == '__main__':
    MyApp().run()
