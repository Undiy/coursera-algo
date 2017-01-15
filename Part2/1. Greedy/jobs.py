from lib2to3.pgen2.tokenize import double3prog


def schedulde_by_diff(jobs):

    diffs_and_jobs = [ (weight - length, weight, length) for (weight, length) in jobs ]

    diffs_and_jobs.sort(reverse=True)

    print(diffs_and_jobs)

    return get_weighted_times( ((weight, length) for (diff, weight, length) in diffs_and_jobs) )


def schedulde_by_ratio(jobs):

    ratios_and_jobs = [ ( float(weight) / length, weight, length) for (weight, length) in jobs ]

    ratios_and_jobs.sort(reverse=True)

    print(ratios_and_jobs)

    return get_weighted_times( ((weight, length) for (ratio, weight, length) in ratios_and_jobs) )


def get_weighted_times(jobs):

    new_time = 0
    weighted_times = list()

    for (weight, length) in jobs:
        new_time = length + new_time
        weighted_times.append(new_time * weight)

    print(weighted_times)
    return weighted_times