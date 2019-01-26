from PyQt5.QtWidgets import QApplication, QDialog

# import the dialog form that has been converted into python
from hello_world_dialog import Ui_HelloWorldDialogBase

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    window = QDialog()
    helloWorld = Ui_HelloWorldDialogBase()
    helloWorld.setupUi(window)

    # populate a comboBox element with sequential values
    for i in range(10):
        helloWorld.comboBox.addItem(str(i))

    # make the "Hello?" push button do something
    def hello():
        if helloWorld.messageBox.text() == "":
            helloWorld.messageBox.setText("Hello, World!")
        else:
            helloWorld.messageBox.setText("")

    helloWorld.pushButton.clicked.connect(hello)

    window.show()
    sys.exit(app.exec_())
