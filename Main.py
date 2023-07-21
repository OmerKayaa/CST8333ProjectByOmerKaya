from PyQt6 import QtWidgets


from Business import BusinessLayer
from Persistence import PersistenceLayer
from Presentation import PresentationLayer


# Omer Kaya


"""
This is the main driver script that handles the instantiation of the PersistenceLayer, BusinessLayer, 
and PresentationLayer classes and starts the Qt application.
"""


def main():
    persistence = PersistenceLayer()

    business = BusinessLayer(persistence)

    app = QtWidgets.QApplication([])
    presentation = PresentationLayer(business)
    presentation.show()

    app.exec()


if __name__ == '__main__':
    main()

