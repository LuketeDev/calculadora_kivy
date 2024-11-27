from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

Window.size = (350, 400)


class CalculadoraApp(App):
    def build(self):
        self.operators = ["/", "X", "+", "-"]
        self.last_was_operator = None
        self.last_button = None
        main_layout = BoxLayout(orientation="vertical")
        self.solution = TextInput(
            multiline=False,
            readonly=True,
            halign="right",
            font_size="55",
            size_hint_y=1.2,
        )
        main_layout.add_widget(self.solution)
        buttons = [
            "AC",
            ["7", "8", "9", "/"],
            ["4", "5", "6", "X"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
        ]
        for row in buttons:
            h_layout = BoxLayout()
            if str(row) == "AC":
                button = Button(
                    text="AC",
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            for label in row:
                if label == "A":
                    break
                button = Button(
                    text=label,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)
        equals = Button(
            text="=",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )
        equals.bind(on_press=self.on_solution)
        main_layout.add_widget(equals)
        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":
            self.solution.text = ""
        elif button_text == "AC":
            if self.solution.text:
                if self.solution.text[0] != "E":
                    self.solution.text = self.solution.text[:-1]
                else:
                    self.solution.text = ""
        else:
            if current and (self.last_was_operator and button_text in self.operators):
                return
            elif current == "" and button_text in self.operators:
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

    def on_solution(self, instance):
        text = self.solution.text

        if text:
            try:
                solution = str(eval(self.solution.text))
                self.solution.text = solution
            except ZeroDivisionError as exc:
                self.solution.text = "Erro: divisão por 0"
            except SyntaxError as sexc:
                self.solution.text = "Erro de Sintaxe"


__name__ = "Calculadora"
if __name__ == "Calculadora":
    app = CalculadoraApp()
    app.run()
