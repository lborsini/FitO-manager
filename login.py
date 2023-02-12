from PyQt5 import QtWidgets, uic


#iniciar la aplicacion
app = QtWidgets.QApplication([])

# Cargar todos los archivos .uic(Interfaces creadas)
login = uic.loadUi("Interfaz/login.ui")
mainWindow = uic.loadUi("Interfaz/mainWindow.ui")

#Ejecutable
login.show()
app.exec()