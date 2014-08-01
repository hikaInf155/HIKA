import pickle

dataType={'Value':'',

        'String':'Value',
        'Number':'Value',

        'Place':'String',
        'Time':'Number'}
dicFile=open('dataDic.dat','wb')
pickle.dump(dataType,dicFile)
dicFile.close()
