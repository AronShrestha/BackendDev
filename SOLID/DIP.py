from abc import ABC 

class CurrencyConvertorInteface(ABC):
    """
    This is the abstraction(=>interface) to reduce the coupling(dependency)
    """

    def convert(self, from_currency, to_currency, amount)->float:
        pass


class FXConverter(CurrencyConvertorInteface):

    def convert(self, from_currency, to_currency, amount) -> float:
        print('Converting currency using FX API')
        print(f'{amount} {from_currency} = {amount * 1.2} {to_currency}')
        return amount * 2


class AlphaConverter(CurrencyConvertorInteface):
    def convert(self, from_currency, to_currency, amount) -> float:
        print('Converting currency using Alpha API')
        print(f'{amount} {from_currency} = {amount * 1.2} {to_currency}')
        return amount * 1.15


class App:

    def __init__(self, converter : CurrencyConvertorInteface):
        """
        add the __init__ method to the App class and initialize the CurrencyConverterInterface object:
        """
        self.converter = converter
    
    def start(self):
        self.converter.convert('EUR', 'USD', 1000)



if __name__ == '__main__':
    converter = FXConverter()
    app = App(converter)
    app.start()
    converter2 = AlphaConverter()
    app2 = App(converter)
    app2.start()