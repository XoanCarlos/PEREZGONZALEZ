import var


class Clientes():
    '''
    eventos clientes
    '''
    def validarDni(dni):
        '''
        Código que controla si el dni o nie es correcto
        :return:
        '''
        try:
            tabla = 'TRWAGMYFPDXBNJZSQVHLCKE'
            dig_ext = 'XYZ'
            reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
            numeros = '0123456789'
            dni = dni.upper()
            if len(dni) == 9:
                dig_control = dni[8]
                dni = dni[:8]
                if dni[0] in dig_ext:
                    dni  = dni.replace(dni[0],reemp_dig_ext[dni[0]])
                return len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni)%23 ] == dig_control

        except:
            print('Error módulo validar DNI')
            return None

    def validoDni():
        '''
        muestra mensaje de dni válido
        :return:
        '''
        try:
            dni = var.ui.editDni.text()
            if Clientes.validarDni(dni):
                var.ui.lblValidar.setStyleSheet('QLabel {color: green;}')
                var.ui.lblValidar.setText('V')
                var.ui.editDni.setText(dni.upper())
            else:
                var.ui.lblValidar.setStyleSheet('QLabel {color: red;}')
                var.ui.lblValidar.setText('X')
                var.ui.editDni.setText(dni.upper())

        except:
            print('Error módulo escribir valido DNI')
            return None

    def selSexo():
        try:
            if var.ui.rbtFem.isChecked():
                print('has elegido femenino')
            if var.ui.rbtMasc.isChecked():
                print('has elegido masculino')
        except Exception as error:
            print('Error: %s' % str(error))

    def selPago():
        try:
            if var.ui.chkEfec.isChecked():
                print('Pagas con Efectivo')
            if var.ui.chkTar.isChecked():
                print('Pagas con Tarjeta')
            if var.ui.chkTrans.isChecked():
                print('Pagas con Transferencia')

        except Exception as error:
            print('Error: %s' % str(error))

    def selProv(prov):
        try:
            print('Has seleccionado la provincia de ',prov)
            return prov
        except Exception as error:
            print('Error: %s' % str(error))

    '''
    Abrir la ventana calendario
    '''
    def abrirCalendar():
        try:
            var.dlgcalendar.show()
        except Exception as error:
            print('Error: %s ' % str(error))

    '''
    Este módulo se ejecuta cuando clickeamos en un día del calendar, es decir, clicked.connect de calendar
    '''

    def cargarFecha(qDate):
        try:
            data = ('{0}/{1}/{2}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.editClialta.setText(str(data))
            var.dlgcalendar.hide()
        except Exception as error:
            print('Error cargar fecha: %s ' % str(error))