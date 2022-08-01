# Create micro library that allows users to work with notes about ukrainian films.
# Note should contain film_name, note, rating (rating - is 1 - 5 rating of the film)
# Micro lib should contain the next functionality:
# 1 - Read notes from .csv file
# 2 - Add note to .csv file
# 3 - Remove note from .csv file
# 4 - Print notes to console
# 5 - Get films with the highest rating
# 6 - Get films with the lowest rating
# 7 - Get average rating among all films
import pandas as pd


class Filmix:
    _filename = None
    _df = None

    def read(self, filename):
        self._df = pd.read_csv(filename, delimiter=',')
        self._filename = filename

    def add(self, film):
        try:
            df = pd.DataFrame(film)
            if 0 < df['rating'].item() < 6:
                df.to_csv(self._filename, mode='a', index=False, header=False)
                self._df = df
            else:
                raise ValueError('Rating should be 1 - 5')
        except ValueError:
            print("Check input - {'film_name': ['your_film_name'], 'note': ['your_note'], 'rating': ['your_rating']}")

    def remove(self, idx):
        self._df.drop([idx], axis=0, inplace=True)
        self._df.to_csv(self._filename, mode='w', index=False)

    def show(self):
        print(self._df)

    def highest(self):
        return self._df[self._df.rating == self._df.rating.max()]

    def lowest(self):
        return self._df[self._df.rating == self._df.rating.min()]

    def average(self):
        return self._df['rating'].mean()


if __name__ == '__main__':
    f = Filmix()
    f.read('data.csv')
    # film_note = {'film_name': ['batman'], 'note': ['batman notes'], 'rating': [1]}
    # f.add(film_note)
    # f.read()
    # print(f.average())
    # f.remove(12)
    # print(f.highest())
    # print(f.lowest())
    # f.show()
