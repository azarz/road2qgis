import json
from qgis.PyQt import QtGui, QtCore, QtWidgets, QtNetwork


# Autocomplete code from user eyllanesc https://stackoverflow.com/questions/55027186/pyqt5-autocomplete-qlineedit-google-places-autocomplete
class SuggestionPlaceModel(QtGui.QStandardItemModel):
    """
    """
    finished = QtCore.pyqtSignal()
    error = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(SuggestionPlaceModel, self).__init__(parent)
        self._manager = QtNetwork.QNetworkAccessManager(self)
        self._reply = None

    @QtCore.pyqtSlot(str)
    def search(self, text):
        self.clear()
        if self._reply is not None:
            self._reply.abort()
        if text:
            r = self.create_request(text)
            self._reply = self._manager.get(r)
            self._reply.finished.connect(self.on_finished)
        loop = QtCore.QEventLoop()
        self.finished.connect(loop.quit)
        loop.exec_()

    def create_request(self, text):
        url = QtCore.QUrl("https://wxs.ign.fr/calcul/geoportail/geocodage/rest/0.1/completion")
        query = QtCore.QUrlQuery()
        query.addQueryItem("type", "StreetAddress,PositionOfInterest")
        query.addQueryItem("maximumResponses", "5")
        query.addQueryItem("text", text)
        url.setQuery(query)
        request = QtNetwork.QNetworkRequest(url)
        return request

    @QtCore.pyqtSlot()
    def on_finished(self):
        reply = self.sender()
        if reply.error() == QtNetwork.QNetworkReply.NoError:
            data = json.loads(reply.readAll().data())
            if data['status'] == 'OK':
                for result in data['results']:
                    self.appendRow(AutocompleteItem(result['fulltext'], result["x"], result["y"]))
            self.error.emit(data['status'])
        self.finished.emit()
        reply.deleteLater()
        self._reply = None

class AutocompleteItem(QtGui.QStandardItem):
    def __init__(self, text, x, y):
        """
        """
        QtGui.QStandardItem.__init__(self, text)
        self.longitude = x
        self.latitude = y

class Completer(QtWidgets.QCompleter):
    """
    """
    def splitPath(self, path):
        self.model().search(path)
        self.popup().setMinimumWidth(360)
        return super(Completer, self).splitPath(path)
