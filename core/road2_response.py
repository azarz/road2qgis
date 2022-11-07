from road2qgis.core.road2_portion import Road2Portion

class Road2Response:
    """Classe représentant une réponse du service d'itinéraires road2

    Attributes
    ----------
    resource
    resourceVersion
    start
    end
    profile
    optimization
    geometry
    crs
    distanceUnit
    timeUnit
    bbox
    distance
    duration
    constraints
    portions
    """

    def __init__(self, response):
        """Constructeur de la classe

        Parameters
        ----------
        response : dict
            Résultat du parsing du json de la réponse
        """
        self._resource = response["resource"]
        self._resourceVersion = response["resourceVersion"]
        self._start = tuple(map(float, response["start"].split(",")))
        self._end = tuple(map(float, response["end"].split(",")))
        self._profile = response["profile"]
        self._optimization = response["optimization"]
        self._geometry = response["geometry"]
        self._crs = response["crs"]
        self._distanceUnit = response["distanceUnit"]
        self._timeUnit = response["timeUnit"]
        self._bbox = list(map(float, response["bbox"]))
        self._distance = float(response["distance"])
        self._duration = float(response["duration"])
        self._constraints = response["constraints"]
        self._portions = [Road2Portion(portion) for portion in response["portions"]]

    @property
    def resource(self):
        """
        """
        return self._resource

    @property
    def resourceVersion(self):
        """
        """
        return self._resourceVersion

    @property
    def start(self):
        """
        """
        return self._start

    @property
    def end(self):
        """
        """
        return self._self

    @property
    def profile(self):
        """
        """
        return self._profile

    @property
    def optimization(self):
        """
        """
        return self._optimization

    @property
    def geometry(self):
        """
        """
        return self._geometry

    @property
    def crs(self):
        """
        """
        return self._self

    @property
    def distanceUnit(self):
        """
        """
        return self._distanceUnit

    @property
    def timeUnit(self):
        """
        """
        return self._timeUnit

    @property
    def bbox(self):
        """
        """
        return self._bbox

    @property
    def distance(self):
        """
        """
        return self._distance

    @property
    def duration(self):
        """
        """
        return self._duration

    @property
    def constraints(self):
        """
        """
        return self._constraints

    @property
    def portions(self):
        """
        """
        return self._portions

    def getFeature(self):
        """Returns a representation of the route response in a single feature

        Returns
        -------
        dict
            geojson representation of the response
        """
        feature_properties = {}
        feature_properties["distance"] = self._distance
        feature_properties["duration"] = self._duration
        feature_properties["distanceUnit"] = self._distanceUnit
        feature_properties["timeUnit"] = self._timeUnit

        return {
            "type": "Feature",
            "geometry": self.geometry,
            "properties": feature_properties
        }

    def getFeatureCollections(self):
        """Returns a representation of the route portions in a list of FeatureCollections

        Returns
        -------
        list
            list of geojson FeatureCollections representing the portions
        """

        return [ portion.getFeatureCollection() for portion in self._portions ]
