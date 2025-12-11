import joblib
import pandas as pd
from course.utils import find_project_root
from sklearn.metrics import confusion_matrix
import plotly.graph_objects as go


def predict(model_path, X_test_path, y_pred_path, y_pred_prob_path):
    model = joblib.load(model_path)
    X_test = pd.read_csv(X_test_path)
    """Form an object y_pred containing a list of your classifer predictions"""
    y_pred = model.predict(X_test)
    y_pred_series = pd.Series(y_pred, name='predicted_built_age')
    y_pred_series.to_csv(y_pred_path, index=False)
    """Form an object y_pred_prob containing a list of
    the probability of your classier predictions"""
    y_pred_prob = model.predict_proba(X_test)[:, 1]
    y_pred_prob_series = pd.Series(y_pred_prob, name='predicted_built_age')
    y_pred_prob_series.to_csv(y_pred_prob_path, index=False)


def pred_lda():
    base_dir = find_project_root()
    model_path = base_dir / 'data_cache' / 'models' / 'lda_model.joblib'
    X_test_path = base_dir / 'data_cache' / 'energy_X_test.csv'
    y_pred_path = base_dir / 'data_cache' / 'models' / 'lda_y_pred.csv'
    y_pred_prob_path = base_dir / 'data_cache' / 'models' / 'lda_y_pred_prob.csv'
    predict(model_path, X_test_path, y_pred_path, y_pred_prob_path)
    #confusion matrix
    y_test_path = base_dir / 'data_cache' / 'energy_y_test.csv'
    y_test = pd.read_csv(y_test_path).squeeze()
    y_pred = pd.read_csv(y_pred_path).squeeze()
    labels = [True, False]
    cm = confusion_matrix(y_test, y_pred)
    TP = cm[0, 0]
    FN = cm[0, 1]
    FP = cm[1, 0]
    TN = cm[1, 1]
    fig = go.Figure(
        data=[
            go.Table(
                header=dict(
                    values=["", "Predicted = TRUE", "Predicted = FALSE"],
                    fill_color="lightgrey",
                    align="center",
                    font=dict(size=14)
                ),
                cells=dict(
                    values=[
                        ["Actual = TRUE", "Actual = FALSE"],
                        [
                            f"{TP}<br>(True Positive)",
                            f"{FP}<br>(False Positive)"
                        ],
                        [
                            f"{FN}<br>(False Negative)",
                            f"{TN}<br>(True Negative)"
                        ]
                    ],
                    align="center"))])

    fig.update_layout(
        title="LDA Confusion Matrix (TP / FP / FN / TN)"
    )
    outpath = base_dir / 'data_cache' / 'vignettes' / 'supervised_classification' / 'confusion_matrix_LDA.html'
    fig.write_html(outpath)


def pred_qda():
    base_dir = find_project_root()
    model_path = base_dir / 'data_cache' / 'models' / 'qda_model.joblib'
    X_test_path = base_dir / 'data_cache' / 'energy_X_test.csv'
    y_pred_path = base_dir / 'data_cache' / 'models' / 'qda_y_pred.csv'
    y_pred_prob_path = base_dir / 'data_cache' / 'models' / 'qda_y_pred_prob.csv'
    predict(model_path, X_test_path, y_pred_path, y_pred_prob_path)
    #confusion matrix
    y_test_path = base_dir / 'data_cache' / 'energy_y_test.csv'
    y_test = pd.read_csv(y_test_path).squeeze()
    y_pred = pd.read_csv(y_pred_path).squeeze()
    labels = [True, False]
    cm = confusion_matrix(y_test, y_pred)
    TP = cm[0, 0]
    FN = cm[0, 1]
    FP = cm[1, 0]
    TN = cm[1, 1]
    fig = go.Figure(
        data=[
            go.Table(
                header=dict(
                    values=["", "Predicted = TRUE", "Predicted = FALSE"],
                    fill_color="lightgrey",
                    align="center",
                    font=dict(size=14)
                ),
                cells=dict(
                    values=[
                        ["Actual = TRUE", "Actual = FALSE"],
                        [
                            f"{TP}<br>(True Positive)",
                            f"{FP}<br>(False Positive)"
                        ],
                        [
                            f"{FN}<br>(False Negative)",
                            f"{TN}<br>(True Negative)"
                        ]
                    ],
                    align="center"))])

    fig.update_layout(
        title="QDA Confusion Matrix (TP / FP / FN / TN)"
    )
    outpath = base_dir / 'data_cache' / 'vignettes' / 'supervised_classification' / 'confusion_matrix_QDA.html'
    fig.write_html(outpath)
