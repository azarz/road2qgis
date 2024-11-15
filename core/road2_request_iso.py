from collections import defaultdict
import requests

from road2qgis.core.road2_response_iso import Road2ResponseIso

class Road2RequestIso:
    """Classe représentant une requête du service d'isochrone road2

    Attributes
    ----------
    server_url
    resource
    point
    costValue
    costType
    profile
    direction
    geometryFormat
    crs
    timeUnit
    distanceUnit
    constraints
    """

    def __init__(self, server_url, resource, point, costValue, costType, **options):
        """Constructeur de la classe

        Parameters
        ----------
        server_url : str
            url du serveur sur lequel faire la requête
        resource : str
            ressource à interroger
        point : tuple(float, float) :
            point de départ ou d'arrivée de l'isochrone
        options : dict
            options facultatives de l'isochrone
        """

        self._server_url = server_url
        self._resource = resource
        self._point = point
        self._costValue = costValue
        self._costType = costType

        options = defaultdict(lambda: "", options)
        self._profile = options["profile"]
        self._direction = options["direction"]
        self._geometryFormat = options["geometryFormat"]
        self._crs = options["crs"]
        self._timeUnit = options["timeUnit"]
        self._distanceUnit = options["distanceUnit"]
        self._constraints = options["constraints"]

    def doRequest(self):
        """Exécute la requête HTTP GET

        Returns
        ----------
        Road2ResponseIso
            réponse du service d'isochrone

        """
        params = {
            "resource": self._resource,
            "point": "{},{}".format(self._point[0], self._point[1]),
            "costValue": self._costValue,
            "costType": self._costType,
            "direction": self._direction,
            "profile": self._profile,
            "geometryFormat": self._geometryFormat,
            "crs": self._crs,
            "timeUnit": self._timeUnit,
            "distanceUnit": self._distanceUnit,
            "constraints": self._constraints,
        }

        req = requests.get(self._server_url, params)
        return Road2ResponseIso(req.json())

if __name__ == "__main__":
    url = "https://data.geopf.fr/navigation/isochrone"
    point = 2.337306, 48.849319
    costValue = 300
    costType = "time"
    req = Road2RequestIso(url, "bdtopo-valhalla", point, costValue, costType)
    resp = req.doRequest()

    print(resp.start)
    print(resp.bbox[0])
