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

    def __repr__(self) -> str:
        return "Email(local_part={!r}, domain_part={!r})".format(*self._parts)

    def __eq__(self, rhs) -> bool:
        if not isinstance(rhs, Email):
            return NotImplemented
        return self._parts == rhs._parts

    def __ne__(self, rhs) -> bool:
        return not (self == rhs)

    def __hash__(self) -> str:
        return hash(self._parts)

    @property
    def local(self):
        return self._parts[0]
