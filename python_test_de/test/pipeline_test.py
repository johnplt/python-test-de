import unittest
import os
from python_test_de import pipelines
import pandas as pd


class MyTestCase(unittest.TestCase):
    def test_get_drugs_data(self):
        test_drugs_filename = os.path.join(os.path.dirname(__file__), 'drugs_test.csv')
        test_data = {'atccode': ['AA', 'BB'],
                     'drug': ['AMINE', 'BMINE']}
        test_df = pd.DataFrame(test_data)
        pd.testing.assert_frame_equal(test_df, pipelines.get_drugs_data(test_drugs_filename))

    def test_get_article_data_csv(self):
        test_drugs_filename = os.path.join(os.path.dirname(__file__), 'pubmed_test.csv')

        test_data = {'id': [1, 2],
                     'title': ["hello article on amine", "hello article on bmine"],
                     'date': ['01/01/2019', '01/01/2019'],
                     'journal': ['Journal A', 'Journal B']}

        test_df = pd.DataFrame(test_data)
        test_df['date'] = pd.to_datetime(test_df['date']).dt.strftime('%Y-%m-%d')
        pd.testing.assert_frame_equal(test_df, pipelines.get_articles_data(test_drugs_filename))


    def test_get_article_data_json(self):
        test_drugs_filename = os.path.join(os.path.dirname(__file__), 'pubmed_test.json')

        test_data = {'id': [5],
                     'title': ["Hi article on bmine"],
                     'date': ['01/01/2020'],
                     'journal': ['Journal B']}

        test_df = pd.DataFrame(test_data)
        test_df['date'] = pd.to_datetime(test_df['date']).dt.strftime('%Y-%m-%d')

        pd.testing.assert_frame_equal(test_df, pipelines.get_articles_data(test_drugs_filename))

    def test_drugs_mentions_pubmed(self):
        test_drugs_filename = os.path.join(os.path.dirname(__file__), 'drugs_test.csv')
        test_pubmed_csv_filename = os.path.join(os.path.dirname(__file__), 'pubmed_test.csv')
        test_pubmed_json_filename = os.path.join(os.path.dirname(__file__), 'pubmed_test.json')

        cfg = {'paths':
                   {'drugs_path': test_drugs_filename,
                    'pubmed_csv_path': test_pubmed_csv_filename,
                    'pubmed_json_path': test_pubmed_json_filename}
               }
        results_df = pipelines.get_pubmed_mentions(cfg)

        expected_results = {'drug': ['AMINE', 'BMINE', 'BMINE'],
                            'title': ["hello article on amine", "hello article on bmine", "Hi article on bmine"],
                            'journal': ['Journal A', 'Journal B', 'Journal B'],
                            'date': ['01/01/2019', '01/01/2019', '01/01/2020']}

        expected_results_df = pd.DataFrame(expected_results)

        expected_results_df['date'] = pd.to_datetime(expected_results_df['date']).dt.strftime('%Y-%m-%d')
        pd.testing.assert_frame_equal(results_df, expected_results_df)


if __name__ == '__main__':
    unittest.main()
