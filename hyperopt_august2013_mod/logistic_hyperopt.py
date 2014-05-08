from hyperopt import hp

space = {"lrate" : hp.uniform("lrate", 0, 10),
         "l2_reg" : hp.uniform("l2_reg", 0, 1),
         "batchsize" : hp.uniform("batchsize", 20, 2000),
         "n_epochs" : hp.uniform("n_epochs", 5, 2000)}
