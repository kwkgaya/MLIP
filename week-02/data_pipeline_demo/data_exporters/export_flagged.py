import os
from mage_ai.settings.repo import get_repo_path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data(df, *args, **kwargs):
    # Write the result into the Mage project folder (data_pipeline_demo/)
    path = os.path.join(get_repo_path(), 'flagged_transactions.csv')
    df.to_csv(path, index=False)
    print(f'Saved {len(df)} rows to {path}')