# Created by: Jacob Liberty
# Created on: Sep 28 2017
# Created for: ICS3U
# This program shows how global and local variables are used

import ui

variableX = 25

def local_button_touch_up_inside(sender):
    # shows with local variable
    
    variableX = 10
    variableY = 30
    variableZ = variableX + variableY
    
    view['local_variable_label'].text = str(variableZ)
        
def global_button_touch_up_inside(sender):
    # shows with global variable
    
    global variableX
    variableX = variableX + 1
    variableY = 30
    variableZ = variableX + variableY
    
    view['global_variable_label'].text = str(variableZ)

view = ui.load_view()
view.present('sheet')
