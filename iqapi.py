from iqoptionapi.stable_api import IQ_Option
I_want_money = IQ_Option("username", "password")
I_want_money.connect()


I_want_money.buy(10, "EURUSD", "call", 10)
print('sss', I_want_money.get_balance())


# Follow  this url  to make  trade in  iq  logic  in case of long term forex trading
# https://libraries.io/pypi/iqoption-stable-api
