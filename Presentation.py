from PyQt6 import QtWidgets, QtCore

from Record import Record_DTO

# Omer Kaya


"""
The PresentationLayer class provides a graphical user interface for the user to interact with the records data.
It uses the PyQt library to build the interface, which includes a table for displaying records and buttons for
navigating between pages of records and adding new records. It interacts with the BusinessLayer to retrieve 
and manipulate data.
"""


class PresentationLayer(QtWidgets.QWidget):
    def __init__(self, business):
        super().__init__()
        self.business = business
        self.header = ['id', 'REF_DATE', 'GEO', 'DGUID', 'Type_of_product', 'Type_of_storage', 'UOM', 'UOM_ID',
                       'SCALAR_FACTOR', 'SCALAR_ID', 'VECTOR', 'COORDINATE', 'VALUE', 'STATUS', 'SYMBOL', 'TERMINATE',
                       'DECIMALS']

        self.number_of_records = 0  # Number of total records
        self.records_per_page = 100  # change this to control how many records per page
        self.current_page = 0  # Current page variable

        self.update_number_of_records()

        self.init_ui()

    def init_ui(self):
        self.layout = QtWidgets.QVBoxLayout()

        self.setWindowTitle("Omer Kaya 041035516")  # set the window title

        # create a table for records display and add it to the layout
        self.table = QtWidgets.QTableWidget()
        self.table.setColumnCount(16)
        self.table.setHorizontalHeaderLabels(self.header)
        self.table.setMinimumHeight(200)  # set minimum height for table
        self.table.setMinimumWidth(500)  # set minimum width for table
        self.layout.addWidget(self.table)

        # Add delete button
        self.delete_button = QtWidgets.QPushButton("Delete record")
        self.delete_button.clicked.connect(self.on_delete_button_clicked)
        self.layout.addWidget(self.delete_button)

        # Add record section
        self.add_record_layout = QtWidgets.QGridLayout()
        self.add_record_fields = [QtWidgets.QLineEdit() for _ in range(16)]
        for i, field in enumerate(self.add_record_fields):  # loop through the fields
            self.add_record_layout.addWidget(QtWidgets.QLabel(self.header[i+1]), i, 0)
            self.add_record_layout.addWidget(field, i, 1)
        self.add_record_button = QtWidgets.QPushButton("Add record")
        self.add_record_button.clicked.connect(self.on_add_record_clicked)
        self.add_record_layout.addWidget(self.add_record_button, len(self.add_record_fields), 0, 1, 2)
        self.layout.addLayout(self.add_record_layout)

        # Create navigation buttons
        self.button_first = QtWidgets.QPushButton("↞")
        self.button_first.clicked.connect(self.on_first_button_clicked)

        self.button_prev = QtWidgets.QPushButton("←")
        self.button_prev.clicked.connect(self.on_prev_button_clicked)

        self.button_next = QtWidgets.QPushButton("→")
        self.button_next.clicked.connect(self.on_next_button_clicked)

        self.button_last = QtWidgets.QPushButton("↠")
        self.button_last.clicked.connect(self.on_last_button_clicked)

        # Create a horizontal layout
        self.button_layout = QtWidgets.QHBoxLayout()

        # Add buttons to the layout
        self.button_layout.addWidget(self.button_first)
        self.button_layout.addWidget(self.button_prev)
        self.button_layout.addWidget(self.button_next)
        self.button_layout.addWidget(self.button_last)

        # Add the button layout to the main layout
        self.layout.addLayout(self.button_layout)

        # Set Layout
        self.setLayout(self.layout)

        self.update_records_display()

    @QtCore.pyqtSlot()
    def on_delete_button_clicked(self):
        selected_rows = self.table.selectionModel().selectedRows()
        for selected_row in selected_rows:
            row = selected_row.row()
            record_id = int(self.table.item(row, 0).text())  # Retrieve record ID from the first column
            self.business.delete_record(record_id)
            self.table.removeRow(row)
        self.update_records_display()

    @QtCore.pyqtSlot()
    def on_add_record_clicked(self):
        new_record_data = [field.text() for field in self.add_record_fields]
        new_record = Record_DTO(*new_record_data)
        self.business.add_record(new_record)
        # Clear the input fields after adding a record
        for field in self.add_record_fields:
            field.clear()
        self.update_records_display()

    def update_records_display(self):
        # Clear the table
        self.table.setRowCount(0)

        # Disconnect the cellChanged signal to avoid multiple connections
        try:
            self.table.cellChanged.disconnect()
        except TypeError:
            pass  # Ignore if it was not connected

        # Calculate the range of records to display on the current page
        start = self.current_page * self.records_per_page
        end = start + self.records_per_page

        # Get the records
        records = self.business.get_records()

        # Add records to the table
        for idx, record in enumerate(records[start:end]):
            self.table.insertRow(idx)

            # Here you can order your attributes as you like
            attributes = [record.id, record.REF_DATE, record.GEO, record.DGUID, record.Type_of_product,
                          record.Type_of_storage, record.UOM, record.UOM_ID, record.SCALAR_FACTOR,
                          record.SCALAR_ID, record.VECTOR, record.COORDINATE, record.VALUE, record.STATUS,
                          record.SYMBOL, record.TERMINATE, record.DECIMALS]

            for i, attribute in enumerate(attributes):
                self.table.setItem(idx, i, QtWidgets.QTableWidgetItem(str(attribute)))

        # Enable/disable next/prev buttons based on the current page number
        enable_previous = self.current_page > 0
        self.button_prev.setEnabled(enable_previous)
        self.button_first.setEnabled(enable_previous)

        enable_next = end < self.number_of_records
        self.button_next.setEnabled(enable_next)
        self.button_last.setEnabled(enable_next)

        # Connect the cellChanged signal
        self.table.cellChanged.connect(self.on_cell_changed)

    @QtCore.pyqtSlot()
    def on_first_button_clicked(self):
        self.current_page = 0
        self.update_records_display()

    @QtCore.pyqtSlot()
    def on_prev_button_clicked(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.update_records_display()

    @QtCore.pyqtSlot()
    def on_next_button_clicked(self):
        if (self.current_page + 1) * self.records_per_page < self.number_of_records:
            self.current_page += 1
            self.update_records_display()

    @QtCore.pyqtSlot()
    def on_last_button_clicked(self):
        self.current_page = self.number_of_records // self.records_per_page
        if self.number_of_records % self.records_per_page == 0:
            self.current_page -= 1
        self.update_records_display()

    @QtCore.pyqtSlot(int, int)
    def on_cell_changed(self, row, column):
        new_value = self.table.item(row, column).text()
        record_id = int(self.table.item(row, 0).text())  # Retrieve record ID from the first column
        column_name = self.header[column]  # Assuming self.header contains the column names
        self.business.edit_record(record_id, {column_name: new_value})

    def update_number_of_records(self):
        self.number_of_records = len(self.business.get_records())  # Number of total records
