from typing import Self


class Email:

    @classmethod
    def from_text(cls, address: str) -> (Self | ValueError):
        if '@' not in address:
            raise ValueError("Email addresses must contains '@'")
        local_part, _, domain_part = address.partition('@')
        return cls(local_part, domain_part)

    def __init__(self, local_part: str, domain_part: str):
        if len(local_part) + len(domain_part) > 255:
            raise ValueError("Email addresses too long")
        self._parts = (local_part, domain_part)

    def __str__(self) -> str:
        return '@'.join(self._parts)

    def __repr__(self) -> str:
        return "Email(local_part={!r}, domain_part={!r})".format(*self._parts)

    def __eq__(self, rhs: any) -> bool:
        if not isinstance(rhs, Email):
            return NotImplemented
        return self._parts == rhs._parts

    def __ne__(self, rhs: any) -> bool:
        return not (self == rhs)

    def __hash__(self) -> str:
        return hash(self._parts)

    @property
    def local(self) -> str:
        return self._parts[0]

    @property
    def domain(self) -> str:
        return self._parts[1]

    def replace(self, local: str = None, domain: str = None) -> Self:
        return Email(local_part=local or self._parts[0],
                     domain_part=domain or self._parts[1])
