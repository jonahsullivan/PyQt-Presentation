from PyQt5.QtWidgets import QApplication


# import the dialog form as a class
from hello_world_dialog import Ui_HelloWorldDialogBase

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    helloWorld = Ui_HelloWorldDialogBase()

    # # populate a comboBox element with sequential values
    # for i in range(10):
    #     helloWorld.comboBox.addItem(str(i))

    helloWorld.show()
    sys.exit(app.exec_())
