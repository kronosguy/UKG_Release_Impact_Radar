from __future__ import annotations

import hashlib
import random


def derive_hex(*parts: object, digest_size: int = 32) -> str:
    payload = "|".join(str(part) for part in parts).encode("utf-8")
    return hashlib.blake2b(payload, digest_size=digest_size).hexdigest()


def seed_int(*parts: object) -> int:
    return int(derive_hex(*parts, digest_size=16), 16)


def rng(*parts: object) -> random.Random:
    return random.Random(seed_int(*parts))


def stable_id(prefix: str, *parts: object, length: int = 26) -> str:
    return f"{prefix}_{derive_hex(*parts, digest_size=20)[:length]}"
