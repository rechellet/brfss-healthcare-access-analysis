"""
Feature set definitions for the BRFSS healthcare access project.

This file keeps variable selection modular so notebooks can import
consistent feature groups for preprocessing, modeling, and reporting.
"""


def get_target_variable():
    return "MEDCOST1"


def get_demographic_features():
    return [
        "_STATE",
        "SEXVAR",
        "MARITAL",
        "EDUCA",
        "RENTHOM1",
        "_AGE80",
        "_RACEGR3",
    ]


def get_socioeconomic_features():
    return [
        "INCOME3",
        "EMPLOY1",
        "VETERAN3",
    ]


def get_healthcare_access_features():
    return [
        "PRIMINS2",
        "PERSDOC3",
        "CHECKUP1",
    ]


def get_general_health_features():
    return [
        "GENHLTH",
        "PHYSHLTH",
        "MENTHLTH",
        "POORHLTH",
    ]


def get_chronic_condition_features():
    return [
        "CVDINFR4",
        "CVDCRHD4",
        "CVDSTRK3",
        "ASTHMA3",
        # ASTHNOW excluded for now due to BRFSS skip logic and overlap with ASTHMA3
        "CHCSCNC1",
        "CHCOCNC1",
        "CHCCOPD3",
        "ADDEPEV3",
        "CHCKDNY2",
    ]


def get_health_behavior_features():
    return [
        "EXERANY2",
        "SMOKE100",
        "_BMI5",
    ]


def get_potential_additional_features():
    return [
        "LASTDEN4",
        "RMVTETH4",
    ]


def get_all_predictor_features(include_additional=True):
    features = (
        get_demographic_features()
        + get_socioeconomic_features()
        + get_healthcare_access_features()
        + get_general_health_features()
        + get_chronic_condition_features()
        + get_health_behavior_features()
    )

    if include_additional:
        features += get_potential_additional_features()

    return features


def get_modeling_variables(include_additional=True):
    return [get_target_variable()] + get_all_predictor_features(
        include_additional=include_additional
    )