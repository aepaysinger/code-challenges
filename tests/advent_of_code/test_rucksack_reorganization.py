from unittest.mock import patch


from code_challenges.advent_of_code.rucksack_reorganization import find_priority


@patch("code_challenges.advent_of_code.rucksack_reorganization.rucksack_reorganization")
def test_rucksack_reorganization_a(rucksack_reorganization_mock):
    rucksack_reorganization_mock.return_value = ['VdzVHmNpdVmBBCpmQLTNfTtMhMJnhFhTTf', 'FgqsZbqDDFqRrhhJnsnLMTfhJG', 'bRRRPrRRwSwbDqgjvDZbRbQzpzmQVWCzzBdvQBFCzlWV', 'GcDdRdvhRssRhGDdShCRtqWjlQzqWgqzNfNjfQWWjt', 'mwwnnPFwmVrPmJmzfNzqCjQCbgVlgC', 'nPnHHLrHwmJTrCTJpThBscBSdSLGZvZBvRhZ', 'RVQQcVlcSRclfZCCCnMJJTSTnC', 'NdHwjdwjbBBZrrZrbJDZJJ', 'wmhjGGBGwwmjtjtdPlfRcpVQlhRppVJF']
    actual = find_priority()
    expected = "priority_level_amount = 242 priority_level_amount_of_3 = 97"

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.rucksack_reorganization.rucksack_reorganization")
def test_rucksack_reorganization_b(rucksack_reorganization_mock):
    rucksack_reorganization_mock.return_value = ['DLCzPzTzZDdLdGSGfSGrsnQGzr', 'LNPPLHNPHQNQSBFDWDPgggFv', 'hszfWCWJhrBMsSSBgvFD', 'GGZjfmJTjmZfrJrZrZJRGwNQnlLNHWjLVjlwdVNHpV', 'BdNVdTcGVclmTwrTnwPwrHCr', 'zttBWzfLsCggHPwDrf']
    actual = find_priority()
    expected = "priority_level_amount = 149 priority_level_amount_of_3 = 48"

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.rucksack_reorganization.rucksack_reorganization")
def test_rucksack_reorganization_c(rucksack_reorganization_mock):
    rucksack_reorganization_mock.return_value = ['MSRVnMjnVRVnPlcsrtMtschgDl', 'NWHBwJBwBBQCHHqwWQGBNgdrFFtsthcqdltdDsqttq', 'CCTTGCNCCBfNJNNWbGGnvVzDSRfDRSZvLPSzRn', 'MpRfjRjWpZzzzRzZSpjzZjTCQcGdHLWNGqdBdcBWWBLccn', 'lrbrsPQDPQglDtwggcLCqnCdNNdHBLsqNd', 'blwbJggvgbwlvQbvtgwmvVwRfTzfMMjFVfSFjZjMTSTSzj', 'ttSGjHWVrwWrWWvhzvhmhDfR', 'qMBdNNsccQgfDRzRmqlhRl']
    actual = find_priority()
    expected = "priority_level_amount = 244 priority_level_amount_of_3 = 73"

    assert actual == expected, f"Returned {actual} instead of {expected}"
