import numpy
import bob.io.base

from bob.bio.base.extractor import Extractor

_data = [0., 1., 2., 3., 4.]

class DummyExtractor (Extractor):
  def __init__(self, **kwargs):
    Extractor.__init__(self, requires_training=True)
    self.model = False

  def train(self, train_data, extractor_file):
    assert isinstance(train_data, list)
    bob.io.base.save(_data, extractor_file)

  def load(self, extractor_file):
    data = bob.io.base.load(extractor_file)
    assert (_data == data).all()
    self.model = True

  def __call__(self, data):
    """Does nothing, simply converts the data type of the data, ignoring any annotation."""
    assert self.model
    return data.astype(numpy.float).flatten()

extractor = DummyExtractor()
