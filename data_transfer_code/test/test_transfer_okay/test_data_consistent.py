"""
=============================================
Writer: MaskerTim

README:
This is the test program for check after and befor-transfer data.
You can try it to test whether all data is consistent or not.
=============================================
""" 

import pickle

if __name__=="__main__":
    # load the before-transfer data
    before_file = open("test/test_data/test.p", "rb",)
    b_data = pickle.load(before_file)
    b_data = b_data['Y_test']
    b_data = b_data.tolist()
    before_file.close()
    
    # load the after-transfer data
    after_file = open("test/test_data/after.p", "rb")
    a_data = pickle.load(after_file)
    after_file.close()
    # pop the "test" message
    a_data.pop(0)

    for i in range(len(a_data)):
        ad = a_data[i].tolist()
        if b_data[i] != ad:
            print('data is not consistent')
            break

    print('All data is consistent. Congraduation!')
