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
            textcif = 'A0000000H'
            textnom = 'IMPORTACIÓN Y EXPORTACIÓN TEIS, S.L.'
            textdir = 'Avenida Galicia, 101 - Vigo'
            texttlfo = '886 12 04 64'
            var.rep.drawString(50, 805, textcif)
            var.rep.drawString(50, 790, textnom)
            var.rep.drawString(50, 775, textdir)
            var.rep.drawString(50, 760, texttlfo)
            var.rep.drawImage(logo, 450, 752)
        except Exception as error:
            print("Error cabecera informe: %s" % str(error))

    def pie(textlistado):
        try:
            var.rep.line(50,50, 525, 50)
            fecha = datetime.today()
            fecha = fecha.strftime('%d.%m.%Y  %H.%M.%S')
            var.rep.setFont('Helvetica-Oblique', size=7)
            var.rep.drawString(460, 40, str(fecha))
            var.rep.drawString(275, 40, str('Página %s' % var.rep.getPageNumber()))
            var.rep.drawString(50, 40, str(textlistado))
        except Exception as error:
            print('Error en el píe de informe: %s'  % str(error))

    def cabecerainf(self):
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
            print('Error en cabecera 2 : %s' % str(error))

    def reportCli(self):
        try:
            textlistado = 'LISTADO DE CLIENTES'
            var.rep = canvas.Canvas('informes/listadoclientes.pdf', pagesize=A4)
            Printer.cabecera(self)
            Printer.cabecerainf(self)
            query = QtSql.QSqlQuery()
            query.prepare('select codigo, dni, apellidos, nombre, fechalta from clientes order by apellidos, nombre')
            var.rep.setFont('Helvetica', size=10)
            if query.exec_():
                i = 50
                j = 690
                Printer.pie(textlistado)
                while query.next():
                    if j <= 80:
                        var.rep.showPage()
                        Printer.cabecera(self)
                        Printer.pie(textlistado)
                        Printer.cabecerainf(self)
                        i = 50
                        j = 690
                    var.rep.setFont('Helvetica', size=10)
                    var.rep.drawString(i, j, str(query.value(0)))
                    var.rep.drawString(i+30, j, str(query.value(1)))
                    var.rep.drawString(i+130, j, str(query.value(2)))
                    var.rep.drawString(i+280, j, str(query.value(3)))
                    var.rep.drawRightString(i+470, j, str(query.value(4)))
                    j=j-25

            var.rep.save()
            rootPath = ".\\informes"
            cont = 0
            for file in os.listdir(rootPath):
                if file.endswith('.pdf'):
                    os.startfile("%s/%s" % (rootPath, file))
                cont = cont + 1

        except Exception as error:
            print('Error reporcli %s' % str(error))
