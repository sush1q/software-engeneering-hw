from app import *


if __name__ == '__main__':
    test_app = App('test-db')
    
    test_app.save('test_prod3', 1, 100, 2)
    test_app.save('test_prod4', 2, 1000, 1)
    
    data = test_app.show_all()
    
    print('smth')

