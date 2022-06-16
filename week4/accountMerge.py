class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        # build input into a graph
        emails = collections.defaultdict(
            set
        )  # dont want to traverse multiple duplicate emails
        emailToName = {}

        for account in accounts:

            name = account[0]

            for email in account[1:]:

                # connect all of them to the first email
                emails[email].add(account[1])
                emails[account[1]].add(email)

                emailToName[email] = name

        res = []
        visited = set()
        # dfs
        def dfs(email, connected):

            if email in visited:
                return

            visited.add(email)
            connected.append(email)

            for nei in emails[email]:
                if nei not in visited:
                    dfs(nei, connected)

            return connected

        for email in emails:
            if email not in visited:
                connected = []
                dfs(email, connected)
                res.append([emailToName[email]] + sorted(connected))

        return res
