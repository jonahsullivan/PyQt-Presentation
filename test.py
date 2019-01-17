# import the dialog form as a class
from hello_world_dialog import HelloWorldDialog


class HelloWorld:

    def __init__(self):

        # instantiate the dialog form class
        self.dlg = HelloWorldDialog()

    def run(self):

        # show the dialog box
        self.dlg.show()

        # query the dialog class radioButton element’s status
        self.dlg.radioButton.isChecked()

        # populate a comboBox element with sequential values
        for i in range(10):
            self.dlg.comboBox.addItem(str(i))

        # check a radioButton
        self.dlg.radioButton.setChecked(True)
        # set the text for a textLabel
        self.dlg.messageBox.setText("sample text")

        # slot - executes an action
        def print_value(new_value):
            print(str(new_value))
        # signal - initiates an action
        self.dlg.spinBox.valueChanged.connect(print_value(self.dlg.spinbox.value()))
