class Email:

    @classmethod
    def from_text(cls, address):
        if '@' not in address:
            raise ValueError("Email addresses must contains '@'")
        local_part, _, domain_part = address.partition('@')
        return cls(local_part, domain_part)

    def __init__(self, local_part, domain_part):
        if len(local_part) + len(domain_part) > 255:
            raise ValueError("Email addresses too long")
        self._parts = (local_part, domain_part)

    def __str__(self) -> str:
        return '@'.join(self._parts)
