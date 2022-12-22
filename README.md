# Storybuilder

Story Builder: builds story.md from [TPT](https://github.com/5off/tpt) based story folder

## Usage:

> python -m storybuilder -i path/to/outline.md

By default the complete story will be placed in the same folder as oultine.md. If you want to define the output file use -o flag:

> python -m storybuilder -i path/to/outline.md -o /path/to/output_md_file.md

If you want to build the story file with links to scenes (for debug purposes), use -d flag:

> python -m storybuilder -i path/to/outline.md -d

## Example

Try

> python -m storybuilder

By default (without any arguments) storybuilder will use the file /storybuilder/tests/test_story/input/outline.md and will place the story file (built from this outline) into the same folder.

## Tests:

> python -m pytest
