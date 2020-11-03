import sys, var

class Eventos():
    def Salir(self):
        '''
        Módulo para cerrar el programa
        :return:
        '''
        try:
            var.avisosalir.show()
            if var.avisosalir.exec_():
                sys.exit()
            else:
                var.avisosalir.close()
        except Exception as error:
            print('Error %s' % str(error))

    def cargarProv():
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