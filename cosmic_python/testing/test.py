from dataclasses import dataclass

@dataclass
class OrderLine:
    orderid: str
    sku: str
    qty: int


class Batch:
    def __init__(self, ref: str, ) -> None:
        

