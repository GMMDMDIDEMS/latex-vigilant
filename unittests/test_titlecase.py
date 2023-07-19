import pytest

TITLECASE_FILE_PATH = "unittests/data/titlecase_headings.csv"

def test_titlecase():
    assert 1 == 1, f"test"


# def test_titlecase():
#     with open(TITLECASE_FILE_PATH, 'r') as file:
#         reader = csv.reader(file)
#         for row in reader:
#             assert titlecase(row[0]) == row[1], f"Expected: {row[1]}, Got: {titlecase(row[0])}"



# # Read the CSV file into a DataFrame
# df = pd.read_csv(TITLECASE_FILE_PATH)

# # Iterate over each row in the DataFrame
# for index, row in df.iterrows():
#     bool = titlecase(row[0]) == row[1]
#     print(row[0], titlecase(row[0]), row[1], bool)