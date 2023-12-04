with open("roles.txt", encoding="utf-8") as file:
    text = file.read()
    separated_text = text.split("textLines:\n")
    roles = {role:[] for role in separated_text[0].split("\n")[1:]}
    prevrole = ""
    for i in separated_text[1].split("\n"):
        role = i.split("\n")[0].split(":")[0]
        try:
            roles[role].append(i.split("\n")[0].split(":")[1].strip())
            prevrole = role
        except KeyError:
            # if roles[prevrole][-1]:
            #     roles[prevrole][-1] += f"\n{role.strip()}"
            # else:
            roles[prevrole].append(role.strip())
        # roles[role].append(i.split(":")[1])
    print(roles)
