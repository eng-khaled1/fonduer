import logging

from fonduer.supervision.utils.structural import (
    common_ancestor,
    get_ancestor_class_names,
    get_ancestor_id_names,
    get_ancestor_tag_names,
    get_attributes,
    get_next_sibling_tags,
    get_parent_tag,
    get_prev_sibling_tags,
    get_tag,
    lowest_common_ancestor_depth,
)
from fonduer.supervision.utils.tabular import (
    same_document,
    same_table,
    same_row,
    same_col,
    is_tabular_aligned,
    same_cell,
    same_sentence,
    get_max_col_num,
    get_min_col_num,
    get_sentence_ngrams,
    get_neighbor_sentence_ngrams,
    get_cell_ngrams,
    get_neighbor_cell_ngrams,
    get_row_ngrams,
    get_col_ngrams,
    get_aligned_ngrams,
    get_head_ngrams,
)
from fonduer.supervision.utils.textual import (
    get_between_ngrams,
    get_left_ngrams,
    get_right_ngrams,
)
from fonduer.supervision.utils.visual import (
    get_page,
    is_horz_aligned,
    is_vert_aligned,
    is_vert_aligned_left,
    is_vert_aligned_right,
    is_vert_aligned_center,
    same_page,
    get_horz_ngrams,
    get_vert_ngrams,
    get_page_vert_percentile,
    get_page_horz_percentile,
    get_visual_aligned_lemmas,
    get_aligned_lemmas,
)


def is_superset(a, b):
    """Check if a is a superset of b.

    This is typically used to check if ALL of a list of sentences is in the ngrams returned by an lf_helper.

    :param a: A collection of items
    :param b: A collection of items
    :rtype: boolean
    """
    return set(a).issuperset(b)


def overlap(a, b):
    """Check if a overlaps b.

    This is typically used to check if ANY of a list of sentences is in the ngrams returned by an lf_helper.

    :param a: A collection of items
    :param b: A collection of items
    :rtype: boolean
    """
    return not set(a).isdisjoint(b)


def get_matches(lf, candidate_set, match_values=[1, -1]):
    """Return a list of candidates that are matched by a particular LF.

    A simple helper function to see how many matches (non-zero by default) an LF gets.

    :param lf: The labeling function to apply to the candidate_set
    :param candidate_set: The set of candidates to evaluate
    :param match_values: An option list of the values to consider as matched. [1, -1] by default.
    :rtype: a list of candidates
    """
    logger = logging.getLogger(__name__)
    matches = []
    for c in candidate_set:
        label = lf(c)
        if label in match_values:
            matches.append(c)
    logger.info(("%s matches") % len(matches))
    return matches


__all__ = [
    "common_ancestor",
    "get_aligned_lemmas",
    "get_aligned_ngrams",
    "get_ancestor_class_names",
    "get_ancestor_id_names",
    "get_ancestor_tag_names",
    "get_attributes",
    "get_between_ngrams",
    "get_cell_ngrams",
    "get_col_ngrams",
    "get_head_ngrams",
    "get_horz_ngrams",
    "get_left_ngrams",
    "get_matches",
    "get_max_col_num",
    "get_min_col_num",
    "get_neighbor_cell_ngrams",
    "get_neighbor_sentence_ngrams",
    "get_next_sibling_tags",
    "get_page",
    "get_page_horz_percentile",
    "get_page_vert_percentile",
    "get_parent_tag",
    "get_prev_sibling_tags",
    "get_right_ngrams",
    "get_row_ngrams",
    "get_sentence_ngrams",
    "get_tag",
    "get_vert_ngrams",
    "get_visual_aligned_lemmas",
    "is_horz_aligned",
    "is_superset",
    "is_tabular_aligned",
    "is_vert_aligned",
    "is_vert_aligned_center",
    "is_vert_aligned_left",
    "is_vert_aligned_right",
    "lowest_common_ancestor_depth",
    "overlap",
    "same_cell",
    "same_col",
    "same_document",
    "same_page",
    "same_row",
    "same_sentence",
    "same_table",
]
