def get_prompt(prompt_path: str):
    try:
        with open(prompt_path, 'r') as f:
            content = f.read()
            return content

    except (FileNotFoundError, Error) as e:
        print(f"There was an error: {e}")
        return None
