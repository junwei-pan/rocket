class array:
    def __init__(self, lst_value, lst_name = []):
        if lst_name and len(lst_name) != len(lst_value):
            raise ValueError("The length of lst_value and lst_name should be the same")
        self.lst_value = lst_value
        self.lst_name = lst_name
        self.set_name = set(lst_name)

    def __getitem__(self, index):
        '''
        The array class accept both int index and string index.
        '''
        if type(index) is int:
            return self.lst_value[index]
        elif type(index) is str:
            if not index in self.set_name:
                raise ValueError("The given key %s is not in the set of names" % index)
            return self.lst_value[self.lst_name.index(index)]
class matrix:
    def __init__(self):
        self._data = []
        self.row = []
        self.column = []
    
    def add_row(self, lst, lst_feature_name = []):
        self._data.append(lst)

'''
class data:
    def __init__(self):
        self._data = []
        self.features = []
        self.features_by_name = []
        self.lst_feature_name = []
        self.samples = {}
        self.label = []


    def load_data(self, path, delimeter = '\t', f_header = True, f_label = True, lst_excluded = []):
        nf_label = -1
        n_line = -1
        for line in open(path):
            n_line += 1
            lst = line.strip('\n').split(delimeter)
            # First exclude useless columns
            if lst_excluded:
                for i in range(len(lst_excluded)):
                    lst_excluded[i] -= i
                for i in lst_excluded:
                    lst = lst[:i] + lst[i+1:]
            # Get the index list for features
            if n_line == 0:
                if not f_label:
                    nf_label = len(lst)
                # Get the header
                if f_header:
                        self.lst_feature_name = line.strip('\n').split(delimeter)[:nf_label]
                continue
'''
