import pandas as pd
import matplotlib.pyplot as plt

class Komparator:
    def __init__(self, df):
        if not (isinstance(df, pd.DataFrame)):
            print("error: wrong arguments")
            return None
        self.df = df

    def _guard(fn):
        def inner(self, categorical_var, numerical_var):
            columns = self.df.columns.values
            if not (isinstance(categorical_var, str)
                    and isinstance(numerical_var, str)
                    and self.df[categorical_var].dtype.kind in 'O'
                    and self.df[numerical_var].dtype.kind in 'iuf'):
                print("error: wrong arguments")
                return None
            ret = fn(self, categorical_var, numerical_var)
            return ret
        return inner

    @_guard
    def compare_box_plots(self, categorical_var, numerical_var):
        """
        displays a series of box plots to compare how the distribution of
        numerical_var changes if we only consider the subpopulation which
        belongs to categorical_var. There is as many box plots as categories
        """
        self.df.boxplot(column=numerical_var, by=categorical_var)
        plt.show()

    @_guard
    def density(self, categorical_var, numerical_var):
        """
        displays the density of the numerical variable. Each subpopulation are
        represented by a separate curve on the graph
        """
        grp = self.df.groupby(categorical_var)

        grp[numerical_var].plot(kind='density')
        plt.legend(grp.size().index)
        plt.suptitle(f'{numerical_var} density by {categorical_var}')
        plt.xlabel(f"{numerical_var}")
        plt.show()

    @_guard
    def compare_histograms(self, categorical_var, numerical_var):
        """
        plots the numerical variable in a separate histogram for each category
        """
        self.df.hist(column=numerical_var, by=categorical_var)
        plt.suptitle(f"{numerical_var} histograms by {categorical_var}")
        plt.show()
