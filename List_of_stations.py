
def List_of_stations():
  class list_for_testing:
    def __init__(self, name, label, coord, river, town, typical_range):
      self.name = name
      self.label = label
      self.coord = coord
      self.river = river
      self.town = town
      self.typical_range = typical_range

  S1 = list_for_testing("s1", "label1", (1, 2), "river1", "town1", (1,2))
  S2 = list_for_testing("s2", "label2", (2, 3), "river2", "town2" (2,1))
  S3 = list_for_testing("s3", "label3", (3, 4), "river3", "town3", None)
  S4 = list_for_testing("s4", "label4", (4, 5), "river4", "town4", (3,4))
  S5 = list_for_testing("s5", "label5", (5, 6), "river5", "town5", (4,5))

  return [S1, S2, S3, S4, S5]



