from ncov.reader import get_data

data = get_data('湖北', '', '2020-01-30', '2020-02-05')
data.to_csv('1.csv', index=False)