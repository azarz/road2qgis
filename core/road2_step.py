class Road2Step:
    """Classe représentant un step dans une réponse road2

    Attributes
    ----------
    geometry : str
        Géométrie de l'étape au format GeoJSON
    attributes : dict
       Attributs demandés dans la requête
    distance : float
        Distance de l'étape dans l'unité demandée (mètre par défaut)
    duration : float
        Durée de l'étape dans l'unité demandée (seconde par défaut)
    instruction : dict
        Dans le cas d'une ressource supportant les instructions, instruction de navigation
    """

    def __init__(self, step):
        """Constructeur de la classe

        Parameters
        ----------
        step : dict
            Représentation du step, obtenue en parsant le JSON de la réponse
        """
        self._geometry = step["geometry"]
        self._attributes = step["attributes"]
        self._distance = float(step["distance"])
        self._duration = float(step["duration"])
        self._instruction = step["instruction"]

    @property
    def geometry(self):
        """Géométrie de l'étape au format GeoJSON

        Returns
        -------
        str
            géométrie de l'étape
        """
        return self._geometry

    @property
    def attributes(self):
        """Attributs de l'étape

        Returns
        -------
        dict
            attributs de l'étape
        """
        return self._attributes

    @property
    def distance(self):
        """Distance de l'étape dans l'unité demandée (mètre par défaut)

        Returns
        -------
        float
            distance de l'étape
        """
        return self._distance

    @property
    def duration(self):
        """Durée de l'étape dans l'unité demandée (seconde par défaut)

        Returns
        -------
        float
            durée de l'étape
        """
        return self._duration

    @property
    def duration(self):
        """Durée de l'étape dans l'unité demandée (seconde par défaut)

        Returns
        -------
        float
            durée de l'étape
        """
        return self._duration

    @property
    def instruction(self):
        """Instruction de navigation

        Returns
        -------
        dict
            instruction de navigation
        """
        return self._instruction

    def getFeature(self):
        """Returns a representation of the route step in a feature

        Returns
        -------
        dict
            geojson representation of the step
        """
        feature_properties = {}
        feature_properties["distance"] = self._distance
        feature_properties["duration"] = self._duration
        feature_properties["attributes"] = self._attributes
        feature_properties["instruction"] = self._instruction

        return {
            "type": "Feature",
            "geometry": self.geometry,
            "properties": feature_properties
        }
