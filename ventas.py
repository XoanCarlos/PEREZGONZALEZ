import var
import conexion
from PyQt5 import QtWidgets, QtCore
from time import sleep

class Ventas:

    def altaFactura(self):
        try:
            dni = var.ui.editDniclifac.text()
            fecha = var.ui.editDatafac.text()
            apel = var.ui.editApelclifac.text()
            if dni != '' and fecha != '':
                conexion.Conexion.altaFac(dni, fecha, apel)
            conexion.Conexion.mostrarFacturas(self)
            conexion.Conexion.cargarFac2(self)
            Ventas.prepararTablaventas(0)

        except Exception as error:
            print('Error alta factura %s' % str(error))
            return None

    def abrirCalendar(self):
        '''
        Abrir la ventana calendario
        '''
        try:
            var.dlgcalendar.show()
        except Exception as error:
            print('Error: %s ' % str(error))

    def cargarFechafac(qDate):
        ''''
        Este módulo se ejecuta cuando clickeamos en un día del calendar, es decir, clicked de calendar
        '''
        try:
            if var.ui.tabWidget.currentIndex() == 1:
                data = ('{0}/{1}/{2}'.format(qDate.day(), qDate.month(), qDate.year()))
                var.ui.editDatafac.setText(str(data))
                var.dlgcalendar.hide()
        except Exception as error:
            print('Error cargar fecha factura: %s ' % str(error))

    def cargarFact(self):
        '''
        Módulo que carga los datos de la factura y cliente
        :return:
        '''
        try:
            var.subfac = 0.00
            var.fac = 0.00
            var.iva = 0.00
            fila = var.ui.tabFac.selectedItems()
            if fila:
                fila = [dato.text() for dato in fila]
            codf = fila[0]
            var.ui.lblNumFac.setText(str(codf))
            var.ui.editDatafac.setText(str(fila[1]))
            conexion.Conexion.cargarFac(str(codf))
        except Exception as error:
            print('Error cargar Factura: %s ' % str(error))

    def prepararTablaventas(index):
        '''
        Modulo que prepara tabla Ventas, carga un combo en la tabla
        y carga dicho combo con los datos del producto
        :return:
        '''
        try:
            var.cmbventa = QtWidgets.QComboBox()
            conexion.Conexion.cargarCmbventa(var.cmbventa)
            var.ui.tabVenta.setRowCount(index + 1)
            var.ui.tabVenta.setItem(index, 0, QtWidgets.QTableWidgetItem())
            var.ui.tabVenta.setCellWidget(index, 1, var.cmbventa)
            var.ui.tabVenta.setItem(index, 2, QtWidgets.QTableWidgetItem())
            var.ui.tabVenta.setItem(index, 3, QtWidgets.QTableWidgetItem())
            var.ui.tabVenta.setItem(index, 4, QtWidgets.QTableWidgetItem())
        except Exception as error:
            print('Error Preparar tabla de ventas: %s ' % str(error))

    def procesoVenta(self):
        try:
            var.subfac = 0.00
            var.venta = []
            codfac = var.ui.lblNumFac.text()
            var.venta.append(int(codfac))
            articulo = var.cmbventa.currentText()
            dato = conexion.Conexion.obtenCodPrec(articulo)
            var.venta.append(int(dato[0]))
            var.venta.append(articulo)
            row = var.ui.tabVenta.currentRow()
            cantidad = var.ui.tabVenta.item(row, 2).text()
            cantidad = cantidad.replace(',', '.')
            var.venta.append(int(cantidad))
            precio = dato[1].replace(',', '.')
            var.venta.append(round(float(precio),2))
            subtotal = round(float(cantidad)*float(dato[1]), 2)
            var.venta.append(subtotal)
            var.venta.append(row)
            #sleep(1)
            if codfac != '' and articulo != '' and cantidad != '':
                conexion.Conexion.altaVenta()
                var.subfac = round(float(subtotal) + float(var.subfac),2)
                var.ui.lblSubtotal.setText(str(var.subfac))
                var.iva = round(float(var.subfac) * 0.21, 2)
                var.ui.lblIva.setText(str(var.iva))
                var.fac = round(float(var.iva) + float(var.subfac), 2)
                var.ui.lblTotal.setText(str(var.fac))
                Ventas.mostrarVentasfac()
            else:
               var.ui.lblstatus.setText('Faltan Datos de la Factura')

        except Exception as error:
            print('Error proceso venta: %s ' % str(error))

    def mostrarVentasfac():
        try:
            var.cmbventa = QtWidgets.QComboBox()
            codfac = var.ui.lblNumFac.text()
            conexion.Conexion.listadoVentasfac(codfac)
            conexion.Conexion.cargarCmbventa(var.cmbventa)
        except Exception as error:
            print('Error proceso mostrar ventas por factura: %s' %str(error))


    def anularVenta(self):
        try:
            fila = var.ui.tabVenta.selectedItems()
            if fila:
                fila = [dato.text() for dato in fila]
            codventa = int(fila[0])
            conexion.Conexion.anulaVenta(codventa)
            Ventas.mostrarVentasfac()

        except Exception as error:
            print('Error proceso anular venta de una factura: %s' % str(error))
