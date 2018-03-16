# -*- coding: utf-8 -*-

import os
from utils import word_split, sent_split
from gensim.models import KeyedVectors
import numpy as np
from sklearn.cluster import KMeans
from scipy import spatial
import logging


__name__ = 'text-summarizer'
logger = logging.getLogger(__name__)


class TextSummarizer:

    def __init__(self, txt_path):
        self._load(txt_path)
        self._compute_vec()
        self._cluster()
        self._build_kd_tree()

    def _load(self, txt_path):
        try:
            with open(os.path.abspath(txt_path), 'r') as txt_f:
                doc = txt_f.read()
                self._sentences = sent_split(doc)
        except FileNotFoundError as e:
            raise e

    def _compute_vec(self):
        """ We construct a map sentence-vector for each sentence in doc """

        model = KeyedVectors.load_word2vec_format(os.path.abspath('files/wiki.simple.vec'))
        s_vectors = []
        for sent in self._sentences:
            w_vectors = []

            for w in word_split(sent):
                try:
                    w_vec = model.word_vec(w)
                    w_vectors.append(w_vec)
                except Exception as e:
                    logger.debug(e)
                    continue

            w_vectors = np.asarray(w_vectors)

            s_vector = np.mean(w_vectors, axis=0)
            s_vectors.append(s_vector)

        self._vectors = np.asarray(s_vectors)

    def _cluster(self):
        """ Cluster vectors to find centroids """
        n_cluster = int(len(self._sentences) * 0.2)
        kmeans = KMeans(n_clusters=n_cluster)
        kmeans.fit(self._vectors)

        self._centroids = kmeans.cluster_centers_

    def _build_kd_tree(self):
        self._tree = spatial.KDTree(self._vectors)

    def summarize(self):
        idxs = set()
        for centroid in self._centroids:
            dis, idx = self._tree.query(centroid)
            idxs.add(idx)

        imp_sentences = [self._sentences[idx] for idx in list(sorted(idxs))]

        return '\n'.join(imp_sentences)



