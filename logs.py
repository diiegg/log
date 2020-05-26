from pyparsing import Word, alphas, Suppress, Combine, nums, string, Optional, Regex

month = Word(string.uppercase, string.lowercase, exact=3)
integer = Word(nums)
serverDateTime = Combine(month + " " + integer + " " + integer + ":" + integer + ":" + integer)
hostname = Word(alphas + nums + "_" + "-")
daemon = Word(alphas + "/" + "-" + "_") + Optional(Suppress("[") + integer + Suppress("]")) + Suppress(":")
message = Regex(".*")
bnf = serverDateTime + hostname + daemon + message

with open('/var/log/syslog') as syslogFile:
    for line in syslogFile:
               try:
                   fields = bnf.parseString(line)
               except:
                print line
 









