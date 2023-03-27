class Email:
    def __init__(self, local_part, domain_part):
        if len(local_part) + len(domain_part) > 255:
            raise ValueError("Email addresses too long")
        self._parts = (local_part, domain_part)
