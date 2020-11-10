from PyQt5 import QtWidgets, QtSql

class Conexion():
    def db_connect(filename):
        try:
            db = QtSql.QSqlDatabase.addDatabase('QSQLite')
            db.setDatabaseName(filename)
            if not db.open():
                QtWidgets.QMessageBox.critical(None, 'No se puede abrir la base de datos','No se puede establecer conexion.\n' 'Haz Click para Cancelar.', QtWidgets.QMessageBox.Cancel)
                return False
            else:
                print('Conexión Establecida')
            return True
        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)