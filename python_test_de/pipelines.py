""" Module containing  pipeline functions of the Python project """

import pandasql as ps
import pandas as pd
import os
import sys
import logging
from python_test_de import constant
import json


def get_drugs_data(data_path):
    """Reads and parses  drugs data

    :param data_path: a String corresponding to the Path of file
    :return: A pandas dataframe
    """
    try:
        return pd.read_csv(data_path)
    except FileNotFoundError:
        logging.exception('File does not exist or file path contains an error.')
        sys.exit(1)


def get_articles_data(data_path):
    """Reads and parses data articles from pubmed or clinicals trials

    :param data_path: a String corresponding to the Path of file
    :return: A pandas Dataframe
    """
    try:
        extension = os.path.splitext(data_path)[1]
        if extension == '.csv':
            df = pd.read_csv(data_path, parse_dates=['date'])
        elif extension == '.json':
            df = pd.read_json(data_path)
        else:
            raise ValueError("File extension {} is not supported. Please give a JSON or CSV file".format(extension))

        df['date'] = df['date'].dt.strftime('%Y-%m-%d')
        df.columns = ['id', 'title', 'date', 'journal']
        return df

    except ValueError as ve:
        logging.exception(ve)
        sys.exit(1)

    except FileNotFoundError:
        logging.exception('File does not exist or file path contains an error.')
        sys.exit(1)


def get_drugs_mentions(cfg, articles_path_list):
    """Gets all mentions for each drugs in articles

    :param cfg: A path corresponding to the config file
    :param articles_path_list: A list of string corresponding to articles path name
    :return:
    """
    drugs_df = get_drugs_data(cfg['paths']['drugs_path'])
    articles_df_list = map(lambda x: get_articles_data(cfg['paths'][x]), articles_path_list)
    article_df = pd.concat(articles_df_list)

    q1 = """SELECT a.drug, b.title, b.journal, b.date
               FROM drugs_df a
               INNER JOIN article_df b on LOWER(b.title) LIKE '%' || LOWER(a.drug) || '%' """

    return ps.sqldf(q1)


def get_pubmed_mentions(cfg, articles_path_list=constant.PUBMED_ARTICLES_PATH_LIST):
    """Gets all mentions for each drugs in pubmed articles

    :param cfg: A path corresponding to the config file
    :param articles_path_list: A list of string corresponding to articles path name
    :return: A Dataframe
    """
    return get_drugs_mentions(cfg, articles_path_list)


def get_clinical_trials_mentions(cfg, articles_path_list=constant.CLINICAL_TRIALS_ARTICLES_PATH_LIST):
    """Gets all mentions for each drugs in clinicle articles

    :param cfg: Dataframe with all drugs
    :param articles_path_list: A list of string corresponding to articles path name
    :return: A Dataframe
    """
    return get_drugs_mentions(cfg, articles_path_list)


def generate_link_graph_json(cfg):
    """Generates A json file corresponding to the link graph of drugs, articles and journals
    
    :param cfg: A path corresponding to the config file
    :return: A json file
    """
    pubmed_mentions_df = get_pubmed_mentions(cfg)
    pubmed_mentions_df['article_type'] = 'pubmed'
    clinicals_trials_mentions_df = get_clinical_trials_mentions(cfg)
    clinicals_trials_mentions_df['article_type'] = 'clinicals_trials'
    mentions_drugs_df = pd.concat([
        pubmed_mentions_df,
        clinicals_trials_mentions_df
    ])
    json_df = (mentions_drugs_df.groupby(['drug'], as_index=True)
               .apply(lambda x: x[['journal', 'article_type', 'date']].to_dict('r'))
               .reset_index()
               .rename(columns={0: 'mentions'})
               .to_json(orient='records'))

    json_object = json.dumps(
                json.loads(json_df),
                indent=2,
                sort_keys=True
            )

    with open(cfg['paths']['output_path'], 'w') as output_file:
        output_file.write(json_object)
