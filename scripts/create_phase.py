"""
Script for a dialog window where users can create a phase with custom structure 
"""
from typing import Optional
from diffpy.structure.atom import Atom
from diffpy.structure.lattice import Lattice
from diffpy.structure.structure import Structure
from orix.crystal_map import Phase
from PySide6.QtWidgets import QDialog, QWidget

from ui.ui_new_phase import Ui_NewPhaseDialog


class NewPhaseDialog(QDialog):
    """
    Dialog window where users can create a phase with custom structure
    """

    def __init__(self, parent: QWidget, default_color=None) -> None:
        """
        Dialog window where users can create a phase with custom structure

        Parameters
        ----------
        parent : QWidget
            The parent widget
        default_color : str
            The color which is assigned to the phase if none is specified
        """
        super().__init__(parent)
        self.ui = Ui_NewPhaseDialog()
        self.ui.setupUi(self)
        self.setupConnections()
        self.ui.labelMessage.setHidden(True)
        self.default_color = default_color

    def setupConnections(self):
        self.ui.buttonBox.accepted.connect(self.validatePhaseParameters)
        self.ui.pushButtonAddAtom.clicked.connect(self.addEmptyAtom)
        self.ui.pushButtonRemoveAtom.clicked.connect(self.removeAtom)
        self.ui.tableWidgetAtoms.itemSelectionChanged.connect(self.setAtomButtons)
        self.ui.checkBoxStructure.toggled.connect(
            lambda toggle: self.setAtomButtons(toggle)
        )

    def setAtomButtons(self, structure_enabled=True):
        """
        Enables/ disables the ability to remove atoms from the table
        """
        remove = self.ui.pushButtonRemoveAtom
        atomsTable = self.ui.tableWidgetAtoms
        if not structure_enabled:
            atomsTable.selectionModel().clearSelection()
            remove.setEnabled(False)
        elif (
            len(atomsTable.selectionModel().selectedRows())
            and atomsTable.rowCount() > 1
        ):
            remove.setEnabled(True)
        else:
            remove.setEnabled(False)

    def addEmptyAtom(self):
        """
        Adds an empty atom row to the table of atoms
        """
        atomsTable = self.ui.tableWidgetAtoms
        atomsTable.setRowCount(atomsTable.rowCount() + 1)
        atomsTable.setVerticalHeaderLabels(
            f"Atom {str(num + 1)}" for num in range(atomsTable.rowCount())
        )

    def removeAtom(self):
        """
        Removes an atom row from the table of atoms
        """
        atomsTable = self.ui.tableWidgetAtoms
        indexes = atomsTable.selectionModel().selectedRows()
        for i in range(len(indexes), 0, -1):
            atomsTable.removeRow(indexes[i - 1].row())
        atomsTable.setVerticalHeaderLabels(
            f"Atom {str(num + 1)}" for num in range(atomsTable.rowCount())
        )

    def validatePhaseParameters(self) -> None:
        """
        Checks whether entries satisfies input requirements

        If all input requirements are satisifed, the parameters are saved
        as a dicitonary in the class, named kwargs.
        If not; display message to the user about which entires are
        wrong.

        """
        kwargs = dict()
        message = ""
        kwargs["name"] = self.ui.lineName.text()
        kwargs["space_group"] = self.ui.lineSpaceGroup.text()
        if not len(kwargs["name"]):
            message += "\nNo name was given"
        if not kwargs["space_group"].isnumeric() or int(
            kwargs["space_group"]
        ) not in range(1, 231, 1):
            message += "\nSpace group must be an integer in range [1, 230]"
        else:
            kwargs["space_group"] = int(self.ui.lineSpaceGroup.text())
        kwargs["color"] = self.ui.lineColor.text()
        if self.ui.checkBoxStructure.isChecked():
            atomsTable = self.ui.tableWidgetAtoms
            latticeTable = self.ui.tableWidgetLattice
            ATOM_ELEMENT_INDX = 0
            ATOM_X_INDX = 1
            ATOM_Y_INDX = 2
            ATOM_Z_INDX = 3
            ATOM_OCCUP = 4
            atoms = []
            lattice_kwargs = {}
            for row in range(atomsTable.rowCount()):
                element_item = atomsTable.item(row, ATOM_ELEMENT_INDX)
                if not element_item or not len(element_item.text()):
                    message += f"\nAtom {row + 1} has no element"
                elif not element_item.text().isnumeric() and True in (
                    char.isnumeric() for char in element_item.text()
                ):
                    message += f"\nAtom {row + 1} element cannot be a combination of numbers and letters"
                elif (
                    not element_item.text().isnumeric()
                    and not element_item.text()[0].isupper()
                ):
                    message += f"\nAtom {row + 1} element's first letter must be a captial letter"
                else:
                    try:
                        atom = Atom(
                            atype=atomsTable.item(row, ATOM_ELEMENT_INDX).text(),
                            xyz=[
                                float(atomsTable.item(row, ATOM_X_INDX).text()),
                                float(atomsTable.item(row, ATOM_Y_INDX).text()),
                                float(atomsTable.item(row, ATOM_Z_INDX).text()),
                            ],
                            occupancy=float(atomsTable.item(row, ATOM_OCCUP).text()),
                        )
                        if atom.element.isnumeric():
                            atom.element = int(atom.element)
                        atoms.append(atom)
                    except:
                        message += f"\nAtom {row + 1} contains illegal values"
            for col, kwarg in enumerate(["a", "b", "c", "alpha", "beta", "gamma"]):
                cell = latticeTable.item(0, col)
                if cell is not None and cell.text().replace(".", "").isnumeric():
                    lattice_kwargs[kwarg] = float(cell.text())
                else:
                    message += f"\nLattice parameter '{kwarg}' contains {'illegal value '+cell.text() if cell else 'nothing'}"
            try:
                kwargs["structure"] = Structure(
                    atoms, lattice=Lattice(**lattice_kwargs)
                )
            except:
                pass
        if len(message):
            self.ui.labelMessage.setText(message[1:])
            self.ui.labelMessage.setHidden(False)
            return
        self.kwargs = kwargs
        self.accept()

    def get_phase(
        self,
        name: str,
        space_group: int,
        structure: Optional[Structure] = None,
        color: Optional[str] = "",
    ):
        """
        Returns a phase which contains the input parameters

        Parameters
        ----------
        name : str
            The name of the phase.
        space_group: int
            The space group of the phase.
        structure: Structure
            Structure object of the phase.
            If none is given, a default strucutre object is used
            in the returned phase.
        color:
            The color which is assigned to the phase.
        
        Returns
        -------
        Phase
            A phase containing parameters derived from the input parameters.
        """
        if not len(color):
            color = self.default_color
        try:
            if structure:
                return Phase(
                    name,
                    space_group,
                    structure=structure,
                    color=color,
                )
            else:
                return Phase(name, space_group, color=color)
        except Exception as e:
            raise e
