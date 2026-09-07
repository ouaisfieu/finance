# -*- coding: utf-8 -*-
"""Vigie — agrégation des trente-quatre dossiers."""

from dossiers_a import DOSSIERS_A
from dossiers_b import DOSSIERS_B
from dossiers_c import DOSSIERS_C
from dossiers_d import DOSSIERS_D

DOSSIERS = {}
for _bloc in (DOSSIERS_A, DOSSIERS_B, DOSSIERS_C, DOSSIERS_D):
    _doublons = set(DOSSIERS) & set(_bloc)
    if _doublons:
        raise SystemExit("Slugs en double : %s" % ", ".join(sorted(_doublons)))
    DOSSIERS.update(_bloc)
