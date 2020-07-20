"""Dessert classes."""


class Cupcake:
    """A cupcake."""
    cache = {}

    def __init__(self, name, flavor, price):
      cache = {}
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

      while self.qty > 0 and amount > 0:
        self.qty = self.qty - 1
        amount +- 1
      if self.qty < 0:
        print('Sorry, these cupcakes are sold out')



    @staticmethod
    def scale_recipe(ingredients, amount):

      for ingredient in ingredients:
        ingredient[1] = ingredient[1] * amount

      return ingredients

    @classmethod
    def get(cls, name):
      if self.name not in Class.cache:
        print(f"Sorry, that cupcake doesn't exist")




    def __repr__(self):
        """Human-readable printout for debugging."""

        return f'<Cupcake name="{self.name}" qty={self.qty}>'


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
