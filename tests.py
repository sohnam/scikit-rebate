from skrebate import ReliefF, SURF, SURFstar, MultiSURF
from sklearn.pipeline import make_pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
import pandas as pd
import numpy as np

np.random.seed(3249083)

genetic_data = pd.read_csv('https://github.com/EpistasisLab/penn-ml-benchmarks/raw/master/datasets/GAMETES_Epistasis_2-Way_20atts_0.4H_EDM-1_1/GAMETES_Epistasis_2-Way_20atts_0.4H_EDM-1_1.csv.gz', sep='\t', compression='gzip')
genetic_data = genetic_data.sample(frac=0.25)

features, labels = genetic_data.drop('class', axis=1).values, genetic_data['class'].values

def test_relieff_pipeline():
    """Ensure that ReliefF works in a sklearn pipeline"""
    np.random.seed(49082)

    clf = make_pipeline(ReliefF(n_features_to_select=2, n_neighbors=100),
                        RandomForestClassifier(n_estimators=100))

    assert np.mean(cross_val_score(clf, features, labels, cv=3)) > 0.7

def test_surf_pipeline():
    """Ensure that SURF works in a sklearn pipeline"""
    np.random.seed(240932)

    clf = make_pipeline(SURF(n_features_to_select=2),
                        RandomForestClassifier(n_estimators=100))

    assert np.mean(cross_val_score(clf, features, labels, cv=3)) > 0.7

def test_surfstar_pipeline():
    """Ensure that SURF* works in a sklearn pipeline"""
    np.random.seed(9238745)

    clf = make_pipeline(SURFstar(n_features_to_select=2),
                        RandomForestClassifier(n_estimators=100))

    assert np.mean(cross_val_score(clf, features, labels, cv=3)) > 0.7

def test_multisurf_pipeline():
    """Ensure that MultiSURF works in a sklearn pipeline"""
    np.random.seed(320931)

    clf = make_pipeline(MultiSURF(n_features_to_select=2),
                        RandomForestClassifier(n_estimators=100))

    assert np.mean(cross_val_score(clf, features, labels, cv=3)) > 0.7
