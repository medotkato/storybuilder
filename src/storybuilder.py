def parse_story_md(story_md_file: str) -> dict:
    parsed_story = ""
    return parsed_story

def collect_scenes(parsed_story: dict) -> list:
    scenes = []
    return scenes

def concatenate_scenes(scenes: list) -> str:
    catx_scenes = "\n".join(scenes)
    return catx_scenes

def write_full_story_to_file(story: str, filename: str) -> bool:
    hey = type(story)
    print (f"writing story {hey} to {filename}")
    return True

def main():

    story_md_file = "story.md"
    filename = "story_full.md"

    parsed_story = parse_story_md(story_md_file)
    scenes = collect_scenes(parsed_story)
    formatted_story = concatenate_scenes(scenes)
    write_full_story_to_file(formatted_story, filename)

    print (f"Done! Story was successfully built and written into {filename}")

    return True

if __name__ == "__main__":
    main()
