def parse_command(user_wants):
    if not user_wants.strip():  # Если пустая строка — вернуть None
        return None, None
    parts = user_wants.split(maxsplit=1)
    command = parts[0]
    args = parts[1] if len(parts) > 1 else ""
    return command, args.strip()