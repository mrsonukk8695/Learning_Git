#!/usr/bin/env python3
# Adding a line that tells about the changes and the work that this files from which users can understand what this code perform easily
import re
def rearrange_name(name):
    result = re.search(r"^([\w .-]*), ([\w .-]*)$", name)
    if result == None:
        return name
    return "{} {}".format(result[2], result[1])
print("Master")
