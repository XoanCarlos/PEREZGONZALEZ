import sys, var, clients, conexion, main
from datetime import datetime
from PyQt5 import QtWidgets
import zipfile, os, shutil


class FileDialogGuardar(QtWidgets.QFileDialog):
    def __init__(self):
        super(FileDialogGuardar, self).__init__()
        self.setWindowTitle('Guardar Archivo')
        self.setModal(True)



class Eventos():

    def Salir(event):
        '''
        Módulo para cerrar el programa
        :return:
        '''
        try:
            #var.lblMensalir.setText('Desea Salir de Xestión')
            var.dlgsalir.show()
            if var.dlgsalir.exec_():
                #print(event)
                sys.exit()
            else:
                var.dlgsalir.hide()
                event.ignore()

        except Exception as error:
            print('Error %s' % str(error))

    def closeSalir(event):
        try:
            if var.dlgsalir.exec_():
                var.dlgsalir.hide()
               #necesario para que ignore X de la ventana
        except Exception as error:
            print('Error %s' % str(error))

    def cargarProv(self):
        """
        carga las provincias al iniciar el programa
        :return:
        """
        try:
            prov = ['','A Coruña', 'Lugo', 'Ourense', 'Pontevedra', 'Vigo']
            for i in prov:
                var.ui.cmbProv.addItem(i)

        except Exception as error:
            print('Error: %s' % str(error))

    def Backup():
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y.%m.%d.%H.%M.%S')
            var.copia = (str(fecha) + '_backup.zip')
            var.filedlgsave = FileDialogGuardar()
            option = QtWidgets.QFileDialog.Options()
            QtWidgets.QFileDialog.getSaveFileName(None,'Guardar Copia', var.copia, '.zip', options=option)
            if var.filedlgsave.Accepted:
                directorio = var.filedlgsave.getExistingDirectory()
                fichzip = zipfile.ZipFile(var.copia, 'w')
                fichzip.write(var.filebd, os.path.basename(var.filebd), zipfile.ZIP_DEFLATED)
                fichzip.close()
                var.ui.lblstatus.setText('BASE DE DATOS CREADA')
            shutil.move(str(var.copia), str(directorio))
        except Exception as error:
            print('Error: %s' % str(error))

    def AbrirDir(self):
        try:
            var.filedlgabrir.show()
        except Exception as error:
            print('Error abrir explorador: %s ' % str(error))

    def AbrirPrinter(self):
        try:
            var.dlgImprimir.setWindowTitle('Imprimir')
            var.dlgImprimir.setModal(True)
            var.dlgImprimir.show()
        except Exception as error:
            print('Error abrir imprimr: %s ' % str(error))

    def AbrirAviso(men):
        try:
            var.lblMensalir.setText(men)
            var.dlgaviso.show()
        except Exception as error:
            print('Error abrir ventana aviso: %s ' % str(error))

    def Confirmar():
        try:
            if var.cliente:
                clients.Clientes.bajaCliente()
                var.dlgaviso.hide()
                var.cliente = False
                conexion.Conexion.mostrarClientes(None)
            if var.backup:
                var.backup = False
                var.dlgaviso.hide()
        except Exception as error:
            print('Error botón confirma: %s ' % str(error))

    def Anular():
        try:
            var.dlgaviso.hide()
        except Exception as error:
            print('Error botón anula: %s ' % str(error))

    def mostrarAvisocli():
        try:
            var.cliente = True
            var.backup = False
            var.lblMensaviso.setText('¿Desea eliminar el cliente?')
            var.dlgaviso.show()
        except Exception as error:
            print('Error mostrar aviso: %s ' % str(error))

    # def mostrarAvisobackup():
    #     try:
    #         var.cliente = False
    #         var.backup = True
    #         var.lblMensaviso.setText('Copia de Seguridad Creada')
    #         var.dlgaviso.show()
    #     except Exception as error:
    #         print('Error mostrar aviso: %s ' % str(error))