class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        if not emails:
            return 0

        uniueEmailSet = set()

        for email in emails:
            localName, domainName = email.split("@")
            localName = localName.split("+")[0]
            localName = localName.replace(".", "")
            uniueEmailSet.add((localName, domainName))

        print(len(uniueEmailSet))
        return len(uniueEmailSet)