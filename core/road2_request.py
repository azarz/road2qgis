from collections import defaultdict
import requests

from road2qgis.core.road2_response import Road2Response

class Road2Request:
    """Classe représentant une requête du service d'itinéraires road2

    Attributes
    ----------
    server_url
    resource
    start
    end
    intermediates
    profile
    optimization
    getSteps
    waysAttributes
    geometryFormat
    crs
    timeUnit
    distanceUnit
    constraints
    """

    def __init__(self, server_url, resource, start, end, **options):
        """Constructeur de la classe

        Parameters
        ----------
        server_url : str
            url du serveur sur lequel faire la requête
        resource : str
            ressource à interroger
        start : tuple(float, float) :
            point de départ de l'itinéraire
        end : tuple(float, float) :
            point d'arrivée de l'itinéraire
        options : dict
            options facultatives de l'itinéraire
        """

        self._server_url = server_url
        self._resource = resource
        self._start = start
        self._end = end

        options = defaultdict(lambda: "", options)
        self._intermediates = options["intermediates"]
        self._profile = options["profile"]
        self._optimization = options["optimization"]
        self._getSteps = options["getSteps"]
        self._waysAttributes = options["waysAttributes"]
        self._geometryFormat = options["geometryFormat"]
        self._crs = options["crs"]
        self._timeUnit = options["timeUnit"]
        self._distanceUnit = options["distanceUnit"]
        self._constraints = options["constraints"]

    def doRequest(self):
        """Exécute la requête HTTP GET

        Returns
        ----------
        Road2Response
            réponse du service

        """
        params = {
            "resource": self._resource,
            "start": "{},{}".format(self._start[0], self._start[1]),
            "end": "{},{}".format(self._end[0], self._end[1]),
            "intermediates": "|".join([",".join((str(interm[0]), str(interm[1]))) for interm in self._intermediates]),
            "profile": self._profile,
            "optimization": self._optimization,
            "getSteps": str(self._getSteps).lower(),
            "waysAttributes": self._waysAttributes,
            "geometryFormat": self._geometryFormat,
            "crs": self._crs,
            "timeUnit": self._timeUnit,
            "distanceUnit": self._distanceUnit,
            "constraints": self._constraints,
        }

        req = requests.get(self._server_url, params)
        return Road2Response(req.json())

if __name__ == "__main__":
    url = "https://wxs.ign.fr/calcul/geoportail/itineraire/rest/1.0.0/route"
    start = 2.337306, 48.849319
    end = 2.367776, 48.852891
    req = Road2Request(url, "bdtopo-osrm", start, end)
    resp = req.doRequest()

    print(resp.start)
    print(resp.bbox[0])
