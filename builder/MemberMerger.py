from typing import List

from JavaMember import JavaMember


def merge(members1: List[JavaMember], members2: List[JavaMember]) -> List[JavaMember]:
    member_lookup = {member.variable_name: True for member in members1}

    merged_members = [member for member in members1]

    for member in members2:
        if member.variable_name not in member_lookup:
            member_lookup[member.variable_name] = True
            merged_members.append(member)

    return merged_members