import numpy as np
import matplotlib.pyplot as plt
import DataReader 

class NeuralNet:
    def __init__(self,eta):
        self.eta = eta
        self.w = 0
        self.b = 0
    def __forward(self,x):
        z = self.w * x +self.b
        return z
    def __backward(self,x,y,z):
        dz = z - y
        dw = dz * x
        db = dz
        return dw,db
    def __update(self,dw,db):

        self.w = self.w - self.eta * dw
        self.b = self.b - self.eta * db

    def train(self,dataReader):
        for i in range(dataReader.num_train):
            x,y = dataReader.GetSingleTrainSample(i)
            z = self.__forward(x)
            dw,db = self.__backward(x,y,z)
            self.__update(dw,db)
            
    def inference(self,x):
        return self.__forward(x)

def ShowResult(net,dataReader):
    X,Y = dataReader.GetWholeTrainSamples()
    # draw sample data
    plt.plot(X, Y, "b.")
    # draw predication data
    PX = np.linspace(0,1,10)
    PZ = net.inference(PX)
    plt.plot(PX, PZ, "r")
    plt.title("Air Conditioner Power")
    plt.xlabel("Number of Servers(K)")
    plt.ylabel("Power of Air Conditioner(KW)")
    plt.show()

if __name__ == '__main__':
    # read data
    eta = 0.5
    sdr =DataReader.DataReader_1_0("D:\\FileIO\\data.npz") #创建对象
    sdr.ReadData()
    # create net
    eta = 0.1
    net = NeuralNet(eta)
    net.train(sdr)
    # result
    print("w=%f,b=%f" %(net.w, net.b))
    # predication
    result = net.inference(1.346)
    print("result=", result)
    ShowResult(net, sdr)
