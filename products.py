import var, events

class Products():
    '''
    Eventos asociados a los artículos
    '''
    def limpiarPro(self):
        '''
        limpia los datos del formulario cliente
        :return: none
        '''
        try:
            product = [var.ui.editArtic, var.ui.editPrec, var.ui.editStock]
            for i in range(len(product)):
                product[i].setText('')
            var.ui.lblCodPro.setText('')
        except Exception as error:
            print('Error limpiar widgets: %s ' % str(error))

