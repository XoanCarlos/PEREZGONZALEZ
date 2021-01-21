from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from PyQt5 import QtSql
import os
from datetime import datetime
import var


class Printer:

    def cabecera(self):
        try:
            logo = '.\\img\logo.jpg'
            var.rep.setTitle('INFORMES')
            var.rep.setAuthor('Administración')
            var.rep.setFont('Helvetica', size=10)
            var.rep.line(45, 820, 525, 820)
            var.rep.line(45, 745, 525, 745)
            textcif = 'CIF: A0000000H'
            textnom = 'IMPORTACIÓN Y EXPORTACIÓN TEIS, S.L.'
            textdir = 'Avenida Galicia, 101 - Vigo'
            texttlfo = 'Tlfo: 886 12 04 64'
            var.rep.drawString(50, 805, textcif)
            var.rep.drawString(50, 790, textnom)
            var.rep.drawString(50, 775, textdir)
            var.rep.drawString(50, 760, texttlfo)
            var.rep.drawImage(logo, 450, 752)
        except Exception as error:
            print("Error cabecera informe: %s" % str(error))

    def pie(textlistado):
        try:
            var.rep.line(50, 50, 525, 50)
            fecha = datetime.today()
            fecha = fecha.strftime('%d.%m.%Y  %H.%M.%S')
            var.rep.setFont('Helvetica-Oblique', size=7)
            var.rep.drawString(460, 40, str(fecha))
            var.rep.drawString(275, 40, str('Página %s' % var.rep.getPageNumber()))
            var.rep.drawString(50, 40, str(textlistado))
        except Exception as error:
            print('Error en el píe de informe: %s'  % str(error))

    def cabeceracli(self):
        try:
            var.rep.setFont('Helvetica-Bold', size=9)
            textlistado = 'LISTADO DE CLIENTES'
            var.rep.drawString(255, 735, textlistado)
            var.rep.line(45, 730, 525, 730)
            itemcli = ['Cod', 'DNI', 'APELLIDOS', 'NOMBRE', 'FECHA ALTA']
            var.rep.drawString(45, 710, itemcli[0])
            var.rep.drawString(90, 710, itemcli[1])
            var.rep.drawString(180, 710, itemcli[2])
            var.rep.drawString(325, 710, itemcli[3])
            var.rep.drawString(465, 710, itemcli[4])
            var.rep.line(45, 703, 525, 703)
        except Exception as error:
            print('Error en cabecera 2 de clientes : %s' % str(error))

    def reportCli(self):
        try:

            textlistado = 'LISTADO DE CLIENTES'
            var.rep = canvas.Canvas('informes/listadoclientes.pdf', pagesize=A4)
            Printer.cabecera(self)
            Printer.cabeceracli(self)
            Printer.pie(textlistado)
            query = QtSql.QSqlQuery()
            query.prepare('select codigo, dni, apellidos, nombre, fechalta from clientes order by apellidos, nombre')
            var.rep.setFont('Helvetica', size=10)
            if query.exec_():
                i = 50  #valores del eje X
                j = 690 #valores del eje Y
                while query.next():
                     if j <= 80:
                         var.rep.drawString(440, 70, 'Página siguiente...')
                         var.rep.showPage()
                         Printer.cabecera(self)
                         Printer.pie(textlistado)
                         Printer.cabeceracli(self)
                         i = 55
                         j = 690
                     var.rep.setFont('Helvetica', size=10)
                     var.rep.drawString(i, j, str(query.value(0)))
                     var.rep.drawString(i + 30, j, str(query.value(1)))
                     var.rep.drawString(i + 130, j, str(query.value(2)))
                     var.rep.drawString(i + 275, j, str(query.value(3)))
                     var.rep.drawRightString(i + 465, j, str(query.value(4)))
                     j=j-25

            var.rep.save()
            rootPath = ".\\informes"
            cont = 0
            for file in os.listdir(rootPath):
                if file.endswith('listadoclientes.pdf'):
                    os.startfile("%s/%s" % (rootPath, file))
                cont = cont + 1
        except Exception as error:
            print('Error reporcli %s' % str(error))

    def cabecerapro(self):
        try:
            var.rep.setFont('Helvetica-Bold', size=9)
            textlistado = 'LISTADO DE PRODUCTOS'
            var.rep.drawString(255, 735, textlistado)
            var.rep.line(45, 730, 525, 730)
            itempro = ['Código', 'NOMBRE', 'PRECIO (€)', 'STOCK']
            var.rep.drawString(45, 710, itempro[0])
            var.rep.drawString(170, 710, itempro[1])
            var.rep.drawString(350, 710, itempro[2])
            var.rep.drawString(475, 710, itempro[3])
            var.rep.line(45, 703, 525, 703)
        except Exception as error:
            print('Error en cabecera 2 de productos : %s' % str(error))

    def reportPro(self):
        try:
            textlistado = 'LISTADO DE PRODUCTOS'
            var.rep = canvas.Canvas('informes/listadoproductos.pdf', pagesize=A4)
            Printer.cabecera(self)
            Printer.cabecerapro(self)
            Printer.pie(textlistado)
            query = QtSql.QSqlQuery()
            query.prepare('select codigo, producto, precio, stock from productos order by producto')
            var.rep.setFont('Helvetica', size=10)
            if query.exec_():
                 i = 50  # valores del eje X
                 j = 690  # valores del eje Y
                 while query.next():
                     if j <= 80:
                         var.rep.drawString(440, 70, 'Página siguiente...')
                         var.rep.showPage()
                         Printer.cabecera(self)
                         Printer.pie(textlistado)
                         Printer.cabecerapro(self)
                         i = 50
                         j = 690
                     var.rep.setFont('Helvetica', size=10)
                     var.rep.drawString(i, j, str(query.value(0)))
                     var.rep.drawString(i + 100, j, str(query.value(1)))
                     var.rep.drawRightString(i + 325, j, str(query.value(2)))
                     var.rep.drawRightString(i + 450, j, str(query.value(3)))
                     j = j - 25
            var.rep.save()
            rootPath = ".\\informes"
            cont = 0
            for file in os.listdir(rootPath):
                if file.endswith('listadoproductos.pdf'):
                    os.startfile("%s/%s" % (rootPath, file))
                cont = cont + 1

        except Exception as error:
            print('Error reporcli %s' % str(error))

    def cabecerafac(codfac):
        try:
            var.rep.setFont('Helvetica-Bold', size=11)
            var.rep.drawString(55, 725, 'Cliente: ')
            var.rep.setFont('Helvetica', size=10)
            var.rep.drawString(50, 650, 'Factura nº : %s' % str(codfac))
            var.rep.line(45, 665, 525, 665)
            var.rep.line(45, 640, 525, 640)
            var.rep.setFont('Helvetica', size=10)
            query = QtSql.QSqlQuery()
            query.prepare('select dni, fecha from facturas where codfac = :codfac')
            query.bindValue(':codfac', int(codfac))
            if query.exec_():
                while query.next():
                    dni = str(query.value(0))
                    var.rep.drawString(55, 710, 'DNI: %s' % str(query.value(0)))
                    var.rep.drawString(420, 650, 'Fecha: %s' % str(query.value(1)))
            query1 = QtSql.QSqlQuery()
            query1.prepare('select apellidos, nombre, direccion, provincia, formaspago from clientes where dni = :dni')
            query1.bindValue(':dni', str(dni))
            if query1.exec_():
                while query1.next():
                    var.rep.drawString(55, 695, str(query1.value(0)) + ', ' + str(query1.value(1)))
                    var.rep.drawString(300, 695, 'Formas de Pago: ')
                    var.rep.drawString(55, 680, str(query1.value(2)) + ' - ' + str(query1.value(3)))
                    var.rep.drawString(300, 680, str(query1.value(4).strip('[]').replace('\'', '').replace(',', ' -')))  #\ caracter escape indica que lo siguiente tiene un significado especial
            var.rep.line(45, 625, 525, 625)
            var.rep.setFont('Helvetica-Bold', size=10)
            temven = ['CodVenta', 'Artículo', 'Cantidad', 'Precio-Unidad(€)', 'Subtotal(€)']
            var.rep.drawString(50, 630, temven[0])
            var.rep.drawString(140, 630, temven[1])
            var.rep.drawString(275, 630, temven[2])
            var.rep.drawString(360, 630, temven[3])
            var.rep.drawString(470, 630, temven[4])
            var.rep.setFont('Helvetica-Bold', size=12)
            var.rep.drawRightString(500, 160, 'Subtotal:   ' + "{0:.2f}".format(float(
                var.ui.lblSubtotal.text())) + ' €')
            var.rep.drawRightString(500, 140, 'IVA:     ' + "{0:.2f}".format(float(var.ui.lblIva.text())) + ' €')
            var.rep.drawRightString(500, 115, 'Total Factura: ' + "{0:.2f}".format(float(
                var.ui.lblTotal.text())) + ' €')
        except Exception as error:
            print('Error cabecfac %s' % str(error))

    def reportFac(self):
        try:
            textlistado = 'FACTURA'
            var.rep = canvas.Canvas('informes/factura.pdf', pagesize=A4)
            Printer.cabecera(self)
            Printer.pie(textlistado)
            codfac = var.ui.lblNumFac.text()
            Printer.cabecerafac(codfac)
            query = QtSql.QSqlQuery()
            query.prepare('select codventa, codarticventa, cantidad, precio from ventas where codfacventa = :codfac')
            query.bindValue(':codfac', int(codfac))
            if query.exec_():
                i = 55  # valores del eje X
                j = 600  # valores del eje Y
                while query.next():
                    if j <= 100:
                        var.rep.drawString(440, 110, 'Página siguiente...')
                        var.rep.showPage()
                        Printer.cabecera(self)
                        Printer.pie(textlistado)
                        Printer.cabecerafac(self)
                        i = 50
                        j = 600
                    var.rep.setFont('Helvetica', size=10)
                    var.rep.drawString(i, j, str(query.value(0)))
                    var.rep.drawString(i + 90, j, str(query.value(1)))
                    var.rep.drawRightString(i + 245, j, str(query.value(2)))
                    var.rep.drawRightString(i + 355, j, "{0:.2f}".format(float(query.value(3))))
                    subtotal = round(float(query.value(2)) * float(query.value(3)),2)
                    var.rep.drawRightString(i + 450, j, "{0:.2f}".format(float(subtotal)) + ' €')
                    j = j - 20

            var.rep.save()
            rootPath = ".\\informes"
            cont = 0
            for file in os.listdir(rootPath):
                if file.endswith('factura.pdf'):
                    os.startfile("%s/%s" % (rootPath, file))
                cont = cont + 1

        except Exception as error:
            print('Error reporfac %s' % str(error))

