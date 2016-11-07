## Development Process {#section-2-3}

### Introduction

An important part of any sizeable software project is the selection of an appropriate development 
process. A development process imposes a particular structure on the development of a product. The 
process used for the development of this project was created with the following factors in mind:

- Project lifespan: Work on the project will last at least 8 months; other developers may also
continue working on the project after the two school terms are complete

- Team Size: There are four team members working on the project, the process needs to keep everyone 
synchronized and organize the assignment of work to team members

- Reporting: The final project report is critical to the project's success, the process should make
 the report easier to write in a consistent manner

- Code Quality: The process should ensure that work products are of the quality expected of a fourth
 year project.

- Maintainability and Extensibility: The end result of the project should be maintainable and 
extensible; a developer who is new to the project should have an easy time developing for it.

- Ease of Implementation: The process should not be an obstacle to development

Given these goals, the process used for this project incorporates some elements of Extreme Programming
and other Agile methodologies. Use of practices which are widely accepted in industry also ensures 
that new developers are comfortable working on the project. The process prescribes some practices to
be used for: Source Code Management, Code Reviews, Issue Tracking, and Testing.

### Source Code Management

The project uses a source code management tool to achieve the following goals:

- Allows many team members to work on the same codebase and maintain a consistent master copy of the
 product

- Track changes to files in order to locate changes that may have introduced bugs

- Allows team members to work independently and simultaneously 

This project uses git because it provides solutions to all of these issues. Git is familiar to all
team members, in addition to being a de-facto standard in the open source software community.
Using git over other SCM tools makes the process easier to follow, and improves the experience of any
new developer that might choose to maintain the project.

The project's git repository is hosted on Github. Github allows the team to access the project anywhere,
and makes sharing code with new developers simple. Additionally, Github provides some project
management tools that can be used elsewhere in the process, as explained in subsequent sections.

### Branching and Code Reviews

We make strategic use of a git feature, branching, in order to ensure that code which makes it into the
official version of our software is of the quality expected of a fourth year project. A technique we
are using to ensure code quality is peer code review. By frequently reviewing code, we can share
knowledge between team members with different amounts of experience in particular technologies. 

In order for code reviews to be effective, we believe that the review should be as short as possible,
and focused on a particular feature. This ensures that reviewers are motivated to provide high quality 
feedback. In order to encourage this, we have adopted the "feature branches" branching strategy. Work
on a particular feature is submitted to its own branch; branches are merged to master once work on the 
feature has been completed. A code review is required before any branch may be merged into master. 
Feature branches helps to ensure that code reviews are short and focused.

### Continuous Integration

A practice which complements the branching strategy adopted by this project is continuous integration. 
In combination with test automation, continuous integration allows team members to get early 
feedback about changes they make to the codebase. Proper use of  continuous integration can ensure
that the project's master copy remains in a working state at all times. One of the benefits of
maintaining working software at all times is that the project is always demoable.

The continuous integration tool chosen for this project is Travis CI. Travis CI is a free hosted CI 
system. Travis can be easily integrated with Github repositories, making it the obvious choice for 
this project. 

Github rules were created to ensure that any code which is merged into the master branch does not 
break existing work. Merges to master are blocked until Travis has successfully run unit tests on the
merged code.

### Issue Tracking

In order for the team to measure the progress of the project, and to ensure that tasks are not forgotten, 
it is important for this process to incorporate a process for tracking tasks. Issue tracking may also 
simplify the task of writing the final report by providing a list of the tasks completed during the
project.

Another advantage of issue tracking is that team members can be explicitly assigned to specific issues
to work on; this ensures that efforts are not duplicated. 

A good issue tracking tool:

- Provides a visible list of things to do
- Allows tasks to be ordered so that team members know what to do next
- Provides a forum for discussion of tasks

Github provides an issue tracking system which can be used to accomplish these goals. The Github 
issue tracking system is not ideal for some tasks, such as prioritization of issues. In the interest
of minimizing the number of tools required to follow this process, however, Github issue tracking was
selected as the team's issue tracking tool.

Github issues are organized into groups of tasks which must be completed during each one-week iteration
of development. Issues are prioritized using labels (minor, major, critical). Issues are assigned to
a team member when work begins; when work on an issue is completed the issue is closed using a commit
message.

### Testing practices

Agile processes generally encourage a short feedback loop for developers (problems with code should
be exposed as early as possible). This project uses principles of test-driven development (TDD) and
behaviour-driven development (BDD) in order to ensure that development remains focused on problems 
which are relevant to the end user. Any change to the code should be accompanied by an automated test
or set of tests which exercises **end user functionality**. That is, automated tests should function
as an executable specification of requirements for the unit under test.
