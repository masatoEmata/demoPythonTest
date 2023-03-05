class Cal(object):
    def add_num_and_double(self, x, y):
        if type(x) is not int or type(y) is not int:
            raise ValueError
        res = x + y
        res *= 2
        return res
