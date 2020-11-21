""" Module containing  pipeline functions of the Python project """

import pandasql as ps

def get_pudmed_mentions(drugs_df, pubmed_df):
    """Gets all mentions for each drugs in pubmed articles

    :param drugs_df: Dataframe with all drugs
    :param pubmed_df: Dataframe of pubmed articles and journals
    :return: A Dataframe
    """

    q1 = """SELECT a.drug, b.title, b.journal, b.date
           FROM drugs_df a
           LEFT OUTER JOIN pubmed_df b on LOWER(b.title) LIKE '%' || LOWER(a.drug) || '%' """

    return ps.sqldf(q1)

def get_clinical_trials_mentions(drugs_df, clinical_trials_df):
    """Gets all mentions for each drugs in clinicle articles

    :param drugs_df: Dataframe with all drugs
    :param clinical_trials_df: Dataframe of pubmed articles and journals
    :return: A Dataframe
    """

    q1 = """SELECT a.drug, b.scientific_title, b.journal, b.date
           FROM drugs_df a
           LEFT OUTER JOIN clinical_trials_df b on LOWER(b.scientific_title) LIKE '%' || LOWER(a.drug) || '%' """

    return ps.sqldf(q1)
