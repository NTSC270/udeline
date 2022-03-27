

def parse(member):
    badges = member.public_flags
    output = []

    if badges.bug_hunter:
        output.append("bug_hunter")
    if badges.bug_hunter_level_2:
        output.append("bug_hunter_2")
    if badges.early_supporter:
        output.append("early_supporter")
    if badges.early_verified_bot_developer:
        output.append("verified_bot_dev")
    if badges.hypesquad_balance:
        output.append("balance")
    if badges.hypesquad_bravery:
        output.append("bravery")
    if badges.hypesquad_brilliance:
        output.append("brilliance")
    if badges.partner:
        output.append("partner")
    if badges.staff:
        output.append("staff")
    if badges.verified_bot:
        output.append("verified_bot")

    return output