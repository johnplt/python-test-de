""" Main file """

import argparse
import logging
import traceback
import utils
import pipelines
import pandas as pd
import pandasql as ps

from datetime import datetime

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Start Python DE test Job')
    parser.add_argument(
        '--global_config_file_path',
        help='Folder path of the global configuration file',
        default='',
        type=str
    )

    args = parser.parse_args()

    try:
        # Get the configuration files
        global_cfg = utils.get_configuration(
            args.global_config_file_path
        )
        drugs_df = pd.read_csv(global_cfg['paths']['drugs_path'])
        clinical_trials_df = pd.read_csv(global_cfg['paths']['clinical_trials_path'])
        pubmed_df = pd.concat(
            [pd.read_csv(global_cfg['paths']['pubmed_csv_path']),
            pd.read_json(global_cfg['paths']['pubmed_json_path'])]
        )

        print(pubmed_df['date'])

        # print(pipelines.get_pudmed_mentions(drugs_df, pubmed_df))
        #
        # print(pipelines.get_clinical_trials_mentions(drugs_df, clinical_trials_df))



    except Exception:
        logging.exception('An error occured check log.')
        traceback.print_exc()