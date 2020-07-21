"""Dessert classes."""


class Cupcake:
    """A cupcake."""
    cache = {}


    def __repr__(self):
        """Human-readable printout for debugging."""

        return f'<Cupcake name="{self.name}" qty={self.qty}>'

    def __init__(self, name, flavor, price):

      self.name = name
      self.flavor = flavor
      self.price = price
      self.qty = 0

      self.cache[name] = self

    def add_stock(self, amount):
      self.qty = self.qty + amount

    def sell(self, amount):

      #if self.qty > 0 and self.qty < amount:
       # print(f'Not enough cupcakes. there are {self.qty} left.')

      if self.qty == 0:
        print('Sorry, these cupcakes are sold out')

      if self.qty < amount:
        self.qty = 0
        return

      self.qty -= amount

    @staticmethod
    def scale_recipe(ingredients, amount):


      return [(ingredient, qty * amount)
              for ingredient, qty in ingredients]

    @classmethod
    def get(cls, name):

      if name not in cls.cache:
        print(f'Sorry, that cupcake doesn\'t exist')
        return

      return cls.cache[name]

class Brownie(Cupcake):

  cache = {}
  flavor = 'chocolate'

  def __init__(self, name, price, qty):
    super().__init__(name, price, qty)
    self.qty = qty

    def add_stock(self, amount):
      return super().add_stock()

    def sell(self, amount):
      return super().sell()

    @staticmethod
    def scale_recipe(ingredients, amount):
      return super().scale_recipe()

    @staticmethod
    def get(cls, name):
      return super().get()





if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
