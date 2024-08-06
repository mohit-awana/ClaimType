import sys
import os

project_dir = '/Users/mo/Downloads/workspace/ClaimType/'

sys.path.append(os.path.abspath(os.path.join(project_dir, 'src')))

import os
import pandas as pd
from nltk.corpus import stopwords

from ClaimType import logger
from ClaimType.utils.common import get_size
from ClaimType.entity.config_entity import DataTransformationConfig


class DataTransform:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def transform(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        source_ur = self.config.source_url
        download_path = self.config.unzip_dir
        df = pd.read_excel(source_ur)
        df = df.dropna()
        df['total'] = df['Claim Description'] + '' + df['Coverage Code']
        stop = list(stopwords.words('english'))

        @staticmethod
        def change(t):
            t = t.split()
            return ' '.join([(i) for (i) in t if i not in stop])
        df['total'] = df['total'].apply(change)

        return df.to_csv(download_path)
        
        

