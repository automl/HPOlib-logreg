from hyperopt import hp
from hyperopt.pyll import scope


space = {"lrate" : hp.uniform("lrate", 0, 10),
         "l2_reg" : hp.uniform("l2_reg", 0, 1),
         "batchsize" : scope.int(hp.quniform("batchsize", 20, 2000, 1)),
         "n_epochs" : scope.int(hp.quniform("n_epochs", 5, 2000, 1))}
