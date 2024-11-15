class Road2ResponseIso:
    """Classe représentant une réponse du service d'isochrones road2

    Attributes
    ----------
    resource
    resourceVersion
    point
    profile
    costType
    costValue
    direction
    geometry
    crs
    distanceUnit
    timeUnit
    constraints
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
        self._point = tuple(map(float, response["point"].split(",")))
        self._profile = response["profile"]
        self._costType = response["costType"]
        self._costValue = response["costValue"]
        self._direction = response["direction"]
        self._geometry = response["geometry"]
        self._crs = response["crs"]
        if self._costType == "distance" :
            self._distanceUnit = response["distanceUnit"]
            self._timeUnit = ""
        else:
            self._distanceUnit = ""
            self._timeUnit = response["timeUnit"]
        self._constraints = response["constraints"]

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
    def point(self):
        """
        """
        return self._point

    @property
    def profile(self):
        """
        """
        return self._profile

    @property
    def costType(self):
        """
        """
        return self._costType

    @property
    def costValue(self):
        """
        """
        return self._costValue

    @property
    def direction(self):
        """
        """
        return self._direction

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
    def constraints(self):
        """
        """
        return self._constraints

    def getFeature(self):
        """Returns a representation of the isochrone response in a single feature

        Returns
        -------
        dict
            geojson representation of the response
        """
        feature_properties = {}
        feature_properties["costValue"] = self._costValue
        feature_properties["costType"] = self._costType
        if self._costType == "distance":
            feature_properties["distanceUnit"] = self._distanceUnit
        else:
            feature_properties["timeUnit"] = self._timeUnit

        return {
            "type": "Feature",
            "geometry": self.geometry,
            "properties": feature_properties
        }

