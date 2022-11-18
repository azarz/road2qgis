# -*- coding: utf-8 -*-

from qgis.PyQt import QtGui, QtCore, QtWidgets
from qgis.gui import QgsMapToolEmitPoint
from qgis.core import QgsCoordinateReferenceSystem, QgsCoordinateTransform, QgsProject, QgsPoint

from road2qgis.ui.autocomplete import Completer, SuggestionPlaceModel

class LocationSelector(QtWidgets.QWidget):
    """
    Widget used to select a location using geocoding or a click on the map
    """
    location_selected_signal = QtCore.pyqtSignal(int)
    def __init__(self, label, iface):
        super().__init__()

        self.iface = iface
        self.setFixedSize(QtCore.QSize(260, 30))

        self.label = QtWidgets.QLabel(self)
        self.label.resize(50,28)
        self.label.setText(label)

        self._model = SuggestionPlaceModel(self)
        completer = Completer(self, caseSensitivity=QtCore.Qt.CaseInsensitive)
        completer.setModel(self._model)
        completer.activated[QtCore.QModelIndex].connect(self.completion_callback)

        self.textbox = QtWidgets.QLineEdit(self)
        self.textbox.resize(180,28)
        self.textbox.move(50, 0)
        self.textbox.setCompleter(completer)

        self.location_btn = QtWidgets.QPushButton(self)
        self.location_btn.move(230, 0)
        self.location_btn.resize(28, 28)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/plugins/road2qgis/res/reticule.png"))
        self.location_btn.setIcon(icon)

        self._pointTool = None
        self.location_btn.clicked.connect(self.select_location)

        self.text = ""
        self.latitude = None
        self.longitude = None

    def select_location(self):
        """
        """
        canvas = self.iface.mapCanvas()
        # Set the tool and onClick callback
        self._pointTool = QgsMapToolEmitPoint(canvas)
        self._pointTool.canvasClicked.connect(self.point_callback)
        canvas.setMapTool(self._pointTool)

    def point_callback(self, pt):
        """
        """
        project_crs = self.iface.mapCanvas().mapSettings().destinationCrs()
        target_crs = QgsCoordinateReferenceSystem.fromEpsgId(4326)
        tr = QgsCoordinateTransform(project_crs, target_crs, QgsProject.instance())
        point = QgsPoint(pt.x(), pt.y())
        point.transform(tr)
        self.longitude = round(point.x(), 5)
        self.latitude = round(point.y(), 5)
        self.text = "{} / {}".format(self.longitude, self.latitude)
        self.textbox.setText(self.text)
        self.location_selected_signal.emit(1)
        canvas = self.iface.mapCanvas()
        canvas.unsetMapTool(self._pointTool)

    def completion_callback(self, index):
        """
        """
        self.latitude = self._model.takeRow(index.row())[0].latitude
        self.longitude = self._model.takeRow(index.row())[0].longitude
        self.location_selected_signal.emit(1)
