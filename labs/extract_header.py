"""
Write a function named extract_domain that will print the first matching domain name in a given string.

>>> extract_domain("kieran@pdxcodeguild.com")
'pdxcodeguild.com'

>>> extract_domain("domain of jwackman@hvc.rr.com designates 2a00:1450:400c:c09::22d as permitted sender")
'hvc.rr.com'

>>> extract_domain("flowerbowl@gmail.com and kieran@pdxcode.com")
'gmail.com'

"""


def extract_domain(domain):
    """extract between @ and .com"""
    name = domain.index('@') + 1
    com = domain.index('.com') + 4
    result = domain[name:com]  # slicing
    return result

