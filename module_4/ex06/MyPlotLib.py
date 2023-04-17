import pandas as pd
import matplotlib.pyplot as plt

class MyPlotLib:
    def _guard(fn):
        def inner(data, features):
            columns = data.columns.values
            if not (isinstance(data, pd.DataFrame)
                    and isinstance(features, list)
                    and all([(isinstance(col, str)
                              and (col in columns)
                              and data[col].dtype.kind in 'iuf')
                             for col in features])):
                print("error: wrong arguments")
                return None
            ret = fn(data, features)
            return ret
        return inner

    @staticmethod
    @_guard
    def histogram(data, features):
        """
        plots one histogram for each numerical feature in the list
        """
        data[features].hist()
        plt.show()

    @staticmethod
    @_guard
    def density(data, features):
        """
        plots the density curve of each numerical feature in the list
        """
        data[features].plot.density()
        plt.show()

    @staticmethod
    @_guard
    def pair_plot(data, features):
        """
        plots a matrix of subplots (also called scatter plot matrix).
        On each subplot shows a scatter plot of one numerical variable against
        another one. The main diagonal of this matrix shows simple histograms.
        """
        pd.plotting.scatter_matrix(data[features])
        plt.show()

    @staticmethod
    @_guard
    def box_plot(data, features):
        """
        displays a box plot for each numerical variable in the dataset
        """
        data.boxplot(column=features, backend='matplotlib')
        plt.show()
