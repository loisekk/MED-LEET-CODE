class Solution(object):
    def taskSchedulerII(self, tasks, space):
        """
        :type tasks: List[int]
        :type space: int
        :rtype: int
        """
        last_done = {}
        day = 0

        for task in tasks:
            if task in last_done:
                # Jump to the earliest valid day if needed
                day = max(day, last_done[task] + space + 1)

            last_done[task] = day
            day += 1  # Move to next day after doing the task

        return day