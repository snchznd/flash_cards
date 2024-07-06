class Card:
    """This class represents a basic flash card."""

    def __init__(self, question : str, answer : str, additional_info : str = None):
        self.id = self.get_id()
        self.question = question
        self.answer = answer
        self.additional_info = additional_info 
    
    def get_id(self):
        return hash(self)

    def __str__(self):
        representation = ('    question : {0}\n    answer : {1}\n    additional information : {2}'
                          .format(self.question, self.answer, self.additional_info))
        return representation


    def __repr__(self):
        return '{0}("{1}", "{2}", "{3}")'.format(self.__class__.__name__, self.question, self.answer, self.additional_info)