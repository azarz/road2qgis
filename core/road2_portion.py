from road2qgis.core.road2_step import Road2Step

class Road2Portion:
    """Classe représentant une portion dans une réponse road2

    Attributes
    ----------
    start
    end
    distance
    duration
    bbox
    steps
    """

    def __init__(self, portion):
        """Constructeur de la classe

        Parameters
        ----------
        portion : dict
            Représentation de la portion, obtenue en parsant le JSON de la réponse
        """
        self._start = tuple(map(float, portion["start"].split(",")))
        self._end = tuple(map(float, portion["end"].split(",")))
        self._distance = float(portion["distance"])
        self._duration = float(portion["duration"])
        self._bbox = list(map(float, portion["bbox"]))
        self._steps = [Road2Step(step) for step in portion["steps"]]

    @property
    def start(self):
        """Coordonnées du début de portion

        Returns
        -------
        str
            début de la portion
        """
        return self._start

    @property
    def end(self):
        """Coordonnées de la fin de portion

        Returns
        -------
        str
            fin de la portion
        """
        return self._end

    @property
    def distance(self):
        """Distance de la portion dans l'unité demandée (mètre par défaut)

        Returns
        -------
        float
            distance de la portion
        """
        return self._distance

    @property
    def duration(self):
        """Durée de la portion dans l'unité demandée (seconde par défaut)

        Returns
        -------
        float
            durée de la portion
        """
        return self._duration

    @property
    def duration(self):
        """Durée de la portion dans l'unité demandée (seconde par défaut)

        Returns
        -------
        float
            durée de la portion
        """
        return self._duration

    @property
    def bbox(self):
        """
        """
        return self._bbox

    @property
    def steps(self):
        """
        """
        return self._steps

    def getFeatureCollection(self):
        """Returns a representation of the portion in a feature collection containing all the steps

        Returns
        -------
        dict
            geojson representation of the portion
        """
        return {
            "type": "FeatureCollection",
            "features": [ step.getFeature() for step in self._steps ]
        }
