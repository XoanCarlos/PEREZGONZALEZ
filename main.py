from ventana import *
from vencalendar import *
from vensalir import *
from datetime import datetime
import sys, var, events, clients

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_venPrincipal()
        var.ui.setupUi(self)
        '''
        colección de datos
        '''
        var.rbtsex = (var.ui.rbtFem, var.ui.rbtMasc)
        var.chkpago = (var.ui.chkEfec, var.ui.chkTar, var.ui.chkTrans)
        var.avisosalir = DialogSalir()
        var.dlgcalendar = DialogCalendar()

        '''
        conexion de eventos con los objetos
        estamos conectando el código con la interfaz gráfico
        '''
        QtWidgets.QAction(self).triggered.connect(self.close)
        var.ui.btnSalir.clicked.connect(events.Eventos.Salir)
        var.ui.actionSalir.triggered.connect(events.Eventos.Salir)
        var.ui.editDni.editingFinished.connect(clients.Clientes.validoDni)
        var.ui.btCalendar.clicked.connect(clients.Clientes.abrirCalendar)
        for i in var.rbtsex:
            i.toggled.connect(clients.Clientes.selSexo)
        for i in var.chkpago:
            i.stateChanged.connect(clients.Clientes.selPago)
        var.ui.cmbProv.activated[str].connect(clients.Clientes.selProv)

        '''
        Llamada a módulos iniciales
        '''
        events.Eventos.cargarProv()

        '''
        módulos del principal
        '''

    def closeEvent(self, event):
        events.Eventos.Salir()

class DialogSalir(QtWidgets.QDialog):
    def __init__(self):
        super(DialogSalir, self).__init__()
        var.avisosalir = Ui_venSalir()
        var.avisosalir.setupUi(self)
        var.avisosalir.btnBoxSalir.button(QtWidgets.QDialogButtonBox.Yes).clicked.connect(events.Eventos.Salir)
        var.avisosalir.btnBoxSalir.button(QtWidgets.QDialogButtonBox.No).clicked.connect(events.Eventos.Salir)

class DialogCalendar(QtWidgets.QDialog):
    def __init__(self):
        super(DialogCalendar, self).__init__()
        var.dlgcalendar = Ui_calendar()
        var.dlgcalendar.setupUi(self)
        mesactual = datetime.now().month
        anoactual = datetime.now().year
        var.dlgcalendar.Calendar.setSelectedDate((QtCore.QDate(anoactual,mesactual,1)))
        var.dlgcalendar.Calendar.clicked.connect(clients.Clientes.cargarFecha)



if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())