"""
Data class. Endpoint methods used these defined classes to
auto. convert incoming data or send data
"""
from pydantic import BaseModel


class NERRequest(BaseModel):
    """
    A Pydantic model representing the input for a prediction.

    Attributes:
    -----------
    text : str
        The input data in string format for which a prediction is to be made.
    """

    text: str


class NERResponse(BaseModel):
    """
    A Pydantic model representing the output for a prediction.

    Attributes:
    -----------
    summary : str
        The input data in string format for which a prediction was made.
    """

    ner: dict
