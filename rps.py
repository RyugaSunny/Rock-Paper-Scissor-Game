from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton
from random import choice

matrix = [
  [["Draw","Rock"], ["You Won","Scissor"], ["You Lost","Paper"]],
  [["You Lost","Rock"], ["Draw","Scissor"], ["You Won","Paper"]],
  [["You Won","Rock"], ["You Lost","Scissor"], ["Draw","Paper"]],
]


class myscreen(MDScreen):
    def rps(self,a):
        x = matrix[a][choice([0, 1, 2])]
        if self.label:  # check if label exists
            self.remove_widget(self.label)
        self.label=MDLabel(text=f"Computer choose {x[1]}\n\n     {x[0].upper()}",halign="center",pos_hint={"center_x": 0.5, "center_y": 0.3})
        self.add_widget(self.label) 
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label=None
        b1=MDRectangleFlatButton(text="Rock",pos_hint={"center_x": 0.2, "center_y": 0.7},size_hint = (0.2,0.4),
                                 on_press=lambda instance:self.rps(0)
                                 )
        b2=MDRectangleFlatButton(text="Paper",pos_hint={"center_x": 0.5, "center_y": 0.7},size_hint = (0.2,0.4),
                                 on_press=lambda instance:self.rps(2)
                                 )
        b3=MDRectangleFlatButton(text="Scissor",pos_hint={"center_x": 0.8, "center_y": 0.7},size_hint = (0.2,0.4),
                                 on_press=lambda instance:self.rps(1)
                                 )
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)

class rps(MDApp):
    def build(self):
        self.theme_cls.theme_style="Dark"
        return myscreen()


rps().run()