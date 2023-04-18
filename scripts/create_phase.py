from diffpy.structure.atom import Atom
from diffpy.structure.lattice import Lattice
from diffpy.structure.structure import Structure
from orix.crystal_map import Phase
from PySide6.QtWidgets import QDialog

from ui.ui_new_phase import Ui_NewPhaseDialog


class NewPhaseDialog(QDialog):
    def __init__(self, parent, default_color=None) -> None:
        super().__init__(parent)
        self.ui = Ui_NewPhaseDialog()
        self.ui.setupUi(self)
        self.setupConnections()
        self.ui.labelMessage.setHidden(True)
        self.params = dict()
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
        atomsTable = self.ui.tableWidgetAtoms
        atomsTable.setRowCount(atomsTable.rowCount() + 1)
        atomsTable.setVerticalHeaderLabels(
            f"Atom {str(num + 1)}" for num in range(atomsTable.rowCount())
        )

    def removeAtom(self):
        atomsTable = self.ui.tableWidgetAtoms
        indexes = atomsTable.selectionModel().selectedRows()
        for i in range(len(indexes), 0, -1):
            atomsTable.removeRow(indexes[i - 1].row())
        atomsTable.setVerticalHeaderLabels(
            f"Atom {str(num + 1)}" for num in range(atomsTable.rowCount())
        )

    def validatePhaseParameters(self) -> None:
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
            atoms = []
            lattice_kwargs = {}
            for row in range(atomsTable.rowCount()):
                element_item = atomsTable.item(row, ATOM_ELEMENT_INDX)
                if not element_item or not len(element_item.text()):
                    message += f"\nAtom {row + 1} has no element"
                else:
                    try:
                        atoms.append(
                            Atom(
                                atype=atomsTable.item(row, ATOM_ELEMENT_INDX).text(),
                                xyz=[
                                    float(atomsTable.item(row, ATOM_X_INDX).text()),
                                    float(atomsTable.item(row, ATOM_Y_INDX).text()),
                                    float(atomsTable.item(row, ATOM_Z_INDX).text()),
                                ],
                            )
                        )
                    except Exception as e:
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
        name: str = "",
        space_group: int = None,
        structure: Structure = None,
        color: str = "",
    ):
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
