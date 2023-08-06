class FXConverter:
    def convert(self, from_currency, to_currency, amount):
        print(f'{amount} {from_currency} = {amount * 1.2} {to_currency}')
        return amount * 1.2


class App:
    def start(self):
        converter = FXConverter()
        converter.convert('EUR', 'USD', 100)


if __name__ == '__main__':
    app = App()
    app.start()


# In this example, we have two classes FXConverter and App.

# The FXConverter class uses an API from an imaginary FX 
# third-party to convert an amount from one currency to another. 
# For simplicity, we hardcoded the exchange rate as 1.2. 
# In practice, you will need to make an API call to get the
# exchange rate.

# The App class has a start() method that uses an instance 
# of the FXconverter class to convert 100 EUR to USD.

# The App is a high-level module. However, The App depends 
# heavily on the FXConverter class that is dependent on the 
# FX’s API.


# In the future, if the FX’s API changes, it’ll break the code.
#  Also, if you want to use a different API, you’ll need to change
#   the App class.

# To prevent this, you need to invert the dependency so that the 
# FXConverter class needs to adapt to the App class.

# To do that, you define an interface and make the App dependent 
# on it instead of FXConverter class. And then you change the 
# FXConverter to comply with the interface.