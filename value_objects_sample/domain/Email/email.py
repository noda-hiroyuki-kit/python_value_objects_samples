class Email:
    def __init__(self, local_part, domain_part):
        self._parts = (local_part, domain_part)
