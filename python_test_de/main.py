""" Main file """

import argparse
import logging
import traceback
from python_test_de import utils, pipelines
import pandas as pd
import json
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
        cfg = utils.get_configuration(
            args.global_config_file_path
        )

        # Log configuration
        logging.basicConfig(
            level=logging.INFO,
            filename="{}{}.log".format(
                cfg['paths']['logs_path'],
                str(datetime.now().strftime('%Y%m%d_%H%M'))
            ),
            filemode='a'
        )

        # Generate link graph
        logging.info('Started link graph generation')
        pipelines.generate_link_graph_json(cfg)

        logging.info('Ended generates link graph generation')

        # Get journal mentionning most number of drugs
        logging.info('Started number of distinct drugs by journal')
        with open(cfg['paths']['output_path']) as data_file:
            mentions_data = json.load(data_file)

        df = pd.json_normalize(mentions_data, 'mentions', ['drug'], record_prefix='mentions_')
        nb_uniq_mentions_journal = df.groupby('mentions_journal')\
            .drug.nunique()\
            .sort_values(ascending=False)\
            .reset_index(name='count')
        print(nb_uniq_mentions_journal)

        logging.info('Ended number of distinct drugs by journal')

    except Exception:
        logging.exception('An error occurred check log.')
        traceback.print_exc()
