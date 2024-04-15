"""
Controller class between our endpoints and core ml module.
"""
from app.core.ner import get_ner_model

MIN_LENGTH = 5
MAX_LENGTH = 500


class NerError(Exception):
    pass


class ModelService:
    def __init__(self):
        """
        Object Initialization for class

        :Params:
        None
        :Returns:
        None
        """
        self._model = get_ner_model()

    def get_ner(self, text: str) -> str:
        """
        Extract the entities using the spacy models.

        Args:
            text (str): The text to extract entities.

        Returns:
            str: List of extracted entities.

        Raises:
            NerError: If the text is too short or if there's an error in the NER process.
        """

        if not text or len(text.split()) < MIN_LENGTH:
            #logger.warning("Received a short text for ner.")
            raise NerError("Please provide a bigger text.")

        try:
            ner = self._model(text)
            ner_ = {ent.text: ent.label_ for ent in ner.ents}
            return ner_
        except Exception as e:
            #logger.error(f"Error during NER: {str(e)}")
            raise NerError(f"Failed to extract the entities: {str(e)}")

    def configure(self, **kwargs):
        """
        Method for future utilization

        :Params:
        None
        :Returns:
        None
        """
        pass

    def change(self, model_name):
        """
        Method for future utilization

        :Params:
        None
        :Returns:
        None
        """
        pass

    def clear(self):
        """
        Method for future utilization

        Parameters:
        None

        Returns:
        None
        """
        pass
