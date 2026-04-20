def count_user_actions(logs):
    counts = {}
    for entry in logs:
        parts = entry.split(" | ")
        username = parts[1]
        if username in counts:
            counts[username] += 1
        else:
            counts[username] = 1
    return counts


def most_common_domains(emails):
    counts = {}
    for email in emails:
        domain = email.split("@")[1]
        if domain in counts:
            counts[domain] += 1
        else:
            counts[domain] = 1
    max_count = 0
    for domain in counts:
        if counts[domain] > max_count:
            max_count = counts[domain]
    result = []
    for domain in counts:
        if counts[domain] == max_count:
            result.append(domain)
    return result


def most_active_user(messages):
    counts = {}
    for message in messages:
        username = message.split(":")[0]
        if username in counts:
            counts[username] += 1
        else:
            counts[username] = 1
    top_user = None
    top_count = 0
    for user in counts:
        if counts[user] > top_count:
            top_count = counts[user]
            top_user = user
    return top_user


def shift_encipher(s, shift):
    result = ""
    for ch in s:
        if "a" <= ch <= "z":
            result += chr((ord(ch) - ord("a") + shift) % 26 + ord("a"))
        elif "A" <= ch <= "Z":
            result += chr((ord(ch) - ord("A") + shift) % 26 + ord("A"))
        else:
            result += ch
    return result


def shift_decipher(s, shift):
    return shift_encipher(s, -shift)


def rail_fence_decipher(s):
    n = len(s)
    split = (n + 1) // 2
    first = s[:split]
    second = s[split:]
    result = ""
    for i in range(len(second)):
        result += first[i] + second[i]
    if len(first) > len(second):
        result += first[-1]
    return result


if __name__ == "__main__":
    logs = [
        "2026-01-01 10:00 | alice | login",
        "2026-01-01 10:05 | bob | logout",
        "2026-01-01 10:10 | alice | upload",
    ]
    print(count_user_actions(logs))

    print(most_common_domains(["alice@gmail.com", "bob@yahoo.com", "carol@gmail.com"]))
    print(most_common_domains(["a@gmail.com", "b@yahoo.com"]))

    messages = ["alice: hello there", "bob: hi", "alice: how are you"]
    print(most_active_user(messages))

    print(shift_encipher("attack at dawn!", 3))
    print(shift_encipher("Hello, World! 123", 1))
    print(shift_encipher("AbcZ-9", 1))

    print(shift_decipher("Dwwdfn dw gdzq!", 3))
    print(shift_decipher("Ifmmp, Xpsme! 123", 1))
    print(shift_decipher("BcdA-9", 1))

    print(rail_fence_decipher("ATCADWTAKTAN"))
    print(rail_fence_decipher("HLOOLELWRD"))
    print(rail_fence_decipher("HLOEL"))
