import numpy as np
from CellAlignDTW import CellAlignDTW

def test_cellaligndtw_initialization(sample_df, cluster_ordering):
    aligner = CellAlignDTW(
        df=sample_df,
        cluster_ordering=cluster_ordering,
        subject_col='subject',
        score_col='score',
        cell_id_col='cell_id',
        cell_type_col='cell_type'
    )
    
    assert aligner.df.equals(sample_df)
    assert aligner.cluster_ordering == cluster_ordering
    assert aligner.cutoff_points is None

def test_cellaligndtw_align(sample_df, cluster_ordering):
    aligner = CellAlignDTW(
        df=sample_df,
        cluster_ordering=cluster_ordering,
        subject_col='subject',
        score_col='score',
        cell_id_col='cell_id',
        cell_type_col='cell_type'
    )
    
    aligner.align()
    assert aligner.cutoff_points is not None
    assert np.isin('aligned_score', aligner.df.columns).any()

