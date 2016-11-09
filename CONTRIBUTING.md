Contributing Guidelines
=======================

## General Guidelines

- All pull requests must pass CI
- All pull requests must be reviewed by one person
- No pushing to master
- Pull requests only as big as they need to be
- Write good descriptions for comments
- Explain your interface, not your implementation
- Math should be explained
- 100 characters line max
- All public interfaces need automated tests

### Styles

- No if's without brackets
- Add spaces around operators: do `x + 1` not `x+1`
- No more than 1 level of ternary operator
- No more than 1 level of scope reach


## Git Commits

### Commit Content

A commit should be addressing one concern or task. Commits should be relatively small and change as
few files as possible. A commit should be a single unit of work so that cherry picking and
reverting can be effective.

### Commit Messages

Commit messages should be descriptive and succinct. When development is being done with respect to
a particular issue logged on Github, the commit message should reference it. If a commit fixes a
bug then it should indicate it in the Github style commit messages. Commits should follow these 7
principles in general:

1. Separate subject from body with a blank line.
2. Limit the subject line to 50 characters.
3. Capitalize the subject line.
4. Do not end the subject line with a period.
5. Use the imperative mood in the subject line.
6. Wrap the body at 72 characters.
7. Use the body to explain what and why vs. how.

Please remember that a commit message should be a title to a description of a change. An example of
a good commit message is the following:

```
Derezz the master control program

MCP turned out to be evil and had become intent on world domination.
This commit throws Tron's disc into MCP (causing its deresolution)
and turns it back into a chess game.

Resolves: #123
See also: #456, #789
```

Not all commit messages need a body but if there is something complex being changed then it should
be explained. An average commit message may be as simple as the following:

```
Simplify serialize.h's exception handling
```

For more information on this, please read <http://chris.beams.io/posts/git-commit/>, and remember,
everything you write matters, everything.

### Online Commits

If you are working on a file online, ensure that you change the default commit message. Every
commit is valuable and knowing what was changed is very important. The default `Updated MyDoc.md`
is not useful and should be avoided.

## Pull Requests

### Descriptions

Pull requests titles should be treated as a commit message and follow the same conventions as above

### Reviews

Pull request reviews should examine style but more importantly they should review the logic applied
to solve a particular issue. This
[article](https://github.com/blog/1943-how-to-write-the-perfect-pull-request) offers a good
explanation of pull request etiquette. The major highlights are the following:

- Familiarize yourself with the context of the issue, and reasons why this Pull Request exists.
- If you disagree strongly, consider giving it a few minutes before responding; think before you react.
- Ask, don’t tell. (“What do you think about trying…?” rather than “Don’t do…”)
- Explain your reasons why code should be changed. (Not in line with the style guide? A personal preference?)
- Offer ways to simplify or improve code.
- Avoid using derogatory terms, like “stupid”, when referring to the work someone has produced.
- Be humble. (“I’m not sure, let’s try…”)
- Avoid hyperbole. (“NEVER do…”)
- Aim to develop professional skills, group knowledge and product quality, through group critique.
- Be aware of negative bias with online communication. (If content is neutral, we assume the tone is negative.) Can you use positive language as opposed to neutral?

## Report Guidelines

> For markdown syntax reference, please refer to <https://michelf.ca/projects/php-markdown/extra/>

### File Names

File names must have the `.md` extension and should be named as the minor section number with the
section title. For example, a section that would go into the 3-Technical major section and
1-Background minor section with the title of 'Introduction' would be named
`./3-Technical/1-Background/1-Introduction.md`. Please note that the order of the files in the
report directory dictates the order that they are rendered in. This makes the ordering of the files
critical so ensure that it is correctly named.

### Headers

Major section headers should be h1 (`#`). Minor sections should be h2 (`##`). Minor subsections should
be h3 (`###`). All other header levels should not be numbered. To avoid numbering a header, add a `{-}`
to the end of the header line. This character will remove the header from the automatic header
counting.

### Appendix Headers

Appendix headers must be manually set. Appendix headers must start with a letter instead of a number
and should be followed by a dash and the minor subsection number. Please note, there is one less
level of header numbering in the appendix. Appendix letters are actually subsection identifiers and
the major section is ignored.

Appendix headers should be directly linkable and identified by the appendix section and subsection
number. Adding a direct link can be done by placing `{#A-1}` on the header line. For example, the
header in section ### B-1 Automation Systems would be followed by `{#B-1}`. The final result would
appear as: `### B-1 Automation Systems {- #B-1}.`

### Tables Headers

Table headers dictate the width that a table is rendered. Table header lines need to be as wide as
possible to accommodate the content of each column.

For example:

```
| C1     | C2                                          |
| -----  | ---                                         |
| Hello  | The quick brown fox jumps over the lazy dog |
```

Will render as

```
| C1     | C2    |
| -----  | ---   |
| Hello  | The   |
|        | quick |
|        | brown |
|        | fox   |
...
```

To render it properly, extend the header line to the end

```
| C1     | C2                                          |
| -----  | ------------------------------------------- |
| Hello  | The quick brown fox jumps over the lazy dog |
```

### Links

All direct links must be wrapped in `<url>`. This includes links that are within references. If a
link is not wrapped in this style then it will not be clickable.

### References

References should be placed inline after the sentence that used external information. All technical
information must be referenced. References must be added to the `5-Reference` section of the report
in IEEE format.

For inline citations, use the markdown syntax `[^my-reference]` to refer to a specific reference
point. To maintain unique reference links, reference ids should be different per file. A reference
link in a file should begin with the number of the major section, followed by minor section then
the section title followed by the link number all dash separated. For example, a reference in the
file `./3-Technical/1-Background/1-Introduction.md` file would appear as `[^3-1-Introduction-1]`
(note that the last number is an incrementing number and refers to the link order within that
file).

In the reference section, references must be added in IEEE format and can be linked by using the
following syntax `[^my-reference]: Reference`. For example, a reference from the file
`./6-Appendix/B-Research/1-AutomationSystems.md` would appear in the reference section as
`[^B-AutomationSystems-1]: Insteon®, "Home," in Insteon, Insteon, 2016. [Online]. Available: <http://www.insteon.com/>. Accessed: Oct. 6, 2016.`

**Please note** that the references for appendices are different then normal sections as they do
not have the major section number. The appendix is the only section that does not require the major
section since it will always begin with a unique letter.



